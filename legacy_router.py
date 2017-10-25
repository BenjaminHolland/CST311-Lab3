#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Host,Node
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def init_network():
	#no idea what ipBase does
	net=Mininet(topo=None,build=False,ipBase='10.0.0.0/25')
	r1=net.addHost('r1',cls=Node,ip='10.0.0.2/25')
	r1.cmd('sysctl -w net.ipv4.ip_foward=1')
	
	#set up host one to be device 2 on subnetwork 1 of network 10.0.0.0		
	h1=net.addHost('h1',cls=Host,ip='10.0.0.3/25',
 		defaultRoute='via 10.0.0.2')
	#set up host two to be device 2 on subnetwork 2 of network 10.0.0.0 	
	h2=net.addHost('h2',cls=Host,ip='10.0.0.130/25',
		 defaultRoute='via 10.0.0.129')
	
	
	#link in
	net.addLink(h1,r1,
		intfName1='h1eth0',params1={'ip':'10.0.0.3/25'},
		intfName2='r1eth0',params2={'ip':'10.0.0.2/25'})

	net.addLink(h2,r1,
		intfName1='h2eth0',params1={'ip':'10.0.0.130/25'},
		intfName2='r1eth1',params2={'ip':'10.0.0.129/25'})

	net.build()

	CLI(net)
	net.stop()
if __name__=='__main__':
	setLogLevel('info')
	init_network()
