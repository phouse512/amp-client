# import subprocess
import nmap
# print subprocess.check_output(['arp', '-a'])


CLIENT_PORT = 5031


# a method to scan all the clients for a given ip subnet
# note: run ifconfig for en0 to get the local ip
def scan_clients(range):

	nm = nmap.PortScanner()
	nm.scan('10.159.210.*', str(CLIENT_PORT))

	hosts_lists = [(x, nm[x]['tcp'][CLIENT_PORT]['state']) for x in nm.all_hosts()]

	# return states of the port
	for host in hosts_lists:
		# if port open, we want to store this so we can run our custom scan
		print host


scan_clients('range')
