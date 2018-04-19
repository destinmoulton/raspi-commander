import remi.gui as gui

from guicomponents.generic_refresh_button import GenericRefreshButton
from Styles import LastRefreshedStyles
from config import TIME_FORMAT
from helpers import timehelper


class RefreshBar:
    def __init__(self, refresh_handler):
        self.refresh_handler = refresh_handler

    def build_refresh_bar(self):
        generic_refresh_button = GenericRefreshButton()
        refresh_button = generic_refresh_button.build_button(
            "Refresh", self.run_refresh)

        self.box_last_refreshed = gui.Widget()

        hbox_refresh_bar = gui.HBox()
        hbox_refresh_bar.append(refresh_button)
        hbox_refresh_bar.append(self.box_last_refreshed)
        return hbox_refresh_bar

    def run_refresh(self):
        self.refresh_handler()

    def update_refresh_time(self):
        # Update the refresh time
        self.box_last_refreshed.empty()
        self.box_last_refreshed.append(
            self.get_last_refreshed())

    def get_last_refreshed(self):

        time = timehelper.get_now_formatted()
        text = "Last refreshed: {}".format(time)

        lb = gui.Label(text, style=LastRefreshedStyles["text"])

        cont = gui.Widget()
        cont.append(lb)
        return cont
