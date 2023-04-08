import dearpygui.dearpygui as dpg

from dpgutils.theme import apply_theme
from .themes import theme_list


# def print_me(sender):
#     print(f"Menu Item: {sender}")


def set_and_apply_theme(self,i):
    try:
        self.dpg_config.data['theme_id'] = i
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()
    except:
        self.dpg_config.data['theme_id'] = 8
        apply_theme(self.dpg_config.data['theme_id'])
        self.dpg_config.save()
    

def theme_menu_item(self,i,t):
    dpg.add_menu_item(label= str(i) + ': ' + t.name, callback=lambda: set_and_apply_theme(self,i))

def menu(self):
    with dpg.viewport_menu_bar():

        dpg.add_menu_item(label="[+item]", 
            callback= self.add_new_item
            )
        
        with dpg.menu(label="[run_all_items]"):
            with dpg.menu(label="you sure ?"):
                dpg.add_menu_item(label="Yes", 
                    callback= self.run_all_items
                    )
                dpg.add_menu_item(label="No")
            
        with dpg.menu(label="[Save]"):
            dpg.add_menu_item(label="Save Layout", 
                callback=lambda: dpg.save_init_file(self.layout), 
                )
            
        with dpg.menu(label="[Themes]"):
            for ith,th in enumerate(theme_list):
                theme_menu_item(self,ith,th)