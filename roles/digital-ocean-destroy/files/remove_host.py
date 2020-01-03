#!/usr/bin/env python3
import sys
import yaml


def remove_droplet_from_hosts_file(hosts_file, droplet_id):
    with open(hosts_file, 'rb') as hosts_file_fh:
        code = yaml.load(hosts_file_fh, Loader=yaml.FullLoader)

    for key in code['all']['children']['digital_ocean']['hosts']:
        if code['all']['children']['digital_ocean']['hosts'][key]['id'] == int(droplet_id):
            code['all']['children']['digital_ocean']['hosts'][key]['status'] = 'destroyed'

    with open(hosts_file, 'w+') as outfile:
        yaml.dump(code, outfile)

remove_droplet_from_hosts_file(sys.argv[1], sys.argv[2])

