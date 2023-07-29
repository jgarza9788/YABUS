import os,re
import dearpygui.dearpygui as dpg
import dpgutils.misc as misc 

header_btns = [
    # ['',25,'red mark if item is not runable'],
    # ['',25,'enabled or not'],
    # ['',25,'run this row'],
    # ['',25,'remove this row'],
    # ['source',250,'the source that we will backup'],
    # ['',25,'open source folder'],
    # ['dest_root',250,'the destination we will copy the source to'],
    # ['',25,'open dest_root folder'],
    # ['ex_reg',250,'exclude anything that matches this regex pattern'],
    # ['lastbackup',250,'YYYY.mm.dd | HH:MM'],

    ['   ',124],
    ['Source',283],
    ['Destination Root',283],
    ['ex_reg',250],
    ['LastBackUp',250]
    
]


LOGGER = None

def edit_folder(self,tag:str,sd:str):
    """used to edit a foldewr

    Args:
        tag (str): tag of the item that sent it
        sd (str): column name 
    """
    global LOGGER
    LOGGER.info(f'edit_folder({tag},{sd})')

    try:
        self.index = int(tag)
        # print(sd,self.yabus.config['items'][self.index][sd])
        print(self.yabus.config.data['items'][self.index][sd])
        dpg.configure_item(sd,default_path=self.yabus.config.data['items'][self.index][sd])
        dpg.show_item(sd)
        user_data.yabus.process_config()
        build(user_data)

        # self.update_output_text()
    except Exception as e:
        LOGGER.error(str(e))
        LOGGER.error('while trying to pick a directory, you might not have permission')
        
