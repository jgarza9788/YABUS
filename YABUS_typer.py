import typer
app = typer.Typer()
from rich import print

from typing import Union

import os
import json5 as json
import pandas as pd

# data manager
from utils.dataMan import DataManager
from utils.driveList import get_drives

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
    useStreamHandler=True,
    strIO=logStream,
    )

# init YABUS obj
yabus = YABUS(
            config_dir = os.path.join(DIR,'config.json'),
            verbose= True,
            logger = logger
            )


def process_config():
    yabus.process_config()
    os.system('cls')

def format_lastbackup(lastbackup:str):
    if lastbackup == None:
        return 'None'
    return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]


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
    df = df[['enable','runable','source','root_dest','ex_reg','lastbackup']]
    print(df)

@app.command()
def toggle_enable(index):
    """toggles the enable flag

    Args:
        index (_type_): the index(s) to toggle
    """
    # print(index)
    # print(type(index))
    errors = []
    for i in index.split(','):
        try:
            yabus.toggle_enable(index=int(i))
        except Exception as e:
            logger.debug(e)
            errors.append({"index":i,"message":e})
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def source(index:str,new_source:str):
    """change the source

    Args:
        index (str): index(s) to change
        new_source (str): new value
    """

    errors = change_data(index,'source',new_source)    
    yabus.config.save()
    process_config()
    print(*errors,sep='\n')
    show()


@app.command()
def root_dest(index:str,new_root_dest:str):
    """change the root_dest

    Args:
        index (str): index(s) to change
        new_root_dest (str): new value
    """
    errors = change_data(index,'root_dest',new_root_dest)    
    yabus.config.save()
    process_config()
    print(*errors,sep='\n')
    show()

@app.command()
def ex_reg(index:str,new_ex_reg:str):
    """change the ex_reg

    Args:
        index (str): index(s) to change
        new_ex_reg (str): new value
    """
    errors = change_data(index,'ex_reg',new_ex_reg)    
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
        show()
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
def delete_item(index:str):
    """deletes an item
    """

    index = [int(i) for i in index.split(',')]
    index.sort(reverse=True)

    for i in index:
        try:
            yabus.remove_One(int(i))
        except Exception as e:
            pass
    process_config()
    show()

@app.command()
def delete(index:str):
    delete_item(index)

@app.command()
def remove(index:str):
    delete_item(index)

@app.command()
def run_all():
    try:
        yabus.backup()
        process_config()
        show()
    except Exception as e:
        print(e)

@app.command()
def run_one(index:int):
    try:
        yabus.backup_One(index)
        process_config()
        show()
    except Exception as e:
        print(e)

@app.command()
def show_log(lines:str="50"):
    lines = int(lines)
    log_text = logStream.getvalue().split('\n')
    log_text.reverse()
    log_text = log_text[0:lines]
    print(*log_text,sep='\n')

@app.command()
def drives():
    print(*get_drives(),sep='\n')

if __name__ == "__main__":
    os.system('cls')
    app()