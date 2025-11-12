from telnetlib import Telnet

print(70*'*')
print('Connection Information')
print(70*'*')
HOST = input('Specify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

print(70*'*')
print('User Information' )
print(70*'*')
num_users = input('How many users would you like to create: ')
num_users = int(num_users)

ab = Telnet(HOST)
ab.write(USER.encode('ascii') + b'\n')
ab.write(PASS.encode('ascii') + b'\n')
ab.write(b'config t\n')

while (num_users > 0):
    username = input('Specify the Username to be created : ')
    userpass = input('Specify the Password: ')
    user_cmd='Username ' + username + ' privilege 15 password ' + userpass + '\n'
    ab.write(user_cmd.encode('ascii'))
    num_users -= 1

ab.write(b'end\n')
ab.write(b'sh run | inc username\n')
ab.write(b'exit\n')
print (ab.read_all().decode('ascii'))
input('Press Enter to Continue')
