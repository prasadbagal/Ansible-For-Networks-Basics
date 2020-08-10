import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.40', 'prasad', '1234')
iosvl2.open()

iosvl2.load_merge_candidate(filename='commands')

print(iosvl2.compare_config())

print("done merginf")

print("commiting the changes .........")

iosvl2.commit_config()

print("done commiting!!")

iosvl2.rollback()

print("done rollback")

iosvl2.close()
