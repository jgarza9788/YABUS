
"""\
YABUS
yet another backup script

this is a UI for the main YABUS script
"""
__author__ = "Justin Garza"
__copyright__ = "Copyright 2023, Justin Garza"
__credits__ = ["Justin Garza"]
__license__ = "FSL"
__version__ = "1.0.1"
__maintainer__ = "Justin Garza"
__email__ = "Justin Garza"
__status__ = "Development"



import os,datetime,pathlib,time
import json5 as jason
import pandas as pd


import dearpygui.dearpygui as dpg
from dpgutils.theme import apply_theme
from dpgutils.menu import menu
# from dpgutils.items_window import items_window
import dpgutils.items_window as iw
from dpgutils.output_window import output_window

# import nerdfonts as nf

# used for multi threading
from concurrent.futures import ThreadPoolExecutor

# data manager
from utils.dataMan import DataManager

# logging
import logging
from logging import Logger
from utils.logMan import createLogger
from io import StringIO
# import time

from YABUS import YABUS

class MainWindow():

    def change_folder_callback(self,sender, app_data):
        try:
            self.logger.info('change_folder_callback')

            print('index: ',self.index)
            print("Sender: ", sender)
            print("App Data: ", app_data)

            self.yabus.config.data['items'][self.index][sender] = app_data['file_path_name']
            self.yabus.config.save()
            iw.build(self)

        except Exception as e:
            self.logger.error('change_folder_callback')
            print('sorry error!')
            print(str(e))

    def update_log(self):
        try:
            if (time.time() - self.rendertime) > 0.5:
                loglines = self.logStream.getvalue().split('\n')
                loglines.reverse()
                dpg.set_value('output_text', '\n'.join(loglines))
                self.rendertime = time.time()
        except:
            pass

    def __init__(self,config_dir=None,verbose=False):
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.verbose = verbose

        self.logStream = StringIO()

        self.logger = createLogger(
            root=os.path.join(self.dir,'log'),
            useStreamHandler=self.verbose,
            strIO=self.logStream,
            )
        self.config_dir = config_dir
        if self.config_dir == None or self.config_dir == '':
            self.config_dir = os.path.join(self.dir,'config.json')


        self.dpg_config = DataManager(
            file_dir=os.path.join(self.dir,'dpgutils','dpg_config.json'),
            logger=self.logger,
            default={}
            )

        self.rendertime = time.time()
        
        self.yabus = YABUS(
            config_dir = self.config_dir,
            save_cache_as_csv=self.verbose,
            verbose= self.verbose,
            logger = self.logger
            )

        dpg.create_context()
        # dpg.show_style_editor()

        self.dpg_config.data['theme_id'] = self.dpg_config.data.get('theme_id',8)
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()


        # try:
        #     t = get_theme(8)
        # except Exception as e:
        #     print(str(e))
        # print(type(t),t)
        # dpg.bind_theme(self.dpg_config.data['theme_id'])

        with dpg.font_registry():
            fontpath = os.path.join(self.dir,'dpgutils','Roboto_Mono_Nerd_Font_Complete_Mono.ttf')
            with dpg.font(fontpath, 15) as f1:
                default_font = f1
                self.default_font = default_font
                dpg.add_font_range(0x0100, 0xfeff)
            
            fontpath = os.path.join(self.dir,'dpgutils','Roboto_Mono_Bold_Nerd_Font_Complete_Mono.ttf')
            with dpg.font(fontpath, 25) as f2:
                large_font = f2
                self.large_font = large_font
                dpg.add_font_range(0x0100, 0xfeff)

        dpg.bind_font(default_font)
        # dpg.show_font_manager()  

        self.layout = os.path.join(self.dir,'dpgutils','layout.ini')
        dpg.configure_app(
            docking=True, 
            docking_space=True,
            load_init_file=self.layout,
            # wait_for_input=True
            # manual_callback_management=True
            ) 
        
        dpg.create_viewport(title="YABUS",width=1180,height=1180,x_pos = 400,y_pos = 25,)
        dpg.setup_dearpygui()

        self.items_window = '##items_window'
        self.output_window = '##output_window'

        menu(self)
        iw.items_window(self)

        # self.lastLogTm = 0 
        output_window(self)
        # logging.basicConfig(level=logging.DEBUG)
        # logging.setLogRecordFactory(self.update_log)
        

        # dpg.set_primary_window("##items_window", True)
        dpg.show_viewport()
        dpg.set_viewport_vsync(True)

        while dpg.is_dearpygui_running():
            self.update_log()
            dpg.render_dearpygui_frame()

        # dpg.start_dearpygui()
        dpg.destroy_context()  

        

    # def update_log(*args, **kwargs):
    #     print('*'*10)
    #     print(*args,sep='\n')
    #     print(**kwargs)
    #     print('*'*10)




    def add_new_item(self):
        self.yabus.add_new_item()
        self.yabus.process_config()
        iw.build(self)
        # self.update_output_text()

    def run_all_items(self):
        self.yabus.process_config()
        iw.build(self)
        self.yabus.backup()
        iw.build(self)
        # self.update_output_text()
    
    def run(self,index:int):
        self.yabus.process_config()
        iw.build(self)
        self.yabus.backup_One(index)
        iw.build(self)
        # self.update_output_text()

    def remove_item(self,index:int):
        self.yabus.remove_One(index)
        iw.build(self)
        # self.update_output_text()

    def enable_disable(self,index:int):
        # self.yabus.process_config()
        self.logger.info(f'{index}')
        self.yabus.enable_disable(index)
        iw.build(self)
        # self.update_output_text()


if __name__ == "__main__":
    MW = MainWindow(verbose=True)

    # for i in nf.icons:
    #     print(nf.icons[i],i)


