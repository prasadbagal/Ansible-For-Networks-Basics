import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.130', 'prasad', '1234')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=4))

print("--------------------------------------------------------------")

ios_output = iosvl2.get_interfaces()
print(json.dumps(ios_output, indent=4))

print("--------------------------------------------------------------")

ios_output = iosvl2.get_interfaces_ip()
print(json.dumps(ios_output, indent=4))

print("--------------------------------------------------------------")

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, indent=4))

print("--------------------------------------------------------------")

ios_output = iosvl2.get_vlans()
print(json.dumps(ios_output, indent=4))

iosvl2.close()
