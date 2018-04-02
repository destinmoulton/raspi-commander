import remi.gui as gui

from Styles import RefreshBoxStyles


class RefreshBox:
    def __init__(self):
        self.button_handlers = []

        self.hbox_bt = gui.HBox()

        bt_refresh_all = gui.Button(
            "Refresh All", style=RefreshBoxStyles["refresh_bt_all"])
        bt_refresh_all.set_on_click_listener(self.on_refresh_all)

        self.hbox_bt.append(bt_refresh_all)

    def build_refresh_box(self):
        return self.hbox_bt

    def add_button(self, title, handler):
        bt = gui.Button(title, style=RefreshBoxStyles["refresh_bt_gen"])
        self.hbox_bt.append(bt)
        self.hbox_bt.set_on_click_listener(self._on_click_gen_refresh, handler)

        self.button_handlers.append(handler)

    def _on_click_gen_refresh(self, widget, handler):
        handler()

    def on_refresh_all(self, widget):
        self.refresh_all()

    def refresh_all(self):
        for handler in self.button_handlers:
            handler()
