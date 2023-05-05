import dearpygui.dearpygui as dpg
 

def log_window(self):
    with dpg.window(tag=self.log_window,
        label='log',
        # show=False,
        no_collapse=True,
        width=500,
        height=250
        ):



        # dpg.add_text('',tag='output_text')
        dpg.add_input_text(
            label='',
            tag='log_text',
            multiline=True,
            width=-1,
            height=-1,
            )

