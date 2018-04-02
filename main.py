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

        self.refreshbox = RefreshBox()
        self.ipbox = IPBox()
        self.servicesbox = ServicesBox(self.stdoutbox)
        self.scriptbox = ScriptBox(self.stdoutbox, self.refreshbox.refresh_all)

        self.refreshbox.add_button(
            "Refresh IP Address", self.ipbox.on_refresh_ip)
        self.refreshbox.add_button("Refresh Scripts",
                                   self.scriptbox.on_refresh_scripts)
        self.refreshbox.add_button("Refresh Services",
                                   self.servicesbox.on_refresh_services)

        vbox_main = gui.VBox()
        vbox_main.append(self.refreshbox.build_refresh_box())
        vbox_main.append(self._build_middle_box())
        vbox_main.append(self.stdoutbox.build_stdout_box())

        return vbox_main

    def _build_middle_box(self):

        middle_style = {
            "margin": "20px",
            "align-items": "left"

        }
        middle_container = gui.HBox(style=middle_style)

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
