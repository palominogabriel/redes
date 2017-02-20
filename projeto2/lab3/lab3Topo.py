#!/usr/bin/env python

"""
Laboratorio 3 - roteamento dinamico

12 hosts
6 switches(cada um com 2 hosts)

4 roteadores WAN


"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import lg, info, setLogLevel
from mininet.util import dumpNodeConnections, quietRun, moveIntf
from mininet.cli import CLI
from mininet.node import Switch, OVSKernelSwitch

from subprocess import Popen, PIPE, check_output
from time import sleep, time
from multiprocessing import Process
from argparse import ArgumentParser

import sys
import os
import termcolor as T
import time

setLogLevel('info')

def log(s, col="green"):
    print T.colored(s, col)


class Router(Switch):
    """Defines a new router that is inside a network namespace so that the
    individual routing entries don't collide.

    """
    ID = 0
    def __init__(self, name, **kwargs):
        kwargs['inNamespace'] = True
        Switch.__init__(self, name, **kwargs)
        Router.ID += 1
        self.switch_id = Router.ID

    @staticmethod
    def setup():
        return

    def start(self, controllers):
        pass

    def stop(self):
        self.deleteIntfs()

    def log(self, s, col="magenta"):
        print T.colored(s, col)


class Lab3Topo(Topo):
    """
    ADAPTADO DE BGP.PY
    """
    def __init__(self):
        # Add default members to class.
        super(Lab3Topo, self ).__init__()
        num_hosts_per_switches = 2
        num_switches_per_routers = 2
        num_routers = 3
        num_hosts = num_routers * num_hosts_per_switches * num_switches_per_routers

    #criam-se os roteadores, switches e hosts, nesta ordem

	routers = []
        for i in xrange(num_routers):
            router = self.addSwitch('R%d' % (i+1))
	    routers.append(router)
        switches = []
        for i in xrange(num_routers):
            router = 'R%d' % (i+1)
            for j in xrange(num_switches_per_routers):
                switchname = 's%d-%d' % (i+1, j+1)
                switch = self.addNode(switchname)
                switches.append(switch)
                self.addLink(router, switch)
                hosts = []
                for k in xrange(num_hosts_per_switches):
                    hostname = 'h%d-%d-%d' % (i+1, j+1, k+1)
                    host = self.addNode(hostname)
                    hosts.append(host)
                    self.addLink(switch, host)

        for i in xrange(num_routers-1):
            self.addLink('R%d' % (i+1), 'R%d' % (i+2))


        return


def getIP(hostname):
    if( "s" in hostname):
        AS, idx = hostname.replace('s', '').split('-')
    else:
        AS, idx, hid = hostname.replace('h', '').split('-')
    AS = int(AS)

    ip = '%s.0.%s.1/24' % (10+AS, idx)
    return ip


def getGateway(hostname):
    if ("s" in hostname):
        AS, idx = hostname.replace('s', '').split('-')
    else:
        AS, idx, hid = hostname.replace('h', '').split('-')
    AS = int(AS)

    gw = '%s.0.%s.254' % (10+AS, idx)
    return gw



def main():
    os.system("rm -f /tmp/R*.log /tmp/R*.pid logs/*")
    os.system("mn -c >/dev/null 2>&1")
    os.system("killall -9 zebra bgpd > /dev/null 2>&1")

    net = Mininet(topo=Lab3Topo(), switch=Router)
    net.start()
    for router in net.switches:
        router.cmd("sysctl -w net.ipv4.ip_forward=1")
        router.waitOutput()

    log("Waiting .900 seconds for sysctl changes to take effect...")
    sleep(.900)

    for router in net.switches:
        if router.name == 'R4' :
            continue
        router.cmd("/usr/lib/quagga/zebra -f conf/zebra-%s.conf -d -i /tmp/zebra-%s.pid > logs/%s-zebra-stdout 2>&1" % (router.name, router.name, router.name))
        router.waitOutput()
        router.cmd("/usr/lib/quagga/bgpd -f conf/bgpd-%s.conf -d -i /tmp/bgp-%s.pid > logs/%s-bgpd-stdout 2>&1" % (router.name, router.name, router.name), shell=True)
        router.waitOutput()
        log("Starting zebra and bgpd on %s" % router.name)

    for host in net.hosts:
        host.cmd("ifconfig %s-eth0 %s" % (host.name, getIP(host.name)))
        host.cmd("route add default gw %s" % (getGateway(host.name)))



    CLI(net)
    net.stop()
    os.system("killall -9 zebra bgpd")


if __name__ == "__main__":
    main()


