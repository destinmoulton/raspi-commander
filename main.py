import remi.gui as gui
from remi import start, App

from ScriptBox import ScriptBox
from ServicesBox import ServicesBox

from config import IP


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        main_container = gui.Widget()
        main_container.style['margin'] = "20px"

        script_box = ScriptBox()
        main_container.append(script_box.build_script_box())

        servicesbox = ServicesBox()
        main_container.append(servicesbox.build_services_box())

        # returning the root widget
        return main_container


# starts the webserver
start(MyApp,
      address=IP,
      port=9090,
      enable_file_cache=False,
      update_interval=0.1)
