#!/usr/bin/python3.9
########################## Import ##########################

import ipaddress
import os

########################## COLOR ##########################

# color for a beautiful script !

clear = '\033[0m'
red = '\033[91m'
blue = '\033[94m'
backRed = '\033[41m'
backBlue = '\033[44m'
blink = '\033[5m'

########################## FUNCTION ########################## 
############### NEW HOST ###############
def newHostname(newHostname):
	with open('/etc/hosts', 'r') as file: # open the file /etc/hosts to read data
		data = file.readlines() # insert a list of lines into data
	data[1] = '127.0.1.1	' + newHostname # the Hostname is on the 2th line, so this replace by the new hostname
	with open('temp.txt', 'w') as file: #create a temporary file because '/etc/hosts' is protected
		file.writelines( data )
	os.system('sudo mv temp.txt /etc/hosts') # use sudo command to overwrite protected files
	with open('/etc/hostname', 'r') as file: # repeat with other files
		data = file.readlines()
	data[0] = newHostname
	with open('temp.txt', 'w') as file:
		file.writelines( data )
	os.system('sudo mv temp.txt /etc/hostname')
	
############### Interface ###############
def newInterface():
	fileLine = 11 # set the first lines we write on the files
	os.system('sudo cp /Configuratron-DEB11/interfaces.txt /etc/network/interfaces')
	print(blink+backBlue+"configure an new interface? [N/Y]"+clear) 
	var = input()
	while (var == 'y' or var == 'Y' or var == 'YES' or var == 'yes'):
		print("")
		os.system('nmcli device status')
		print("")
		print(backRed+ "interface name?"+clear)
		interfaceName = input()
		print(blink+backBlue+"this interface is parameter in DHCP? [N/Y]"+clear) 
		var = input()
		if (var == 'y' or var == 'Y' or var == 'YES' or var == 'yes'):
			
			with open('/etc/network/interfaces', 'r') as file: # open the file interfaces.txt to read data
				data = file.readlines() # insert a list of lines into data
			data[fileLine] = 'auto ' + interfaceName + '\n'# whrite data on the file
			fileLine = fileLine + 1
			data[fileLine] = 'allow-hotplug ' + interfaceName + '\n'
			fileLine = fileLine + 1
			data[fileLine] = 'iface ' + interfaceName + ' inet dhcp\n'
			fileLine = fileLine + 2
			
			with open('temp.txt', 'w') as file: #create a temporary file because /etc/network/interfaces is protected
				file.writelines( data )
			os.system('sudo mv temp.txt /etc/network/interfaces') # use sudo command to overwrite protected files

		else:
			print(backRed+"server IP?"+clear)
			ipAddress = input()
			if ipaddress.ip_address(ipAddress): # test if ip address is good
				print(blue+"IP Valide"+clear)
		
			print(backRed+"Netmask?"+clear)
			netmask = input()
			if ipaddress.ip_address(netmask): # test if Netmask is good
				print(blue+"IP Valide"+clear)
			print(blink+backBlue+"this interface has Gateway ? [N/Y]"+clear) 
			var = input()
			if (var == 'y' or var == 'Y' or var == 'YES' or var == 'yes'):
				print(backRed+"Gateway?"+clear)
				gateway = input()
				if ipaddress.ip_address(gateway): # test if gateway is good
					print(blue+"IP Valide"+clear)
				with open('/etc/network/interfaces', 'r') as file: # open the file interfaces.txt to read data
					data = file.readlines() # insert a list of lines into data
				data[fileLine] = 'auto ' + interfaceName + '\n'# whrite data on the file
				fileLine = fileLine + 1
				data[fileLine] = 'iface ' + interfaceName + ' inet static\n'
				fileLine = fileLine + 1
				data[fileLine] = 'address ' + ipAddress + '\n'
				fileLine = fileLine + 1
				data[fileLine] = 'netmask ' + netmask + '\n'
				fileLine = fileLine + 1
				data[fileLine] = 'gateway ' + gateway + '\n'
				fileLine = fileLine + 2
				with open('temp.txt', 'w') as file: #create a temporary file because /etc/network/interfaces is protected
					file.writelines( data )
				os.system('sudo mv temp.txt /etc/network/interfaces') # use sudo command to overwrite protected files
			else:
				with open('/etc/network/interfaces', 'r') as file: # open the file interfaces.txt to read data
					data = file.readlines() # insert a list of lines into data
				data[fileLine] = 'auto ' + interfaceName + '\n'# whrite data on the file
				fileLine = fileLine + 1
				data[fileLine] = 'iface ' + interfaceName + ' inet static\n'
				fileLine = fileLine + 1
				data[fileLine] = 'address ' + ipAddress + '\n'
				fileLine = fileLine + 1
				data[fileLine] = 'netmask ' + netmask + '\n'
				fileLine = fileLine + 2
				with open('temp.txt', 'w') as file: #create a temporary file because /etc/network/interfaces is protected
					file.writelines( data )
				os.system('sudo mv temp.txt /etc/network/interfaces') # use sudo command to overwrite protected files
		print(blink+backBlue+"configure an new interface? [N/Y]"+clear) 
		var = input()
