from netmiko import Netmiko
import json
#from netmiko import ConnectHandler

my_device_info = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.162',
    'username': 'prasad',
    'password': '1234'
}

#Step:1 backup
###############################################################################
net_connect = Netmiko(**my_device_info)
output = net_connect.send_command('show run')

with open("backup/Backup-"+my_device_info['ip'], 'w') as backup_file:
    backup_file.write(output)
    print("Backup successfull !!!")

###############################################################################
#Step:2
with open("configs/test_config_b", "r") as command_file:
    all_commands = command_file.read().split('\n')

net_connect = Netmiko(**my_device_info)
output2 = net_connect.send_config_set(all_commands)
print ("COnfiguration successfull!!")
################################################################################
#step:3
with open("reports/"+my_device_info['ip'], 'w') as report_file:
    report_file.write(output2)
    print("report  successfull !!!")
