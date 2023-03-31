import os,datetime,pathlib
import json5 as jason
import pandas as pd


# import subprocess as sp
# from threading import Thread
# from multiprocessing.pool import ThreadPool

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



def scan_folder(root:str):
    
    
    
    # rootnum_minus_one = len(root.split('\\')) - 1
    rootnum_minus_one = len(root.split('\\')) 
    # print(rootnum_minus_one)
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

            if len(result)%1000 == 0:
                print('Scanning:', ['|','/','-','\\'][index%4],len(result),' files found ',' '*100,end='\r')
            # print(f'Scanning: {len(result)} files')

            # print(os.stat(fullpath))

    # df = pd.DataFrame(result)
    return pd.DataFrame(result)


def process(row):
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

    return result



def process_item(item:dict):
    dir = os.path.dirname(os.path.realpath(__file__))

    if item.get('lastbackup',None) == None:
        item['lastbackup'] = datetime.datetime.now().strftime('%Y%m%d%H%M')

    logger = createLogger(root=os.path.join(dir,'log'),useStreamHandler=False)

    
    logger.info(f'raw item: {item}')
    
    # checks
    if item.get('source',None) == None:
        logger.error('no source')
        return 1

    if os.path.exists(item.get('source',None)) == False:
        logger.error('invalid source path ')
        return 1

    if item.get('root_dest',None) != None:
        logger.info('root_dest will be used, and override dest')
        item['dest'] = os.path.join(item['root_dest'], item['source'].split('\\')[-1] )

    if item.get('dest',None) == None:
        logger.error('no dest ')
        return 1

    if os.path.exists(item.get('dest',None)) == False:
        # make the full path
        # os.mkdir(item['dest'])
        pathlib.Path(item['dest']).mkdir(parents=True, exist_ok=True)

    item['options'] = item.get('options','') 

    # create archive directory
    archive_dir = os.path.join(item['dest'],'.archive',item['lastbackup'])
    pathlib.Path(archive_dir).mkdir(parents=True, exist_ok=True)

    print(f'{item["source"]} --> {item["dest"]}')
    logger.info(item)


    logger.info('Scanning Source and Dest')

    executor = ThreadPoolExecutor(12)
    futures = []
    for x in [item['source'],item['dest']]:
        f = executor.submit(scan_folder, (x))
        futures.append(f)
    
    results = []
    for f in futures:
        results.append(f.result())

    df_source = results[0]
    df_dest = results[1]

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

    logger.info('scan - done')
    logger.info('comparing files')

    df = pd.merge(df_source,df_dest,how='outer',on='relpath')

    df['archive_dir'] = archive_dir
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

    logger.info('compare - done')

    logger.info('prepare and process')

    records = df.to_dict(orient='records')

    # print('preparing...')
    executor = ThreadPoolExecutor(12)
    futures = []
    for index,record in enumerate(records):

        if index%500 == 0:
            p = (index+1)/len(records)
            print( 'preparing: ', ('#'*(int(p)*100)).ljust(100,'-') ,end='\r')

        f = executor.submit(process, (record))
        futures.append(f)
    print('done preparing')
    
    # print('processing...')
    results = []
    for index,f in enumerate(futures):

        if index%500 == 0:
            p = (index+1)/len(futures)
            print( 'processing: ', ('#'*(int(p)*100)).ljust(100,'-') ,end='\r')

        results.append(f.result())


    print('done processing')

    logger.info('commands')
    for r in results:
        logger.info(r)


if __name__ == '__main__':
    config = {
        # 'source': r'C:\Users\JGarza\Pictures',
        # 'source': r'D:\UnityProjects\JellyObject',
        'source': r'D:\UnityProjects',
        'root_dest': r'C:\Users\JGarza\Desktop\x',
        'options': '',
        'ex_reg':r'',
        'lastbackup': None #202303302110
    }
    process_item(config)

    # print(config)

