import remi.gui as gui
import subprocess
import urllib.request

from LastRefreshed import LastRefreshed
from Styles import IPBoxStyles


class IPBox:
    def build_ip_box(self):

        lb_title = gui.Label("External IP Address", style=IPBoxStyles["title"])

        self.lb_ip_addr = gui.Label("", style=IPBoxStyles["ipaddr"])

        self.lastrefreshed = LastRefreshed()
        self.hbox_last_refreshed = gui.VBox()

        vbox_ip_box = gui.VBox(style=IPBoxStyles["ipbox_box"])
        vbox_ip_box.append(lb_title)
        vbox_ip_box.append(self.lb_ip_addr)
        vbox_ip_box.append(self.hbox_last_refreshed)

        return vbox_ip_box

    def on_refresh_ip(self):
        self.refresh_ip()

    def refresh_ip(self):
        ip = self._get_external_ip_address()
        self.lb_ip_addr.set_text(ip)

        self.hbox_last_refreshed.empty()
        self.hbox_last_refreshed.append(
            self.lastrefreshed.get_last_refreshed())

    def _get_external_ip_address(self):
        try:
            return urllib.request.urlopen('https://ident.me', None, 5).read().decode('utf8')
        except:
            return "Unable to find server."
