#!/usr/bin/env python3
from datetime import datetime
import sys
import yaml


def add_droplet_to_hosts_file(hosts_file, ipaddr, droplet_id):
    now = datetime.now()
    current_time = now.strftime("%Y%m%d-%H%M%S")

    with open(hosts_file, 'rb') as hosts_file_fh:
        code = yaml.load(hosts_file_fh, Loader=yaml.FullLoader)

    code['all']['children']['digital_ocean']['hosts'][ipaddr] = dict()
    code['all']['children']['digital_ocean']['hosts'][ipaddr]['id'] = int(droplet_id)
    code['all']['children']['digital_ocean']['hosts'][ipaddr]['ansible_host'] = ipaddr
    code['all']['children']['digital_ocean']['hosts'][ipaddr]['status'] = 'active'
    code['all']['children']['digital_ocean']['hosts'][ipaddr]['creation_time'] = current_time

    for key in code['all']['children']['digital_ocean']['vars']['creation_defaults']:
        code['all']['children']['digital_ocean']['hosts'][ipaddr][key] = \
            code['all']['children']['digital_ocean']['vars']['creation_defaults'][key]

    with open(hosts_file, 'w+') as hosts_file_fh:
        yaml.dump(code, hosts_file_fh)

add_droplet_to_hosts_file(sys.argv[1], sys.argv[2], sys.argv[3])

