This python script reads date and time from a serially attached GPS and sets the system time on Raspberry Pi. It is used to set the date and time when the Pi is used where it is not attached to a network that provides time services. It is designed to set the time if you are able to use a network or not.

This script:

Collects Time and Date from GPS.

Reformats the information from NMEA sentance for use as an argument to the "date -s" command.

Shuts down the network time service - because you can't set the time manually if its running.

Sets the system time with date -s

Restarts the network time service - in case you are connected to a network.

To make use the of the script on boot:

Place a copy in /opt/set_time_from_gps/set_time_from_gps.py

add the line "/opt/set_time_from_gps/set_time_from_gps.py" to /etc/rc.local as root (use sudo) prior to the exit 0 line.

Future enhancements are to add logging and GPS checksum verification. 
