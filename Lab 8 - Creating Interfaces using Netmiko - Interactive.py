from netmiko import ConnectHandler

print(70*'*')
print('Connection Information')
print(70*'*')

HOST = input("Enter IP Address of the Device: ")
USER = input("Enter your SSH username: ")
PASS = input("Enter your SSH Password: ")

print(70*'*')
print('Interface Information')
print(70*'*')

Interface = input('\nWhat Interface would you like to configure : ')
Ipaddr = input('Specify the IP Address : ')
SMask = input('Specify the Subnet mask : ')

Interface_cmd = 'Interface ' + Interface
Ipaddr_cmd = 'ip address ' + Ipaddr + ' ' + SMask

ABC = {
    'device_type': 'cisco_ios',
    'host':   HOST,
    'username': USER,
    'password': PASS
}
myssh = ConnectHandler(**ABC)

config_commands = [ Interface_cmd , Ipaddr_cmd, 'no shut']

myssh.send_config_set(config_commands)
output = myssh.send_command('show ip int brief')
print(output)
input("Press ENTER to finish")
