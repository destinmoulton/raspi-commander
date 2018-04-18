### Raspi Commander

Raspi Commander is a tool to monitor services, external ip address, and to run and execute scripts through a simple web interface. Raspi Commander uses [remi](https://github.com/dddomodossola/remi) to create the web application interface.

### remi

[dddomodossola/remi: Python REMote Interface library](https://github.com/dddomodossola/remi)

`sudo pip3 install git+https://github.com/dddomodossola/remi.git`

#### Configuring Raspi Commander

Configure the options in config.py:

```python
IP = "127.0.0.1" # IP Address of the raspberry pi

SCRIPTS_PATH = "/path/to/scripts"

# The services you want to monitor
SERVICES_TO_MONITOR = [
    'samba',
    'ssh'
]
```

#### Starting the Server

`python3 main.py`

#### Scripts

Place your scripts in the folder configured in `SCRIPTS_PATH` in `config.py`.

You can run two different types of scripts.

*   Bash Scripts
*   JSON files that contain a `python list` of commands to run

The format of a JSON file is:

```
{
    "name": "A test JSON script to run 'ls'.",
    "cmds": [["ls", "-alt"]]
}
```

#### Permissions and SUDO

I setup my "pi" user to have all sudo priveleges. I am not worried about security and prefer the convenience.

The other way would be to grant automatic `sudo` priveleges for only the commands that you want to run remotely.
