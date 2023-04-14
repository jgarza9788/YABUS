
"""\
YABUS
yet another backup script

"""
__author__ = "Justin Garza"
__copyright__ = "Copyright 2023, Justin Garza"
__credits__ = ["Justin Garza"]
__license__ = "FSL"
__version__ = "1.0.1"
__maintainer__ = "Justin Garza"
__email__ = "Justin Garza"
__status__ = "Development"


import os,datetime,pathlib
import json5 as jason
import pandas as pd


import shutil

# used for multi threading
from concurrent.futures import ThreadPoolExecutor

# data manager
from utils.dataMan import DataManager

# logging
from logging import Logger
from utils.logMan import createLogger

## Pandas Options
# show all the columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


class YABUS():
    def __init__(self,
                config_dir:str = None,
                save_cache_as_csv:bool = False,
                verbose:bool = False,
                logger:Logger = None
                ):
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.verbose = verbose

        self.logger = logger
        if self.logger == None:
            self.logger = createLogger(
                root=os.path.join(self.dir,'log'),
                useStreamHandler=self.verbose
                )
        
        self.config_dir = config_dir
        if self.config_dir == None or self.config_dir == '':
            self.config_dir = os.path.join(self.dir,'config.json')

        self.default_config = {
            "items": [
                {
                'source': 'X:\\',
                'root_dest': 'Y:\\',
                'ex_reg':r'',
                'lastbackup': None,
                'enable': True, 
                'runable': True
                }
            ]
        }

        self.progress_numerator = 0 
        self.progress_denominator = 0

        self.config = DataManager(file_dir=self.config_dir,logger=self.logger,default=self.default_config.copy())

        self.process_config()

        self.scan_cache = pd.DataFrame()
        self.save_cache_as_csv = save_cache_as_csv

    def items(self):
        """returns a list of items that should be synced

        Returns:
            _type_: _description_
        """
        return self.config.data['items']

    def process_config(self):
        """makes sure the config file is good
        """
        self.logger.info('start')

        for item in self.items():
            self.logger.info(item)

            item['runable'] = True
            item['enable'] = item.get('enable',True)

            item['source'] = item.get('source','')
            item['root_dest'] = item.get('root_dest','')
            item['dest'] = item.get('dest','')

            lbu = item.get('lastbackup','0'*12) #000000000000 if there is no lastbackup
            item['archive_dir'] = os.path.join(item['dest'],'.archive',str(lbu))
            
            # checks
            if item.get('source',None) == None:
                item['source'] = ''
                item['runable'] = False
                self.logger.error('no source - this will be disabled')

            if os.path.exists(item.get('source',None)) == False:
                item['runable'] = False
                self.logger.error('invalid source path - will be disabled')

            if item.get('root_dest','') != '':
                self.logger.info('root_dest will be used, and override dest')
                item['dest'] = os.path.join(item['root_dest'], item['source'].split('\\')[-1] )

            # if dest doesn't exist we'll make it 
            if item.get('dest',None) != None and os.path.exists(item.get('dest',None)) == False:
                try:
                    pathlib.Path(item['dest']).mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    self.logger.error(e)
                    item['runable'] = False
                    self.logger.error('invalid dest path - will be disabled')

            if item.get('dest','') == '':
                item['runable'] = False
                item['dest'] = ''
                self.logger.error('no dest - will be disabled')
        
        self.config.save()
        self.logger.info('done')

    def bar(self,num:int,den:int,size:int=75):
        """makes a load bar"""
        p = (num)/den 
        return '[' + ('#'*(int(p * size))).ljust(size,'-') + ']'

    def _scan_folder(self,root:str):
        """scans a folder and returns a dataframe for all the files"""
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
        return pd.DataFrame(result)

    def _return_df(self,root:str == None):
        """returns a blank pd.DataFrame()

        Args:
            root (str): _description_

        Returns:
            _type_: _description_
        """
        return pd.DataFrame()

    def scan(self,filter_index:int=None):
        """prepares the scan_cache (a dataframe for all the files/folders that needs to be archived/backedup)
        """
        self.logger.info('Scanning Start ...')

        self.progress_numerator = 0 
        self.progress_denominator = 0

        self.scan_cache = pd.DataFrame()
        self.logger.info('scan_cache - cleared')

        executor = ThreadPoolExecutor(4)
        futures = []
        futures_map_source = {}
        futures_map_dest = {}

        items = self.items()
        if filter_index != None:
            try:
                items = [items[filter_index]]
            except Exception as e:
                self.logger.error(str(e))

        self.progress_denominator += len(items)
        for index,item in enumerate(items):
            self.progress_numerator += 1
            
            funct = self._scan_folder
            if item.get('runable',False) == False or item.get('enable',False) == False:
                funct = self._return_df

            f = executor.submit(funct, (item['source']))
            futures_map_source[str(index) + ':' + item['source']] = len(futures)
            futures.append(f)

            f = executor.submit(funct, (item['dest']))
            futures_map_dest[str(index) + ':' + item['dest']] = len(futures)
            futures.append(f)
                
        results = []
        self.progress_denominator += len(futures)
        for f in futures:
            self.progress_numerator += 1
            results.append(f.result())

        # self.logger.info(f'futures_map_source: {str(futures_map_source)}')
        # self.logger.info(f'futures_map_dest: {str(futures_map_dest)}')

        total_files_found = 0 

        self.progress_denominator += len(items)
        for index,item in enumerate(items):
            self.progress_numerator += 1

            df_source = results[ futures_map_source[str(index) + ':' +item['source']] ]
            df_dest = results[ futures_map_dest[str(index) + ':' +item['dest']] ]

            total_files_found += len(df_source)
            total_files_found += len(df_dest)
            print(f' Files Found {total_files_found}',end='\r')

            if len(df_source) + len(df_dest) == 0 :
                self.scan_cache = pd.concat([self.scan_cache,pd.DataFrame()])
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

            
            df = pd.merge(df_source,df_dest,how='outer',on='relpath')

            df['index'] = index
            if filter_index != None:
                df['index'] = filter_index

            df['archive_dir'] = item['archive_dir']
            # df['options'] = item.get('options','')
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
            df.loc[ ((df['backup'] == True) & (df['fullpath_x'].isna() == False) & (df['fullpath_y'].isna() == False)) ,'archive'] = True
                    
            self.scan_cache = pd.concat([self.scan_cache,df])
            # print('scan: ',self.bar(len(self.scan_cache),len(self.items())),end='\r')

        if self.save_cache_as_csv == True:
            fn = os.path.join(self.logger.dir,f'cache_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.csv')
            self.logger.info(f'cache saved: {fn}')
            self.scan_cache.to_csv(fn,index=False)

        self.logger.info(f'scan_cache size: {len(self.scan_cache)}')
        self.logger.info('end')

    def _backup(self,row:dict) -> dict:
        """perform all the actions for backup one row of data

        Args:
            row (_type_): _description_

        Returns:
            _type_: returns a row and the actions that were performed
        """

        result = {'actions':[],'row': row}

        if row.get('skip',False) == True:
            result['actions'].append('skip')
            return result

        if row.get('archive',False) == True:
            #archive the file
            try:
                rpmf = '\\'.join(row['relpath'].split('\\')[:-1])
                # adir = row["archive_dir"]
                # if len(rpmf) > 0:
                #     adir = os.path.join(row["archive_dir"],rpmf)
                # self.logger.info(adir)

                adir = os.path.join(row['rootpath_y'],row["archive_dir"],rpmf)
                self.logger.info(adir)

                pathlib.Path(adir).mkdir(parents=True, exist_ok=True)
                shutil.copy2(row["fullpath_y"],adir)
                result['actions'].append('archive')
            except Exception as e:
                self.logger.error(str(e))

        if row.get('remove_dest',False) == True:
            try:
                os.remove(row["fullpath_y"])
                result['actions'].append('remove_dest')
            except Exception as e:
                self.logger.error(str(e))

        if row.get('backup',False) == True:
            try:
                dest = row['fullpath_x'].replace(row['rootpath_x'], row['rootpath_y'])
                pathlib.Path('\\'.join(dest.split('\\')[:-1])).mkdir(parents=True, exist_ok=True)
                shutil.copy2(row["fullpath_x"],dest)
                result['actions'].append('backup')
            except Exception as e:
                self.logger.error(str(e))

        return result

    def backup(self):
        """backups all the rows of data
        """
        self.logger.info('start')
        if len(self.scan_cache) == 0:
            self.logger.info('no scan_cache detected')
            self.scan()
        
        records = self.scan_cache.to_dict(orient='records')

        self.progress_denominator += len(records)
        executor = ThreadPoolExecutor(4)
        futures = []
        self.logger.info('1/4')
        for index,record in enumerate(records):
            self.progress_numerator += 1

            if index%100 == 0:
                print( 'backup process 1/4: ', self.bar((index+1),len(records)) ,end='\r')

            f = executor.submit(self._backup, (record))
            futures.append(f)
        print( 'backup process 1/4: ', self.bar(1,1))
        
        results = []
        self.progress_denominator += len(futures)
        self.logger.info('2/4')
        for index,f in enumerate(futures):
            self.progress_numerator += 1
            if index%100 == 0:
                print( 'backup process 2/4: ', self.bar((index+1),len(records)) ,end='\r')
            results.append(f.result())

        indexes= []
        self.progress_denominator += len(results)
        for r in results:
            self.logger.info(r)
            self.progress_numerator += 1
            i = int(r['row']['index'])
            if i in indexes:
                pass
            else:
                indexes.append(i)
                self.config.data['items'][i]['lastbackup'] = datetime.datetime.now().strftime('%Y%m%d%H%M')
                print(i,datetime.datetime.now().strftime('%Y%m%d%H%M'))
        self.config.save()

        print( 'backup process 2/4: ', self.bar(1,1))

        ## clean up process
        rootpaths_y = self.scan_cache.rootpath_y.unique().tolist()

        self.progress_denominator += len(rootpaths_y)
        executor = ThreadPoolExecutor(4)
        futures = []
        self.logger.info('3/4')
        for index,rpy in enumerate(rootpaths_y):
            self.progress_numerator += 1

            if index%100 == 0:
                print( 'backup process 3/4: ', self.bar((index+1),len(rootpaths_y)) ,end='\r')

            f = executor.submit(self.clean_empty_folders, (rpy))
            futures.append(f)
        print( 'backup process 3/4: ', self.bar(1,1))
        
        self.progress_denominator += len(futures)
        self.logger.info('4/4')
        for index,f in enumerate(futures):
            self.progress_numerator += 1
            if index%100 == 0:
                print( 'backup process 4/4: ', self.bar((index+1),len(rootpaths_y)) ,end='\r')
            f.result()

        print( 'backup process 4/4: ', self.bar(1,1))
        print('done')
        self.logger.info('end')
        
        self.progress_numerator = 0
        self.progress_denominator = 0
        self.scan_cache = []

    def clean_empty_folders(self,dir:str):
        """removes blank folders from the dir

        Args:
            dir (str): _description_
        """
        # cleaning 
        clean_count = 1
        while clean_count > 0:
            # remove folders that are empty
            clean_count = 0
            for dirpath, dirnames, filenames in os.walk(dir):
                if len(dirnames) == 0 and len(filenames) == 0:
                    self.logger.info(f'{dirpath} is empty - deleting')
                    os.rmdir(dirpath)
                    clean_count += 1

    def get_progress(self) -> float:
        """returns a float between 0.0 and 1.0 to show progress

        Returns:
            _type_: _description_
        """
        if self.progress_denominator > 0:
            return self.progress_numerator/self.progress_denominator
        else:
            return 0.0

    def backup_One(self,index:int):
        """performs a backup on one item

        Args:
            index (int): the index number of the item
        """
        try:
            self.logger.info(f'only backing up one: {self.items()[index]}')
            self.scan(index)
            if len(self.scan_cache) > 0:
                self.backup()
        except Exception as e:
            self.logger.error(str(e))
    
    def remove_One(self,index:int):
        """removes an item from the list of items

        Args:
            index (int): the index of the item that will be removed
        """
        try:
            self.logger.info(f'removing one: {self.items()[index]}')
            del self.config.data['items'][index]
            self.config.save()
        except Exception as e:
            self.logger.error(str(e))

    def toggle_enable(self,index:int):
        """toggles enable and disable at the index

        Args:
            index (int): the item index that will be toggled
        """
        try:
            self.logger.info(f'toggle item: {self.items()[index]}')
            new_value = not (self.config.data['items'][index]['enable'] )
            self.config.data['items'][index]['enable'] = new_value
            self.config.save()
        except Exception as e:
            self.logger.error(str(e))

    def _replace(self,col:str,oldvalue:str,newvalue:str):
        """replaces values in a column

        Args:
            col (str): _description_
            oldvalue (str): _description_
            newvalue (str): _description_
        """
        self.logger.info(f'replace {oldvalue} with {newvalue} in {col}')
        for item in self.items():
            try:
                item[col] = item[col].replace(oldvalue,newvalue)
            except Exception as e:
                self.logger.error( str(item) + ' - ' + str(e)) 
        self.process_config()

    def replace_root_dest(self,oldvalue:str,newvalue:str):
        """replaces values in the root_dest column

        Args:
            oldvalue (str): _description_
            newvalue (str): _description_
        """
        self._replace('root_dest',oldvalue,newvalue)
    
    def add_new_item(self):
        """adds new item to list
        """
        self.logger.info('adding new item')
        new = self.default_config['items'][0].copy()
        self.config.data['items'].append(new)
        self.config.save()




if __name__ == '__main__':

    yabus = YABUS(verbose=False)
    yabus.backup()


