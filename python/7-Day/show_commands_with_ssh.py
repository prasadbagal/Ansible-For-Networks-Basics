from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.166',
    'username': 'prasad',
    'password': '1234'
}

net_connect = ConnectHandler(**my_device_info)
output = net_connect.send_command('show ip int brief')
print (output)
---------



from netmiko import ConnectHandler

my_device_info = { "device_type": "cisco_ios",
                   "ip": "192.168.122.131",
                   "username": "prasad",
                   "password": "1234" }


net_connect = ConnectHandler(**my_device_info)  #connecting via ssh

output = net_connect.send_command("show ip interf b")

print(output)

print(type(output))
