import sys
import subprocess


class SystemCtl:
    """Interface for the raspbian systemctl command for service management"""

    def __init__(self, stdoutbox):
        self.stdoutbox = stdoutbox

    def is_active(self, service_name):
        """Return True if service is running"""

        cmd = ['systemctl', 'status', service_name + ".service"]

        try:
            output = subprocess.check_output(cmd, universal_newlines=True)
            self.stdoutbox.append(output)
            for line in output.split("\n"):
                if 'Active:' in line:
                    if '(running)' in line:
                        return True
            return False
        except subprocess.CalledProcessError:
            return False

    def run(self, service_name, command):
        """Run a systemctl command on a service"""

        cmd = ['sudo', 'systemctl', command, service_name]
        output = subprocess.check_output(cmd, universal_newlines=True)
        self.stdoutbox.append(output)
