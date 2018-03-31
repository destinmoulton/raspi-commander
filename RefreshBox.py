import remi.gui as gui


class RefreshBox:
    def __init__(self, servicesbox, ipbox, scriptbox):
        self.servicesbox = servicesbox
        self.ipbox = ipbox
        self.scriptbox = scriptbox

    def build_refresh_box(self):
        hbox_bt = gui.HBox()

        bt_refresh_all = gui.Button("Refresh All")
        bt_refresh_all.style['padding'] = "5px"
        bt_refresh_all.style['margin'] = "5px"
        bt_refresh_all.style['background-color'] = "green"
        bt_refresh_all.set_on_click_listener(self.on_refresh_all)

        bt_refresh_ip = gui.Button('Refresh IP Address')
        bt_refresh_ip.style['padding'] = "5px"
        bt_refresh_ip.style['margin'] = "5px"
        bt_refresh_ip.set_on_click_listener(self.ipbox.on_refresh_ip)

        bt_refresh_scripts = gui.Button('Refresh Script List')
        bt_refresh_scripts.style['padding'] = "5px"
        bt_refresh_scripts.style['margin'] = "5px"
        bt_refresh_scripts.set_on_click_listener(
            self.scriptbox.on_refresh_scripts)

        bt_refresh_services = gui.Button('Refresh Services')
        bt_refresh_services.style['padding'] = "5px"
        bt_refresh_services.style['margin'] = "5px"
        bt_refresh_services.set_on_click_listener(
            self.servicesbox.on_refresh_services)

        hbox_bt.append(bt_refresh_all)
        hbox_bt.append(bt_refresh_ip)
        hbox_bt.append(bt_refresh_services)
        hbox_bt.append(bt_refresh_scripts)

        return hbox_bt

    def on_refresh_all(self, widget):
        self.ipbox.on_refresh_ip(widget)
        self.scriptbox.on_refresh_scripts(widget)
        self.servicesbox.on_refresh_services(widget)
