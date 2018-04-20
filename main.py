import remi.gui as gui
from remi import start, App

from guicomponents.ipbox import IPBox
from guicomponents.title_bar import TitleBar
from guicomponents.scriptbox import ScriptBox
from guicomponents.servicesbox import ServicesBox
from guicomponents.stdoutbox import StdoutBox

from config import IP
from Styles import MainStyles


class RaspiCommander(App):
    def __init__(self, *args):
        super(RaspiCommander, self).__init__(*args)

    def main(self):
        self.stdoutbox = StdoutBox()

        self.title_bar = TitleBar()
        self.ipbox = IPBox()
        self.servicesbox = ServicesBox(self.stdoutbox)
        self.scriptbox = ScriptBox(
            self.stdoutbox, self.title_bar.refresh_all)

        self.title_bar.add_refresh_handler(self.ipbox.handle_refresh_ip)
        self.title_bar.add_refresh_handler(
            self.scriptbox.handle_refresh_scripts)
        self.title_bar.add_refresh_handler(
            self.servicesbox.handle_refresh_services)

        vbox_main = gui.VBox()
        vbox_main.append(self.title_bar.build_title_bar())
        vbox_main.append(self._build_middle_box())
        vbox_main.append(self.stdoutbox.build_stdout_box())

        return vbox_main

    def _build_middle_box(self):

        middle_container = gui.HBox(style=MainStyles['middle_container'])

        vbox_left = gui.VBox()

        vbox_left.append(self.ipbox.build_ip_box())
        self.ipbox.refresh_ip_box()

        vbox_left.append(self.servicesbox.build_services_box())
        self.servicesbox.refresh_service_table()

        middle_container.append(vbox_left)

        middle_container.append(self.scriptbox.build_script_box())
        self.scriptbox.refresh_scripts_table()

        # returning the root widget
        return middle_container



# starts the webserver
start(RaspiCommander,
      address=IP,
      port=9090,
      enable_file_cache=False,
      update_interval=0.1)
