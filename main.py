import os
import remi.gui as gui
from remi import start, App

from guicomponents.ipbox import IPBox
from guicomponents.title_bar import TitleBar
from guicomponents.scriptbox import ScriptBox
from guicomponents.servicesbox import ServicesBox
from guicomponents.stdoutbox import StdoutBox

from config import IP, PORT, JS_FILES
from Styles import MainStyles


class RaspiCommander(App):
    def __init__(self, *args):
        static_path = os.path.join(os.path.dirname(__file__), 'res')
        super(RaspiCommander, self).__init__(
            *args, static_file_path=static_path)

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

        self.title_bar.add_widget_to_middle(self.ipbox.build_ip_box())

        vbox_main = gui.VBox()
        vbox_main.append(self.title_bar.build_title_bar())
        vbox_main.append(self._build_middle_box())
        vbox_main.append(self.stdoutbox.build_stdout_box())

        for js_file in JS_FILES:
            # Add the javascript scripts to the end
            js = gui.Tag(_type='script')
            js.attributes["src"] = "/res/{}".format(js_file)
            vbox_main.add_child(js_file, js)

        return vbox_main

    def _build_middle_box(self):

        middle_container = gui.HBox(style=MainStyles['middle_container'])
        middle_container.style["align-items"] = "stretch"

        vbox_left = gui.VBox()

        self.ipbox.refresh_ip_box()

        vbox_left.append(self.servicesbox.build_services_box())
        self.servicesbox.refresh_service_table()

        middle_container.append(vbox_left)

        middle_container.append(self.scriptbox.build_script_box())
        self.scriptbox.refresh_scripts_table()

        # returning the root widget
        return middle_container


if __name__ == "__main__":
    # Starts the remi web server
    start(RaspiCommander,
          address=IP,
          port=PORT,
          enable_file_cache=False,
          update_interval=0.1)
