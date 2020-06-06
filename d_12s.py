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

    info("*** Adding Controller 1 and Controller 2")
    print("")
    print("")

    # add Controller
    c1 = net.addController(name='Controller1', controller=RemoteController, ip='10.0.2.5', port=6633)

    c2 = net.addController(name='Controller2', controller=RemoteController, ip='10.0.2.6', port=6633)


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
    Host19 = net.addHost( 'h19' )
    Host20 = net.addHost( 'h20' )
    Host21 = net.addHost( 'h21' )
    Host22 = net.addHost( 'h22' )
    Host23 = net.addHost( 'h23' )
    Host24 = net.addHost( 'h24' )
    Host25 = net.addHost( 'h25' )
    Host26 = net.addHost( 'h26' )
    Host27 = net.addHost( 'h27' )
    Host28 = net.addHost( 'h28' )
    Host29 = net.addHost( 'h29' )
    Host30 = net.addHost( 'h30' )
    Host31 = net.addHost( 'h31' )
    Host32 = net.addHost( 'h32' )
    Host33 = net.addHost( 'h33' )
    Host34 = net.addHost( 'h34' )
    Host35 = net.addHost( 'h35' )
    Host36 = net.addHost( 'h36' )
  
    #switches
    Switch1 = net.addSwitch( 's1' )
    Switch2 = net.addSwitch( 's2' )
    Switch3 = net.addSwitch( 's3' )
    Switch4 = net.addSwitch( 's4' )
    Switch5 = net.addSwitch( 's5' )
    Switch6 = net.addSwitch( 's6' )
    Switch7 = net.addSwitch( 's7' )
    Switch8 = net.addSwitch( 's8' )
    Switch9 = net.addSwitch( 's9' )
    Switch10 = net.addSwitch( 's10' )
    Switch11 = net.addSwitch( 's11' )
    Switch12 = net.addSwitch( 's12' )

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
    net.addLink( Host19, Switch7 )
    net.addLink( Host20, Switch7 )
    net.addLink( Host21, Switch7 )
    net.addLink( Host22, Switch8 )
    net.addLink( Host23, Switch8 )
    net.addLink( Host24, Switch8 )
    net.addLink( Host25, Switch9 )    
    net.addLink( Host26, Switch9 )
    net.addLink( Host27, Switch9 )
    net.addLink( Host28, Switch10 )
    net.addLink( Host29, Switch10 )
    net.addLink( Host30, Switch10 )
    net.addLink( Host31, Switch11 )
    net.addLink( Host32, Switch11 )
    net.addLink( Host33, Switch11 )
    net.addLink( Host34, Switch12 )
    net.addLink( Host35, Switch12 )
    net.addLink( Host36, Switch12 )


    net.addLink( Switch1, Switch2 )
    net.addLink( Switch2, Switch3 )
    net.addLink( Switch3, Switch4 )
    net.addLink( Switch4, Switch5 )
    net.addLink( Switch5, Switch6 )
    net.addLink( Switch6, Switch7 )
    net.addLink( Switch7, Switch8 )
    net.addLink( Switch8, Switch9 )
    net.addLink( Switch9, Switch10 )
    net.addLink( Switch10, Switch11 )
    net.addLink( Switch11, Switch12 )


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('s1').start([c1])
    net.get('s2').start([c1])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])
    net.get('s7').start([c2])
    net.get('s8').start([c2])
    net.get('s9').start([c2])
    net.get('s10').start([c2])
    net.get('s11').start([c2])
    net.get('s12').start([c2])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()
