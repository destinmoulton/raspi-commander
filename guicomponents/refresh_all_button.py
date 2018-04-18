import remi.gui as gui

from Styles import RefreshBoxStyles


class RefreshAllButton:
    def __init__(self):
        self.button_handlers = []

        self.hbox_top = gui.HBox(style=RefreshBoxStyles["container"])

        title = gui.Label("RaspiCommander", style=RefreshBoxStyles["title"])
        bt_refresh_all = gui.Button(
            "Refresh All", style=RefreshBoxStyles["refresh_bt_all"])
        bt_refresh_all.set_on_click_listener(self.on_refresh_all)

        self.hbox_top.append(title)
        self.hbox_top.append(bt_refresh_all)

    def build_refresh_box(self):
        return self.hbox_top

    def add_refresh_handler(self, handler):
        self.button_handlers.append(handler)

    def on_refresh_all(self, widget):
        self.refresh_all()

    def refresh_all(self):
        """Run all of the refresh handlers"""
        for handler in self.button_handlers:
            handler()
