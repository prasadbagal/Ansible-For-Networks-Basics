from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.166',
    'username': 'prasad',
    'password': '1234'
}

net_connect = ConnectHandler(**my_device_info)
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)
---------------
