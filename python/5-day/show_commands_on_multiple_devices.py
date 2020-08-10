##############################################################################
# Script for running show command 'show ip interf b' on multiple network devices,
# username, Password hardcoded into script. HOSTS is the list of hosts
##############################################################################
import getpass
import telnetlib

uname = 'prasad'
passwd = '1234'

HOST = ["192.168.122.161", "192.168.122.162", "192.168.122.163"]
for host in HOST:

    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(uname.encode('ascii') + b"\n")
    if passwd:
        tn.read_until(b"Password: ")
        tn.write(passwd.encode('ascii') + b"\n")

    tn.write(b"show ip inter br\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
