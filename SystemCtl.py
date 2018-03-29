import sys
import subprocess


class SystemCtl:
    def is_active(self, service_name):
        """Return True if service is running"""
        cmd = ['systemctl', 'status', service_name]

        result = subprocess.check_output(cmd)
        output = result.decode('utf8')
        for line in output.split("\n"):
            if 'Active:' in line:
                if '(running)' in line:
                    return True
        return False

    def run(self, service_name, command):
        cmd = ['sudo', 'systemctl', command, service_name]
        subprocess.check_output(cmd)
