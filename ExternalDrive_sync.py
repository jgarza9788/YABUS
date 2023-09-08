import os,time
import shutil
import json5 as json
from utils.dataMan import DataManager
from YABUS import YABUS 

config = DataManager('.\\misc\\ExternalDrive_config.json')
yabus = YABUS(config_dir=config.file_dir,verbose=True)
yabus.backup()