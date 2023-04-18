YABUS
---
yet another back up script


# Description
On windows there is a lack of good backup scripts.  
This project has the following features.
1. uses multiprocessing to quickly backup files.
2. outputs logs and csv files 
3. stores old versions in .archive directories
4. DearPyGUI version with themes!


# road map
* cli 
* update the dearpygui 
* ttkbootstrap


# how to use?

## install requirements
```
pip install -r requirements.txt
```

## in a python file

1. create/edit the .\config.json
   * please see the config.json file
     * source: the folder you want to backup
     * root_dest: is the root of where you want the folder backup to
       * for many people this would be a D: drive or another drive
     * ex_reg: excludes any file that matches this regex pattern
     * lastbackup: the last time this set was backuped up
     * enabled: weather this item is enabled or not.
     * dest: the actual destination we are backing up to
       * this will be overwritten by the root_dest
     * archive_dir: the archive directory for this set 
     * runnable: weather it's possible to execute this item
```
from YABUS import YABUS
yabus = YABUS( config_dir = '.\config.json')
yabus.backup()
```

## using the dearpygui version
```
python YABUS_dpg.py
```


<video width="640" height="480" controls>
  <source src="./misc/20230417.mp4" type="video/mp4">
</video>

<!-- ![image](/misc/202304092225.png) -->
