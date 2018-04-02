import remi.gui as gui
import subprocess
import urllib.request


class IPBox:
    def build_ip_box(self):
        style_ip_title = {"font-weight": "bold", "padding-right": "4px"}
        lb_ip_title = gui.Label("External IP:", style=style_ip_title)

        self.lb_ip_addr = gui.Label("")
        self.lb_ip_addr.style['color'] = "purple"

        hbox_ip = gui.HBox()
        hbox_ip.style['align-items'] = "left"
        hbox_ip.append(lb_ip_title)
        hbox_ip.append(self.lb_ip_addr)

        vbox_ip_box = gui.VBox(width=300)
        vbox_ip_box.style['align-items'] = "left"
        vbox_ip_box.style['border'] = "2px solid gray"
        vbox_ip_box.style['padding'] = "10px"
        vbox_ip_box.style['margin'] = "10px"
        vbox_ip_box.append(hbox_ip)

        return vbox_ip_box

    def on_refresh_ip(self):
        self.refresh_ip()

    def refresh_ip(self):
        ip = self._get_external_ip_address()
        self.lb_ip_addr.set_text(ip)

    def _get_external_ip_address(self):
        return urllib.request.urlopen('https://ident.me').read().decode('utf8')
