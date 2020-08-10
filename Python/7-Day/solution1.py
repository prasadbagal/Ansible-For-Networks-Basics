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
output = net_connect.send_command('show ip interface bri', use_textfsm=True)
print(type(output))
#json_op = dict(json.dumps(output, indent=3))
#print(type(json_op))
for i in output:
   if i['intf'] == 'GigabitEthernet3/1' and i['status'] == 'down':
       p = net_connect.send_config_set(['int GigabitEthernet3/1', 'descrip I am not active', 'no shut', 'exit', 'do wr'])
       print(p)
   elif i['intf'] == 'GigabitEthernet3/1' and i['status'] == 'up':
       p = net_connect.send_config_set(['int GigabitEthernet3/1', 'descrip I am active'])
       print(p)
