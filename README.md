# digitalocean-openvpn-server

Installing on a DigitalOcean droplet, this project uses Ansible to configure and harden an OpenVPN server and create the corresponding OpenVPN client configuration.

## Getting Started

```
git clone https://github.com/rootviper/openvpn-server.git /path/to/install

```

### Creating a droplet

This process will automatically update the hosts.yml file and set a variable "status" to "created."  This is significant, as the setup playbook will run on droplets with status "created" but not for status "destroyed."  A droplet is given status "destroyed" after one runs the destroy playbook.

Change to the installation directory
```
cd /path/to/install
```

Copy the example hosts file and modify it, minimally replacing the following values:

"oauth_token": 64-character DigitalOcean OAuth token

"ssh_keys": numeric DigitalOcean SSH key identifier (this may be removed entirely)

"ansible_ssh_private_key_file": Fully-qualified path to the private key file to be used by Ansible

```
cp hosts.yml.example hosts.yml
vim hosts.yml
```

Run the create.yml playbook, optionally using the digital_ocean_create.sh script

```
$ ./digital_ocean_create.sh

PLAY [digital_ocean_api] *********************************************************************************************

TASK [digital-ocean-create : Create a new droplet using the DigitalOcean API] ****************************************
changed: [localhost]

TASK [digital-ocean-create : Create the backup directory if it does not exist] ***************************************
changed: [localhost]

TASK [digital-ocean-create : Create backup of hosts file] ************************************************************
changed: [localhost]

TASK [digital-ocean-create : Add the new host to the hosts file] *****************************************************
changed: [localhost]

TASK [digital-ocean-create : debug] **********************************************************************************
ok: [localhost] => {
    "msg": "ID is xxxxxxxx, IP is w.x.y.z"
}

PLAY RECAP ***********************************************************************************************************
localhost                  : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

./digital_ocean_create.sh completed in 28 seconds
```

### Configuring an existing droplet

Run the setup.yml playbook, optionally using the digital_ocean_setup.sh script.  The playbook will prompt for a CA private key passphrase and a server private key passphrase with which to encrypt the keys on the server.

```
$ ./digital_ocean_setup.sh
Create a CA private key passphrase:
Create a server private key passphrase:
...
```

### Creating client certificates to use with the server

Run the client.yml playbook, optionally using the digital_ocean_client_config.sh script.  This process can be run an indefinite number of times to use on various devices, e.g. laptops, phone, tablets.

```
$ ./digital_ocean_client_config.sh
Enter the CA private key passphrase:
Create a client private key passphrase:
...
```

###  Destroying a single droplet

Run the destroy.yml playbook, optionally using the digital_ocean_destroy.sh script.  The playbook will prompt for the DigitalOcean droplet ID, which can be obtained from the hosts.yml file, in which this value is automatically populated when the create.yml playbook is run.

```
$ ./digital_ocean_destroy.sh 
Enter the droplet ID to destroy: xxxxxxxxx

```

## Running the tests

No tests have yet been written for this project

## License

This project is licensed under the GNU General Public License, Version 3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

[ansible-role-repo-epel](https://github.com/geerlingguy/ansible-role-repo-epel)

