
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


-------------------------------------------------------------------

#check if Gi0/3 is in vlan200 if yes then configure desciption in Gi0/3 as "HelloIamNetworkEngineer"

for i in output:
    if i['vlan_id'] == '200':
        if "Gi0/3" in i["interfaces"]:
            cmd_list = ["int Gi0/3", "descri HelloIamNetworkEngineer"]
            net_connect.send_config_set(cmd_list )
            print("Done!!")
print("Good Bye!!!!")


-------------
export NET_TEXTFSM=/path/to/ntc-templates/templates/
