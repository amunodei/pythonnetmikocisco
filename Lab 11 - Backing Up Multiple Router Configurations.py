from netmiko import ConnectHandler

USER = input('Enter the Username: ')
PASS = input('Enter the Password: ')

with open('devices.txt') as devfile:
    for IP in devfile:
        ABC = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': USER,
            'password': PASS
        }

        myssh = ConnectHandler(**ABC)

        shhost = myssh.send_command('show run | i hostname')
        hostname=shhost.split()
        print("Backing up " + hostname[1])

        backupfilename = hostname[1] + '-Backup.txt'

        shrun = myssh.send_command('show run')
        backupfile = open(backupfilename, "w")
        backupfile.write(shrun)
        backupfile.close()

input('Press ENTER to Continue')
