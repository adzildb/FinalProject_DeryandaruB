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
    Host37 = net.addHost( 'h37' )
    Host38 = net.addHost( 'h38' )
    Host39 = net.addHost( 'h39' )
    Host40 = net.addHost( 'h40' )
    Host41 = net.addHost( 'h41' )
    Host42 = net.addHost( 'h42' )
    Host43 = net.addHost( 'h43' )
    Host44 = net.addHost( 'h44' )
    Host45 = net.addHost( 'h45' )
    Host46 = net.addHost( 'h46' )
    Host47 = net.addHost( 'h47' )
    Host48 = net.addHost( 'h48' )
    Host49 = net.addHost( 'h49' )
    Host50 = net.addHost( 'h50' )
    Host51 = net.addHost( 'h51' )
    Host52 = net.addHost( 'h52' )
    Host53 = net.addHost( 'h53' )
    Host54 = net.addHost( 'h54' )
    Host55 = net.addHost( 'h55' )
    Host56 = net.addHost( 'h56' )
    Host57 = net.addHost( 'h57' )
    Host58 = net.addHost( 'h58' )
    Host59 = net.addHost( 'h59' )
    Host60 = net.addHost( 'h60' )
    Host61 = net.addHost( 'h61' )
    Host62 = net.addHost( 'h62' )
    Host63 = net.addHost( 'h63' )
    Host64 = net.addHost( 'h64' )
    Host65 = net.addHost( 'h65' )
    Host66 = net.addHost( 'h66' )
    Host67 = net.addHost( 'h67' )
    Host68 = net.addHost( 'h68' )
    Host69 = net.addHost( 'h69' )
    Host70 = net.addHost( 'h70' )
    Host71 = net.addHost( 'h71' )
    Host72 = net.addHost( 'h72' )

  
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
    Switch13 = net.addSwitch( 's13' )
    Switch14 = net.addSwitch( 's14' )
    Switch15 = net.addSwitch( 's15' )
    Switch16 = net.addSwitch( 's16' )
    Switch17 = net.addSwitch( 's17' )
    Switch18 = net.addSwitch( 's18' )
    Switch19 = net.addSwitch( 's19' )
    Switch20 = net.addSwitch( 's20' )
    Switch21 = net.addSwitch( 's21' )
    Switch22 = net.addSwitch( 's22' )
    Switch23 = net.addSwitch( 's23' )
    Switch24 = net.addSwitch( 's24' )


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
    net.addLink( Host37, Switch13 )
    net.addLink( Host38, Switch13 )
    net.addLink( Host39, Switch13 )
    net.addLink( Host40, Switch14 )
    net.addLink( Host41, Switch14 )
    net.addLink( Host42, Switch14 )
    net.addLink( Host43, Switch15 )    
    net.addLink( Host44, Switch15 )
    net.addLink( Host45, Switch15 )
    net.addLink( Host46, Switch16 )
    net.addLink( Host47, Switch16 )
    net.addLink( Host48, Switch16 )
    net.addLink( Host49, Switch17 )
    net.addLink( Host50, Switch17 )
    net.addLink( Host51, Switch17 )
    net.addLink( Host52, Switch18 )
    net.addLink( Host53, Switch18 )
    net.addLink( Host54, Switch18 )
    net.addLink( Host55, Switch19 )
    net.addLink( Host56, Switch19 )
    net.addLink( Host57, Switch19 )
    net.addLink( Host58, Switch20 )
    net.addLink( Host59, Switch20 )
    net.addLink( Host60, Switch20 )
    net.addLink( Host61, Switch21 )    
    net.addLink( Host62, Switch21 )
    net.addLink( Host63, Switch21 )
    net.addLink( Host64, Switch22 )
    net.addLink( Host65, Switch22 )
    net.addLink( Host66, Switch22 )
    net.addLink( Host67, Switch23 )
    net.addLink( Host68, Switch23 )
    net.addLink( Host69, Switch23 )
    net.addLink( Host70, Switch24 )
    net.addLink( Host71, Switch24 )
    net.addLink( Host72, Switch24 )

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
    net.addLink( Switch12, Switch13 )
    net.addLink( Switch13, Switch14 )
    net.addLink( Switch14, Switch15 )
    net.addLink( Switch15, Switch16 )
    net.addLink( Switch16, Switch17 )
    net.addLink( Switch17, Switch18 )
    net.addLink( Switch18, Switch19 )
    net.addLink( Switch19, Switch20 )
    net.addLink( Switch20, Switch21 )
    net.addLink( Switch21, Switch22 )
    net.addLink( Switch22, Switch23 )
    net.addLink( Switch23, Switch24 )


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('s1').start([c1])
    net.get('s2').start([c1])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])
    net.get('s7').start([c1])
    net.get('s8').start([c1])
    net.get('s9').start([c1])
    net.get('s10').start([c1])
    net.get('s11').start([c1])
    net.get('s12').start([c1])
    net.get('s13').start([c2])
    net.get('s14').start([c2])
    net.get('s15').start([c2])
    net.get('s16').start([c2])
    net.get('s17').start([c2])
    net.get('s18').start([c2])
    net.get('s19').start([c2])
    net.get('s20').start([c2])
    net.get('s21').start([c2])
    net.get('s22').start([c2])
    net.get('s23').start([c2])
    net.get('s24').start([c2])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()
