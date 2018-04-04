### Raspi Commander

Raspi Commander is a tool to monitor services, external ip address, and to run and execute scripts through a simple web interface. Raspi Commander uses [remi](https://github.com/dddomodossola/remi) to create the web application interface.

### remi

[dddomodossola/remi: Python REMote Interface library](https://github.com/dddomodossola/remi)

`sudo pip3 install git+https://github.com/dddomodossola/remi.git`

### scripts

Scripts can be stored as either `.sh` bash scripts or as `.json` files with the following format:

```
{
    "name": "Test ls",
    "cmds": [["ls", "/path/to/ls"]]
}
```

Note: The "cmds" need to be List of Lists `[[]]`
