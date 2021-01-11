-Tugas Akhir-

1. Download file onos ver. 1.13.2

   https://repo1.maven.org/maven2/org/onosproject/onos-releases/1.13.2/onos-1.13.2.zip
   
2. Melakukan instalasi controller onos pada directory /opt di linux
   
   sudo cp /opt/onos/init/onos.initd /etc/init.d/onos
   sudo cp /opt/onos/init/onos.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable onos
  
3. Menjalankan onos

   sudo systemctl start onos.service

4. Setelah itu, mininet dapat dijalankan dengan source code sesuai topologi yang dibutuhkan dan perlu disesuaikan IP address controller pada source code tersebut.

   Copy file python ke folder mininet,
   sudo python [nama file python]
