import remi.gui as gui
from remi import start, App

from IPBox import IPBox
from ScriptBox import ScriptBox
from ServicesBox import ServicesBox

from config import IP


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        main_container = gui.HBox()

        main_container.style['margin'] = "20px"
        main_container.style['align-items'] = "left"

        vbox_left = gui.VBox()

        ipbox = IPBox()
        vbox_left.append(ipbox.build_ip_box())
        ipbox.refresh_ip()

        servicesbox = ServicesBox()
        vbox_left.append(servicesbox.build_services_box())
        servicesbox.refresh_service_table()

        main_container.append(vbox_left)

        scriptbox = ScriptBox()
        main_container.append(scriptbox.build_script_box())
        scriptbox.refresh_scripts_table()

        # returning the root widget
        return main_container


# starts the webserver
start(MyApp,
      address=IP,
      port=9090,
      enable_file_cache=False,
      update_interval=0.1)
