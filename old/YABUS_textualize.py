from textual.app import App, ComposeResult
# from textual.widgets import Footer, Label, Tabs

from rich.console import RenderableType
from rich.markdown import Markdown


from textual.reactive import reactive
from textual.containers import (
    Container,
    Horizontal,
    HorizontalScroll,
    VerticalScroll,
    Vertical
)
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
    Checkbox,
    RichLog,
    
)

import os
dir = os.path.dirname(os.path.realpath(__file__))

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

yabus = YABUS(
    config_dir = os.path.join(dir,'config.json'),
    verbose= False
    # logger = self.logger
    )

Tab_List = [
    "Settings",
    "Log",
    "About"
]

ABOUT_MD = """
# YABUS (textualized interface)
yet another back up script

author: Justin Garza  
copyright: Copyright 2023, Justin Garza  
credits:["Justin Garza"]  
license: FSL  
version: 0.1  
maintainer: Justin Garza  
email: JGarza9788@gmail.com  
status: Development  

"""

def format_lastbackup(lastbackup:str):
    if lastbackup == None:
        return 'None'
    return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]


def get_items_ui():
    result = []
    for index,i in enumerate(yabus.items()):
        result.append(
            Vertical(
                Label(f"#{str(index)}"),
                Horizontal(
                    Label('Source'),
                    Input(i['source'],placeholder="source")
                ),
                Horizontal(
                    Label('root_dest'),
                    Input(i['root_dest'],placeholder="root_dest")
                ),
                Horizontal(
                    Label('ex_reg'),
                    Input(i['ex_reg'],placeholder="ex_reg")
                ),
                Horizontal(
                    Label('lastbackup'),
                    Label(format_lastbackup(i['lastbackup'])),
                ),
            )
        )
        result.append(Label("-"*225))
    return result

class Settings(Container):
    def compose(self) -> ComposeResult:
        # yield Horizontal(
        #             Button(),
        #             Button(),
        #             Button(),
        #             Button(),
        #             id="settings_bar"
        #             )
        # yield Horizontal(
        #     Label("runable"),
        #     Label("enable"),
        #     Label("run"),
        #     Label("delete"),
        #     Label('Source'),
        #     Label('Dest_Root'),
        #     Label('ex_reg'),
        #     Label('LastBackUp'),
        #     id="headers"
        #     )
        yield VerticalScroll(
            *get_items_ui()
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.add_log("[b magenta]Start!")
        # self.app.query_one(".location-first").scroll_visible(duration=0.5, top=True)


class YABUS_App(App):
    """Demonstrates the Tabs widget."""

    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    # Label {
    #     margin:1 1;
    #     width: 100%;
    #     height: 100%;
    #     background: $panel;
    #     border: tall $primary;
    #     content-align: center middle;
    # }

    Vertical{
        height: 15;
        content-align: left top;
    }

    Label{
        
        min-width: 3;
        height: 3;
        # margin:0 1;
        background: $panel;
        border: tall $primary;
        content-align: center middle;
    }

    .title{
        width: 100%;
        height:3;
    }

    # #settings_grid{
    #     layout: grid;
    #     grid-size: 10 10;
    #     # grid-gutter: 1;
    #     # height: 100vh;
    #     # width:100%;
    # }

    #settings_bar{
        height: 3;
    }

    #headers{
        height:3;
    }

    #About{
        margin: 5;
    }

    # Column {
    #     height: auto;
    #     min-height: 10vh;
    #     align: center top;
    #     overflow: hidden;
    # }
    
    .none{
        display:none;
        width:0;
        height:0;
    }
    """

    BINDINGS = [
        ("ctrl+q","app.quit","Quit"),
        ("ctrl+t", "app.toggle_dark", "Toggle Dark mode"),
        # ("ctrl+l", "app.toggle_class('Log', '-hidden')", "Log"),
        ("ctrl+q", "app.quit", "Quit"),
    ]

    def add_log(self, renderable: RenderableType) -> None:
        self.query_one(RichLog).write(renderable)

    def compose(self) -> ComposeResult:
        yield Tabs()
        # yield Label("Settings",id="Settings",classes="-hidden")
        
        yield Settings(
                id="Settings"
                )
        
        yield Static(Markdown(ABOUT_MD),id="About")

        # yield Column(
        #     Static(Markdown(ABOUT_MD)),
        #     id="About"
        #     )
        
        yield RichLog(classes="-hidden", wrap=False, highlight=True, markup=True,id="Log")
        
        yield Footer()

    def on_mount(self) -> None:
        """Focus the tabs when the app starts."""
        tabs = self.query_one(Tabs)
        for t in Tab_List:
            tabs.add_tab(t)
        self.query(Tabs)[0].focus()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """Handle TabActivated message sent by Tabs."""
        self.add_log(event.tab)
        self.add_log(event.tab.label_text)
        
        for t in Tab_List:
            try:
                self.query_one(f"#{t}").add_class("none")
            except Exception as e:
                self.add_log(str(e))

        try:
            self.query_one(f"#{event.tab.label_text}").toggle_class("none")
        except Exception as e:
            self.add_log(str(e))


        # label = self.query_one(Label)
        # if event.tab is None:
        #     # When the tabs are cleared, event.tab will be None
        #     label.visible = False
        # else:
        #     label.visible = True
        #     label.update(event.tab.label)

    # def action_add(self) -> None:
    #     """Add a new tab."""
    #     tabs = self.query_one(Tabs)
    #     # Cycle the names
    #     Tab_List[:] = [*Tab_List[1:], Tab_List[0]]
    #     tabs.add_tab(Tab_List[0])

    # def action_remove(self) -> None:
    #     """Remove active tab."""
    #     tabs = self.query_one(Tabs)
    #     active_tab = tabs.active_tab
    #     if active_tab is not None:
    #         tabs.remove_tab(active_tab.id)

    # def action_clear(self) -> None:
    #     """Clear the tabs."""
    #     self.query_one(Tabs).clear()


if __name__ == "__main__":
    YABUS_App().run()
    
