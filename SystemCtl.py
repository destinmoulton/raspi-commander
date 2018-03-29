import sys
import subprocess

from config import SUDO_PASSWORD


class SystemCtl:
    def is_active(self, service_name):
        """Return True if service is running"""
        cmd = ['systemctl', 'status', service_name]

        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf8')
        for line in output.split("\n"):
            if 'Active:' in line:
                if '(running)' in line:
                    return True
        return False

    def run(self, service_name, command):
        cmd = ['sudo', 'systemctl', command, service_name]
        subprocess.run(
            cmd, stdout=subprocess.PIPE)

        # print result.stdout.decode('utf8')
