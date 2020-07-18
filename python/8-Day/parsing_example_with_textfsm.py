#you need to have ntc_textfsm and env variable set for NET_TEXTFSM

from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.130',
    'username': 'prasad',
    'password': '1234'
}

net_connect = ConnectHandler(**my_device_info)
output = net_connect.send_command('show vlan', use_textfsm=True)
print(output)
