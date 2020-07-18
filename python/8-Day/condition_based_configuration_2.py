# check if status if "GigabitEthernet3/0" is down, if yes then change hostname of device to 'hostname NetworkSwitch'

from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.131',
    'username': 'prasad',
    'password': '1234'
}

net_connect = ConnectHandler(**my_device_info)
output = net_connect.send_command('show ip interf b', use_textfsm=True)
print(output, indent)


for i in output:
    if i["intf"] == 'GigabitEthernet3/0' and i['status'] == 'down':
        cmd_list = ['hostname NetworkSwitch']
        net_connect.send_config_set(cmd_list)
        print("done!!")
