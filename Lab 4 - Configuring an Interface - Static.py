from telnetlib import Telnet

ab = Telnet('172.25.1.1')
ab.write(b'khawar\n')
ab.write(b'cisco\n')
ab.write(b'config t\n')
ab.write(b'Interface Loopback55\n')
ab.write(b'ip address 55.5.5.5 255.255.255.0\n')
ab.write(b'end\n')
ab.write(b'sh ip int brief\n')
ab.write(b'exit\n')
print (ab.read_all().decode('ascii'))
input('Press ENTER to Continue')
