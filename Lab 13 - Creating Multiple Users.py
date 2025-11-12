from netmiko import ConnectHandler

HOST = input("Enter IP Address of the Device: ")
user = input("Enter your SSH username: ")
PASS = input("Enter your SSH Password: ")

ABC = {
    'device_type': 'cisco_ios',
    'host':   HOST,
    'username': user,
    'password': PASS
}
myssh = ConnectHandler(**ABC)

user_num = input('How many users need to be created: ')
user_num = int(user_num)

while user_num > 0:

    NEW_USER = input('Specify the Username to be create: ')
    NEW_PASS = input('Specify the Password for the User: ')
    USER_CMD = 'Username ' + NEW_USER + ' privileg 15 password  ' + NEW_PASS
    config_commands = [USER_CMD]
    myssh.send_config_set(config_commands)
    user_num -=1

print('---------------------------------\n')

shuser = myssh.send_command('show running-config | inc username')
print(shuser)
print('Users created successfully')

input('Press Enter to Continue')
