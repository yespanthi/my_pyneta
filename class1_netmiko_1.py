#!usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

password = getpass()

nx_os_device = {
    'host':" nxos1.lasthop.io",
    'username': "pyclass",
    'password': password,
    'device_type' : "cisco_nxos"
    }
net_connect = Netmiko(**nx_os_device)
output = net_connect.find_prompt()
print(output)

