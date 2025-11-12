from netmiko import ConnectHandler

ABC = {
    'device_type': 'cisco_ios',
    'ip': '172.25.1.1',
    'username': 'khawar',
    'password': 'cisco'
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

print(hostname[1] + ' Backed up successfully')

myssh.disconnect()
input('Press ENTER to Continue')
