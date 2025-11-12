from netmiko import ConnectHandler

ABC = {
    'device_type': 'cisco_ios',
    'host':   '172.25.1.1',
    'username': 'khawar',
    'password': 'cisco'
}
myssh = ConnectHandler(**ABC)

config_commands = [ 'banner motd #Authorized KBITS.LIVE Users Only#',
                    'no ip domain-lookup',
                    'line con 0',
                    ' logg sync', 'no exec-timeout'
                    ]
myssh.send_config_set(config_commands)
output1 = myssh.send_command('sh runn | inc banner')
output2 = myssh.send_command('show run | sec line')
output3 = myssh.send_command('show ip eigrp neighbor')
print(output1)
print(output2)
print(output3)
input('Thanks for using the program')

