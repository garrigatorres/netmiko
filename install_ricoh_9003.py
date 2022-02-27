from netmiko import ConnectHandler
from getpass import getpass

servidorRemot = {
    'device_type': 'linux',
    'host': '10.21.0.80',
    'username': 'root',
    'password': 'perprotegir'
}

net_connect = ConnectHandler(**servidorRemot)

command = "systemctl stop cups-browsed"
output = net_connect.send_command(command)

command = "systemctl disable cups-browsed"
output = net_connect.send_command(command)

command = "lpadmin -p Ricoh-9003 -E -v ipp://192.168.0.250/ipp/print -m everywhere"
output = net_connect.send_command(command)

command = "chmod 777 /etc/cups/ppd/Ricoh-9003.ppd"
output = net_connect.send_command(command)

command = "wget http://192.168.0.2/IC10/Ricoh-9003.ppd"
output = net_connect.send_command(command)

command = "mv Ricoh-9003.ppd /etc/cups/ppd/"
output = net_connect.send_command(command)

net_connect.disconnect()
