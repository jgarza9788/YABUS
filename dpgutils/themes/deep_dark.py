# Author: janekb04
from __future__ import annotations

from typing import Optional, Sequence

import dearpygui.dearpygui as dpg

name = """Deep Dark"""
styles: dict[int, Sequence[float]] = {
    dpg.mvStyleVar_Alpha: [1.0],
    dpg.mvStyleVar_WindowPadding: [8.0, 8.0],
    dpg.mvStyleVar_WindowRounding: [7.0],
    dpg.mvStyleVar_WindowBorderSize: [1.0],
    dpg.mvStyleVar_WindowMinSize: [32.0, 32.0],
    dpg.mvStyleVar_WindowTitleAlign: [0.0, 0.5],
    dpg.mvStyleVar_ChildRounding: [4.0],
    dpg.mvStyleVar_ChildBorderSize: [1.0],
    dpg.mvStyleVar_PopupRounding: [4.0],
    dpg.mvStyleVar_PopupBorderSize: [1.0],
    dpg.mvStyleVar_FramePadding: [5.0, 2.0],
    dpg.mvStyleVar_FrameRounding: [3.0],
    dpg.mvStyleVar_FrameBorderSize: [1.0],
    dpg.mvStyleVar_ItemSpacing: [6.0, 6.0],
    dpg.mvStyleVar_ItemInnerSpacing: [6.0, 6.0],
    dpg.mvStyleVar_CellPadding: [6.0, 6.0],
    dpg.mvStyleVar_IndentSpacing: [25.0],
    dpg.mvStyleVar_ScrollbarSize: [15.0],
    dpg.mvStyleVar_ScrollbarRounding: [9.0],
    dpg.mvStyleVar_GrabMinSize: [10.0],
    dpg.mvStyleVar_GrabRounding: [3.0],
    dpg.mvStyleVar_TabRounding: [4.0],
    dpg.mvStyleVar_ButtonTextAlign: [0.5, 0.5],
    dpg.mvStyleVar_SelectableTextAlign: [0.0, 0.0],
}
colors: dict[int, Sequence[int, int, int, Optional[int]]] = {
    dpg.mvThemeCol_Text: [255, 255, 255, 255],
    dpg.mvThemeCol_TextDisabled: [127, 127, 127, 255],
    dpg.mvThemeCol_WindowBg: [25, 25, 25, 255],
    dpg.mvThemeCol_ChildBg: [25, 25, 25, 255],
    dpg.mvThemeCol_PopupBg: [25, 25, 25, 255],
    dpg.mvThemeCol_Border: [48, 48, 48, 73],
    dpg.mvThemeCol_BorderShadow: [0, 0, 0, 61],
    dpg.mvThemeCol_FrameBg: [12, 12, 12, 137],
    dpg.mvThemeCol_FrameBgHovered: [48, 48, 48, 137],
    dpg.mvThemeCol_FrameBgActive: [51, 56, 58, 255],
    dpg.mvThemeCol_TitleBg: [0, 0, 0, 255],
    dpg.mvThemeCol_TitleBgActive: [15, 15, 15, 255],
    dpg.mvThemeCol_TitleBgCollapsed: [0, 0, 0, 255],
    dpg.mvThemeCol_MenuBarBg: [35, 35, 35, 255],
    dpg.mvThemeCol_ScrollbarBg: [12, 12, 12, 137],
    dpg.mvThemeCol_ScrollbarGrab: [86, 86, 86, 137],
    dpg.mvThemeCol_ScrollbarGrabHovered: [102, 102, 102, 137],
    dpg.mvThemeCol_ScrollbarGrabActive: [142, 142, 142, 137],
    dpg.mvThemeCol_CheckMark: [84, 170, 219, 255],
    dpg.mvThemeCol_SliderGrab: [86, 86, 86, 137],
    dpg.mvThemeCol_SliderGrabActive: [142, 142, 142, 137],
    dpg.mvThemeCol_Button: [12, 12, 12, 137],
    dpg.mvThemeCol_ButtonHovered: [48, 48, 48, 137],
    dpg.mvThemeCol_ButtonActive: [51, 56, 58, 255],
    dpg.mvThemeCol_Header: [0, 0, 0, 132],
    dpg.mvThemeCol_HeaderHovered: [0, 0, 0, 91],
    dpg.mvThemeCol_HeaderActive: [51, 56, 58, 84],
    dpg.mvThemeCol_Separator: [71, 71, 71, 73],
    dpg.mvThemeCol_SeparatorHovered: [112, 112, 112, 73],
    dpg.mvThemeCol_SeparatorActive: [102, 112, 119, 255],
    dpg.mvThemeCol_ResizeGrip: [71, 71, 71, 73],
    dpg.mvThemeCol_ResizeGripHovered: [112, 112, 112, 73],
    dpg.mvThemeCol_ResizeGripActive: [102, 112, 119, 255],
    dpg.mvThemeCol_Tab: [0, 0, 0, 132],
    dpg.mvThemeCol_TabHovered: [35, 35, 35, 255],
    dpg.mvThemeCol_TabActive: [51, 51, 51, 91],
    dpg.mvThemeCol_TabUnfocused: [0, 0, 0, 132],
    dpg.mvThemeCol_TabUnfocusedActive: [35, 35, 35, 255],
    dpg.mvThemeCol_PlotLines: [255, 0, 0, 255],
    dpg.mvThemeCol_PlotLinesHovered: [255, 0, 0, 255],
    dpg.mvThemeCol_PlotHistogram: [255, 0, 0, 255],
    dpg.mvThemeCol_PlotHistogramHovered: [255, 0, 0, 255],
    dpg.mvThemeCol_TableHeaderBg: [0, 0, 0, 132],
    dpg.mvThemeCol_TableBorderStrong: [0, 0, 0, 132],
    dpg.mvThemeCol_TableBorderLight: [71, 71, 71, 73],
    dpg.mvThemeCol_TableRowBg: [0, 0, 0, 0],
    dpg.mvThemeCol_TableRowBgAlt: [255, 255, 255, 15],
    dpg.mvThemeCol_TextSelectedBg: [51, 56, 58, 255],
    dpg.mvThemeCol_DragDropTarget: [84, 170, 219, 255],
    dpg.mvThemeCol_NavHighlight: [255, 0, 0, 255],
    dpg.mvThemeCol_NavWindowingHighlight: [255, 0, 0, 178],
    dpg.mvThemeCol_NavWindowingDimBg: [255, 0, 0, 51],
    dpg.mvThemeCol_ModalWindowDimBg: [255, 0, 0, 89],
}
