import dearpygui.dearpygui as dpg

from typing import Optional, Sequence

from .themes import THEME,theme_list


dpg_keys =[
    dpg.mvGraphicsBackend_D3D11,
    dpg.mvGraphicsBackend_D3D12,
    dpg.mvGraphicsBackend_VULKAN,
    dpg.mvGraphicsBackend_METAL,
    dpg.mvGraphicsBackend_OPENGL,
    dpg.mvMouseButton_Left,
    dpg.mvMouseButton_Right,
    dpg.mvMouseButton_Middle,
    dpg.mvMouseButton_X1,
    dpg.mvMouseButton_X2,
    dpg.mvKey_0,
    dpg.mvKey_1,
    dpg.mvKey_2,
    dpg.mvKey_3,
    dpg.mvKey_4,
    dpg.mvKey_5,
    dpg.mvKey_6,
    dpg.mvKey_7,
    dpg.mvKey_8,
    dpg.mvKey_9,
    dpg.mvKey_A,
    dpg.mvKey_B,
    dpg.mvKey_C,
    dpg.mvKey_D,
    dpg.mvKey_E,
    dpg.mvKey_F,
    dpg.mvKey_G,
    dpg.mvKey_H,
    dpg.mvKey_I,
    dpg.mvKey_J,
    dpg.mvKey_K,
    dpg.mvKey_L,
    dpg.mvKey_M,
    dpg.mvKey_N,
    dpg.mvKey_O,
    dpg.mvKey_P,
    dpg.mvKey_Q,
    dpg.mvKey_R,
    dpg.mvKey_S,
    dpg.mvKey_T,
    dpg.mvKey_U,
    dpg.mvKey_V,
    dpg.mvKey_W,
    dpg.mvKey_X,
    dpg.mvKey_Y,
    dpg.mvKey_Z,
    dpg.mvKey_Back,
    dpg.mvKey_Tab,
    dpg.mvKey_Clear,
    dpg.mvKey_Return,
    dpg.mvKey_Shift,
    dpg.mvKey_Control,
    dpg.mvKey_Alt,
    dpg.mvKey_Pause,
    dpg.mvKey_Capital,
    dpg.mvKey_Escape,
    dpg.mvKey_Spacebar,
    dpg.mvKey_Prior,
    dpg.mvKey_Next,
    dpg.mvKey_End,
    dpg.mvKey_Home,
    dpg.mvKey_Left,
    dpg.mvKey_Up,
    dpg.mvKey_Right,
    dpg.mvKey_Down,
    dpg.mvKey_Select,
    dpg.mvKey_Print,
    dpg.mvKey_Execute,
    dpg.mvKey_PrintScreen,
    dpg.mvKey_Insert,
    dpg.mvKey_Delete,
    dpg.mvKey_Help,
    dpg.mvKey_LWin,
    dpg.mvKey_RWin,
    dpg.mvKey_Apps,
    dpg.mvKey_Sleep,
    dpg.mvKey_NumPad0,
    dpg.mvKey_NumPad1,
    dpg.mvKey_NumPad2,
    dpg.mvKey_NumPad3,
    dpg.mvKey_NumPad4,
    dpg.mvKey_NumPad5,
    dpg.mvKey_NumPad6,
    dpg.mvKey_NumPad7,
    dpg.mvKey_NumPad8,
    dpg.mvKey_NumPad9,
    dpg.mvKey_Multiply,
    dpg.mvKey_Add,
    dpg.mvKey_Separator,
    dpg.mvKey_Subtract,
    dpg.mvKey_Decimal,
    dpg.mvKey_Divide,
    dpg.mvKey_F1,
    dpg.mvKey_F2,
    dpg.mvKey_F3,
    dpg.mvKey_F4,
    dpg.mvKey_F5,
    dpg.mvKey_F6,
    dpg.mvKey_F7,
    dpg.mvKey_F8,
    dpg.mvKey_F9,
    dpg.mvKey_F10,
    dpg.mvKey_F11,
    dpg.mvKey_F12,
    dpg.mvKey_F13,
    dpg.mvKey_F14,
    dpg.mvKey_F15,
    dpg.mvKey_F16,
    dpg.mvKey_F17,
    dpg.mvKey_F18,
    dpg.mvKey_F19,
    dpg.mvKey_F20,
    dpg.mvKey_F21,
    dpg.mvKey_F22,
    dpg.mvKey_F23,
    dpg.mvKey_F24,
    dpg.mvKey_F25,
    dpg.mvKey_NumLock,
    dpg.mvKey_ScrollLock,
    dpg.mvKey_LShift,
    dpg.mvKey_RShift,
    dpg.mvKey_LControl,
    dpg.mvKey_RControl,
    dpg.mvKey_LMenu,
    dpg.mvKey_RMenu,
    dpg.mvKey_Browser_Back,
    dpg.mvKey_Browser_Forward,
    dpg.mvKey_Browser_Refresh,
    dpg.mvKey_Browser_Stop,
    dpg.mvKey_Browser_Search,
    dpg.mvKey_Browser_Favorites,
    dpg.mvKey_Browser_Home,
    dpg.mvKey_Volume_Mute,
    dpg.mvKey_Volume_Down,
    dpg.mvKey_Volume_Up,
    dpg.mvKey_Media_Next_Track,
    dpg.mvKey_Media_Prev_Track,
    dpg.mvKey_Media_Stop,
    dpg.mvKey_Media_Play_Pause,
    dpg.mvKey_Launch_Mail,
    dpg.mvKey_Launch_Media_Select,
    dpg.mvKey_Launch_App1,
    dpg.mvKey_Launch_App2,
    dpg.mvKey_Colon,
    dpg.mvKey_Plus,
    dpg.mvKey_Comma,
    dpg.mvKey_Minus,
    dpg.mvKey_Period,
    dpg.mvKey_Slash,
    dpg.mvKey_Tilde,
    dpg.mvKey_Open_Brace,
    dpg.mvKey_Backslash,
    dpg.mvKey_Close_Brace,
    dpg.mvKey_Quote,
    dpg.mvAll,
    dpg.mvTool_About,
    dpg.mvTool_Debug,
    dpg.mvTool_Doc,
    dpg.mvTool_ItemRegistry,
    dpg.mvTool_Metrics,
    dpg.mvTool_Style,
    dpg.mvTool_Font,
    dpg.mvFontAtlas,
    dpg.mvAppUUID,
    dpg.mvInvalidUUID,
    dpg.mvDir_None,
    dpg.mvDir_Left,
    dpg.mvDir_Right,
    dpg.mvDir_Up,
    dpg.mvDir_Down,
    dpg.mvComboHeight_Small,
    dpg.mvComboHeight_Regular,
    dpg.mvComboHeight_Large,
    dpg.mvComboHeight_Largest,
    dpg.mvPlatform_Windows,
    dpg.mvPlatform_Apple,
    dpg.mvPlatform_Linux,
    dpg.mvColorEdit_AlphaPreviewNone,
    dpg.mvColorEdit_AlphaPreview,
    dpg.mvColorEdit_AlphaPreviewHalf,
    dpg.mvColorEdit_uint8,
    dpg.mvColorEdit_float,
    dpg.mvColorEdit_rgb,
    dpg.mvColorEdit_hsv,
    dpg.mvColorEdit_hex,
    dpg.mvColorEdit_input_rgb,
    dpg.mvColorEdit_input_hsv,
    dpg.mvPlotColormap_Default,
    dpg.mvPlotColormap_Deep,
    dpg.mvPlotColormap_Dark,
    dpg.mvPlotColormap_Pastel,
    dpg.mvPlotColormap_Paired,
    dpg.mvPlotColormap_Viridis,
    dpg.mvPlotColormap_Plasma,
    dpg.mvPlotColormap_Hot,
    dpg.mvPlotColormap_Cool,
    dpg.mvPlotColormap_Pink,
    dpg.mvPlotColormap_Jet,
    dpg.mvPlotColormap_Twilight,
    dpg.mvPlotColormap_RdBu,
    dpg.mvPlotColormap_BrBG,
    dpg.mvPlotColormap_PiYG,
    dpg.mvPlotColormap_Spectral,
    dpg.mvPlotColormap_Greys,
    dpg.mvColorPicker_bar,
    dpg.mvColorPicker_wheel,
    dpg.mvTabOrder_Reorderable,
    dpg.mvTabOrder_Fixed,
    dpg.mvTabOrder_Leading,
    dpg.mvTabOrder_Trailing,
    dpg.mvTimeUnit_Us,
    dpg.mvTimeUnit_Ms,
    dpg.mvTimeUnit_S,
    dpg.mvTimeUnit_Min,
    dpg.mvTimeUnit_Hr,
    dpg.mvTimeUnit_Day,
    dpg.mvTimeUnit_Mo,
    dpg.mvTimeUnit_Yr,
    dpg.mvDatePickerLevel_Day,
    dpg.mvDatePickerLevel_Month,
    dpg.mvDatePickerLevel_Year,
    dpg.mvCullMode_None,
    dpg.mvCullMode_Back,
    dpg.mvCullMode_Front,
    dpg.mvFontRangeHint_Default,
    dpg.mvFontRangeHint_Japanese,
    dpg.mvFontRangeHint_Korean,
    dpg.mvFontRangeHint_Chinese_Full,
    dpg.mvFontRangeHint_Chinese_Simplified_Common,
    dpg.mvFontRangeHint_Cyrillic,
    dpg.mvFontRangeHint_Thai,
    dpg.mvFontRangeHint_Vietnamese,
    dpg.mvNode_PinShape_Circle,
    dpg.mvNode_PinShape_CircleFilled,
    dpg.mvNode_PinShape_Triangle,
    dpg.mvNode_PinShape_TriangleFilled,
    dpg.mvNode_PinShape_Quad,
    dpg.mvNode_PinShape_QuadFilled,
    dpg.mvNode_Attr_Input,
    dpg.mvNode_Attr_Output,
    dpg.mvNode_Attr_Static,
    dpg.mvPlotBin_Sqrt,
    dpg.mvPlotBin_Sturges,
    dpg.mvPlotBin_Rice,
    dpg.mvPlotBin_Scott,
    dpg.mvXAxis,
    dpg.mvYAxis,
    dpg.mvPlotMarker_None,
    dpg.mvPlotMarker_Circle,
    dpg.mvPlotMarker_Square,
    dpg.mvPlotMarker_Diamond,
    dpg.mvPlotMarker_Up,
    dpg.mvPlotMarker_Down,
    dpg.mvPlotMarker_Left,
    dpg.mvPlotMarker_Right,
    dpg.mvPlotMarker_Cross,
    dpg.mvPlotMarker_Plus,
    dpg.mvPlotMarker_Asterisk,
    dpg.mvPlot_Location_Center,
    dpg.mvPlot_Location_North,
    dpg.mvPlot_Location_South,
    dpg.mvPlot_Location_West,
    dpg.mvPlot_Location_East,
    dpg.mvPlot_Location_NorthWest,
    dpg.mvPlot_Location_NorthEast,
    dpg.mvPlot_Location_SouthWest,
    dpg.mvPlot_Location_SouthEast,
    dpg.mvNodeMiniMap_Location_BottomLeft,
    dpg.mvNodeMiniMap_Location_BottomRight,
    dpg.mvNodeMiniMap_Location_TopLeft,
    dpg.mvNodeMiniMap_Location_TopRight,
    dpg.mvTable_SizingFixedFit,
    dpg.mvTable_SizingFixedSame,
    dpg.mvTable_SizingStretchProp,
    dpg.mvTable_SizingStretchSame,
    dpg.mvFormat_Float_rgba,
    dpg.mvFormat_Float_rgb,
    dpg.mvThemeCat_Core,
    dpg.mvThemeCat_Plots,
    dpg.mvThemeCat_Nodes,
    dpg.mvThemeCol_Text,
    dpg.mvThemeCol_TextDisabled,
    dpg.mvThemeCol_WindowBg,
    dpg.mvThemeCol_ChildBg,
    dpg.mvThemeCol_Border,
    dpg.mvThemeCol_PopupBg,
    dpg.mvThemeCol_BorderShadow,
    dpg.mvThemeCol_FrameBg,
    dpg.mvThemeCol_FrameBgHovered,
    dpg.mvThemeCol_FrameBgActive,
    dpg.mvThemeCol_TitleBg,
    dpg.mvThemeCol_TitleBgActive,
    dpg.mvThemeCol_TitleBgCollapsed,
    dpg.mvThemeCol_MenuBarBg,
    dpg.mvThemeCol_ScrollbarBg,
    dpg.mvThemeCol_ScrollbarGrab,
    dpg.mvThemeCol_ScrollbarGrabHovered,
    dpg.mvThemeCol_ScrollbarGrabActive,
    dpg.mvThemeCol_CheckMark,
    dpg.mvThemeCol_SliderGrab,
    dpg.mvThemeCol_SliderGrabActive,
    dpg.mvThemeCol_Button,
    dpg.mvThemeCol_ButtonHovered,
    dpg.mvThemeCol_ButtonActive,
    dpg.mvThemeCol_Header,
    dpg.mvThemeCol_HeaderHovered,
    dpg.mvThemeCol_HeaderActive,
    dpg.mvThemeCol_Separator,
    dpg.mvThemeCol_SeparatorHovered,
    dpg.mvThemeCol_SeparatorActive,
    dpg.mvThemeCol_ResizeGrip,
    dpg.mvThemeCol_ResizeGripHovered,
    dpg.mvThemeCol_ResizeGripActive,
    dpg.mvThemeCol_Tab,
    dpg.mvThemeCol_TabHovered,
    dpg.mvThemeCol_TabActive,
    dpg.mvThemeCol_TabUnfocused,
    dpg.mvThemeCol_TabUnfocusedActive,
    dpg.mvThemeCol_DockingPreview,
    dpg.mvThemeCol_DockingEmptyBg,
    dpg.mvThemeCol_PlotLines,
    dpg.mvThemeCol_PlotLinesHovered,
    dpg.mvThemeCol_PlotHistogram,
    dpg.mvThemeCol_PlotHistogramHovered,
    dpg.mvThemeCol_TableHeaderBg,
    dpg.mvThemeCol_TableBorderStrong,
    dpg.mvThemeCol_TableBorderLight,
    dpg.mvThemeCol_TableRowBg,
    dpg.mvThemeCol_TableRowBgAlt,
    dpg.mvThemeCol_TextSelectedBg,
    dpg.mvThemeCol_DragDropTarget,
    dpg.mvThemeCol_NavHighlight,
    dpg.mvThemeCol_NavWindowingHighlight,
    dpg.mvThemeCol_NavWindowingDimBg,
    dpg.mvThemeCol_ModalWindowDimBg,
    dpg.mvPlotCol_Line,
    dpg.mvPlotCol_Fill,
    dpg.mvPlotCol_MarkerOutline,
    dpg.mvPlotCol_MarkerFill,
    dpg.mvPlotCol_ErrorBar,
    dpg.mvPlotCol_FrameBg,
    dpg.mvPlotCol_PlotBg,
    dpg.mvPlotCol_PlotBorder,
    dpg.mvPlotCol_LegendBg,
    dpg.mvPlotCol_LegendBorder,
    dpg.mvPlotCol_LegendText,
    dpg.mvPlotCol_TitleText,
    dpg.mvPlotCol_InlayText,
    dpg.mvPlotCol_XAxis,
    dpg.mvPlotCol_XAxisGrid,
    dpg.mvPlotCol_YAxis,
    dpg.mvPlotCol_YAxisGrid,
    dpg.mvPlotCol_YAxis2,
    dpg.mvPlotCol_YAxisGrid2,
    dpg.mvPlotCol_YAxis3,
    dpg.mvPlotCol_YAxisGrid3,
    dpg.mvPlotCol_Selection,
    dpg.mvPlotCol_Query,
    dpg.mvPlotCol_Crosshairs,
    dpg.mvNodeCol_NodeBackground,
    dpg.mvNodeCol_NodeBackgroundHovered,
    dpg.mvNodeCol_NodeBackgroundSelected,
    dpg.mvNodeCol_NodeOutline,
    dpg.mvNodeCol_TitleBar,
    dpg.mvNodeCol_TitleBarHovered,
    dpg.mvNodeCol_TitleBarSelected,
    dpg.mvNodeCol_Link,
    dpg.mvNodeCol_LinkHovered,
    dpg.mvNodeCol_LinkSelected,
    dpg.mvNodeCol_Pin,
    dpg.mvNodeCol_PinHovered,
    dpg.mvNodeCol_BoxSelector,
    dpg.mvNodeCol_BoxSelectorOutline,
    dpg.mvNodeCol_GridBackground,
    dpg.mvNodeCol_GridLine,
    dpg.mvNodesCol_GridLinePrimary,
    dpg.mvNodesCol_MiniMapBackground,
    dpg.mvNodesCol_MiniMapBackgroundHovered,
    dpg.mvNodesCol_MiniMapOutline,
    dpg.mvNodesCol_MiniMapOutlineHovered,
    dpg.mvNodesCol_MiniMapNodeBackground,
    dpg.mvNodesCol_MiniMapNodeBackgroundHovered,
    dpg.mvNodesCol_MiniMapNodeBackgroundSelected,
    dpg.mvNodesCol_MiniMapNodeOutline,
    dpg.mvNodesCol_MiniMapLink,
    dpg.mvNodesCol_MiniMapLinkSelected,
    dpg.mvNodesCol_MiniMapCanvas,
    dpg.mvNodesCol_MiniMapCanvasOutline,
    dpg.mvStyleVar_Alpha,
    dpg.mvStyleVar_WindowPadding,
    dpg.mvStyleVar_WindowRounding,
    dpg.mvStyleVar_WindowBorderSize,
    dpg.mvStyleVar_WindowMinSize,
    dpg.mvStyleVar_WindowTitleAlign,
    dpg.mvStyleVar_ChildRounding,
    dpg.mvStyleVar_ChildBorderSize,
    dpg.mvStyleVar_PopupRounding,
    dpg.mvStyleVar_PopupBorderSize,
    dpg.mvStyleVar_FramePadding,
    dpg.mvStyleVar_FrameRounding,
    dpg.mvStyleVar_FrameBorderSize,
    dpg.mvStyleVar_ItemSpacing,
    dpg.mvStyleVar_ItemInnerSpacing,
    dpg.mvStyleVar_IndentSpacing,
    dpg.mvStyleVar_CellPadding,
    dpg.mvStyleVar_ScrollbarSize,
    dpg.mvStyleVar_ScrollbarRounding,
    dpg.mvStyleVar_GrabMinSize,
    dpg.mvStyleVar_GrabRounding,
    dpg.mvStyleVar_TabRounding,
    dpg.mvStyleVar_ButtonTextAlign,
    dpg.mvStyleVar_SelectableTextAlign,
    dpg.mvPlotStyleVar_LineWeight,
    dpg.mvPlotStyleVar_Marker,
    dpg.mvPlotStyleVar_MarkerSize,
    dpg.mvPlotStyleVar_MarkerWeight,
    dpg.mvPlotStyleVar_FillAlpha,
    dpg.mvPlotStyleVar_ErrorBarSize,
    dpg.mvPlotStyleVar_ErrorBarWeight,
    dpg.mvPlotStyleVar_DigitalBitHeight,
    dpg.mvPlotStyleVar_DigitalBitGap,
    dpg.mvPlotStyleVar_PlotBorderSize,
    dpg.mvPlotStyleVar_MinorAlpha,
    dpg.mvPlotStyleVar_MajorTickLen,
    dpg.mvPlotStyleVar_MinorTickLen,
    dpg.mvPlotStyleVar_MajorTickSize,
    dpg.mvPlotStyleVar_MinorTickSize,
    dpg.mvPlotStyleVar_MajorGridSize,
    dpg.mvPlotStyleVar_MinorGridSize,
    dpg.mvPlotStyleVar_PlotPadding,
    dpg.mvPlotStyleVar_LabelPadding,
    dpg.mvPlotStyleVar_LegendPadding,
    dpg.mvPlotStyleVar_LegendInnerPadding,
    dpg.mvPlotStyleVar_LegendSpacing,
    dpg.mvPlotStyleVar_MousePosPadding,
    dpg.mvPlotStyleVar_AnnotationPadding,
    dpg.mvPlotStyleVar_FitPadding,
    dpg.mvPlotStyleVar_PlotDefaultSize,
    dpg.mvPlotStyleVar_PlotMinSize,
    dpg.mvNodeStyleVar_GridSpacing,
    dpg.mvNodeStyleVar_NodeCornerRounding,
    dpg.mvNodeStyleVar_NodePadding,
    dpg.mvNodeStyleVar_NodeBorderThickness,
    dpg.mvNodeStyleVar_LinkThickness,
    dpg.mvNodeStyleVar_LinkLineSegmentsPerLength,
    dpg.mvNodeStyleVar_LinkHoverDistance,
    dpg.mvNodeStyleVar_PinCircleRadius,
    dpg.mvNodeStyleVar_PinQuadSideLength,
    dpg.mvNodeStyleVar_PinTriangleSideLength,
    dpg.mvNodeStyleVar_PinLineThickness,
    dpg.mvNodeStyleVar_PinHoverRadius,
    dpg.mvNodeStyleVar_PinOffset,
    dpg.mvNodesStyleVar_MiniMapPadding,
    dpg.mvNodesStyleVar_MiniMapOffset,
    dpg.mvInputText,
    dpg.mvButton,
    dpg.mvRadioButton,
    dpg.mvTabBar,
    dpg.mvTab,
    dpg.mvImage,
    dpg.mvMenuBar,
    dpg.mvViewportMenuBar,
    dpg.mvMenu,
    dpg.mvMenuItem,
    dpg.mvChildWindow,
    dpg.mvGroup,
    dpg.mvSliderFloat,
    dpg.mvSliderInt,
    dpg.mvFilterSet,
    dpg.mvDragFloat,
    dpg.mvDragInt,
    dpg.mvInputFloat,
    dpg.mvInputInt,
    dpg.mvColorEdit,
    dpg.mvClipper,
    dpg.mvColorPicker,
    dpg.mvTooltip,
    dpg.mvCollapsingHeader,
    dpg.mvSeparator,
    dpg.mvCheckbox,
    dpg.mvListbox,
    dpg.mvText,
    dpg.mvCombo,
    dpg.mvPlot,
    dpg.mvSimplePlot,
    dpg.mvDrawlist,
    dpg.mvWindowAppItem,
    dpg.mvSelectable,
    dpg.mvTreeNode,
    dpg.mvProgressBar,
    dpg.mvSpacer,
    dpg.mvImageButton,
    dpg.mvTimePicker,
    dpg.mvDatePicker,
    dpg.mvColorButton,
    dpg.mvFileDialog,
    dpg.mvTabButton,
    dpg.mvDrawNode,
    dpg.mvNodeEditor,
    dpg.mvNode,
    dpg.mvNodeAttribute,
    dpg.mvTable,
    dpg.mvTableColumn,
    dpg.mvTableRow,
    dpg.mvDrawLine,
    dpg.mvDrawArrow,
    dpg.mvDrawTriangle,
    dpg.mvDrawImageQuad,
    dpg.mvDrawCircle,
    dpg.mvDrawEllipse,
    dpg.mvDrawBezierCubic,
    dpg.mvDrawBezierQuadratic,
    dpg.mvDrawQuad,
    dpg.mvDrawRect,
    dpg.mvDrawText,
    dpg.mvDrawPolygon,
    dpg.mvDrawPolyline,
    dpg.mvDrawImage,
    dpg.mvDragFloatMulti,
    dpg.mvDragIntMulti,
    dpg.mvSliderFloatMulti,
    dpg.mvSliderIntMulti,
    dpg.mvInputIntMulti,
    dpg.mvInputFloatMulti,
    dpg.mvDragPoint,
    dpg.mvDragLine,
    dpg.mvAnnotation,
    dpg.mvLineSeries,
    dpg.mvScatterSeries,
    dpg.mvStemSeries,
    dpg.mvStairSeries,
    dpg.mvBarSeries,
    dpg.mvErrorSeries,
    dpg.mvVLineSeries,
    dpg.mvHLineSeries,
    dpg.mvHeatSeries,
    dpg.mvImageSeries,
    dpg.mvPieSeries,
    dpg.mvShadeSeries,
    dpg.mvLabelSeries,
    dpg.mvHistogramSeries,
    dpg.mv2dHistogramSeries,
    dpg.mvCandleSeries,
    dpg.mvAreaSeries,
    dpg.mvColorMapScale,
    dpg.mvSlider3D,
    dpg.mvKnobFloat,
    dpg.mvLoadingIndicator,
    dpg.mvNodeLink,
    dpg.mvTextureRegistry,
    dpg.mvStaticTexture,
    dpg.mvDynamicTexture,
    dpg.mvStage,
    dpg.mvDrawLayer,
    dpg.mvViewportDrawlist,
    dpg.mvFileExtension,
    dpg.mvPlotLegend,
    dpg.mvPlotAxis,
    dpg.mvHandlerRegistry,
    dpg.mvKeyDownHandler,
    dpg.mvKeyPressHandler,
    dpg.mvKeyReleaseHandler,
    dpg.mvMouseMoveHandler,
    dpg.mvMouseWheelHandler,
    dpg.mvMouseClickHandler,
    dpg.mvMouseDoubleClickHandler,
    dpg.mvMouseDownHandler,
    dpg.mvMouseReleaseHandler,
    dpg.mvMouseDragHandler,
    dpg.mvHoverHandler,
    dpg.mvActiveHandler,
    dpg.mvFocusHandler,
    dpg.mvVisibleHandler,
    dpg.mvEditedHandler,
    dpg.mvActivatedHandler,
    dpg.mvDeactivatedHandler,
    dpg.mvDeactivatedAfterEditHandler,
    dpg.mvToggledOpenHandler,
    dpg.mvClickedHandler,
    # dpg.mvDoubleClickedHandler,
    dpg.mvDragPayload,
    dpg.mvResizeHandler,
    dpg.mvFont,
    dpg.mvFontRegistry,
    dpg.mvTheme,
    dpg.mvThemeColor,
    dpg.mvThemeStyle,
    dpg.mvThemeComponent,
    dpg.mvFontRangeHint,
    dpg.mvFontRange,
    dpg.mvFontChars,
    dpg.mvCharRemap,
    dpg.mvValueRegistry,
    dpg.mvIntValue,
    dpg.mvFloatValue,
    dpg.mvFloat4Value,
    dpg.mvInt4Value,
    dpg.mvBoolValue,
    dpg.mvStringValue,
    dpg.mvDoubleValue,
    dpg.mvDouble4Value,
    dpg.mvColorValue,
    dpg.mvFloatVectValue,
    dpg.mvSeriesValue,
    dpg.mvRawTexture,
    dpg.mvSubPlots,
    dpg.mvColorMap,
    dpg.mvColorMapRegistry,
    dpg.mvColorMapButton,
    dpg.mvColorMapSlider,
    dpg.mvTemplateRegistry,
    dpg.mvTableCell,
    dpg.mvItemHandlerRegistry,
    dpg.mvInputDouble,
    dpg.mvInputDoubleMulti,
    dpg.mvDragDouble,
    dpg.mvDragDoubleMulti,
    dpg.mvSliderDouble,
    dpg.mvSliderDoubleMulti,
    dpg.mvCustomSeries,
    dpg.mvReservedUUID_0,
    dpg.mvReservedUUID_1,
    dpg.mvReservedUUID_2,
    dpg.mvReservedUUID_3,
    dpg.mvReservedUUID_4,
    dpg.mvReservedUUID_5,
    dpg.mvReservedUUID_6,
    dpg.mvReservedUUID_7,
    dpg.mvReservedUUID_8,
    dpg.mvReservedUUID_9
]


def apply_theme(theme_id:int=8):

    newTheme = theme_list[theme_id]
    # print(newTheme)

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            for dpg_id, style in newTheme.styles.items():
                dpg.add_theme_style(dpg_id, *style, category=dpg.mvThemeCat_Core)
            for dpg_id, color in newTheme.colors.items():
                dpg.add_theme_color(dpg_id, color, category=dpg.mvThemeCat_Core)  
        for dpg_key in dpg_keys:
            try:
                with dpg.theme_component(dpg_key,enabled_state=False):
                    for dpg_id, style in newTheme.styles.items():
                        dpg.add_theme_style(dpg_id, *style, category=dpg.mvThemeCat_Core)
                    for dpg_id, color in newTheme.colors.items():
                        color = [int(c*0.5) for c in color]
                        dpg.add_theme_color(dpg_id, color, category=dpg.mvThemeCat_Core)  
            except Exception as e:
                print(str(e))
                pass

    dpg.bind_theme(global_theme)