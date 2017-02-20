#!/usr/bin/env python

"""
Laboratorio 2

10 hosts
5 switches(cada um com 2 hosts)

2 roteadores


        r  ---------------------r
    |   \       \      *      |  \
 s      s       s      *    s     s
h h    h h     h h     *   h h   h h
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class Lab2Topo( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )


        # Hosts da topologia
        h1 = self.addHost('h1', ip="192.168.1.100/24",defaultRoute="via 192.168.1.1")
        h2 = self.addHost('h2', ip="192.168.1.101/24",defaultRoute="via 192.168.1.1")

        h3 = self.addHost('h3', ip="192.168.2.100/24",defaultRoute="via 192.168.2.1")
        h4 = self.addHost('h4', ip="192.168.2.101/24",defaultRoute="via 192.168.2.1")

        h5 = self.addHost('h5', ip="192.168.3.100/24",defaultRoute="via 192.168.3.1")
        h6 = self.addHost('h6', ip="192.168.3.101/24",defaultRoute="via 192.168.3.1")


        h7 = self.addHost('h7', ip="192.168.8.100/24",defaultRoute="via 192.168.8.1")
        h8 = self.addHost('h8', ip="192.168.8.101/24",defaultRoute="via 192.168.8.1")

        h9 = self.addHost('h9', ip="192.168.9.100/24",defaultRoute="via 192.168.9.1")
        h10 = self.addHost('h10', ip="192.168.9.101/24",defaultRoute="via 192.168.9.1")


        # Switches
        switchLan1 = self.addSwitch('s1')
        switchLan2 = self.addSwitch('s2')
        switchLan3 = self.addSwitch('s3')
        switchLan8 = self.addSwitch('s8')
        switchLan9 = self.addSwitch('s9')


        # Add links
        self.addLink( h1, switchLan1 )
        self.addLink( h2, switchLan1 )

        self.addLink( h3, switchLan2 )
        self.addLink( h4, switchLan2 )

        self.addLink( h5, switchLan3 )
        self.addLink( h6, switchLan3 )


        self.addLink(h7, switchLan8)
        self.addLink(h8, switchLan8)

        self.addLink(h9, switchLan9)
        self.addLink(h10, switchLan9)


        #Routers
        defaultIP = '198.168.0.240/30'  # IP address for r0-eth1
        routerSede = self.addNode('r0', cls=LinuxRouter, ip=defaultIP)

        self.addLink(switchLan1, routerSede, intfName2='r0-eth1', params2={'ip': '192.168.1.1/24'})
        self.addLink(switchLan2, routerSede, intfName2='r0-eth2', params2={'ip': '192.168.2.1/24'})
        self.addLink(switchLan3, routerSede, intfName2='r0-eth3', params2={'ip': '192.168.3.1/24'})


        defaultIP2 = '198.168.0.241/30'  # IP address for r1-eth1
        routerFilial = self.addNode('r1', cls=LinuxRouter, ip=defaultIP2)

        self.addLink(switchLan8, routerFilial, intfName2='r1-eth1', params2={'ip': '192.168.8.1/24'})
        self.addLink(switchLan9, routerFilial, intfName2='r1-eth2', params2={'ip': '192.168.9.1/24'})


        #Router ----- Router
        self.addLink(routerSede,routerFilial)




def createTopo():
    topo = Lab2Topo()
    net = Mininet( topo = topo )
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createTopo()
