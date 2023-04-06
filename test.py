import os,time
import shutil
import json5 as json
from dataMan import DataManager

from main import YABUS

def clean():
    try:
        shutil.rmtree('.\\test')
    except:
        pass

def prepare_files():
    os.mkdir('.\\test')
    os.mkdir('.\\test\\A')
    os.mkdir('.\\test\\B')
    os.mkdir('.\\test\\B\\A')


    One = DataManager('.\\test\\A\\One.json')
    Two = DataManager('.\\test\\A\\Two.json')

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

    yabus = YABUS(config_dir=config.file_dir,verbose=False,save_cache_as_csv=True)
    yabus.backup()

def checks():

    print('checking files')
    
    #these files should exists
    filelist = [
            '.\\test\\A\\One.json',
            '.\\test\\A\\Two.json',
            '.\\test\\B\\A\\One.json',
            '.\\test\\B\\A\\Two.json',
        ]

    for f in filelist:
        assert os.path.isfile(f), f' {f} should exists'

    #count the number of files in .archive, should be 2
    filelist = []
    archive_dir = '.\\test\\B\\A\\.archive'
    for dirpath, dirnames, filenames in os.walk(archive_dir):
        for filename in filenames:
            filelist.append(os.path.join(dirpath,filename))
    
    assert len(filelist) == 2, 'should archive 2 files'

    # make sure the backup matches the original
    with open('.\\test\\A\\Two.json','r') as fileA:
        with open('.\\test\\B\\A\\Two.json','r') as fileB:
            assert json.load(fileA) == json.load(fileB)

    print('please see errors above, if any')

if __name__ == '__main__':
    clean()
    prepare_files()
    run_yabus()
    checks()
    clean()


# this is the result that is expected 
"""
\\test\\A
>One.json 
>Two.json

.\\test\\B\\A
>One.json
>Two.json
.archive\\############\\
>Two.json 
>Three.json
"""

    


