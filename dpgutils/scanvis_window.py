import os,re
# import numpy as np
import dearpygui.dearpygui as dpg
import dpgutils.misc as misc 


last_len_scan_cache = 0

def build_scanvis(self):
    global last_len_scan_cache
    if last_len_scan_cache == len(self.yabus.scan_cache):
        return

    try:
        dpg.delete_item("##sv")
    except:
        pass

    if len(self.yabus.scan_cache) == 0:
        last_len_scan_cache = len(self.yabus.scan_cache)
        return

    try:

        filter_text = dpg.get_value('##sv_filter')
        # print('filter_text:',filter_text)

        if len(filter_text) > 0:
            dpg.configure_item('##sv_filterbtn',label='')
        else:
            dpg.configure_item('##sv_filterbtn',label='')

        with dpg.group(tag='##sv',parent=self.scanvis_window):
            
            sc = self.yabus.scan_cache

            with dpg.tree_node(label='Counts'):
                dpg.add_text(f'Files: {len(sc)}')
                dpg.add_text(f'Skip: {len(sc[sc.skip == True])}')
                dpg.add_text(f'Backup: {len(sc[sc.backup == True])}')
                dpg.add_text(f'Archive: {len(sc[sc.archive == True])}')
            

            with dpg.table(
                header_row=True,
                resizable=False,
                row_background=True,
                borders_outerH=True, 
                borders_innerV=True, 
                borders_innerH=True, 
                borders_outerV=True):

                dpg.add_table_column(label='item_index',width=50,width_fixed=True) 
                dpg.add_table_column(label='File',width=750,width_fixed=True) 
                dpg.add_table_column(label='Info',width=157,width_fixed=True) 

                for c in self.yabus.scan_cache.to_dict(orient='records'):
                    if filter_text == None or re.search(filter_text,str(c),re.I):
                        with dpg.table_row():
                            with dpg.table_cell():
                                dpg.add_text(c['index'])
                            with dpg.table_cell():
                                file_btn = dpg.add_button(
                                    label= misc.minimize_path(c['relpath'],140),
                                    width=750,
                                    height=33,
                                    )
                                with dpg.tooltip(file_btn):
                                    dpg.add_text(f'relativepath: {c["relpath"]} \nsource: {c["fullpath_x"]} \ndest: {c["fullpath_y"]}')
                            with dpg.table_cell():
                                with dpg.group(horizontal=True):
                                    insrc =  '' if str(c["fullpath_x"]) != 'nan' else ''
                                    insrc_btn = dpg.add_button(
                                        label= insrc,
                                        )
                                    dpg.bind_item_font(insrc_btn,self.large_font)
                                    with dpg.tooltip(insrc_btn):
                                        if insrc == '':
                                            dpg.add_text('file is in source')
                                        else:
                                            dpg.add_text('file not in source')

                                    indest =  '' if str(c["fullpath_y"]) != 'nan' else ''
                                    indest_btn = dpg.add_button(
                                        label= indest,
                                        )
                                    dpg.bind_item_font(indest_btn,self.large_font)
                                    with dpg.tooltip(indest_btn):
                                        if indest == '':
                                            dpg.add_text('file is in destination')
                                        else:
                                            dpg.add_text('file not in destination')

                                    skip =  '' if c.get("skip",False) == True else ''
                                    skip_btn = dpg.add_button(
                                        label= skip,
                                        )
                                    dpg.bind_item_font(skip_btn,self.large_font)
                                    with dpg.tooltip(skip_btn):
                                        if skip == '':
                                            dpg.add_text('file will be skipped')
                                        else:
                                            dpg.add_text('file will not be skipped')

                                    backup =  '' if c["backup"] == True else ''
                                    backup_btn = dpg.add_button(
                                        label= backup,
                                        )
                                    dpg.bind_item_font(backup_btn,self.large_font)
                                    with dpg.tooltip(backup_btn):
                                        if backup == '':
                                            dpg.add_text('file will be backed up')
                                        else:
                                            dpg.add_text('file will not be backed up')

                                    archive =  '' if c["archive"] == True else ''
                                    archive_btn = dpg.add_button(
                                        label= archive,
                                        )
                                    dpg.bind_item_font(archive_btn,self.large_font)
                                    with dpg.tooltip(archive_btn):
                                        if archive == '':
                                            dpg.add_text('file will be archived')
                                        else:
                                            dpg.add_text('file will not be archived')

        last_len_scan_cache = len(self.yabus.scan_cache)
    except Exception as e:
        self.logger.error(e)
        print(str(e))
        pass

def force_rebuild(self):
    global last_len_scan_cache
    last_len_scan_cache = -1
    build_scanvis(self)

def clear_filter(self):
    dpg.set_value('##sv_filter','')
    force_rebuild(self)

def scanvis_window(self):
    with dpg.window(tag=self.scanvis_window,
        label='scan visualizer',
        show=False,
        no_collapse=True,
        ):

        with dpg.group(horizontal=True) as row:
            info_btn = dpg.add_button(
                label = ''
                )
            with dpg.tooltip(info_btn):
                dpg.add_text('This will show you the actions planed for each file:\n \
is the file in source.\n \
is the file in destination.\n \
will the file be skipped.\n \
will the file be backuped up.\n \
will the file be archived.')

            dpg.add_button(
                label='run a scan',
                callback=lambda: self.yabus.scan()
                )

        with dpg.group(horizontal=True,tag='progress_row1') as row:

            spinnerbtn = dpg.add_button(
                label='',
                tag='##progress_percent1',
                width=58,
                height=25,
            )
            with dpg.tooltip(spinnerbtn):
                dpg.add_button(
                    label='',
                    tag='##progress_status1',
                    width=250,
                    height=25,
                )

            dpg.add_progress_bar(
                tag='##progress_bar1',
                height=25,
                width=-1,
                default_value=0.0,
            )

        with dpg.group(horizontal=True) as row:
            filter_btn = dpg.add_button(
                label='',
                tag='##sv_filterbtn',
                width=25,
                height=25,
                callback=lambda: clear_filter(self)
                )
            dpg.bind_item_font(filter_btn,self.large_font)

            dpg.add_input_text(
                tag='##sv_filter',
                hint='type to filter (regex)',
                height=25,
                width=-1,
                multiline=True,
                callback=lambda: force_rebuild(self),
            )

        build_scanvis(self)