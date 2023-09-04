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

    def __init__(self, driver_class: type[Driver] | None = None, css_path: CSSPathType | None = None, watch_css: bool = False):
        super().__init__(driver_class, css_path, watch_css)

        self.yabus = YABUS()

    def compose(self) -> ComposeResult:
        # yield HorizontalScroll(
        #     # *[Checkbox("one"),Checkbox("two"),Checkbox("three")],
        #     *[Checkbox("hello")],
        #     id="main_container"
        # )
        with VerticalScroll():
            with HorizontalScroll():
                yield Label("Hello, world!")
            for index,i in enumerate(self.yabus.items()):
                with HorizontalScroll():
                    yield Checkbox('',i['enable'])
                    # yield Checkbox('runable',i['runable'])
                    yield Label( "🟢True" if i['runable'] else "🔴False")
                    # yield Checkbox(str(i['enable']),i['enable'])
                    # yield Checkbox(str(i['enable']),i['enable'])
            # yield [Checkbox("one"),Checkbox("two"),Checkbox("three")]
            # yield Checkbox("Arrakis :sweat:")
            # yield Checkbox("Caladan")
            # yield Checkbox("Chusuk")
            # yield Checkbox("[b]Giedi Prime[/b]")
            # yield Checkbox("[magenta]Ginaz[/]")
            # yield Checkbox("Grumman", True)
            # yield Checkbox("Kaitain", id="initial_focus")
            # yield Checkbox("Novebruns", True)

    def on_mount(self):
        # self.query_one("#initial_focus", Checkbox).focus()
        pass


if __name__ == "__main__":
    YABUS_Textualize().run()