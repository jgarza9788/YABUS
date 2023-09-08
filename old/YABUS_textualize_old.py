from __future__ import annotations
from typing import Type

"""\
YABUS
yet another backup script

this is a UI for the main YABUS script
"""
__author__ = "Justin Garza"
__copyright__ = "Copyright 2023, Justin Garza"
__credits__ = ["Justin Garza"]
__license__ = "FSL"
__version__ = "1.5"
__maintainer__ = "Justin Garza"
__email__ = "Justin Garza"
__status__ = "Development"



import os,datetime,pathlib,time
import json5 as jason
import pandas as pd

from importlib_metadata import version
from rich import box
from rich.console import RenderableType
from rich.json import JSON
from rich.markdown import Markdown
from rich.pretty import Pretty
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
from textual._path import CSSPathType

from textual.app import App, CSSPathType, ComposeResult
from textual.binding import Binding
from textual.containers import (
    Container, 
    Horizontal, 
    ScrollableContainer,
    HorizontalScroll,
    VerticalScroll
)
from textual.driver import Driver
from textual.reactive import reactive
from textual.widgets import (
    Footer, 
    Label, 
    Tabs,
    Button,
    DataTable,
    Header,
    Input,
    RichLog,
    Static,
    Switch,
    Checkbox
)

# used for multi threading
# from concurrent.futures import ThreadPoolExecutor

# data manager
from utils.dataMan import DataManager
from utils.driveList import get_drives

# logging
import logging
from logging import Logger
from utils.logMan import createLogger
from io import StringIO
# import time

from YABUS import YABUS

class YABUS_Textualize(App):

    CSS_PATH = "textualize\style.css"

    BINDINGS = [
        # ("a", "add", "Add tab"),
        # ("r", "remove", "Remove active tab"),
        # ("c", "clear", "Clear tabs"),
        ("ctrl+q","app.quit","Quit"),
        ("ctrl+t", "app.toggle_dark", "Toggle Dark mode"),
        # ("ctrl+s", "app.screenshot()", "Screenshot"),
        ("f1", "app.toggle_class('RichLog', '-hidden')", "Notes"),
        Binding("ctrl+q", "app.quit", "Quit", show=True),
    ]

    def add_note(self, renderable: RenderableType) -> None:
        self.query_one(RichLog).write(renderable)

    def __init__(self, driver_class: type[Driver] | None = None, css_path: CSSPathType | None = None, watch_css: bool = False):
        super().__init__(driver_class, css_path, watch_css)

        self.yabus = YABUS()

    def format_lastbackup(self,lastbackup:str):
        if lastbackup == None:
            return 'None'
        return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]

    def compose(self) -> ComposeResult:
        # yield HorizontalScroll(
        #     # *[Checkbox("one"),Checkbox("two"),Checkbox("three")],
        #     *[Checkbox("hello")],
        #     id="main_container"
        # )

        # with VerticalScroll():
        #     with HorizontalScroll():
        #         yield Label("Hello, world!")
        #     for index,i in enumerate(self.yabus.items()):
        #         with HorizontalScroll():
        #             yield Checkbox('',i['enable'])
        #             yield Label("🟢" if i['runable'] else "🔴",id="runable")
        #             yield Input(value=i['source'],placeholder="source")
        #             yield Input(value=i['root_dest'],placeholder="root_dest")
        #             yield Input(value=i['ex_reg'],placeholder="ex_reg")
        #             yield Label(self.format_lastbackup(i['lastbackup']),id="lastbackup")
        yield Container(
            RichLog(classes="-hidden", wrap=False, highlight=True, markup=True,id="notes"),
        )
        yield Footer()

    def on_mount(self):
        # self.query_one("#initial_focus", Checkbox).focus()
        pass

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        print(
            event.checkbox.id, event.checkbox.value, event.checkbox == event.control
        )
        # self.events_received.append(
        #     (event.checkbox.id, event.checkbox.value, event.checkbox == event.control)
        # )


if __name__ == "__main__":
    YABUS_Textualize().run()