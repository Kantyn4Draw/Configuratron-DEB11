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
	os.system('sudo cp interfaces.txt /etc/network/interfaces')
	print(blink+backBlue+"configure an new interface? [N/Y]"+clear) 
	var = input()
	while (var == 'y' or var == 'Y' or var == 'YES' or var == 'yes'):
		print("")
		os.system('nmcli device status')
		print("")
		print(backRed+ "interface name?"+clear)
		interfaceName = input()
		print(backRed+"server IP?"+clear)
		ipAddress = input()
		if ipaddress.ip_address(ipAddress): # test if ip address is good
			print(blue+"Ip OK"+clear)
		
		print(backRed+"Netmask?"+clear)
		netmask = input()
		if ipaddress.ip_address(netmask): # test if Netmask is good
			print(blue+"Netmask OK"+clear)
		print(backRed+"Gateway?"+clear)
		gateway = input()
		if ipaddress.ip_address(gateway): # test if gateway is good
			print(backRed+"gateway OK"+clear)
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
	
		print(fileLine)
		print(blink+backBlue+"configure an new interface? [N/Y]"+clear) 
		var = input()
############### DHCP ###############
def setDhcp():
	os.system('sudo apt-get install isc-dhcp-server -y')
	print(backRed+"domain Name?"+clear)
	domainName = input()
	print(backRed+"DNS server Ip 1 ??"+clear)
	dnsServer1 = input()
	print(backRed+"DNS server Ip 2 ??"+clear)
	dnsServer2 = input()
	print(backRed+"Subnet ??"+clear)
	subnet = input()
	print(backRed+"Netmask ??"+clear)
	netmask = input()
	print(backRed+"Lower range ??"+clear)
	lowRange = input()
	print(backRed+"Upper range ??"+clear)
	upRange = input()
	print(backRed+"options routers ??"+clear)
	routers = input()
	with open('dhcp.txt', 'r') as file: # open the file interfaces.txt to read data
		data = file.readlines() # insert a list of lines into data
	data[6] = 'option domain-name "' + domainName + '";\n'
	data[7] = 'option domain-name-servers ' + dnsServer1 + ', ' + dnsServer2 + ';\n'
	data[9] = 'subnet ' + subnet + ' netmask ' + netmask + ' {\n'
	data[10] = 'range ' + lowRange + ' ' + upRange + ';\n'
	data[11] = 'options routers ' + routers + ';\n'
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
	with open('namedConfLocal.txt', 'r') as file:
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
	with open('db.txt', 'r') as file:
		data = file.readlines()
	data[4] = '@	IN	SOA	'+ zoneName +'. root.'+ zoneName +'. (\n' 
	data[11] = '@	IN	NS	'+ zoneName +'.\n'
	data[13] = '@	IN	A	'+ serverIp + '\n'
	data[15] = 'ns	IN	A	'+ serverIp + '\n'
	data[16] = 'www	IN	A	'+ serverIp + '\n'
	data[17] = 'us	IN	A	'+ serverIp + '\n'
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
print(blink + blue +"Thanks for use my script !! bye"+clear)



