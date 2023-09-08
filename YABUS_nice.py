"""\
YABUS
yet another backup script

this is a UI for the main YABUS script
"""
__author__ = "Justin Garza"
__copyright__ = "Copyright 2023, Justin Garza"
__credits__ = ["Justin Garza"]
__license__ = "FSL"
__version__ = "1.5"
__maintainer__ = "Justin Garza"
__email__ = "Justin Garza"
__status__ = "Development"

from nicegui import ui, Client,Tailwind
from nicegui.elements import markdown

import os
DIR = os.path.dirname(os.path.realpath(__file__))

import json5 as json

# data manager
from utils.dataMan import DataManager
from utils.driveList import get_drives

# logging
import logging
from logging import Logger
from utils.logMan import createLogger
from io import StringIO

logStream = StringIO()

logger = createLogger(
    root=os.path.join(DIR,'log'),
    useStreamHandler=False,
    strIO=logStream,
    )


from YABUS import YABUS

yabus = YABUS(logger=logger)


# building the GUI


dark = ui.dark_mode()
# dark.style('margin: 0; padding: 0;')
dark.enable()

ui.colors(
    primary='#0d6efd', 
    secondary='#6c757d', 
    accent='#052a63', 
    positive='#198754', 
    negative='#dc3545',
    info='#0dcaf0',
    warning='#ffc107'
    )

about_md = '''
# YABUS (NiceGUI interface)
## yet another back up script

* author: Justin Garza  
* copyright: Copyright 2023, Justin Garza  
* credits:["Justin Garza"]  
* license: FSL  
* version: 0.1  
* maintainer: Justin Garza  
* email: JGarza9788@gmail.com  
* status: Development  

## NiceGui
[NiceGui.io](https://nicegui.io/)
'''



def format_lastbackup(lastbackup:str):
    if lastbackup == None:
        return 'None'
    return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]


def add_item():
    yabus.add_new_item()
    yabus_items_ui.refresh()
    ui.notify('added new item',position='top-right')

def remove_item(index:int):
    yabus.remove_One(index)
    yabus_items_ui.refresh()
    ui.notify(f'removed {index}',position='top-right')

def run_all():
    # yabus.process_config()
    # yabus_items_ui.refresh()
    yabus.backup()
    ui.notify('running all items',position='top-right')

def run_one(index:int):
    yabus.backup_One(index)

    yabus_items_ui.refresh()
    ui.notify(f'running {index}',position='top-right')
    yabus_items_ui.refresh()

def toggle_enable(index:int):
    yabus.toggle_enable(index)
    yabus_items_ui.refresh()
    ui.notify(f'{index} is {yabus.items()[index]["enable"]}',position='top-right')

def change_value(value,name,index:int):
    # print(e.value)
    # print(e.label)
    yabus.config.data['items'][index][name] = value
    yabus.config.save()
    # yabus_items_ui.refresh()
    ui.notify(f'{index} {name} is now {value}',position='top-right')

# btn_style = Tailwind().text_color('black').font_weight('bold').background_color('bg-blue-700')
# btn_style = Tailwind().background_color('red-700')
black_text = Tailwind().text_color('black')



def create_row(index:int, item):
    with ui.row().style('height: 5rem; padding: auto'):
        ui.label(f'{index:03d}').style('height: 100%; line-height:5rem; text-align: center;')
        ui.label("⬛" if item['runable'] == True else "⚠️").style('height: 100%; line-height:5rem; text-align: center;')
        ui.checkbox('',value=item['enable'],on_change=lambda: toggle_enable(index)).style('height: 100%')

        btn_run = ui.button('▶️',color='none',on_click=lambda: run_one(index))
        btn_run.style('height: 100%')

        src = ui.input(label='source', value=item['source'],on_change=lambda e: change_value(e.value,'source',index) )
        src.style('width: 20rem; height: 100%')
        
        # ui.input(label='root_dest', value=item['root_dest'],on_change=lambda e: change_value(e.value,'root_dest',index) ).style('width: 20rem; height: 100%').on('blur',lambda: yabus_items_ui.refresh())

        rd = ui.input(label='root_dest', value=item['root_dest'],on_change=lambda e: change_value(e.value,'root_dest',index) )
        rd.style('width: 20rem; height: 100%')
        # rd.on('blur',lambda: yabus_items_ui.refresh())
        # rd.on_value_change(lambda: yabus_items_ui.refresh())

        ui.input(label='ex_reg', value=item['ex_reg'] ).style('width: 10rem; height: 100%')
        ui.label(f'{format_lastbackup(item["lastbackup"])}').style('width: 10rem; height: 100%; line-height:5rem; text-align: center;')
        ui.button('❌',color='none',on_click=lambda: remove_item(index)).style('height: 100%')

@ui.refreshable
def yabus_items_ui():
    yabus.process_config()
    for index,item in enumerate(yabus.items()):
        create_row(index,item)
        ui.splitter(horizontal=True)
    ui.notify('refreshed',position='top-right')
    log_md_ui.refresh()

@ui.refreshable
def log_md_ui():
    lst = logStream.getvalue().split('\n')
    ui.markdown('\n\n'.join(lst[-300:]))
    # TA = ui.textarea(value=logStream.getvalue())
    # TA.style('overflow: visible')


with ui.tabs().classes('w-full,items-start') as tabs:
    main_ui = ui.tab('Main')
    log_ui = ui.tab('Log')
    about_ui = ui.tab('About')
with ui.tab_panels(tabs, value=main_ui).classes('w-full'):
    with ui.tab_panel(main_ui):
        # ui.label('First tab')
        # btn = 
        # ui.button('+ Item', on_click=lambda: add_item()).classes('bg-indigo-950',remove='bg_primary')
        # ui.button('+ Item', on_click=lambda: add_item()).tailwind(btn_style)
        # btn.classes('bg-blue-700')

        with ui.row():
            ui.button('+ Item',color='secondary', on_click=lambda: add_item())
            # ui.label('')
            ui.button('Refresh',color='secondary', on_click=lambda: yabus_items_ui.refresh())
            ui.button('Run All',color='info', on_click=lambda: run_all()).tailwind(black_text)

        ui.splitter(horizontal=True)

        yabus_items_ui()



    with ui.tab_panel(log_ui):
        log_md_ui()
    with ui.tab_panel(about_ui):
        ui.markdown(about_md)


# run the program
ui.run(
    native=True, 
    window_size=(1380, 1380), 
    fullscreen=False
    )


