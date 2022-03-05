#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

nxos1 = {
    'host': "nxos1.lasthop.io",
    'username': "pyclass",
    'password': "88newclass",
    'device_type': "cisco_nxos"
    }

cisco3 = {
    'device_type':"cisco_ios",
    'host': "cisco3.lasthop.io",
    'username':"pyclass",
    'password':"88newclass"
    }
 

for device in [nxos1, cisco3]:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    
    with open("show_version.txt", 'w') as f:
        f.write(output)
    
    

