import remi.gui as gui
from Styles import StdoutBoxStyles


class StdoutBox:
    def __init__(self):
        self.stdouts = []
        self.lst_termout = gui.ListView(style=StdoutBoxStyles["list"])

    def append(self, data):
        self.stdouts.append(data)
        data = data.replace("\n", "<br/>")
        self.lst_termout.append(gui.ListItem(data))

    def build_stdout_box(self):
        lb_title = gui.Label("Terminal Output", style=StdoutBoxStyles["title"])
        bt_clear = gui.Button("Clear", style=StdoutBoxStyles["clear_button"])
        bt_clear.set_on_click_listener(self.on_click_clear)

        hbox_top = gui.HBox(style=StdoutBoxStyles["top_container"])
        hbox_top.style["justify-content"] = "left"
        hbox_top.append(lb_title)
        hbox_top.append(bt_clear)

        vbox_stdout = gui.VBox(style=StdoutBoxStyles["stdout_section"])
        vbox_stdout.append(hbox_top)
        vbox_stdout.append(self.lst_termout)
        return vbox_stdout

    def on_click_clear(self, widget):
        self.lst_termout.empty()
