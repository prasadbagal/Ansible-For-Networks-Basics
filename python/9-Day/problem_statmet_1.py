# Problem statment:- 1
# Push config from file and print the diffs
# check the diffs
# prompt for Y/N for rollback
# If yes rollback the changes if no commit the changes.

from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver("192.168.122.131", "prasad", "1234"

iosvl2.open()
iosvl2.load_merge_candidate(filename='commands')
print("Done Configuration")

print(iosvl2.compare_config())
decide = input("Want ot commit? Y/N")
if decide.lower() == "y":
    print("Commiing the changes ........")
    iosvl2.commit_config()
    print("Done Commiting !!!")


elif decide.lower() == "n":
    print("Rolling Back the changes ........")
    iosvl2.rollback()
    print("Done rollback !!!")

else:
    print("Wrong option selected. Please try again")

iosvl2.close()
