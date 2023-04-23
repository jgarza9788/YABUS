import dearpygui.dearpygui as dpg
 

def output_window(self):
    with dpg.window(tag=self.output_window,
        label='output',
        show=False,
        no_collapse=True,
        ):


        # dpg.add_text('',tag='output_text')
        dpg.add_input_text(
            label='',
            tag='output_text',
            multiline=True,
            width=-1,
            height=-1,
            )

