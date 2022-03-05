#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass


nxos1 = {
    'host': "nxos1.lasthop.io",
    'username': "pyclass",
    'password': "88newclass",
    'device_type': "cisco_nxos"
    }
    

nxos2 = {
    'host': "nxos2.lasthop.io",
    'username': "pyclass",
    'password': "88newclass",
    'device_type': "cisco_nxos"
    }


for device in [nxos1, nxos2]:
    net_connect = Netmiko(**device)
    output_prompt = net_connect.find_prompt()
    print(output_prompt)

