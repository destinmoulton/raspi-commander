import json
import os
import remi.gui as gui
import subprocess
from pprint import pprint

from config import SCRIPTS_PATH


class ScriptBox:

    def __init__(self, stdoutbox):
        self.stdoutbox = stdoutbox

    def build_script_box(self):

        lb_lastrun_title = gui.Label("Last Script:")
        lb_lastrun_title.style['font-weight'] = "bold"
        self.lb_lastrun_script = gui.Label("")

        hbox_lastrun = gui.HBox(width=500)
        hbox_lastrun.style['padding-left'] = "10px"
        hbox_lastrun.style['border-bottom'] = "2px solid black"
        hbox_lastrun.style['text-align'] = "left"
        hbox_lastrun.append(lb_lastrun_title)
        hbox_lastrun.append(self.lb_lastrun_script)

        self.vbox_scripts_table = gui.TableWidget(0, 2, use_title=False)

        vbox_script_section = gui.VBox(width=600)
        vbox_script_section.style['align-items'] = "left"
        vbox_script_section.style['border'] = "2px solid gray"
        vbox_script_section.style['padding'] = "10px"
        vbox_script_section.style['margin'] = "10px"

        vbox_script_section.append(hbox_lastrun)
        vbox_script_section.append(self.vbox_scripts_table)

        return vbox_script_section

    def on_refresh_scripts(self, widget):
        """When the "Refresh Script List" button is clicked"""
        self.refresh_scripts_table()

    def on_click_run(self, widget, script):
        """When a script in the table is clicked"""

        if script["type"] == "json":
            # Run a list of commands, ie. ['ls', '/path']
            for cmd in script["cmds"]:
                self._run_cmd(cmd)
        elif script["type"] == "bash":
            # Run a bash file
            cmd = ["/bin/bash", script["path"]]
            self._run_cmd(cmd)

        # Update the label
        self.lb_lastrun_script.set_text(script["name"])

    def _run_cmd(self, cmd):
        """Run a command"""
        output = subprocess.check_output(cmd, universal_newlines=True)
        self.stdoutbox.append(output)

    def refresh_scripts_table(self):
        """Refresh the scripts table"""

        script_paths = self._get_script_paths()
        scripts = self._parse_scripts(script_paths)

        num_rows = len(scripts)
        self.vbox_scripts_table.empty()
        self.vbox_scripts_table.set_row_count(num_rows)

        for script_index, script in enumerate(scripts):
            bt_run = gui.Button("Run")
            bt_run.style['background-color'] = "green"
            bt_run.style['padding'] = "4px"
            bt_run.set_on_click_listener(self.on_click_run, script)

            bt_col = self.vbox_scripts_table.item_at(script_index, 0)
            bt_col.append(bt_run)

            path_col = self.vbox_scripts_table.item_at(script_index, 1)
            path_col.style['padding'] = "4px"
            path_col.set_text(script['name'])

    def _parse_scripts(self, paths):
        """Parse the script paths"""
        scripts = []
        for path in paths:
            filename, ext = os.path.splitext(path)

            if ext == ".json":
                decoded = self._decode_json_script(path)
                decoded["type"] = "json"
                scripts.append(decoded)
            elif ext == ".sh":
                script = {
                    "type": "bash",
                    "name": os.path.basename(path),
                    "path": path
                }
                scripts.append(script)
        return scripts

    def _decode_json_script(self, path):
        f = open(path, mode="r")
        contents = f.read()
        f.close()
        return json.loads(contents)

    def _get_script_paths(self):
        scripts = []
        for subdir, dirs, files in os.walk(SCRIPTS_PATH):
            for file in files:
                scripts.append(os.path.join(subdir, file))

        return scripts
