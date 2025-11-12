from netmiko import ConnectHandler

with open('devices.txt') as devfile:
    for IP in devfile:
        ABC = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'khawar',
            'password': 'cisco'
            }
        myssh = ConnectHandler(**ABC)

        print('Connecting to ' + IP + '-' * 79)
        output = myssh.send_command('sh ip int brief')
        print(output)
        print('-' * 79)

myssh.disconnect()
input('Press ENTER to Continue')
