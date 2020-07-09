from netmiko import ConnectHandler

s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.162',
    'username': 'prasad',
    'password': '1234'
}

s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.166',
    'username': 'prasad',
    'password': '1234'
}


s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.163',
    'username': 'prasad',
    'password': '1234'
}

device_list = [s1, s2, s3]
config_file_list = ['device1_config', 'device2_config', 'device3_config']

for device,config_file  in zip(device_list,config_file_list):
    with open(config_file) as filea:
        lines = filea.read().splitlines()
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)
    print('-----------------------------------------------------------------------------------------------------------------')
