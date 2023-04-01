import os,datetime,pathlib
import json5 as jason
import pandas as pd

import shutil

from concurrent.futures import ThreadPoolExecutor

from dataMan import DataManager

from logging import Logger
from logMan import createLogger

## Pandas Options
# show all the columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


class YABUS():
    def __init__(self,config_dir:str = None,verbose:bool = False):
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.verbose = verbose
        self.logger = createLogger(
            root=os.path.join(self.dir,'log'),
            useStreamHandler=self.verbose
            )
        
        self.config_dir = config_dir
        if self.config_dir == None or self.config_dir == '':
            self.config_dir = os.path.join(self.dir,'config.json')

        self.default_config_item = [
            {
            'source': 'X:\\',
            'root_dest': 'Y:\\',
            'options': '',
            'ex_reg':r'',
            'lastbackup': None,
            'enable': True, 
            'runable': True
            }
        ]

        self.config = DataManager(file_dir=self.config_dir,logger=self.logger,default=self.default_config_item.copy())
        self.process_config()

        self.scan_cache = []

    def process_config(self):
        self.logger.info('start')

        for item in self.config.data:
            self.logger.info(item)

            item['options'] = item.get('options','') 

            item['runable'] = True
            item['enable'] = item.get('enable',True)
            
            if item.get('lastbackup',None) == None:
                item['lastbackup'] = datetime.datetime.now().strftime('%Y%m%d%H%M')

            # checks
            if item.get('source',None) == None:
                item['runable'] = False
                self.logger.error('no source - this will be disabled')

            if os.path.exists(item.get('source',None)) == False:
                item['runable'] = False
                self.logger.error('invalid source path - will be disabled')

            if item.get('root_dest','') != '' or item.get('root_dest','') != None:
                self.logger.info('root_dest will be used, and override dest')
                item['dest'] = os.path.join(item['root_dest'], item['source'].split('\\')[-1] )

            # if dest doesn't exist we'll make it 
            if os.path.exists(item.get('dest',None)) == False:
                try:
                    pathlib.Path(item['dest']).mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    self.logger.info(e)
                    item['runable'] = False
                    self.logger.error('invalid dest path - will be disabled')

            if item.get('dest','') == '':
                item['runable'] = False
                self.logger.error('no dest - will be disabled')

            # create archive directory
            try:
                item['archive_dir'] = os.path.join(item['dest'],'.archive',item['lastbackup'])
                pathlib.Path(item['archive_dir']).mkdir(parents=True, exist_ok=True)
            except:
                pass
        
        self.config.save()
        self.logger.info('done')

    def bar(self,num:int,den:int,size:int = 75):
        p = (num+1)/den 
        return '[' + ('#'*(int(p * size))).ljust(size,'-') + ']'

    def scan_folder(self,root:str):
        rootnum_minus_one = len(root.split('\\')) 
        result = []
        for dirpath, dirnames, filenames in os.walk(root):
            if '.archive' in dirpath:
                continue
            for index,filename in enumerate(filenames):

                fullpath = os.path.join(dirpath,filename)
                relpath = fullpath.split('\\')[rootnum_minus_one:]
                relpath = os.path.join(*relpath)

                s = os.stat(fullpath) 

                result.append(
                    {
                        'relpath': relpath,
                        'fullpath': fullpath,
                        'filename': filename,
                        'size': s.st_size,
                        'modified': s.st_mtime,
                        'rootpath': root
                    }
                )

                # if len(result)%1000 == 0:
                #     print('Scanning:', ['|','/','-','\\'][index%4],len(result),' files found ',' '*100,end='\r')
                    
        # print()
        return pd.DataFrame(result)

    def return_df(self,root:str):
        return pd.DataFrame() 

    def scan(self):
        print('Scanning Start ...')
        self.logger.info('start')
        self.logger.info('scan_cache - cleared')
        self.scan_cache = []

        executor = ThreadPoolExecutor(4)
        futures = []
        futures_map_source = {}
        futures_map_dest = {}

        for index,item in enumerate(self.config.data):
            
            funct = self.scan_folder
            if item.get('runable',False) == False or item.get('enable',False) == False:
                funct = self.return_df

            f = executor.submit(funct, (item['source']))
            futures_map_source[str(index) + ':' + item['source']] = len(futures)
            futures.append(f)

            f = executor.submit(funct, (item['dest']))
            futures_map_dest[str(index) + ':' + item['dest']] = len(futures)
            futures.append(f)
                
        results = []
        for f in futures:
            results.append(f.result())

        self.logger.info(f'futures_map_source: {str(futures_map_source)}')
        self.logger.info(f'futures_map_dest: {str(futures_map_dest)}')

        total_files_found = 0 

        for index,item in enumerate(self.config.data):
            df_source = results[ futures_map_source[str(index) + ':' +item['source']] ]
            df_dest = results[ futures_map_dest[str(index) + ':' +item['dest']] ]

            total_files_found += len(df_source)
            total_files_found += len(df_dest)
            print(f' Files Found {total_files_found}',end='\r')

            if len(df_source) + len(df_dest) == 0 :
                self.scan_cache.append(pd.DataFrame())
                continue

            self.logger.info(f'source: {len(df_source)}')
            self.logger.info(f'dest: {len(df_dest)}')

            # must have specific columns
            columns = [
                'relpath',
                'fullpath',
                'filename',
                'size',
                'modified',
                'rootpath'
            ]

            for col in columns:
                if col not in df_source.columns:
                    df_source[col] = None
                if col not in df_dest.columns:
                    df_dest[col] = None

            self.logger.info('scan - done')
            self.logger.info('comparing files')

            df = pd.merge(df_source,df_dest,how='outer',on='relpath')

            df['archive_dir'] = item['archive_dir']
            df['options'] = item.get('options','')
            df['rootpath_y'] = item['dest']

            df['skip'] =  False
            if len(item.get('ex_reg','')) > 0:
                df.loc[ (df['fullpath_x'].isna() == False ) & (df['fullpath_x'].str.contains(item['ex_reg'],regex=True)) ,'skip'] = True
            #these just need to automatically be skipped
            df.loc[ (df['fullpath_x'].isna() == False ) & (df['fullpath_x'].str.contains(r'(?:desktop\.ini|Thumbs\.db)$',regex=True)) ,'skip'] = True

            df['remove_dest'] = False
            # if not in source, but in destination... remove from destination
            df.loc[ ((df['fullpath_x'].isna() ) & (df['fullpath_y'].isna() == False)) ,'remove_dest'] = True
            
            df['backup'] =  False
            # if the size and modified is different, back up 
            df.loc[ ((df['size_x'] != df['size_y']) | (df['modified_x'] != df['modified_y'])) ,'backup'] = True
            #if not in source... we can't back it up
            df.loc[ df['fullpath_x'].isna() ,'backup'] = False 

            df['archive'] =  False
            # if backup is true, and destination is not null, archive it
            df.loc[ ((df['fullpath_x'].isna() == True) & (df['fullpath_y'].isna() == False)) ,'archive'] = True
                    
            self.scan_cache.append(df)
            # print('scan: ',self.bar(len(self.scan_cache),len(self.config.data)),end='\r')
        print('')
        self.logger.info('end')

    def backup(self,row):
        """perform all the actions for backup one row of data

        Args:
            row (_type_): _description_

        Returns:
            _type_: _description_
        """
        # self.logger.info('start')
        result = {'actions':[],'row': row}

        if row.get('skip',False) == True:
            result['actions'].append('skip')
            return result

        if row.get('archive',False) == True:
            shutil.copy2(row["fullpath_y"],row["archive_dir"])
            result['actions'].append('archive')

        if row.get('remove_dest',False) == True:
            os.remove(row["fullpath_y"])
            result['actions'].append('remove_dest')

        if row.get('backup',False) == True:
            dest = row['fullpath_x'].replace(row['rootpath_x'], row['rootpath_y'])
            pathlib.Path('\\'.join(dest.split('\\')[:-1])).mkdir(parents=True, exist_ok=True)
            shutil.copy2(row["fullpath_x"],dest)
            result['actions'].append('backup')

        if len(result['actions']) > 0:
            self.logger.info(result)

        # self.logger.info('end')
        return result

    def backup_all(self):
        """backups all the rows of data
        """
        self.logger.info('start')
        # make sure there is scan_cache
        if self.scan_cache == []:
            self.scan()
        
        # put all the scan_cache together
        all_cache = pd.DataFrame()
        for i in self.scan_cache:
            all_cache = pd.concat([all_cache,i])

        records = all_cache.to_dict(orient='records')

        executor = ThreadPoolExecutor(4)
        futures = []
        for index,record in enumerate(records):

            if index%10 == 0:
                print( 'backup process 1/2: ', self.bar((index+1),len(records)) ,end='\r')

            f = executor.submit(self.backup, (record))
            futures.append(f)
        print()
        print('done 1/2')
        
        # print('processing...')
        results = []
        for index,f in enumerate(futures):
            if index%10 == 0:
                print( 'backup process 2/2: ', self.bar((index+1),len(records)) ,end='\r')
            results.append(f.result())
        print()
        print('done 2/2')

        self.logger.info('end')
        print('done')
        self.scan_cache = []



if __name__ == '__main__':
    # config = {
    #     # 'source': r'C:\Users\JGarza\Pictures',
    #     # 'source': r'D:\UnityProjects\JellyObject',
    #     'source': r'D:\UnityProjects',
    #     'root_dest': r'C:\Users\JGarza\Desktop\x',
    #     'options': '',
    #     'ex_reg':r'',
    #     'lastbackup': None #202303302110
    # }
    # process_item(config)
    # print(config)

    yabus = YABUS()
    yabus.backup_all()

