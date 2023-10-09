import os,time
import pandas as pd
import shutil
import json5 as json
from utils.dataMan import DataManager

DIR = os.path.dirname(os.path.realpath(__file__))


## Pandas Options
# show all the columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

from YABUS import YABUS

def clean():
    try:
        shutil.rmtree('.\\test')
    except:
        pass

def prepare_files():
    os.mkdir('.\\test')
    os.mkdir('.\\test\\A')
    os.mkdir('.\\test\\A\\A2')
    os.mkdir('.\\test\\B')
    os.mkdir('.\\test\\B\\A')


    One = DataManager('.\\test\\A\\One.json')
    Two = DataManager('.\\test\\A\\Two.json')

    Atwo = DataManager('.\\test\\A\\A2\\Atwo.json')

    # these will be placed in the .archive
    Three = DataManager('.\\test\\B\\A\\Three.json')

    #copy two
    shutil.copy2('.\\test\\A\\Two.json','.\\test\\B\\A\\Two.json')

    time.sleep(1)

    #edit .\\test\\A\\Two.json
    Two.data.append('hello')
    Two.save()


def run_yabus():
    dir = os.path.dirname(os.path.realpath(__file__))
    source = os.path.join(dir,'test','A')
    root_dest = os.path.join(dir,'test','B')
    

    data = {
        "items":[
        {
            "source": source,"root_dest": root_dest
        }
        ]
    }

    config = DataManager('.\\test\\config.json',default=data)

    yabus = YABUS(config_dir=config.file_dir,verbose=False)
    yabus.backup()

def mod_files():
    One = DataManager('.\\test\\A\\One.json')
    One.data.append('world')
    One.save()

    Atwo = DataManager('.\\test\\A\\A2\\Atwo.json')
    Atwo.data.append('123')
    Atwo.save()

    # os.mkdir('.\\test\\B\\A\\empty_file_will_be_deleted')

def run_yabus_2():
    config = DataManager('.\\test\\config.json')
    yabus = YABUS(config_dir=config.file_dir,verbose=False)
    yabus.backup()

def checks():

    print('checking files')
    
    #these files should exists
    filelist = [
            '.\\test\\A\\One.json',
            '.\\test\\A\\Two.json',
            '.\\test\\A\\A2\\Atwo.json',
            '.\\test\\B\\A\\One.json',
            '.\\test\\B\\A\\Two.json',
            '.\\test\\B\\A\\A2\\Atwo.json',
        ]

    for f in filelist:
        assert os.path.isfile(f), f' {f} should exists'

    #count the number of files in .archive, should be 4
    filelist = []
    archive_dir = '.\\test\\B\\A\\.archive'
    for dirpath, dirnames, filenames in os.walk(archive_dir):
        for filename in filenames:
            filelist.append(os.path.join(dirpath,filename))
    
    print(*filelist,sep='\n')
    assert len(filelist) == 4, 'should archive 4 files'

    # make sure the backup matches the original
    with open('.\\test\\A\\Two.json','r') as fileA:
        with open('.\\test\\B\\A\\Two.json','r') as fileB:
            assert json.load(fileA) == json.load(fileB)

    print('please see errors above, if any')


def scan_test():
    """perform a yabus.scan()"""
    clean()
    prepare_files()
    dir = os.path.dirname(os.path.realpath(__file__))
    source = os.path.join(dir,'test','A')
    root_dest = os.path.join(dir,'test','B')
    
    data = {
        "items":[
        {
            "source": source,"root_dest": root_dest
        }
        ]
    }

    config = DataManager('.\\test\\config.json',default=data)
    yabus = YABUS(config_dir=config.file_dir,verbose=False)

    yabus.clear_scan_cache()
    yabus.scan()

    print(*yabus.scan_cache.columns,sep='\n')
    yabus.scan_cache.to_csv(os.path.join(DIR,'cache.csv'))

def scan_v2_test():
    """perform a yabus.scan()"""
    clean()
    prepare_files()
    dir = os.path.dirname(os.path.realpath(__file__))
    source = os.path.join(dir,'test','A')
    root_dest = os.path.join(dir,'test','B')
    
    data = {
        "items":[
        {
            "source": source,"root_dest": root_dest
        }
        ]
    }

    config = DataManager('.\\test\\config.json',default=data)
    yabus = YABUS(config_dir=config.file_dir,verbose=True)

    yabus.process_config()
    print(yabus.items())
    yabus.clear_scan_cache()
    yabus.scan_v2()

    print(*yabus.scan_cache.columns,sep='\n')
    print(yabus.scan_cache)

    # yabus.backup()

    yabus.clear_scan_cache()
    yabus.scan_v2()

    # print(*yabus.scan_cache.columns,sep='\n')
    # print(yabus.scan_cache)
    yabus.scan_cache.to_csv(os.path.join(DIR,'cache_v2.csv'))

    yabus.clear_scan_cache()
    yabus.scan()

    # print(*yabus.scan_cache.columns,sep='\n')
    # print(yabus.scan_cache)
    yabus.scan_cache.to_csv(os.path.join(DIR,'cache.csv'))


def scan_speed():
    clean()
    prepare_files()
    t = time.time()
    # data = {
    #     "items":[
    #     {
    #         "source": r"C:\Users\JGarza\GitHub\YABUS",
    #         "root_dest": r"C:\Users\JGarza\Desktop"
    #     }
    #     ]
    # }

    data = {
        "items":[
        {
            "source": r"D:\UnityProjects",
            "root_dest": r"C:\Users\JGarza\Desktop"
        }
        ]
    }

    config = DataManager('.\\test\\config.json',default=data)
    yabus = YABUS(config_dir=config.file_dir,verbose=False)

    yabus.clear_scan_cache()
    t = time.time()
    yabus.scan()
    yabus.logger.info(f"v1 {time.time() -t}")
    print(f"v1 {time.time() -t}")

    # yabus.clear_scan_cache()
    # t = time.time()
    # yabus.scan_v2()
    # yabus.logger.info(f"v2 {time.time() -t}")
    # print(f"v2 {time.time() -t}")


if __name__ == '__main__':
    # clean()
    # prepare_files()
    # run_yabus()
    # time.sleep(5)
    # mod_files()
    # run_yabus_2()
    # checks()
    # clean()

    # scan_test()
    # clean()
    # scan_v2_test()
    # checks()

    scan_speed()

    # import pandas as pd
    # import json5 as json
    # df = pd.DataFrame(json.loads('[{"one":1,},]'))
    # print(df)


    


