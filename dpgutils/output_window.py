import dearpygui.dearpygui as dpg
 

def output_window(self):
    with dpg.window(tag=self.output_window,
        label='output',
        # no_close=True,
        show=True,
        # no_title_bar=True,
        no_collapse=True,
        horizontal_scrollbar=True,
        ):


        dpg.add_text('',tag='output_text')

