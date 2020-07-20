from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver("192.168.122.131", "prasad", "1234")

iosvl2.open()
iosvl2.load_merge_candidate(filename='commands')  # push the config.
print("Done Configuration")

print(iosvl2.compare_config())  # Compare the config.

iosvl2.close()
