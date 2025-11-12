from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        ROUTER = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'khawar',
            'password': 'cisco'
        }

        myssh = ConnectHandler(**ROUTER)
        hostname = myssh.send_command('show run | i host')
        x = hostname.split()
        device = x[1]
        print('************* Configuring ' + device + ' *************')
        routerid=input('Specify the LDP Router-ID Interface [Loopback0]: ')
        config_commands = ['mpls ldp router-id ' + routerid]
        output = myssh.send_config_set(config_commands)
        print(output)                    
        SIIB = myssh.send_command('show ip int brief')
        log_file = open('TEMP.txt', "w")
        log_file.write(SIIB)
        log_file.write("\n")
        log_file.close()
        file_a = open('TEMP.txt', "r")
        lines = file_a.readlines()

        del lines[0]

        int_file = open('TEMP.txt', "w+")

        for line in lines:
            int_file.write(line)

        int_file.close()

        with open('TEMP.txt') as FILE:
            for LINE in FILE:
                x = LINE.split()
                if (x[1] == 'IP-Address') or (x[1] == 'unassigned'):
                    pass
                elif ('thernet' in x[0]):
                    config_commands = ['Interface ' + x[0],
                                       'mpls ip']
                    output = myssh.send_config_set(config_commands)
                    print(output)
        print(80*'-')
