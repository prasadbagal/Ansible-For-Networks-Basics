# Example of Networking Inventory with Ansible

One of the many use cases for Ansible and the networking modules is to grab information in real time from the network. In this example I will generate a file report using the template module from facts I have gathered with the ios_facts module.

## Requirements

you should have ios devices stated in inventory

```
[ios]
192.168.122.172
192.168.122.170
192.168.122.171
192.168.122.174
[ios:vars]
ansible_network_os='ios'
```

## Usage

```
ansible-playbook -i inventory main.yml -u <user> -k 
```

Note:- -k is for password prompt