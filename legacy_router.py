#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Host,Node
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def init_network():
	net=Mininet(topo=None,build=False,ipBase='10.0.0.0/8')
	r1=net.addHost('r1',cls=Node,ip='0.0.0.0')
	r1.cmd('sysctl -w net.ipv4.ip_foward=1')
	
	h2=net.addHost('h2',cls=Host,ip='10.0.0.2',defaultRoute=None)
	h1=net.addHost('h1',cls=Host,ip='10.0.0.1',defaultRoute=None)
	net.addLink(h1,r1)
	net.addLink(h2,r1)
	net.build()
	CLI(net)
	net.stop()
if __name__=='__main__':
	setLogLevel('info')
	init_network()
