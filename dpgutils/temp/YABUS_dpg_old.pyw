
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
import dpgutils.items_window_v2 as iw
# import dpgutils.scanvis_window as sv
from dpgutils.output_window import output_window

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

    def change_folder_callback(self,sender:str, app_data:dict):
        """a callback to change the folder data

        Args:
            sender (str): the item that sent the message
            app_data (dict): additional data that might be sent
        """
        try:
            print('index: ',self.index)
            print("Sender: ", sender)
            print("App Data: ", app_data)

            self.yabus.config.data['items'][self.index][sender] = app_data['file_path_name']
            self.yabus.config.save()
            self.yabus.process_config()
            iw.build(self)

        except Exception as e:
            print(str(e))

    def update_log(self):
        """updates the log
        """
        try:
            loglines = self.logStream.getvalue().split('\n')
            loglines.reverse()
            # loglines = loglines[0:500]
            dpg.set_value('output_text', '\n'.join(loglines))
        except:
            pass

    def __init__(self,config_dir:str=None,verbose:bool=False):
        """initalizes the application

        Args:
            config_dir (str, optional): _description_. Defaults to None.
            verbose (bool, optional): _description_. Defaults to False.
        """
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

        self.yabus = YABUS(
            config_dir = self.config_dir,
            verbose= self.verbose,
            logger = self.logger
            )

        dpg.create_context()
        # dpg.show_style_editor()

        self.dpg_config.data['theme_id'] = self.dpg_config.data.get('theme_id',8)
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()

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
        
        dpg.create_viewport(title="YABUS",width=1280,height=800,x_pos = 400,y_pos = 25,)
        dpg.setup_dearpygui()

        self.items_window = '##items_window'
        self.output_window = '##output_window'
        self.scanvis_window = '##scanvis_window'

        menu(self)
        output_window(self)
        iw.items_window(self)

        # iw.items_window(self)
        # sv.scanvis_window(self)

        # dpg.set_primary_window("##items_window", True)
        dpg.show_viewport()
        dpg.set_viewport_vsync(True)

        self.rendertime0 = 0.0
        # self.rendertime1 = 0.0

        xtime = 0.0

        while dpg.is_dearpygui_running():

            # we do not need to render these every frame
            # it's not a video game
            if (time.time() - self.rendertime0) > 0.25:

                # xtime = time.time()
                self.update_log()
                # self.logger.info(f'update log: {time.time() - xtime} ')
                # xtime = time.time()
                self.update_pb()
                # self.logger.info(f'update pd: {time.time() - xtime} ')
                # xtime = time.time()
                # self.update_scanvis()
                # self.logger.info(f'update scanvis: {time.time() - xtime} ')
                # xtime = time.time()
                self.rendertime0 = time.time()
            
            # if (time.time() - self.rendertime1) > 1.0:
            #     self.update_scanvis()
            #     self.rendertime1 = time.time()

            dpg.render_dearpygui_frame()

        # dpg.start_dearpygui()
        dpg.destroy_context()  

    def update_scanvis(self):
        # if len(self.yabus.scan_cache) == 0 and self.yabus.progress_status != 'scanning files':
        # if len(self.yabus.scan_cache) == 0:
        #     return 
    
        sv.build_scanvis(self)

    def update_pb(self):
        """updates the progress bar
        """
        slices = ['|','/','-','\\']
        # dpg.configure_item("##progress_spinner", label=slices[self.yabus.progress_numerator%len(slices)])

        status, percent = self.yabus.get_progress()
        # print('\n\n',status,percent,'\n\n')

        for i in range(2):
            try:
                dpg.configure_item(f'##progress_percent{i}', label= '{:0.4f}'.format(percent * 100.0) )
                dpg.configure_item(f'##progress_status{i}', label= status )
                dpg.configure_item(f'##progress_bar{i}', default_value=percent)
            except:
                pass

    def add_new_item(self):
        """adds a new item
        """
        self.yabus.add_new_item()
        self.yabus.process_config()
        iw.build(self)
        # self.update_output_text()

    def remove_last_item(self):
        self.yabus.remove_last_item()
        iw.build(self)

    def run_all_items(self):
        """runs all the items
        """
        self.yabus.process_config()
        iw.build(self)
        self.yabus.clear_scan_cache()
        self.yabus.backup()
        iw.build(self)
        # self.update_output_text()
    
    def run(self,index:int):
        """runs one item

        Args:
            index (int): _description_
        """
        self.yabus.process_config()
        iw.build(self)
        self.yabus.backup_One(index)
        iw.build(self)
        # self.update_output_text()

    def remove_item(self,index:int):
        """removes an item

        Args:
            index (int): _description_
        """
        self.yabus.remove_One(index)
        iw.build(self)
        # self.update_output_text()

    def toggle_enable(self,index:int):
        """toggles enable and disable at the index

        Args:
            index (int): the item index that will be toggled
        """
        self.yabus.toggle_enable(index)
        iw.build(self)


if __name__ == "__main__":
    MW = MainWindow(verbose=True)



