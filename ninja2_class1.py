#!/usr/bin/env
import jinja2

bgp_vars = {
    "peer1_ip":"10.255.255.2",
    "peer1_as": 20
    }
bgp_template = '''
    eature bgp
    router bgp 10
    address-family ipv4 unicast
    network 10.10.200.0/24
    network 10.10.201.0/24
    network 10.10.202.0/24
    neighbor {{peer1_ip}} remote-as {{peer1_as}}
    update-source loopback1
    ebgp-multihop 2
    address-family ipv4 unicast
'''

temp = jinja2.Template(bgp_template)
print(temp.render(bgp_vars))

