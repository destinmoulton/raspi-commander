import remi.gui as gui
from remi import start, App

from IPBox import IPBox
from RefreshBox import RefreshBox
from ScriptBox import ScriptBox
from ServicesBox import ServicesBox
from StdoutBox import StdoutBox

from config import IP


class RaspiCommander(App):
    def __init__(self, *args):
        super(RaspiCommander, self).__init__(*args)

    def main(self):
        self.stdoutbox = StdoutBox()
        self.ipbox = IPBox()
        self.servicesbox = ServicesBox(self.stdoutbox)
        self.scriptbox = ScriptBox(self.stdoutbox)
        self.refreshbox = RefreshBox(
            self.servicesbox, self.ipbox, self.scriptbox)

        vbox_main = gui.VBox()
        vbox_main.append(self.refreshbox.build_refresh_box())
        vbox_main.append(self._build_middle_box())
        vbox_main.append(self.stdoutbox.build_stdout_box())

        return vbox_main

    def _build_middle_box(self):

        middle_container = gui.HBox()
        middle_container.style['margin'] = "20px"
        middle_container.style['align-items'] = "left"

        vbox_left = gui.VBox()

        vbox_left.append(self.ipbox.build_ip_box())
        self.ipbox.refresh_ip()

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
