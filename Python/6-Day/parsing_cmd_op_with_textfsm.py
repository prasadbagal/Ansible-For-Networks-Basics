from netmiko import Netmiko
import json
#from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.162',
    'username': 'prasad',
    'password': '1234'
}

net_connect = Netmiko(**my_device_info)
output = net_connect.send_command('show version', use_textfsm=True)
json_op = json.dumps(output, indent=3)
print (json_op)