############### DHCP ###############
def setDhcp():
	os.system('sudo apt-get install isc-dhcp-server -y')
	print(backRed+"DNS server Ip 1 for DHCP??"+clear)
	dnsServer1 = input()
	if ipaddress.ip_address(dnsServer1):
		print(blue+"IP Valide"+clear)
	print(backRed+"DNS server Ip 2 for DHCP??"+clear)
	dnsServer2 = input()
	if ipaddress.ip_address(dnsServer2):
		print(blue+"IP Valide"+clear)
	print(backRed+"Subnet for DHCP??"+clear)
	subnet = input()
	if ipaddress.ip_address(subnet):
		print(blue+"IP Valide"+clear)
	print(backRed+"Netmask for DHCP??"+clear)
	netmask = input()
	if ipaddress.ip_address(netmask):
		print(blue+"IP Valide"+clear)
	print(backRed+"Lower range for DHCP??"+clear)
	lowRange = input()
	if ipaddress.ip_address(lowRange):
		print(blue+"IP Valide"+clear)
	print(backRed+"Upper range for DHCP??"+clear)
	upRange = input()
	if ipaddress.ip_address(upRange):
		print(blue+"IP Valide"+clear)
	print(backRed+"options routers for DHCP??"+clear)
	routers = input()
	if ipaddress.ip_address(routers):
		print(blue+"IP Valide"+clear)
	with open('/Configuratron-DEB11/dhcp.txt', 'r') as file: # open the file interfaces.txt to read data
		data = file.readlines() # insert a list of lines into data
	data[7] = 'option domain-name-servers ' + dnsServer1 + ', ' + dnsServer2 + ';\n'
	data[9] = 'subnet ' + subnet + ' netmask ' + netmask + ' {\n'
	data[10] = 'range ' + lowRange + ' ' + upRange + ';\n'
	data[11] = 'option routers ' + routers + ';\n'
	data[12] = '}\n'
	with open('temp.txt', 'w') as file: #create a temporary file because /etc/network/interfaces is protected
		file.writelines( data )
	os.system('sudo mv temp.txt /etc/dhcp/dhcpd.conf') # use sudo command to overwrite protected files
	
############### DNS ###############
def setDns():
	os.system('sudo apt-get install bind9 -y')	
	os.system('sudo mv namedConfOptions.txt /etc/bind/named.conf.options') #copy named conf options for the listen-on {"any"}
	print(backRed+"Zone Name?"+clear)
	zoneName = input()
	with open('/Configuratron-DEB11/namedConfLocal.txt', 'r') as file:
		data = file.readlines()
	data[10] = 'zone "' + zoneName + '" {\n'
	data[11] = 'type master;\n'
	data[12] = 'file "etc/bind/db.'+ zoneName + '"; \n'
	data[13] = '};\n'
	with open('temp.txt', 'w') as file:
		file.writelines( data )
	os.system('sudo mv temp.txt /etc/bind/named.conf.local')
	print(backRed+"Serveur ip?"+clear)
	serverIp = input()
	with open('/Configuratron-DEB11/db.txt', 'r') as file:
		data = file.readlines()
	data[4] = '@	IN	SOA	'+ zoneName +'. root.'+ zoneName +'. (\n' 
	data[11] = '@	IN	NS	'+ zoneName +'.\n'
	data[13] = '@	IN	A	'+ serverIp + '\n'
	data[15] = 'ns	IN	A	'+ serverIp + '\n'
	data[16] = 'www	IN	A	'+ serverIp + '\n'
	data[18] = 'mail	IN	A	'+ serverIp + '\n'
	with open('temp.txt', 'w') as file:
		file.writelines( data )
	os.system('sudo mv temp.txt /etc/bind/db.' + zoneName)
	
	
########################## Main Script ##########################

print(backRed + "Welcome on configuratron DEB11" + clear)
print(blue + "hostname?" + clear)
hostname = input()
newHostname(hostname)
print(backBlue + "hostname will be changed after reboot" + clear)
print("")
newInterface()
setDhcp()
setDns()
print(blink+blue+"Do you want to reboot? [N/Y]"+clear) 
var = input()
if (var == 'y' or var == 'Y' or var == 'YES' or var == 'yes'):
	os.system('systemctl reboot')
print(blink + blue +"Thanks for use my script !! bye"+clear)
