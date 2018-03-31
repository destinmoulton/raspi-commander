import remi.gui as gui


class RefreshBox:
    def __init__(self, servicesbox, ipbox, scriptbox):
        self.servicesbox = servicesbox
        self.ipbox = ipbox
        self.scriptbox = scriptbox

    def build_refresh_box(self):
        hbox_bt = gui.HBox()

        base_button_style = {"padding": "5px",
                             "margin": "5px",
                             "border-radius": "3px"}

        refresh_all_style = base_button_style.copy()
        refresh_all_style["background-color"] = "green"
        bt_refresh_all = gui.Button(
            "Refresh All", style=refresh_all_style)

        bt_refresh_all.set_on_click_listener(self.on_refresh_all)

        bt_refresh_ip = gui.Button(
            'Refresh IP Address', style=base_button_style)
        bt_refresh_ip.set_on_click_listener(self.ipbox.on_refresh_ip)

        bt_refresh_scripts = gui.Button(
            'Refresh Script List', style=base_button_style)
        bt_refresh_scripts.set_on_click_listener(
            self.scriptbox.on_refresh_scripts)

        bt_refresh_services = gui.Button(
            'Refresh Services', style=base_button_style)
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
