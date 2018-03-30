import os
import remi.gui as gui
import subprocess

from config import SERVICES_TO_MONITOR

from SystemCtl import SystemCtl


class ServicesBox:
    def __init__(self):
        self.systemctl = SystemCtl()

    def build_services_box(self):
        bt_refresh = gui.Button('Refresh Services')
        bt_refresh.style['padding'] = "5px"
        bt_refresh.set_on_click_listener(self.on_refresh_services)

        hbox_services_menu = gui.HBox()
        hbox_services_menu.style['padding'] = '5px'
        hbox_services_menu.append(bt_refresh)

        lb_lastrun_title = gui.Label("Last Script:")
        lb_lastrun_title.style['font-weight'] = "bold"
        self.lb_lastrun_script = gui.Label("")

        self.vbox_services_table = gui.TableWidget(0, 3, use_title=False)

        vbox_services_section = gui.VBox(width=300)
        vbox_services_section.style['align-items'] = "left"
        vbox_services_section.style['border'] = "2px solid gray"
        vbox_services_section.style['padding'] = "10px"
        vbox_services_section.style['margin'] = "10px"

        vbox_services_section.append(hbox_services_menu)
        vbox_services_section.append(self.vbox_services_table)

        return vbox_services_section

    def on_refresh_services(self, widget):
        '''When the "Refresh Script List" button is clicked
        '''
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

        for service_index, (service, status) in enumerate(service_statuses):
            bt_start = gui.Button("Start")
            bt_start.style['background-color'] = "green"
            bt_start.style['padding'] = "4px"
            bt_start.set_on_click_listener(
                self.on_click_start_service, service)

            bt_stop = gui.Button("Stop")
            bt_stop.style['background-color'] = "red"
            bt_stop.style['padding'] = "4px"
            bt_stop.set_on_click_listener(self.on_click_stop_service, service)

            bt_restart = gui.Button("Restart")
            bt_restart.style['background-color'] = "orange"
            bt_restart.style['padding'] = "4px"
            bt_restart.set_on_click_listener(
                self.on_click_restart_service, service)

            bt_col = self.vbox_services_table.item_at(service_index, 0)
            bt_col.append(bt_start)
            bt_col.append(bt_stop)
            bt_col.append(bt_restart)

            status_text = "Off"
            status_color = "red"
            if status:
                status_text = "On"
                status_color = "green"

            lb_status = gui.Label(status_text)
            lb_status.style['color'] = status_color
            lb_status.style['padding'] = "4px"
            status_col = self.vbox_services_table.item_at(service_index, 1)
            status_col.append(lb_status)

            path_col = self.vbox_services_table.item_at(service_index, 2)
            path_col.style['padding'] = "4px"
            path_col.set_text(service)

    def _get_services_status(self):
        service_statuses = []
        for service in SERVICES_TO_MONITOR:
            service_statuses.append(
                [service, self.systemctl.is_active(service)])

        return service_statuses
