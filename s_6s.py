#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink


def Network():
    net = Mininet(topo=None, build=False, ipBase='192.168.0.0/24', link=TCLink)
  
    info("*** Creating Network")
    print("")
    print("")

    info("*** Adding Controller")
    print("")
    print("")

    # add Controller
    c1 = net.addController(name='Controller1', controller=RemoteController, ip='10.0.2.4', port=6633)

    info("*** Adding hosts")
    print("")

    # Add hosts
    Host1 = net.addHost( 'h1', ip='192.168.0.1/24' )
    Host2 = net.addHost( 'h2', ip='192.168.0.2/24' )
    Host3 = net.addHost( 'h3', ip='192.168.0.3/24' )
    Host4 = net.addHost( 'h4', ip='192.168.0.4/24' )
    Host5 = net.addHost( 'h5', ip='192.168.0.5/24' )
    Host6 = net.addHost( 'h6', ip='192.168.0.6/24' )
    Host7 = net.addHost( 'h7', ip='192.168.0.7/24' )
    Host8 = net.addHost( 'h8', ip='192.168.0.8/24' )
    Host9 = net.addHost( 'h9', ip='192.168.0.9/24' )
    Host10 = net.addHost( 'h10', ip='192.168.0.10/24' )
    Host11 = net.addHost( 'h11', ip='192.168.0.11/24' )
    Host12 = net.addHost( 'h12', ip='192.168.0.12/24' )
    Host13 = net.addHost( 'h13', ip='192.168.0.13/24' )
    Host14 = net.addHost( 'h14', ip='192.168.0.14/24' )
    Host15 = net.addHost( 'h15', ip='192.168.0.15/24' )
    Host16 = net.addHost( 'h16', ip='192.168.0.16/24' )
    Host17 = net.addHost( 'h17', ip='192.168.0.17/24' )
    Host18 = net.addHost( 'h18', ip='192.168.0.18/24' )
  
    #switches
    Switch1 = net.addSwitch( 's1' )
    Switch2 = net.addSwitch( 's2' )
    Switch3 = net.addSwitch( 's3' )
    Switch4 = net.addSwitch( 's4' )
    Switch5 = net.addSwitch( 's5' )
    Switch6 = net.addSwitch( 's6' )

    # Add links
    net.addLink( Host1, Switch1 )
    net.addLink( Host2, Switch1 )
    net.addLink( Host3, Switch1 )
    net.addLink( Host4, Switch2 )
    net.addLink( Host5, Switch2 )
    net.addLink( Host6, Switch2 )
    net.addLink( Host7, Switch3 )
    net.addLink( Host8, Switch3 )
    net.addLink( Host9, Switch3 )
    net.addLink( Host10, Switch4 )
    net.addLink( Host11, Switch4 )
    net.addLink( Host12, Switch4 )
    net.addLink( Host13, Switch5 )
    net.addLink( Host14, Switch5 )
    net.addLink( Host15, Switch5 )
    net.addLink( Host16, Switch6 )
    net.addLink( Host17, Switch6 )
    net.addLink( Host18, Switch6 )
    
    net.addLink( Switch1, Switch2 )
    net.addLink( Switch2, Switch3 )
    net.addLink( Switch3, Switch4 )
    net.addLink( Switch4, Switch5 )
    net.addLink( Switch5, Switch6 )


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('s1').start([c1])
    net.get('s2').start([c1])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()
