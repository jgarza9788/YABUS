
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



import os,datetime,pathlib,time
import json5 as jason
import pandas as pd


import dearpygui.dearpygui as dpg
from dpgutils.theme import apply_theme
from dpgutils.menu import menu
# from dpgutils.items_window import items_window
import dpgutils.main_window as mw
from dpgutils.log_window import log_window
# from dpgutils.drive_window import drive_window

# used for multi threading
from concurrent.futures import ThreadPoolExecutor

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
            self.yabus.process_config()
            self.yabus.config.save()
            mw.build(self)

        except Exception as e:
            print(str(e))

    def update_log(self):
        """updates the log
        """
        try:
            loglines = self.logStream.getvalue().split('\n')
            loglines.reverse()
            # loglines = loglines[0:1000]
            dpg.set_value('log_text', '\n'.join(loglines))
            self.rendertime = time.time()
        except:
            pass

    def __init__(self,config_dir:str=None,verbose:bool=False):
        """initalizes the application

        Args:
            config_dir (str, optional): _description_. Defaults to None.
            verbose (bool, optional): _description_. Defaults to False.
        """
        self.old_lensc = 0
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

        self.main_window = '##main_window'
        self.log_window = '##log_window'
        # self.drive_window = '##drive_window'

        self.get_drives = get_drives

        menu(self)
        log_window(self)
        # iw.items_window(self)
        mw.main_window(self)
        # drive_window(self)

        # dpg.set_primary_window("##items_window", True)
        dpg.show_viewport()
        # dpg.maximize_viewport()
        dpg.set_viewport_vsync(True)

        self.rendertime = 0.0

        while dpg.is_dearpygui_running():

            # we do not need to render these every frame
            # it's not a video game
            if (time.time() - self.rendertime) > 0.25:
                self.update_log()
                self.update_pb()
                self.rendertime = time.time()
                mw.redrive(self.get_drives)

                # if self.drives != get_drives():
                #     dstr = ''
                #     for d in self.drives:
                #         dstr += f'{d["letter"]} : {d["label"]} \n'
                #     dpg.set_value('##drives', dstr)

            dpg.render_dearpygui_frame()

        # dpg.start_dearpygui()
        dpg.destroy_context()  

    def update_pb(self):
        """updates the progress bar
        """
        status, percent = self.yabus.get_progress()
        # print('\n\n',status,percent,'\n\n')

        for i in range(1):
            try:
                # dpg.configure_item(f'##progress_percent{i}', label= '{:0.4f}'.format(percent * 100.0) )
                dpg.configure_item(f'##progress_status{i}', label= status )
                dpg.configure_item(f'##progress_bar{i}', default_value=percent)
            except:
                pass
            # except Exception as ex:
            #     self.logger.error(ex)

            try:

                sc = self.yabus.scan_cache.copy()
                if len(sc) > 0 and len(sc) != self.old_lensc:
                    sc = sc.fillna(0)
                    details = ''
                    details += f'Files: {len(sc)}\n'
                    details += f'Skip: {len(sc[sc.skip == True])}\n'
                    details += f'BackUp: {len(sc[sc.backup == True])}\n'
                    details += f'Archive: {len(sc[sc.archive == True])}\n'
                    details += f'-----\n'

                    totalcnt = len(sc)
                    indexes = list(sc.copy()["index"].unique())

                    for inx in indexes:
                        inxcnt = len(sc[sc["index"] == inx])
                        details += f'{inx} : {inxcnt} : {(inxcnt/totalcnt)*100 :.2f}%\n'
                    
                    dpg.configure_item(f'##progress_details{i}', label=details)

                    self.old_lensc = len(sc)
            
            # except:
            #     pass
            except Exception as ex:
                self.logger.error(ex)

    def add_new_item(self):
        """adds a new item
        """
        self.yabus.add_new_item()
        self.yabus.process_config()
        mw.build(self)

    def remove_last_item(self):
        self.yabus.remove_last_item()
        mw.build(self)

    def run_all_items(self):
        """runs all the items
        """
        self.yabus.process_config()
        mw.build(self)
        self.yabus.clear_scan_cache()
        self.yabus.backup()
        mw.build(self)
    
    def run(self,index:int):
        """runs one item

        Args:
            index (int): _description_
        """
        self.yabus.process_config()
        mw.build(self)
        self.yabus.backup_One(index)
        mw.build(self)
        # self.update_output_text()

    def remove_item(self,index:int):
        """removes an item

        Args:
            index (int): _description_
        """
        self.yabus.remove_One(index)
        mw.build(self)
        # self.update_output_text()

    def toggle_enable(self,index:int):
        """toggles enable and disable at the index

        Args:
            index (int): the item index that will be toggled
        """
        self.yabus.toggle_enable(index)
        self.yabus.process_config()
        mw.build(self)


if __name__ == "__main__":
    MW = MainWindow(verbose=False)