def value_changed(sender:str, app_data:any, user_data:any):
    """used to change a value of an item

    Args:
        sender (str): the itm tag that sent it
        app_data (any): none
        user_data (any): self
    """
    global LOGGER
    LOGGER.info(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    try:
        s = sender.split(',')
        user_data.yabus.config.data['items'][int(s[0])][s[1]] = app_data
        user_data.yabus.config.save()
        user_data.yabus.process_config()
        build(user_data)

    except Exception as e:
        LOGGER.error(str(e))

def remove_item(sender:str, app_data:any, user_data:any):
    """to remove item (this function is trigged by clicking the x)

    Args:
        sender (str): the item tag that sent it
        app_data (any): None
        user_data (any): self
    """
    global LOGGER
    LOGGER.info(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    try:
        s = sender.split(',')
        # ITR = user_data
        # dpg.configure_item("rm_check_dialog", user_data=user_data)

        dpg.set_value('rm_index','index - ' + str(user_data['index']))
        dpg.set_value('rm_source','source - ' + user_data['data']['source'])
        dpg.set_value('rm_root_dest','root_dest - ' + user_data['data']['root_dest'])
        dpg.set_value('rm_lastbackup','lastbackup - ' + misc.format_lastbackup(user_data['data']['lastbackup']) )
        dpg.configure_item("rm_check_dialog", pos=( (dpg.get_viewport_width()//2) - (332//2) ,(dpg.get_viewport_height()//2) - (187//2)))
        dpg.configure_item("rm_check_dialog", show=True)
    except Exception as e:    
        LOGGER.error(str(e))

def toggle_enable(sender:str, app_data:any, user_data:any):
    """toggles enable/disable

    Args:
        sender (_type_): _description_
        app_data (_type_): _description_
        user_data (_type_): _description_
    """
    global LOGGER
    LOGGER.info(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    try:
        s = sender.split(',')
        user_data.yabus.config.data['items'][int(s[0])][s[1]] = not user_data.yabus.config.data['items'][int(s[0])][s[1]]
        user_data.yabus.config.save()
        user_data.yabus.process_config()
        dpg.delete_item(sender)
        build(user_data)
    except Exception as e:
        LOGGER.error(str(e))

def clear_filter(self):
    dpg.set_value('##filter','')
    build(self)

def build(self):
    """builds the main list of items
    """
    try:
        dpg.delete_item("##items")
    except:
        pass

    with dpg.group(tag='##items',parent=self.main_window):
        with dpg.table(
            header_row=True,
            resizable=False,
            # sortable=True,
            row_background=True,
            # borders_outerH=True, 
            # borders_innerV=True, 
            # borders_innerH=True, 
            # borders_outerV=True
            ):

            for index,h in enumerate(header_btns):
                thisheader = dpg.add_table_column(label=h[0],width=h[1],width_fixed=True) 
                if index == 1:
                    dpg.bind_item_font(thisheader,self.large_font)


            filter_text = dpg.get_value('##filter')

            if len(filter_text) > 0:
                dpg.configure_item('##filterbtn',label='')
            else:
                dpg.configure_item('##filterbtn',label='')

            for index,data in enumerate(self.yabus.items()):
                if filter_text!=None and re.search(filter_text,str(data),re.I) :
                    with dpg.table_row():
                        build_row(self,index,data)
                
                if filter_text == None:
                    with dpg.table_row():
                        build_row(self,index,data)

def build_row(self,index:int,data:dict):
    """builds one row in the list 

    Args:
        index (int): the index
        data (dict): data
    """

    with dpg.table_cell():
        with dpg.group(horizontal=True):
            rt =  '' if data['runable'] == False else ' '
            runable_btn = dpg.add_button(
                label=rt,
                tag=str(index) + '_runable',
                width=25,
                height=25
                )
            # dpg.bind_item_theme(runable_btn,red_text)
            dpg.bind_item_font(runable_btn,self.large_font)
            with dpg.tooltip(runable_btn):
                if data['runable'] == False:
                    dpg.add_text('this is not runable/invalid')
                else:
                    dpg.add_text('this is runable')

            enable_btn = dpg.add_button(
                label='' if data['enable'] ==  True else '',
                tag=str(index) + ',enable',
                width=25,height=25,
                # user_data = {'index':index, 'data':data, 'self':self},
                user_data = self,
                callback = toggle_enable,
                enabled=True,
                )
            # dpg.bind_item_theme(enable_btn,green_text)
            dpg.bind_item_font(enable_btn,self.large_font)
            with dpg.tooltip(enable_btn):
                dpg.add_text('enable/disable')

            # print(data['enable'],data['runable'],(data['enable'] and data['runable']))

            run_btn = dpg.add_button(
                label='',
                tag=str(index) + '_run',
                width=25,height=25,
                enabled = (data['enable'] and data['runable']),
                callback = lambda: self.run(index)
                )
            # dpg.bind_item_theme(run_btn,green_text)
            dpg.bind_item_font(run_btn,self.large_font)
            with dpg.tooltip(run_btn):
                dpg.add_text('run this item')

            rm_btn = dpg.add_button(
                label='',
                width=25,height=25,
                # callback = lambda: print('removed..')
                tag= str(index) + ',remove_button',
                user_data = {'index':index, 'data':data, 'self':self},
                callback = remove_item
                )
            # dpg.bind_item_theme(rm_btn,red_text)
            dpg.bind_item_font(rm_btn,self.large_font)

            with dpg.tooltip(rm_btn):
                dpg.add_text('remove this item')

    with dpg.table_cell():
        with dpg.group(horizontal=True):
            source_btn = dpg.add_button(
                label = misc.minimize_path(data['source']),
                tag=str(index) + '_source',
                callback=lambda: edit_folder(self,index,'source'),
                width=250,
                height=25,
                enabled = bool(data['enable']),
                )
            with dpg.tooltip(source_btn):
                dpg.add_text(data['source'])

            slink_btn = dpg.add_button(
                label = '',
                tag=str(index) + '_source_link',
                callback=lambda: os.startfile(data['source']),
                width=25,
                height=25,
                enabled = (data['enable'] and data['runable']),
                )
            dpg.bind_item_font(slink_btn,self.large_font)
            with dpg.tooltip(slink_btn):
                dpg.add_text('open source folder')

    with dpg.table_cell():
        with dpg.group(horizontal=True):
            rootdest_btn = dpg.add_button(
                label = misc.minimize_path(data['root_dest']),
                tag=str(index) + '_root_dest',
                callback=lambda: edit_folder(self,index,'root_dest'),
                width=250,
                height=25,
                enabled = bool(data['enable']),
                )
            with dpg.tooltip(rootdest_btn):
                dpg.add_text(data['root_dest'])

            drlink_btn = dpg.add_button(
                label = '',
                tag=str(index) + '_root_dest_link',
                callback=lambda: os.startfile(data['root_dest']),
                width=25,
                height=25,
                enabled = (data['enable'] and data['runable']),
                )
            dpg.bind_item_font(drlink_btn,self.large_font)
            with dpg.tooltip(drlink_btn):
                dpg.add_text('open dest_root folder')

    with dpg.table_cell():
        with dpg.group(horizontal=True):
            exreg_btn = dpg.add_input_text(
                label='',
                tag= str(index) + ',ex_reg',
                user_data = self,
                default_value=data['ex_reg'],
                width=250,
                height=33,
                # multiline=True,
                enabled = bool(data['enable']),
                callback = value_changed,
                on_enter = True
                )
            with dpg.tooltip(exreg_btn):
                dpg.add_text(data['ex_reg'])
            # exreg_save_btn = dpg.add_button(
            #     label = '󰳻',
            #     width=25,
            #     height=25,
            # )

    with dpg.table_cell():
        with dpg.group(horizontal=True):
            lbu_btn = dpg.add_button(
                label = misc.format_lastbackup(data['lastbackup']),
                tag= str(index) + '_lastbackup',
                width=250,
                height=25,
                enabled = bool(data['enable']),
                )
            with dpg.tooltip(lbu_btn):
                dpg.add_text(misc.time_difference(data['lastbackup']))

def redrive(get_drives):

    dstr = ''
    for d in get_drives():
        dstr += f'{d["letter"]} --- {d["label"]} \n'
    # print(dstr)
    dpg.configure_item('##drives', default_value=dstr)


def main_window(self):
    """creates the item window and manages it
    """

    global LOGGER
    LOGGER = self.logger 

    def rm_confirm():
        """the final function to delete an item
        """
        print(dpg.get_item_configuration('rm_check_dialog'))
        self.remove_item(int(dpg.get_value('rm_index').split(' - ')[1]))
        dpg.configure_item("rm_check_dialog", show=False)

        self.yabus.process_config()
        build(self)
        
    # this is the remove item dialog window
    with dpg.window(label="Remove Item", 
                    modal=True, 
                    show=False, 
                    tag="rm_check_dialog", 
                    #no_title_bar=True,
                    pos= (0,0),
                    # width=500,
                    # height=250,
                    no_resize=True,
                    ):
        try:
            dpg.add_text('Would you like to Remove this one ?')
            dpg.add_text(label='',tag='rm_index')
            dpg.add_text(label='',tag='rm_source')
            dpg.add_text(label='',tag='rm_root_dest')
            dpg.add_text(label='',tag='rm_lastbackup')
            dpg.add_separator()
            # dpg.add_checkbox(label="Don't ask me next time")
            with dpg.group(horizontal=True):
                dpg.add_button(label="Yes", width=75, callback= rm_confirm)
                dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("rm_check_dialog", show=False))
        except:
            LOGGER.warn('error showing dialog')
            dpg.configure_item("rm_check_dialog", show=False)


    with dpg.window(tag=self.main_window,
        label='main',
        # no_close=True,
        show=True,
        # no_title_bar=True,
        no_collapse=True,
        ):

        with dpg.menu_bar():
            dpg.add_menu_item(label="[+item]", 
                callback=lambda: self.add_new_item()
                )

            with dpg.menu(label="[run_all_items]"):
                with dpg.menu(label="you sure ?"):
                    dpg.add_menu_item(label="Yes", 
                        callback= self.run_all_items
                        )
                    dpg.add_menu_item(label="No")

        with dpg.group(horizontal=True,tag='progress_row2') as row:

            statusbtn = dpg.add_button(
                label='',
                tag='##progress_status0',
                width=407,
                height=25,
            )
            with dpg.tooltip(statusbtn):
                dpg.add_button(
                    label='',
                    tag='##progress_details0',
                    # width=-1,
                    # height=-1,
                )
            dpg.add_progress_bar(
                # label='50/100',
                tag='##progress_bar0',
                height=25,
                width=-1,
                default_value=0.0,
                # show=False
            )

        with dpg.tree_node(label='drives',parent=self.main_window):
            # rdbtn = dpg.add_button(
            #     label='',
            #     tag='##re-drive',
            #     width=25,
            #     height=25,
            #     callback=lambda: redrive(self.get_drives)
            # )
            # dpg.bind_item_font(rdbtn,self.large_font)
            dpg.add_text(
                '',
                tag = '##drives'
                )
            redrive(self.get_drives)

        dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='source'
            ,label = 'source'
            ,modal = True
            ,width=650,height=650)
        dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='root_dest'
            ,label = 'root of destination'
            ,modal = True
            ,width=650,height=650)


        with dpg.group(horizontal=True) as row:
            filter_btn = dpg.add_button(
                label='',
                tag='##filterbtn',
                width=25,
                height=25,
                callback=lambda: clear_filter(self)
                )
            dpg.bind_item_font(filter_btn,self.large_font)

            dpg.add_input_text(
                tag='##filter',
                hint='type to filter (regex)',
                height=25,
                width=-1,
                multiline=True,
                callback=lambda: build(self),
                # on_enter=True
            )

        build(self)
