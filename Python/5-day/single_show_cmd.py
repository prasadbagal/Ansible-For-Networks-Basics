import getpass
import telnetlib

uname = 'prasad'
passwd = '1234'
HOST = "192.168.122.40"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(uname.encode('ascii') + b"\n")
if passwd:
  tn.read_until(b"Password: ")
  tn.write(passwd.encode('ascii') + b"\n")

tn.write(b"show ip inter br\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
