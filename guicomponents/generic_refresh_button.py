import remi.gui as gui

from Styles import RefreshBoxStyles


class GenericRefreshButton:
    def build_button(self, title, on_click_handler):
        bt = gui.Button(title, style=RefreshBoxStyles["refresh_bt_gen"])
        # The passed handlers avoid the widget parameter (for callability)
        bt.set_on_click_listener(self._on_click_gen_refresh, on_click_handler)

        return bt

    def _on_click_gen_refresh(self, widget, handler):
        handler()
