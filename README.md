# DIY Smart Plug

### Make a cheap discrete remote controlled two-channel power outlet.

* Remote controlled
* Control from anywhere
* Control both sockets independently
* Easily setup schedules 
* Cheap (I only spent $9)

<img src="https://i.imgur.com/srThsBd.jpg" height="300"> &nbsp; 
<img src="https://media.giphy.com/media/29HVwXORm5pwl53DaS/giphy.gif" height="300"/>

## Overview:
---------

This project provides software and hardware installation instructions for controlling a power outlet remotely via wifi. The software is designed to run on a [Raspberry Pi](www.raspberrypi.org), which is an inexpensive ARM-based computer.

It only cost me $9 to make while commercially available smart plugs can cost up to $50, and most of them are only control one outlet.
* [Insteon Dual On/Off Outlet](https://www.smarthome.com/insteon-2663-222-on-off-outlet-white.html) - $50
* [iHome Smart Plug](https://www.ihomeaudio.com/iSP6X/) - $36
* [WeMo Mini Smart Plug](https://www.belkin.com/us/p/P-F7C063/) - $30
* [iDevices Switch](https://store.idevicesinc.com/idevices-switch/) - $30
* [TP-Link Smart Plug](https://www.tp-link.com/us/products/details/cat-5516_HS105.html) - $27
* [Amazon Smart Plug](http://a.co/d/1IqPLIq) - $25
* [Aukey Wi-Fi Smart Plug (2-pack)](https://www.aukey.com/products/wi-fi-smart-plug-2-pack-sh-pa1) - $25
* [D-Link Wi-Fi Smart Plug](http://us.dlink.com/products/connected-home/wi-fi-smart-plug/) - $18

## Requirements:
-----

**Hardware**

Most hardware components can probably be found lying around.
* [Raspberry Pi Zero W](https://www.microcenter.com/product/486575/raspberry-pi-zero-w) - $5
* [2 Channel Relay Module](https://www.microcenter.com/product/486581/2-channel-5v-relay-module) - $4
* Old cellphone micro usb charger
* Micro SD Card (2GB minimum)
* A wall power outlet
* A bunch of wires

**Software**

* [Raspbian](http://www.raspbian.org/)
* Python (installed with Raspbian)
* Raspberry Pi GPIO Python libs (installed with Raspbian)
* Python MQTT lib

## Hardware Setup:
------

1. **Connect Relay to Raspberry Pi**

    Solder the wires connecting the GPIO ports to the relay.  

    <img src="https://i.imgur.com/nH2Xfcf.png" height="350"> &nbsp; <img src="https://i.imgur.com/2rHtivv.jpg" height="350">


2. **Connect Relay to wall power**

    * Connect to wall power to the NC port of the relay.
    * Connect common port of the relay to power outlet.
    * Connect power outlet to neutral wall power. 
    
    We are using the NC port because in case something breaks down, you'll still have a working power outlet. 

    <img src="https://i.imgur.com/ky61lWA.png" height="350"> &nbsp; <img src="https://i.imgur.com/lk6Fhnq.jpg" height="350">



3. **Connect Raspberry Pi with its power supply**

    Hook up the tongs of the usb phone charger the wall power and plug the microusb into the RPi

    <img src="https://i.imgur.com/P9SgaKd.jpg" height="350">
    

4. **Shove it all in a electrical box and put into the wall**
    
    It took me a lot of finagling, but I managed to fit all in the box. Make sure the box you choose isn't a metal one or else the RPi won't get wifi.

    <img src="https://i.imgur.com/H9C0pc8.jpg" height="350">

## Software Installation:
-----

1. **Install [Raspbian](http://www.raspbian.org/) and setting up wifi:**

    [Tutorial](https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor)

2. **Install the python MQTT library**

    `pip install paho-mqtt`
    
3. **Run python script on startup**

    `sudo crontab -e`

    add this line to the end on the file:

    `@reboot sudo python3 /path/to/python/script/mqtt_switch.py &`

4.  **Setup MQTT broker (on separate computer preferably)**
    
    An MQTT broker is the server the RPI will listen and report to. Publish MQTT messages to the broker and it will distribute the message to its subscribers.

    [Tutorial](http://www.steves-internet-guide.com/install-mosquitto-broker/)

5. **Publishing commands to MQTT broker**

    Several ways you can accomplish [this](https://www.eclipse.org/paho/downloads.php). The easiest way is to use commandline:

    `mosquitto_pub  -h BROKER_IP_ADDRESS -p 1883 -u username -P password -t 'switch/0' -m '0'`
-----
<img src="https://i.imgur.com/KSue9d5.jpg" height="350"> &nbsp; <img src="https://i.imgur.com/5YXorCs.jpg" height="350">

More pics at: https://imgur.com/a/57BR5AR

*Disclaimer: You're dealing with dangerous amounts of electricity, so do this at your own risk. Please be careful. I'm not responsible if anything happens.*
