import dearpygui.dearpygui as dpg

from typing import Optional, Sequence

def get_themes():

    result = {}


    
    # https://github.com/IvanNazaruk/DPG-Template/blob/main/DearPyGui_Theme/themes/visual_studio.py
    name = """Visual Studio"""
    styles: dict[int, Sequence[float]] = {
        dpg.mvStyleVar_Alpha: [1.0],
        dpg.mvStyleVar_WindowPadding: [8.0, 8.0],
        dpg.mvStyleVar_WindowRounding: [0.0],
        dpg.mvStyleVar_WindowBorderSize: [1.0],
        dpg.mvStyleVar_WindowMinSize: [32.0, 32.0],
        dpg.mvStyleVar_WindowTitleAlign: [0.0, 0.5],
        dpg.mvStyleVar_ChildRounding: [0.0],
        dpg.mvStyleVar_ChildBorderSize: [1.0],
        dpg.mvStyleVar_PopupRounding: [0.0],
        dpg.mvStyleVar_PopupBorderSize: [1.0],
        dpg.mvStyleVar_FramePadding: [4.0, 3.0],
        dpg.mvStyleVar_FrameRounding: [0.0],
        dpg.mvStyleVar_FrameBorderSize: [0.0],
        dpg.mvStyleVar_ItemSpacing: [8.0, 4.0],
        dpg.mvStyleVar_ItemInnerSpacing: [4.0, 4.0],
        dpg.mvStyleVar_CellPadding: [4.0, 2.0],
        dpg.mvStyleVar_IndentSpacing: [21.0],
        dpg.mvStyleVar_ScrollbarSize: [14.0],
        dpg.mvStyleVar_ScrollbarRounding: [0.0],
        dpg.mvStyleVar_GrabMinSize: [10.0],
        dpg.mvStyleVar_GrabRounding: [0.0],
        dpg.mvStyleVar_TabRounding: [0.0],
        dpg.mvStyleVar_ButtonTextAlign: [0.5, 0.5],
        dpg.mvStyleVar_SelectableTextAlign: [0.0, 0.0],
    }
    colors: dict[int, Sequence[int, int, int, Optional[int]]] = {
        dpg.mvThemeCol_Text: [255, 255, 255, 255],
        dpg.mvThemeCol_TextDisabled: [151, 151, 151, 255],
        dpg.mvThemeCol_WindowBg: [37, 37, 38, 255],
        dpg.mvThemeCol_ChildBg: [37, 37, 38, 255],
        dpg.mvThemeCol_PopupBg: [37, 37, 38, 255],
        dpg.mvThemeCol_Border: [78, 78, 78, 255],
        dpg.mvThemeCol_BorderShadow: [78, 78, 78, 255],
        dpg.mvThemeCol_FrameBg: [51, 51, 55, 255],
        dpg.mvThemeCol_FrameBgHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_FrameBgActive: [0, 119, 200, 255],
        dpg.mvThemeCol_TitleBg: [37, 37, 38, 255],
        dpg.mvThemeCol_TitleBgActive: [37, 37, 38, 255],
        dpg.mvThemeCol_TitleBgCollapsed: [37, 37, 38, 255],
        dpg.mvThemeCol_MenuBarBg: [51, 51, 55, 255],
        dpg.mvThemeCol_ScrollbarBg: [51, 51, 55, 255],
        dpg.mvThemeCol_ScrollbarGrab: [82, 82, 85, 255],
        dpg.mvThemeCol_ScrollbarGrabHovered: [90, 90, 95, 255],
        dpg.mvThemeCol_ScrollbarGrabActive: [90, 90, 95, 255],
        dpg.mvThemeCol_CheckMark: [0, 119, 200, 255],
        dpg.mvThemeCol_SliderGrab: [29, 151, 236, 255],
        dpg.mvThemeCol_SliderGrabActive: [0, 119, 200, 255],
        dpg.mvThemeCol_Button: [51, 51, 55, 255],
        dpg.mvThemeCol_ButtonHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_ButtonActive: [29, 151, 236, 255],
        dpg.mvThemeCol_Header: [51, 51, 55, 255],
        dpg.mvThemeCol_HeaderHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_HeaderActive: [0, 119, 200, 255],
        dpg.mvThemeCol_Separator: [78, 78, 78, 255],
        dpg.mvThemeCol_SeparatorHovered: [78, 78, 78, 255],
        dpg.mvThemeCol_SeparatorActive: [78, 78, 78, 255],
        dpg.mvThemeCol_ResizeGrip: [37, 37, 38, 255],
        dpg.mvThemeCol_ResizeGripHovered: [51, 51, 55, 255],
        dpg.mvThemeCol_ResizeGripActive: [82, 82, 85, 255],
        dpg.mvThemeCol_Tab: [37, 37, 38, 255],
        dpg.mvThemeCol_TabHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_TabActive: [0, 119, 200, 255],
        dpg.mvThemeCol_TabUnfocused: [37, 37, 38, 255],
        dpg.mvThemeCol_TabUnfocusedActive: [0, 119, 200, 255],
        dpg.mvThemeCol_PlotLines: [0, 119, 200, 255],
        dpg.mvThemeCol_PlotLinesHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_PlotHistogram: [0, 119, 200, 255],
        dpg.mvThemeCol_PlotHistogramHovered: [29, 151, 236, 255],
        dpg.mvThemeCol_TableHeaderBg: [48, 48, 51, 255],
        dpg.mvThemeCol_TableBorderStrong: [79, 79, 89, 255],
        dpg.mvThemeCol_TableBorderLight: [58, 58, 63, 255],
        dpg.mvThemeCol_TableRowBg: [0, 0, 0, 0],
        dpg.mvThemeCol_TableRowBgAlt: [255, 255, 255, 15],
        dpg.mvThemeCol_TextSelectedBg: [0, 119, 200, 255],
        dpg.mvThemeCol_DragDropTarget: [37, 37, 38, 255],
        dpg.mvThemeCol_NavHighlight: [37, 37, 38, 255],
        dpg.mvThemeCol_NavWindowingHighlight: [255, 255, 255, 178],
        dpg.mvThemeCol_NavWindowingDimBg: [204, 204, 204, 51],
        dpg.mvThemeCol_ModalWindowDimBg: [37, 37, 38, 255],
    }


    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            for dpg_id, style in styles.items():
                tag = dpg.add_theme_style(dpg_id, *style, category=dpg.mvThemeCat_Core)
                # all_styles[dpg_id] = tag

            for dpg_id, color in colors.items():
                tag = dpg.add_theme_color(dpg_id, color, category=dpg.mvThemeCat_Core)  # noqa
                # all_colors[dpg_id] = tag

    # color_orange  = (255,140,23)
    # color_grey = (51, 51, 55)
    # color_lightgrey = (200, 200, 200)
    # color_white = (255,255,255)
    # color_blue = (34, 83, 118)


    # with dpg.theme() as global_theme:
    #     with dpg.theme_component(dpg.mvButton,enabled_state=True):
    #         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_grey, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, color_white, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, color_white, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, color_blue, category=dpg.mvThemeCat_Core)
    #     with dpg.theme_component(dpg.mvButton,enabled_state=False):
    #         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_orange, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, color_blue, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, color_blue, category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, color_orange, category=dpg.mvThemeCat_Core)




    result['global_theme'] = global_theme

    # with dpg.theme() as container_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    #     with dpg.theme_component(dpg.mvInputInt):
    #         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (100, 150, 100), category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    # result['container_theme'] = container_theme

    # with dpg.theme() as item_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (200, 200, 100), category=dpg.mvThemeCat_Core)
    #         dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)

    # result['item_theme'] = item_theme



    # dpg.bind_theme(global_theme)
    # dpg.bind_item_theme(win1, container_theme)
    # dpg.bind_item_theme(t2, item_theme)

    # with dpg.theme() as disabled_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [100, 100, 100])
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 37, 37])
    #         dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [100, 0, 0])
    # # self.disabled_theme = disabled_theme
    # result['disabled_theme'] = disabled_theme

    # with dpg.theme() as muted_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [100, 100, 100])
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, [37, 37, 37])
    #         dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [50, 50, 50])
    # # self.disabled_theme = disabled_theme
    # result['muted_theme'] = muted_theme

    # with dpg.theme() as main_button_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         # dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255])
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 100, 255])
    #         dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 200, 255])
    # result['main_button_theme'] = main_button_theme    

    # with dpg.theme() as run_button_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 0, 0])
    #         dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 200, 0])
    #         dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 100, 0])
    # result['run_button_theme'] = run_button_theme

    # with dpg.theme() as run_btn_theme:
    #     with dpg.theme_component(dpg.mvAll, enabled_state=True):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 200, 0])
    #     with dpg.theme_component(dpg.mvAll, enabled_state=False):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 50, 0])

    # result['run_btn_theme'] = run_btn_theme

    # with dpg.theme() as red_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
    # # self.red_text_theme = red_text_theme
    # result['red_text_theme'] = red_text_theme

    
    # with dpg.theme() as green_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [0, 0, 255])
    # # self.red_text_theme = red_text_theme
    # result['green_text_theme'] = green_text_theme

    # with dpg.theme() as grey_text_theme:
    #     with dpg.theme_component(dpg.mvAll):
    #         dpg.add_theme_color(dpg.mvThemeCol_Text, [100, 100, 100])
    # # self.red_text_theme = red_text_theme
    # result['green_text_theme'] = grey_text_theme

    return result