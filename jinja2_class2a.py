#!/usr/bin/env
import jinja2

bgp_vars = {
    "local_as": 10,
    "peer1_ip":"10.255.255.2",
    "peer1_as": 20,
    "advertises_route1": "10.10.200.0/24",
    "advertises_route2": "10.10.201.0/24",
    "advertises_route3": "10.10.202.0/24",
    }

template_file = 'nxos_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

temp = jinja2.Template(bgp_template)
print(temp.render(bgp_vars))

