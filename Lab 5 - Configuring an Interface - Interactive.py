from telnetlib import Telnet

print(70*'*')
print('Connection Information')
print(70*'*')

HOST = input('\nSpecify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

print(70*'*')
print('Interface Information')
print(70*'*')

Interface = input('\nWhat Interface would you like to configure : ')
Ipaddr = input('Specify the IP Address : ')
SMask = input('Specify the Subnet mask : ')

ab = Telnet(HOST)
ab.write(USER.encode('ascii') + b'\n')
ab.write(PASS.encode('ascii') + b'\n')

int_cmd = 'Interface ' + Interface + '\n'
ipaddr_cmd = 'IP Address ' + Ipaddr + ' ' + SMask + '\n'
ab.write(b'config t\n')
ab.write(int_cmd.encode('ascii'))
ab.write(ipaddr_cmd.encode('ascii'))
ab.write(b'end\n')
ab.write(b'sh ip int brief\n')
ab.write(b'exit\n')
print (ab.read_all().decode('ascii'))
input('Press Enter to Continue')
