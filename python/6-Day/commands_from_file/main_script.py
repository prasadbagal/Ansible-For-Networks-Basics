##############################################################################
# Script for executing the commands on remote NW devices,
# commands should have kept in file 'commmands' in the same dir
##############################################################################

import getpass
import telnetlib

with open("commands", "r") as file_content:
    commands = file_content.read()

commands_list = commands.split("\n")

HOST = "192.168.122.161"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

for command in commands_list:
    tn.write(b"%b\n" % command.encode('ascii'))

print(tn.read_all().decode('ascii'))
