import remi.gui as gui

from Styles import TitleBarStyles, ButtonStyles


class TitleBar:
    def __init__(self):
        self.button_handlers = []

        title = gui.Label("Raspi Commander", style=TitleBarStyles["title"])
        bt_refresh_all = gui.Button(
            "Refresh All", style=ButtonStyles["refresh_bt_all"])
        bt_refresh_all.set_on_click_listener(self.on_refresh_all)

        hbox_left = gui.HBox(style=TitleBarStyles["left_box"])
        hbox_left.style["justify-content"] = "left"
        hbox_left.append(title)

        hbox_right = gui.HBox(style=TitleBarStyles["right_box"])
        hbox_right.append(bt_refresh_all)

        self.hbox_top = gui.HBox(style=TitleBarStyles["container"])
        self.hbox_top.append(hbox_left)
        self.hbox_top.append(hbox_right)

    def build_title_bar(self):
        return self.hbox_top

    def add_refresh_handler(self, handler):
        self.button_handlers.append(handler)

    def on_refresh_all(self, widget):
        self.refresh_all()

    def refresh_all(self):
        """Run all of the refresh handlers"""
        for handler in self.button_handlers:
            handler()
