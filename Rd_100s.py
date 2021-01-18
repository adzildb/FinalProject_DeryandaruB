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

    info("*** Creating Network")
    print("")
    print("")

    info("*** Adding Controller")
    print("")
    print("")

    # add Controller
    c1 = net.addController(name='Controller1', controller=RemoteController, ip='10.0.2.4', port=6633)
    c2 = net.addController(name='Controller2', controller=RemoteController, ip='10.0.2.5', port=6633)

    info("*** Adding hosts")
    print("")
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
    Host73 = net.addHost( 'h73' )
    Host74 = net.addHost( 'h74' )
    Host75 = net.addHost( 'h75' )
    Host76 = net.addHost( 'h76' )
    Host77 = net.addHost( 'h77' )
    Host78 = net.addHost( 'h78' )
    Host79 = net.addHost( 'h79' )
    Host80 = net.addHost( 'h80' )
    Host81 = net.addHost( 'h81' )
    Host82 = net.addHost( 'h82' )
    Host83 = net.addHost( 'h83' )
    Host84 = net.addHost( 'h84' )
    Host85 = net.addHost( 'h85' )
    Host86 = net.addHost( 'h86' )
    Host87 = net.addHost( 'h87' )
    Host88 = net.addHost( 'h88' )
    Host89 = net.addHost( 'h89' )
    Host90 = net.addHost( 'h90' )
    Host91 = net.addHost( 'h91' )
    Host92 = net.addHost( 'h92' )
    Host93 = net.addHost( 'h93' )
    Host94 = net.addHost( 'h94' )
    Host95 = net.addHost( 'h95' )
    Host96 = net.addHost( 'h96' )
    Host97 = net.addHost( 'h97' )
    Host98 = net.addHost( 'h98' )
    Host99 = net.addHost( 'h99' )
    Host100 = net.addHost( 'h100' )

    info("*** Adding Switches")
    print("")

    # Add Switches
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
    Switch25 = net.addSwitch( 's25' )
    Switch26 = net.addSwitch( 's26' )
    Switch27 = net.addSwitch( 's27' )
    Switch28 = net.addSwitch( 's28' )
    Switch29 = net.addSwitch( 's29' )
    Switch30 = net.addSwitch( 's30' )
    Switch31 = net.addSwitch( 's31' )
    Switch32 = net.addSwitch( 's32' )
    Switch33 = net.addSwitch( 's33' )
    Switch34 = net.addSwitch( 's34' )
    Switch35 = net.addSwitch( 's35' )
    Switch36 = net.addSwitch( 's36' )
    Switch37 = net.addSwitch( 's37' )
    Switch38 = net.addSwitch( 's38' )
    Switch39 = net.addSwitch( 's39' )
    Switch40 = net.addSwitch( 's40' )
    Switch41 = net.addSwitch( 's41' )
    Switch42 = net.addSwitch( 's42' )
    Switch43 = net.addSwitch( 's43' )
    Switch44 = net.addSwitch( 's44' )
    Switch45 = net.addSwitch( 's45' )
    Switch46 = net.addSwitch( 's46' )
    Switch47 = net.addSwitch( 's47' )
    Switch48 = net.addSwitch( 's48' )
    Switch49 = net.addSwitch( 's49' )
    Switch50 = net.addSwitch( 's50' )
    Switch51 = net.addSwitch( 's51' )
    Switch52 = net.addSwitch( 's52' )
    Switch53 = net.addSwitch( 's53' )
    Switch54 = net.addSwitch( 's54' )
    Switch55 = net.addSwitch( 's55' )
    Switch56 = net.addSwitch( 's56' )
    Switch57 = net.addSwitch( 's57' )
    Switch58 = net.addSwitch( 's58' )
    Switch59 = net.addSwitch( 's59' )
    Switch60 = net.addSwitch( 's60' )
    Switch61 = net.addSwitch( 's61' )
    Switch62 = net.addSwitch( 's62' )
    Switch63 = net.addSwitch( 's63' )
    Switch64 = net.addSwitch( 's64' )
    Switch65 = net.addSwitch( 's65' )
    Switch66 = net.addSwitch( 's66' )
    Switch67 = net.addSwitch( 's67' )
    Switch68 = net.addSwitch( 's68' )
    Switch69 = net.addSwitch( 's69' )
    Switch70 = net.addSwitch( 's70' )
    Switch71 = net.addSwitch( 's71' )
    Switch72 = net.addSwitch( 's72' )
    Switch73 = net.addSwitch( 's73' )
    Switch74 = net.addSwitch( 's74' )
    Switch75 = net.addSwitch( 's75' )
    Switch76 = net.addSwitch( 's76' )
    Switch77 = net.addSwitch( 's77' )
    Switch78 = net.addSwitch( 's78' )
    Switch79 = net.addSwitch( 's79' )
    Switch80 = net.addSwitch( 's80' )
    Switch81 = net.addSwitch( 's81' )
    Switch82 = net.addSwitch( 's82' )
    Switch83 = net.addSwitch( 's83' )
    Switch84 = net.addSwitch( 's84' )
    Switch85 = net.addSwitch( 's85' )
    Switch86 = net.addSwitch( 's86' )
    Switch87 = net.addSwitch( 's87' )
    Switch88 = net.addSwitch( 's88' )
    Switch89 = net.addSwitch( 's89' )
    Switch90 = net.addSwitch( 's90' )
    Switch91 = net.addSwitch( 's91' )
    Switch92 = net.addSwitch( 's92' )
    Switch93 = net.addSwitch( 's93' )
    Switch94 = net.addSwitch( 's94' )
    Switch95 = net.addSwitch( 's95' )
    Switch96 = net.addSwitch( 's96' )
    Switch97 = net.addSwitch( 's97' )
    Switch98 = net.addSwitch( 's98' )
    Switch99 = net.addSwitch( 's99' )
    Switch100 = net.addSwitch( 's100' )

    # Add links
    net.addLink( Host1, Switch1, bw = 1000 )
    net.addLink( Host2, Switch2, bw = 1000 )
    net.addLink( Host3, Switch3, bw = 1000 )
    net.addLink( Host4, Switch4, bw = 1000 )
    net.addLink( Host5, Switch5, bw = 1000 )
    net.addLink( Host6, Switch6, bw = 1000 )
    net.addLink( Host7, Switch7, bw = 1000 )
    net.addLink( Host8, Switch8, bw = 1000 )
    net.addLink( Host9, Switch9, bw = 1000 )
    net.addLink( Host10, Switch10, bw = 1000 )
    net.addLink( Host11, Switch11, bw = 1000 )
    net.addLink( Host12, Switch12, bw = 1000 )
    net.addLink( Host13, Switch13, bw = 1000 )
    net.addLink( Host14, Switch14, bw = 1000 )
    net.addLink( Host15, Switch15, bw = 1000 )
    net.addLink( Host16, Switch16, bw = 1000 )
    net.addLink( Host17, Switch17, bw = 1000 )
    net.addLink( Host18, Switch18, bw = 1000 )
    net.addLink( Host19, Switch19, bw = 1000 )
    net.addLink( Host20, Switch20, bw = 1000 )
    net.addLink( Host21, Switch21, bw = 1000 )
    net.addLink( Host22, Switch22, bw = 1000 )
    net.addLink( Host23, Switch23, bw = 1000 )
    net.addLink( Host24, Switch24, bw = 1000 )
    net.addLink( Host25, Switch25, bw = 1000 )    
    net.addLink( Host26, Switch26, bw = 1000 )
    net.addLink( Host27, Switch27, bw = 1000 )
    net.addLink( Host28, Switch28, bw = 1000 )
    net.addLink( Host29, Switch29, bw = 1000 )
    net.addLink( Host30, Switch30, bw = 1000 )
    net.addLink( Host31, Switch31, bw = 1000 )
    net.addLink( Host32, Switch32, bw = 1000 )
    net.addLink( Host33, Switch33, bw = 1000 )
    net.addLink( Host34, Switch34, bw = 1000 )
    net.addLink( Host35, Switch35, bw = 1000 )
    net.addLink( Host36, Switch36, bw = 1000 )
    net.addLink( Host37, Switch37, bw = 1000 )
    net.addLink( Host38, Switch38, bw = 1000 )
    net.addLink( Host39, Switch39, bw = 1000 )
    net.addLink( Host40, Switch40, bw = 1000 )
    net.addLink( Host41, Switch41, bw = 1000 )
    net.addLink( Host42, Switch42, bw = 1000 )
    net.addLink( Host43, Switch43, bw = 1000 )    
    net.addLink( Host44, Switch44, bw = 1000 )
    net.addLink( Host45, Switch45, bw = 1000 )
    net.addLink( Host46, Switch46, bw = 1000 )
    net.addLink( Host47, Switch47, bw = 1000 )
    net.addLink( Host48, Switch48, bw = 1000 )
    net.addLink( Host49, Switch49, bw = 1000 )
    net.addLink( Host50, Switch50, bw = 1000 )
    net.addLink( Host51, Switch51, bw = 1000 )
    net.addLink( Host52, Switch52, bw = 1000 )
    net.addLink( Host53, Switch53, bw = 1000 )
    net.addLink( Host54, Switch54, bw = 1000 )
    net.addLink( Host55, Switch55, bw = 1000 )
    net.addLink( Host56, Switch56, bw = 1000 )
    net.addLink( Host57, Switch57, bw = 1000 )
    net.addLink( Host58, Switch58, bw = 1000 )
    net.addLink( Host59, Switch59, bw = 1000 )
    net.addLink( Host60, Switch60, bw = 1000 )
    net.addLink( Host61, Switch61, bw = 1000 )    
    net.addLink( Host62, Switch62, bw = 1000 )
    net.addLink( Host63, Switch63, bw = 1000 )
    net.addLink( Host64, Switch64, bw = 1000 )
    net.addLink( Host65, Switch65, bw = 1000 )
    net.addLink( Host66, Switch66, bw = 1000 )
    net.addLink( Host67, Switch67, bw = 1000 )
    net.addLink( Host68, Switch68, bw = 1000 )
    net.addLink( Host69, Switch69, bw = 1000 )
    net.addLink( Host70, Switch70, bw = 1000 )
    net.addLink( Host71, Switch71, bw = 1000 )
    net.addLink( Host72, Switch72, bw = 1000 )
    net.addLink( Host73, Switch73, bw = 1000 )
    net.addLink( Host74, Switch74, bw = 1000 )
    net.addLink( Host75, Switch75, bw = 1000 )
    net.addLink( Host76, Switch76, bw = 1000 )
    net.addLink( Host77, Switch77, bw = 1000 )
    net.addLink( Host78, Switch78, bw = 1000 )
    net.addLink( Host79, Switch79, bw = 1000 )    
    net.addLink( Host80, Switch80, bw = 1000 )
    net.addLink( Host81, Switch81, bw = 1000 )
    net.addLink( Host82, Switch82, bw = 1000 )
    net.addLink( Host83, Switch83, bw = 1000 )
    net.addLink( Host84, Switch84, bw = 1000 )
    net.addLink( Host85, Switch85, bw = 1000 )
    net.addLink( Host86, Switch86, bw = 1000 )
    net.addLink( Host87, Switch87, bw = 1000 )
    net.addLink( Host88, Switch88, bw = 1000 )
    net.addLink( Host89, Switch89, bw = 1000 )
    net.addLink( Host90, Switch90, bw = 1000 )
    net.addLink( Host91, Switch91, bw = 1000 )
    net.addLink( Host92, Switch92, bw = 1000 )
    net.addLink( Host93, Switch93, bw = 1000 )
    net.addLink( Host94, Switch94, bw = 1000 )
    net.addLink( Host95, Switch95, bw = 1000 )
    net.addLink( Host96, Switch96, bw = 1000 )
    net.addLink( Host97, Switch97, bw = 1000 )    
    net.addLink( Host98, Switch99, bw = 1000 )
    net.addLink( Host99, Switch100, bw = 1000 )
    net.addLink( Host100, Switch100, bw = 1000 )


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
    net.addLink( Switch24, Switch25 )
    net.addLink( Switch25, Switch26 )
    net.addLink( Switch26, Switch27 )
    net.addLink( Switch27, Switch28 )
    net.addLink( Switch28, Switch29 )
    net.addLink( Switch29, Switch30 )
    net.addLink( Switch30, Switch31 )
    net.addLink( Switch31, Switch32 )
    net.addLink( Switch32, Switch33 )
    net.addLink( Switch33, Switch34 )
    net.addLink( Switch34, Switch35 )
    net.addLink( Switch35, Switch36 )
    net.addLink( Switch36, Switch37 )
    net.addLink( Switch37, Switch38 )
    net.addLink( Switch38, Switch39 )
    net.addLink( Switch39, Switch40 )
    net.addLink( Switch40, Switch41 )
    net.addLink( Switch41, Switch42 )
    net.addLink( Switch42, Switch43 )
    net.addLink( Switch43, Switch44 )
    net.addLink( Switch44, Switch45 )
    net.addLink( Switch45, Switch46 )
    net.addLink( Switch46, Switch47 )
    net.addLink( Switch47, Switch48 )
    net.addLink( Switch48, Switch49 )
    net.addLink( Switch49, Switch50 )
    net.addLink( Switch50, Switch51 )
    net.addLink( Switch51, Switch52 )
    net.addLink( Switch52, Switch53 )
    net.addLink( Switch53, Switch54 )
    net.addLink( Switch54, Switch55 )
    net.addLink( Switch55, Switch56 )
    net.addLink( Switch56, Switch57 )
    net.addLink( Switch57, Switch58 )
    net.addLink( Switch58, Switch59 )
    net.addLink( Switch59, Switch60 )
    net.addLink( Switch60, Switch61 )
    net.addLink( Switch61, Switch62 )
    net.addLink( Switch62, Switch63 )
    net.addLink( Switch63, Switch64 )
    net.addLink( Switch64, Switch65 )
    net.addLink( Switch65, Switch66 )
    net.addLink( Switch66, Switch67 )
    net.addLink( Switch67, Switch68 )
    net.addLink( Switch68, Switch69 )
    net.addLink( Switch69, Switch70 )
    net.addLink( Switch70, Switch71 )
    net.addLink( Switch71, Switch72 )
    net.addLink( Switch72, Switch73 )
    net.addLink( Switch73, Switch74 )
    net.addLink( Switch74, Switch75 )
    net.addLink( Switch75, Switch76 )
    net.addLink( Switch76, Switch77 )
    net.addLink( Switch77, Switch78 )
    net.addLink( Switch78, Switch79 )
    net.addLink( Switch79, Switch80 )
    net.addLink( Switch80, Switch81 )
    net.addLink( Switch81, Switch82 )
    net.addLink( Switch82, Switch83 )
    net.addLink( Switch83, Switch84 )
    net.addLink( Switch84, Switch85 )
    net.addLink( Switch85, Switch86 )
    net.addLink( Switch86, Switch87 )
    net.addLink( Switch87, Switch88 )
    net.addLink( Switch88, Switch89 )
    net.addLink( Switch89, Switch90 )
    net.addLink( Switch90, Switch91 )
    net.addLink( Switch91, Switch92 )
    net.addLink( Switch92, Switch93 )
    net.addLink( Switch93, Switch94 )
    net.addLink( Switch94, Switch95 )
    net.addLink( Switch95, Switch96 )
    net.addLink( Switch96, Switch97 )
    net.addLink( Switch97, Switch98 )
    net.addLink( Switch98, Switch99 )
    net.addLink( Switch99, Switch100 )

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
    net.get('s13').start([c1])
    net.get('s14').start([c1])
    net.get('s15').start([c1])
    net.get('s16').start([c1])
    net.get('s17').start([c1])
    net.get('s18').start([c1])
    net.get('s19').start([c1])
    net.get('s20').start([c1])
    net.get('s21').start([c1])
    net.get('s22').start([c1])
    net.get('s23').start([c1])
    net.get('s24').start([c1])
    net.get('s25').start([c1])
    net.get('s26').start([c1])
    net.get('s27').start([c1])
    net.get('s28').start([c1])
    net.get('s29').start([c1])
    net.get('s30').start([c1])
    net.get('s31').start([c1])
    net.get('s32').start([c1])
    net.get('s33').start([c1])
    net.get('s34').start([c1])
    net.get('s35').start([c1])
    net.get('s36').start([c1])
    net.get('s37').start([c1])
    net.get('s38').start([c1])
    net.get('s39').start([c1])
    net.get('s40').start([c1])
    net.get('s41').start([c1])
    net.get('s42').start([c1])
    net.get('s43').start([c1])
    net.get('s44').start([c1])
    net.get('s45').start([c1])
    net.get('s46').start([c1])
    net.get('s47').start([c1])
    net.get('s48').start([c1])
    net.get('s49').start([c1])
    net.get('s50').start([c1])
    net.get('s51').start([c2])
    net.get('s52').start([c2])
    net.get('s53').start([c2])
    net.get('s54').start([c2])
    net.get('s55').start([c2])
    net.get('s56').start([c2])
    net.get('s57').start([c2])
    net.get('s58').start([c2])
    net.get('s59').start([c2])
    net.get('s60').start([c2])
    net.get('s61').start([c2])
    net.get('s62').start([c2])
    net.get('s63').start([c2])
    net.get('s64').start([c2])
    net.get('s65').start([c2])
    net.get('s66').start([c2])
    net.get('s67').start([c2])
    net.get('s68').start([c2])
    net.get('s69').start([c2])
    net.get('s70').start([c2])
    net.get('s71').start([c2])
    net.get('s72').start([c2])
    net.get('s73').start([c2])
    net.get('s74').start([c2])
    net.get('s75').start([c2])
    net.get('s76').start([c2])
    net.get('s77').start([c2])
    net.get('s78').start([c2])
    net.get('s79').start([c2])
    net.get('s80').start([c2])
    net.get('s81').start([c2])
    net.get('s82').start([c2])
    net.get('s83').start([c2])
    net.get('s84').start([c2])
    net.get('s85').start([c2])
    net.get('s86').start([c2])
    net.get('s87').start([c2])
    net.get('s88').start([c2])
    net.get('s89').start([c2])
    net.get('s90').start([c2])
    net.get('s91').start([c2])
    net.get('s92').start([c2])
    net.get('s93').start([c2])
    net.get('s94').start([c2])
    net.get('s95').start([c2])
    net.get('s96').start([c2])
    net.get('s97').start([c2])
    net.get('s98').start([c2])
    net.get('s99').start([c2])
    net.get('s100').start([c2])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()

