import subprocess
import nmap

CLIENT_PORT = 5031


# a method to scan all the clients for a given ip subnet
# note: run ifconfig for en0 to get the local ip
def scan_clients(range):

	nmap_output = subprocess.check_output(['nmap', '192.168.1.*', '-p', str(CLIENT_PORT)])
	last_seen_ip = None
	output = []

	for line in nmap_output.splitlines():
		if "Nmap scan report for " in line:
			words = line.split(" ")
			last_seen_ip = words[4]

		if str(CLIENT_PORT) + "/tcp" in line:
			state = line.split(" ")
			output.append({ 'ip': last_seen_ip, 'port_status': state[1]})
			last_seen_ip = ""


	return output

		# print line
	# nm = nmap.PortScanner()
	# # nm.scan('192.168.1.*', str(CLIENT_PORT))
	# #
	# # hosts_lists = [(x, nm[x]['tcp'][CLIENT_PORT]['state']) for x in nm.all_hosts()]
	#
	# # return states of the port
	# for host in hosts_lists:
	# 	# if port open, we want to store this so we can run our custom scan
	# 	print host


print  scan_clients('range')
