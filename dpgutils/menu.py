import dearpygui.dearpygui as dpg

def print_me(sender):
    print(f"Menu Item: {sender}")

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
            
        # with dpg.menu(label="[Themes]"):
        #         dpg.add_menu_item(label="Theme 1", callback=print_me, check=True)