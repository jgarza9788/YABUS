import typer
app = typer.Typer()
from rich import print
# from rich.text import Text

from typing import Union

import os,re
import json5 as json
import pandas as pd

import nerdfonts as nf

# data manager
from utils.dataMan import DataManager
from utils.driveList import get_drives,get_drivedata_details

# logging
import logging
from logging import Logger
from utils.logMan import createLogger
from io import StringIO
# import time

from YABUS import YABUS


DIR = os.path.dirname(os.path.realpath(__file__))

logStream = StringIO()

logger = createLogger(
    root=os.path.join(DIR,'log'),
    useStreamHandler=False,
    strIO=logStream,
    )

# init YABUS obj
yabus = YABUS(
            config_dir = os.path.join(DIR,'config.json'),
            verbose= False,
            logger = logger
            )


def process_config():
    yabus.process_config()
    # os.system('cls')

def format_lastbackup(lastbackup:str):
    if lastbackup == None:
        return 'None'
    return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]

def format_bool(value:str):
    value = str(value).lower()
    if value in ['y','yes','1','true']:
        # return Text().append(nf.icons['fa_check'],style="green")
        return '[X]'
    else:
        return '[ ]'
        # return Text().append(nf.icons['fa_close'],style="red")
        # return nf.icons['fa_close']

def change_data(index:str,name:str,value):
    errors = []
    for i in index.split(','):
        try:
            yabus.config.data['items'][int(i)][name] = value
        except Exception as e:
            logger.debug(e)
            errors.append({"index":i,"message":e})
    return errors

@app.command()
def show():
    """shows the config data
    """
    df = pd.DataFrame(yabus.config.data['items'])
    df['lastbackup'] = df['lastbackup'].apply(format_lastbackup)
    df['enable'] = df['enable'].apply(format_bool)
    df['runable'] = df['runable'].apply(format_bool)
    df = df[['enable','runable','source','root_dest','ex_reg','lastbackup']]
    print(df)

@app.command()
def toggle_enable(indexes:str):
    """toggles the enable flag

    Args:
        indexes (str): a string of numbers separated by a comma
    
    Example:
        python YABUS_typer.py toggle-enable 0,1,2
    """
    # print(index)
    # print(type(index))
    errors = []
    for i in indexes.split(','):
        try:
            yabus.toggle_enable(index=int(i))
        except Exception as e:
            logger.debug(e)
            errors.append({"index":i,"message":e})
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def enable(indexes:str):
    """enable the ones in the index, and disables others

    Args:
        indexes (str): a string of numbers separated by a comma

    Example:
        python YABUS_typer.py enable 0,1,2
    """
    # print(index)
    # print(type(index))

    errors = []
    ilist = indexes.split(',')
    for index,i in enumerate(yabus.items()):
        try:
            if str(index) in ilist:
                yabus.config.data['items'][int(index)]['enable'] = True
            else:
                yabus.config.data['items'][int(index)]['enable'] = False
        except Exception as e:
            logger.debug(e)
            errors.append({"index":i,"message":e})

    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def source(indexes:str,new_source:str):
    """change the source

    Args:
        indexes (str): index(s) to change
        new_source (str): new value

    Example:
        python YABUS_typer.py source 0,1,2 C:\\
    """

    errors = change_data(indexes,'source',new_source)    
    yabus.config.save()
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def root_dest(indexes:str,new_root_dest:str):
    """change the root_dest

    Args:
        indexes (str): index(s) to change
        new_root_dest (str): new value

    Example:
        python YABUS_typer.py root-dest 0,1,2 C:\\
    """
    errors = change_data(indexes,'root_dest',new_root_dest)    
    yabus.config.save()
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def ex_reg(indexes:str,new_ex_reg:str):
    """change the ex_reg, this is used to exclude any file that matches this regex pattern

    Args:
        indexes (str): index(s) to change
        new_ex_reg (str): new value

    Example:
        python YABUS_typer.py ex-reg 0,1,2 .git
    """
    errors = change_data(indexes,'ex_reg',new_ex_reg)    
    yabus.config.save()
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def new_item():
    """adds a new item
    """
    try:
        yabus.add_new_item()
    except Exception as e:
        logger.debug(e)
        print(e)
    process_config()
    show()

@app.command()
def add():
    """adds a new item
    """
    new_item()

@app.command()
def delete_item(indexes:str):
    """deletes an item
    """

    indexes = [int(i) for i in indexes.split(',')]
    indexes.sort(reverse=True)

    for i in indexes:
        try:
            yabus.remove_One(int(i))
        except Exception as e:
            pass
    process_config()
    show()

@app.command()
def delete(indexes:str):
    """deletes an item
    """
    delete_item(indexes)

@app.command()
def remove(indexes:str):
    """deletes an item
    """
    delete_item(indexes)

@app.command()
def run_all():
    """runs all enabled and runable items"""
    try:
        yabus.backup()
        process_config()
        # log_summary()
        show()
    except Exception as e:
        print(e)

@app.command()
def run_one(index:int):
    """runs one item, must be enabled and runable"""
    try:
        yabus.backup_One(index)
        process_config()
        # log_summary()
        show()
    except Exception as e:
        print(e)

@app.command()
def run():
    """runs all enabled and runable items"""
    run_all()

@app.command()
def run_obo():
    """runs all - but one by one"""
    for index,i in enumerate(yabus.items()):
        try:
            print(f"running {index} | {i['source']} --> {i['dest']}")
            yabus.backup_One(index)
            # log_summary()
            print()
        except Exception as e:
            print(e)
    process_config()        
    show()


# def log_summary():
#     """shows the log summary"""
#     log_text = logStream.getvalue().split('\n')[0:100]
#     log_text.reverse()
#     llist = ['Files to Process:',
#     'remove_dest Files:',
#     'Archive Files:',
#     'BackUp Files:',
#     'Skipped Files:',
#     'Files in Cache:'
#     ]

#     result = []
    
#     for i in log_text:
#         for j in llist:
#             if j in i:
#                 result.append(i)
#                 continue
#         if len(result) == len(llist):
#             continue
#     result = result[0:len(llist)]
#     print(*result,sep='\n')

@app.command()
def drives():
    """prints the drives"""
    # print(*get_drives(),sep='\n')
    # print(*get_drivedata_details(),sep='\n')

    for d in get_drivedata_details():
        if d.get('volumename','') == '':
            print(d['letter'])
        else:
            print(d['letter'],'(',d.get('volumename',''),')')
        print(f"{d['used_round']} GB / {d['size_round']} GB")
        print(f"{d['percent_used']}%")
        fillstr = ('#'* int(d['percent_used'] * (50/100))).ljust(50,'-')
        print( '[',fillstr , ']','\n')


if __name__ == "__main__":
    app()

