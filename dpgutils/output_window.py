import dearpygui.dearpygui as dpg
 

def output_window(self):
    with dpg.window(tag=self.output_window,
        label='output',
        no_close=True,
        show=True,
        # no_title_bar=True,
        no_collapse=True,
        horizontal_scrollbar=True,
        ):



        # sync_btn = dpg.add_button(label='',width=25,height=25,
        #                             callback=self.update_log)
        # with dpg.tooltip(sync_btn):
        #     dpg.add_text('sync log')
        # dpg.bind_item_theme(sync_btn,self.themes['muted_theme'])
        # dpg.bind_item_font(sync_btn,self.large_font)

        dpg.add_text('',tag='output_text')

        # dpg.add_input_text(
        #     label='',
        #     tag='output_text',
        #     width=-1,
        #     height=-1,
        #     multiline=True
        #     )



        # # with dpg.tree_node(label="Global"):
        # with dpg.handler_registry(show=True, tag="__mouse_move"):
        #     dpg.add_key_release_handler(key=dpg.mvKey_0,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_1,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_2,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_3,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_4,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_5,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_6,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_7,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_8,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_9,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_A,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_B,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_C,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_D,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_E,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_G,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_H,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_I,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_J,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_K,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_L,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_M,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_N,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_O,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_P,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Q,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_R,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_S,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_T,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_U,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_V,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_W,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_X,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Y,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Z,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Back,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Tab,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Clear,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Return,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Shift,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Control,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Alt,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Pause,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Capital,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Escape,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Spacebar,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Prior,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Next,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_End,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Home,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Left,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Up,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Right,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Down,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Select,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Print,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Execute,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_PrintScreen,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Insert,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Delete,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Help,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_LWin,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_RWin,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Apps,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Sleep,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad0,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad1,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad2,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad3,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad4,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad5,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad6,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad7,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad8,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumPad9,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Multiply,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Add,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Separator,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Subtract,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Decimal,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Divide,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F1,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F2,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F3,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F4,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F5,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F6,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F7,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F8,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F9,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F10,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F11,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F12,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F13,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F14,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F15,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F16,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F17,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F18,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F19,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F20,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F21,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F22,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F23,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F24,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_F25,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_NumLock,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_ScrollLock,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_LShift,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_RShift,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_LControl,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_RControl,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_LMenu,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_RMenu,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Back,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Forward,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Refresh,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Stop,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Search,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Favorites,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Browser_Home,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Volume_Mute,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Volume_Down,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Volume_Up,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Media_Next_Track,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Media_Prev_Track,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Media_Stop,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Media_Play_Pause,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Launch_Mail,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Launch_Media_Select,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Launch_App1,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Launch_App2,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Colon,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Plus,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Comma,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Minus,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Period,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Slash,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Tilde,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Open_Brace,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Backslash,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Close_Brace,callback= self.update_output_text)
        #     dpg.add_key_release_handler(key=dpg.mvKey_Quote,callback= self.update_output_text)
        #     dpg.add_mouse_release_handler(
        #         button=dpg.mvMouseButton_Left,
        #         callback= self.update_output_text
        #         )
        #     dpg.add_mouse_release_handler(
        #         button=dpg.mvMouseButton_Right,
        #         callback= self.update_output_text
        #         )
            # dpg.add_mouse_move_handler(
            #     callback= self.update_output_text
            #     )

