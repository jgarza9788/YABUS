import dearpygui.dearpygui as dpg
import dpgutils.misc as misc 

header_btns = [
    ['',25,'red mark if item is not runable'],
    ['',25,'enabled or not'],
    ['',25,'run this row'],
    ['',25,'remove this row'],
    ['source',250,'the source that we will backup'],
    ['dest_root',250,'the destination we will copy the source to'],
    ['ex_reg',250,'exclude anything that matches this regex pattern'],
    ['lastbackup',250,'YYYY.mm.dd | HH:MM'],
]


LOGGER = None

def edit_folder(self,tag,sd):
    global LOGGER
    LOGGER.info(f'edit_folder({tag},{sd})')

    try:
        self.index = int(tag)
        # print(sd,self.yabus.config['items'][self.index][sd])
        print(self.yabus.config.data['items'][self.index][sd])
        dpg.configure_item(sd,default_path=self.yabus.config.data['items'][self.index][sd])
        dpg.show_item(sd)
        self.update_output_text()
    except Exception as e:
        LOGGER.error(str(e))
        LOGGER.error('while trying to pick a directory, you might not have permission')
        

def value_changed(sender, app_data, user_data):
    global LOGGER
    LOGGER.info(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    try:
        s = sender.split(',')
        user_data.yabus.config.data['items'][int(s[0])][s[1]] = app_data
        user_data.yabus.config.save()
    except Exception as e:
        LOGGER.error(str(e))

def remove_item(sender, app_data, user_data):
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

def enable_disable(sender, app_data, user_data):
    global LOGGER
    LOGGER.info(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    # try:
    #     user_data['self'].enable_disable(user_data['index'])
    # except Exception as e:
    #     LOGGER.error(str(e))

    try:
        s = sender.split(',')
        user_data.yabus.config.data['items'][int(s[0])][s[1]] = not user_data.yabus.config.data['items'][int(s[0])][s[1]]
        user_data.yabus.config.save()
        dpg.delete_item(sender)
        build(user_data)
    except Exception as e:
        LOGGER.error(str(e))



def build(self):
    try:
        dpg.delete_item("##items")
    except:
        pass

    with dpg.group(tag='##items',parent=self.items_window):
        with dpg.group(horizontal=True) as row:
            for h in header_btns:
                btn = dpg.add_button(label=h[0],width=h[1],height=25)
                with dpg.tooltip(btn):
                    dpg.add_text(h[2])
                # dpg.bind_item_theme(btn,self.themes['muted_theme'])
                if len(h[0]) == 1:
                    dpg.bind_item_font(btn,self.large_font)

        for index,data in enumerate(self.yabus.items()):
            build_row(self,index,data)
            # with dpg.group(horizontal=True) as row:
            #     dpg.add_text('')


def build_row(self,index,data):
    LOGGER.info(f'building {index} {data}')
    with dpg.group(horizontal=True,tag=str(index)+'_row') as row:
        # dpg.add_text(str(data))

        rt =  '' if data['runable'] == False else ' '
        runable_btn = dpg.add_button(
            label=rt,
            tag=str(index) + '_runable',
            width=25,
            height=25
            )
        # dpg.bind_item_theme(runable_btn,self.themes['red_text_theme'])
        dpg.bind_item_font(runable_btn,self.large_font)
        with dpg.tooltip(runable_btn):
            if data['runable'] == False:
                dpg.add_text('this is not runable/invalid')
            else:
                dpg.add_text('this is runable')

        # with dpg.group(horizontal=True,width=25):
        # enable_cb = dpg.add_checkbox(
        #     label='',
        #     tag=str(index) + '_enable',
        #     default_value = data['enable'], 
        #     # callback=lambda: self.enable_disable(index),
        #     # enabled = bool(data['enabled']),
        #     enabled = True,
        #     user_data = {'index':index, 'data':data, 'self':self},
        #     callback = enable_disable
        #     )
        # with dpg.tooltip(enable_cb):
        #     dpg.add_text('enabled/disabled')

        enable_btn = dpg.add_button(
            label='' if data['enable'] ==  True else '',
            tag=str(index) + ',enable',
            width=25,height=25,
            # user_data = {'index':index, 'data':data, 'self':self},
            user_data = self,
            callback = enable_disable,
            enabled=True,
            )
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
        # dpg.bind_item_theme(run_btn,self.themes['run_btn_theme'])
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
        # dpg.bind_item_theme(rm_btn,self.themes['red_text_theme'])
        dpg.bind_item_font(rm_btn,self.large_font)

        with dpg.tooltip(rm_btn):
            dpg.add_text('remove this item')

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

        ip_txt = dpg.add_input_text(
            label='',
            tag= str(index) + ',ex_reg',
            user_data = self,
            default_value=data['ex_reg'],
            width=250,
            height=25,
            enabled = bool(data['enable']),
            callback = value_changed
            )
        with dpg.tooltip(ip_txt):
            dpg.add_text(data['ex_reg'])


        lbu_btn = dpg.add_button(
            label = misc.format_lastbackup(data['lastbackup']),
            tag= str(index) + '_lastbackup',
            width=250,
            height=25,
            enabled = bool(data['enable']),
            )
        with dpg.tooltip(lbu_btn):
            dpg.add_text(misc.time_difference(data['lastbackup']))


def items_window(self):

    global LOGGER
    LOGGER = self.logger 

    def rm_confirm():
        print(dpg.get_item_configuration('rm_check_dialog'))
        self.remove_item(int(dpg.get_value('rm_index').split(' - ')[1]))
        dpg.configure_item("rm_check_dialog", show=False)
        

    with dpg.window(label="Remove Item", modal=True, show=False, tag="rm_check_dialog", 
                    #no_title_bar=True,
                    pos= (0,0),
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


    with dpg.window(tag=self.items_window,
        label='items',
        no_close=True,
        show=True,
        # no_title_bar=True,
        no_collapse=True
        ):

        # dpg.add_button(
        #     label="[+item]", 
        #     callback=lambda: self.add_new_item()
        #     )

        with dpg.group(horizontal=True,tag='progress_row') as row:
            dpg.add_button(
                label='',
                tag='##progress_spinner',
                width=25,
                height=25,
            )
            dpg.add_progress_bar(
                # label='50/100',
                tag='##progressbar',
                height=25,
                width=-1,
                default_value=0.0,
                # show=False
            )

        dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='source'
            ,label = 'source'
            ,modal = True
            ,width=650,height=650)
        dpg.add_file_dialog(directory_selector=True, show=False, callback=self.change_folder_callback, tag='root_dest'
            ,label = 'root of destination'
            ,modal = True
            ,width=650,height=650)
            
        build(self)
