import remi.gui as gui
import subprocess
import urllib.request


from guicomponents.refresh_bar import RefreshBar
from Styles import IPBoxStyles


class IPBox:
    def __init__(self):
        self.refresh_bar = RefreshBar(self.on_refresh_ip)

    def build_ip_box(self):
        """Build the External IP Address box from remi components"""

        lb_title = gui.Label("External IP Address", style=IPBoxStyles["title"])

        self.lb_ip_addr = gui.Label("", style=IPBoxStyles["ipaddr"])

        self.hbox_refresh_bar = self.refresh_bar.build_refresh_bar()

        vbox_ip_box = gui.VBox(style=IPBoxStyles["ipbox_box"])
        vbox_ip_box.append(lb_title)
        vbox_ip_box.append(self.lb_ip_addr)
        vbox_ip_box.append(self.hbox_refresh_bar)

        return vbox_ip_box

    def on_refresh_ip(self):
        self.refresh_ip_box()

    def refresh_ip_box(self):
        """Refresh the ip address"""

        ip = self._get_external_ip_address()
        self.lb_ip_addr.set_text(ip)

        self.refresh_bar.update_refresh_time()

    def _get_external_ip_address(self):
        """Get the external ip address from a service"""

        try:
            return urllib.request.urlopen('https://ident.me', None, 5).read().decode('utf8')
        except:
            return "Unable to find server."
