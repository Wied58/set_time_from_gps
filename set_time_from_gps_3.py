#!/usr/bin/python3

import serial
import time
import subprocess
import syslog
syslog.syslog("Attempting to set time from GPS")

#Sat 16 Mar 02:45:17 UTC 2019



port = "/dev/serial0"

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

print ("Looking for GPS Data")

i = 0
while i < 35:
   time.sleep(1.0)
   data = ser.read_until().decode('utf_8')
   sdata = data.split(",")
   if sdata[0] == '$GPRMC' and sdata[2] == 'V':
       	print (sdata)
   elif sdata[0] == '$GPRMC' and sdata[2] != 'V':

        sdate = sdata[9]
        stime = sdata[1]
        
        if   sdate[2:4] == '01':
        	smonth = "JAN"
        elif sdate[2:4] == '02':
        	smonth = "FEB"
        elif sdate[2:4] == '03':
        	smonth = "MAR"
        elif sdate[2:4] == '04':
        	smonth = "APR"
        elif sdate[2:4] == '05':
        	smonth = "MAY"
        elif sdate[2:4] == '06':
        	smonth = "JUN"
        elif sdate[2:4] == '07':
        	smonth = "JUL"
        elif sdate[2:4] == '08':
        	smonth = "AUG"
        elif sdate[2:4] == '09':
        	smonth = "SEP"
        elif sdate[2:4] == '10':
        	smonth = "OCT"
        elif sdate[2:4] == '11':
        	smonth = "NOV"
        elif sdate[2:4] == '12':
        	smonth = "DEC"
        
        print (sdate[0:2] + " " + smonth + " " +"20"+ sdate[4:7] + " " + stime[0:2] + ":" + stime[2:4] + ":" + stime[4:6])
        date_time = sdate[0:2] + " " + smonth + " " +"20"+ sdate[4:7] + " " + stime[0:2] + ":" + stime[2:4] + ":" + stime[4:6]
        
        print ("Shutting down network time service")
        command = ['sudo', 'systemctl', 'stop', 'systemd-timesyncd.service']
        subprocess.call(command)
        
        print("The sysdate before setting with GPS is:")
        subprocess.call('date')

        # Uncomment below for testing while on network.
        # This "holds" the GPS time for 5 seconds. 
        # If on a network the time will be set by the network, the GPS will set the time 5 seconds, but 5 seconds slow, then then when the network is
        # restarted, the time will be proplerly set. 
        #time.sleep(5.0)

        print ("Setting time via GPS.")
        syslog.syslog("Setting time via GPS") 
        command = ['sudo', 'date', '-s', date_time]
        subprocess.call(command)
        
        print("The sysdate after setting with GPS is:")
        subprocess.call('date')

        break

   i += 1

print ("restarting netwotk time servivce")
command = ['sudo', 'systemctl', 'start', 'systemd-timesyncd.service']
subprocess.call(command)
subprocess.call('date')




print ("")
