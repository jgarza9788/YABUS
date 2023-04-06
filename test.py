import os,time
import shutil
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

    time.sleep(5)

    #edit .\\test\\A\\Two.json
    Two.data.append('hello')
    Two.save()


def run_test():
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

    yabus = YABUS(config_dir=config.file_dir,verbose=True,save_cache_as_csv=True)
    yabus.backup()

def checks():
    pass 
    # todo

if __name__ == '__main__':
    clean()
    prepare_files()
    run_test()


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

    


