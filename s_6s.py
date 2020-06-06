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
    Host1 = net.addHost( 'h1' )
    Host2 = net.addHost( 'h2' )
    Host3 = net.addHost( 'h3' )
    Host4 = net.addHost( 'h4' )
    Host5 = net.addHost( 'h5' )
    Host6 = net.addHost( 'h6' )
    Host7 = net.addHost( 'h7' )
    Host8 = net.addHost( 'h8' )
    Host9 = net.addHost( 'h9' )
    Host10 = net.addHost( 'h10' )
    Host11 = net.addHost( 'h11' )
    Host12 = net.addHost( 'h12' )
    Host13 = net.addHost( 'h13' )
    Host14 = net.addHost( 'h14' )
    Host15 = net.addHost( 'h15' )
    Host16 = net.addHost( 'h16' )
    Host17 = net.addHost( 'h17' )
    Host18 = net.addHost( 'h18' )
  
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
