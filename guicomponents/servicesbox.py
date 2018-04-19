import os
import remi.gui as gui
import subprocess

from config import SERVICES_TO_MONITOR

from guicomponents.refresh_bar import RefreshBar
from SystemCtl import SystemCtl
from Styles import ButtonStyles, ServicesBoxStyles


class ServicesBox:
    def __init__(self, stdoutbox):
        self.systemctl = SystemCtl(stdoutbox)
        self.refresh_bar = RefreshBar(self.handle_refresh_services)

    def build_services_box(self):
        """Build the services box from remi components"""

        lb_title = gui.Label("Services", style=ServicesBoxStyles["title"])

        self.vbox_services_table = gui.TableWidget(
            0, 3, use_title=False, style=ServicesBoxStyles["table"])

        vbox_services_section = gui.VBox(
            style=ServicesBoxStyles["container"])

        hbox_refresh_bar = self.refresh_bar.build_refresh_bar()

        vbox_services_section.append(lb_title)
        vbox_services_section.append(self.vbox_services_table)
        vbox_services_section.append(hbox_refresh_bar)

        return vbox_services_section

    def handle_refresh_services(self):
        """When the "Refresh" button is clicked"""

        self.refresh_service_table()

    def on_click_start_service(self, widget, service):
        """Start a service"""

        self.systemctl.run(service, "start")
        self.refresh_service_table()

    def on_click_stop_service(self, widget, service):
        """Stop a service"""

        self.systemctl.run(service, "stop")
        self.refresh_service_table()

    def on_click_restart_service(self, widget,  service):
        """Restart a service"""

        self.systemctl.run(service, "restart")
        self.refresh_service_table()

    def refresh_service_table(self):
        """Refresh the services"""

        service_statuses = self._get_services_status()
        num_rows = len(service_statuses)
        self.vbox_services_table.empty()
        self.vbox_services_table.set_row_count(num_rows)

        self.refresh_bar.update_refresh_time()

        for service_index, (service, status) in enumerate(service_statuses):
            bt_start = gui.Button(
                "Start", style=ButtonStyles["bt_green"])
            bt_start.set_on_click_listener(
                self.on_click_start_service, service)

            bt_stop = gui.Button(
                "Stop", style=ButtonStyles["bt_red"])
            bt_stop.set_on_click_listener(self.on_click_stop_service, service)

            bt_restart = gui.Button(
                "Restart", style=ButtonStyles["bt_orange"])
            bt_restart.set_on_click_listener(
                self.on_click_restart_service, service)

            bt_col = self.vbox_services_table.item_at(service_index, 0)
            bt_col.set_style(ServicesBoxStyles["table_bt_col"])
            bt_col.append(bt_start)
            bt_col.append(bt_stop)
            bt_col.append(bt_restart)

            status_text = "Off"
            status_style = ServicesBoxStyles["status_col_style_off"]
            if status:
                status_text = "On"
                status_style = ServicesBoxStyles["status_col_style_on"]

            lb_status = gui.Label(status_text, style=status_style)
            status_col = self.vbox_services_table.item_at(service_index, 1)
            status_col.append(lb_status)

            path_col = self.vbox_services_table.item_at(service_index, 2)
            path_col.set_style(ServicesBoxStyles["table_service_col"])
            path_col.set_text(service)

    def _get_services_status(self):
        service_statuses = []
        for service in SERVICES_TO_MONITOR:
            service_statuses.append(
                [service, self.systemctl.is_active(service)])

        return service_statuses
