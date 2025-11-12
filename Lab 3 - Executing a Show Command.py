from telnetlib import Telnet

cmd_exec=input('Enter the Command : ')
mytel=Telnet('172.25.1.1')
mytel.write(b'khawar\n')
mytel.write(b'cisco\n')
mytel.write(b'terminal length 0\n')
mytel.write(cmd_exec.encode('ascii') + b'\n')
mytel.write(b'exit\n')
print(mytel.read_all().decode('ascii'))
input('Thanks for using the program')
