import dearpygui.dearpygui as dpg

from dpgutils.theme import apply_theme
from .themes import theme_list


def set_and_apply_theme(self,i:int):
    """applys the theme

    Args:
        i (index): index of theme
    """
    try:
        self.dpg_config.data['theme_id'] = i
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()
    except:
        self.dpg_config.data['theme_id'] = 8
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()
    

def theme_menu_item(self,i:int,t:str):
    """creates a theme item

    Args:
        i (int): index of theme
        t (str): theme name
    """
    # dpg.add_menu_item(label= str(i) + ': ' + t.name, callback=lambda: set_and_apply_theme(self,i))
    dpg.add_button(
        label= (str(i) + ': ' + t.name).ljust(35,' '),
        callback=lambda: set_and_apply_theme(self,i),
        width=250,
        height=25,
        # default_value= self.dpg_config.data['theme_id'] ==  i
        )

def show_or_focus(item_name:str):

    dpg.configure_item(item_name, show=True)
    dpg.focus_item(item_name)



def menu(self):
    """creates the menu
    """
    with dpg.viewport_menu_bar():

        # dpg.add_menu_item(label="[+item]", 
        #     callback=lambda: self.add_new_item()
        #     )
        
        # with dpg.menu(label="[run_all_items]"):
        #     with dpg.menu(label="you sure ?"):
        #         dpg.add_menu_item(label="Yes", 
        #             callback= self.run_all_items
        #             )
        #         dpg.add_menu_item(label="No")

        with dpg.menu(label="[windows]"):
            # with dpg.menu(label="output"):
            dpg.add_button(label="log window", 
                callback= lambda: show_or_focus(self.log_window),
                width=250,
                height=25
                )
            dpg.add_button(label="main window", 
                callback= lambda: show_or_focus(self.main_window),
                width=250,
                height=25
                )
            # dpg.add_button(label="drive window", 
            #     callback= lambda: show_or_focus(self.drive_window),
            #     width=250,
            #     height=25
            #     )
            # dpg.add_button(label="scan visualizer", 
            #     callback= lambda: dpg.configure_item(self.scanvis_window, show=True),
            #     width=250,
            #     height=25
            #     )

            
        with dpg.menu(label="[Save]"):
            dpg.add_button(label="Save Layout", 
                callback=lambda: dpg.save_init_file(self.layout), 
                width=250,
                height=25
                )
            dpg.add_button(label="Save Data", 
                callback=lambda: self.yabus.config.save(), 
                width=250,
                height=25
                )
            
        with dpg.menu(label="[Themes]"):
            for ith,th in enumerate(theme_list):
                theme_menu_item(self,ith,th)