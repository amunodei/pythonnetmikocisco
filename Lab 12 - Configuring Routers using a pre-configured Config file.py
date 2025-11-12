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

        shhost = myssh.send_command('show run | i hostname')
        hostname=shhost.split()
        print("Configuring " + hostname[1])

        Configfilename = hostname[1] + '.txt'
        myssh.send_config_from_file(Configfilename)
        print(hostname[1] + ' Configured')
        myssh.disconnect()

input('Press ENTER To Continue')
