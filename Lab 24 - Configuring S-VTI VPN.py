from netmiko import ConnectHandler

router_num = input("How many routers would you like to configure: ")
router_num = int(router_num)

while router_num > 0:

    HOST = input("Enter IP Address of Device to be Configured: ")
    user = input("Enter your SSH username: ")
    PASS = input("Enter your Password: ")

    ABC = {
        'device_type': 'cisco_ios',
        'host':   HOST,
        'username': user,
        'password': PASS
    }

    z=0
    inter_t = 'Tunnel'
    MYSSH = ConnectHandler(**ABC)
    SIIB = MYSSH.send_command('show ip int brief')
    log_file = open('TEMP.txt', "w")
    log_file.write(SIIB)
    log_file.write("\n")
    log_file.close()
    with open('TEMP.txt') as Tunnelfile:
        for line in Tunnelfile:
            if inter_t in line:
                x = line.split()
                y = x[0]
                z= y[6:]

    z = int(z)
    z += 1
    int_t = str(z)

    peer = input('Type the IP Address of remote peer:')
    print('\nPhase I Parameters\n')
    P1_hash = input('Specify the Phase I Hash - [MD5 | SHA]: ')
    P1_encryption = input('Specify the Phase I Encryption - [DES | 3DES] :')
    P1_group = input('Specify the Phase I DH Group: [1 | 2 | 5] : ')
    psk = input('Specify the Pre-shared-Key : ')
    print('\nPhase II Parameters\n')
    P2_hash = input('Specify the Phase II Hash - [MD5 | SHA]: ')
    P2_encryption = input('Specify the Phase II Encryption - [DES | 3DES] :')
    print('\nTunnel Information\n')
    int_o = input('Specify the Source Interface: ')
    t_network =  input('Specify the Tunnel IP Address: ')
    print('\nRouting Information\n')
    eigrp_as =  input('Specify EIGRP AS: ')
    s_network =  input('Specify the Network to Advertise: ')

    config_file = open('svti.txt', "w")
    config_file.write('crypto isakmp policy 10')
    config_file.write("\n")
    config_file.write(' authentication pre-share ')
    config_file.write("\n")
    config_file.write('hash ' + P1_hash)
    config_file.write("\n")
    config_file.write(' encryption ' + P1_encryption)
    config_file.write("\n")
    config_file.write(' group ' + P1_group)
    config_file.write("\n")
    config_file.write('!\ncrypto isakmp key ' + psk + ' address ' + peer + '\n')
    config_file.write('!\ncrypto ipsec transform-set TSET esp-' + P2_hash + '-hmac esp-' +P2_encryption + '\n')
    config_file.write('!\ncrypto ipsec profile IPROF\n')
    config_file.write(' set transform-set TSET\n')
    config_file.write('!\nInterface Tunnel ' + int_t + '\n')
    config_file.write(' Tunnel destination ' +  peer + '\n')
    config_file.write(' Tunnel Source ' +  int_o + '\n')
    config_file.write(' ip address ' +  t_network + ' 255.255.255.0\n')
    config_file.write(' Tunnel mode ipsec ipv4\n')
    config_file.write(' Tunnel protection ipsec profile IPROF\n')
    config_file.write('!\nrouter eigrp ' +  eigrp_as + '\n')
    config_file.write(' network ' +  s_network + '\n')
    config_file.write(' network ' +  t_network + ' 0.0.0.0\n')
    config_file.close()

    cmdfile = 'svti.txt'
    output=MYSSH.send_config_from_file(cmdfile)
    print(output)
    print('IPSec Configured')
    MYSSH.disconnect()
    router_num -=1
