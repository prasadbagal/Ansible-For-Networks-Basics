from netmiko import ConnectHandler

my_device_info1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.166',   # device1 IP
    'username': 'prasad',
    'password': '1234'
}

my_device_info2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.162',  # device2 IP
    'username': 'prasad',
    'password': '1234'
}

net_connect1 = ConnectHandler(**my_device_info1)
net_connect2 = ConnectHandler(**my_device_info2)

config_commands_1 = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0', 'int loop 1', 'ip address 2.2.2.2 255.255.255.0']
config_commands_2 = ['int loop 0', 'ip address 2.3.4.5 255.255.255.0', 'int loop 4', 'ip address 2.2.2.7 255.255.255.0']


output1 = net_connect1.send_config_set(config_commands_1)
output2 = net_connect2.send_config_set(config_commands_2)
print (output1)
print('-----------------------------------------------------------------------')
print(output2)
