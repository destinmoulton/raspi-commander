import remi.gui as gui


class StdoutBox:
    def __init__(self):
        self.stdouts = []
        self.lst_termout = gui.ListView()
        self.lst_termout.style['border'] = "1px solid green"

    def append(self, data):
        self.stdouts.append(data)
        data = data.replace("\n", "<br/>")
        self.lst_termout.append(gui.ListItem(data))

    def build_stdout_box(self):
        return self.lst_termout
