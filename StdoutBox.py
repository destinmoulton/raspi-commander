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

        vbox_stdout = gui.VBox(style=StdoutBoxStyles["stdout_section"])
        vbox_stdout.append(lb_title)
        vbox_stdout.append(self.lst_termout)
        return vbox_stdout
