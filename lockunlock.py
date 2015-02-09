#!/usr/bin/python2.7

import os
import sys
import time

def LockUnlock(line):
    str_conn = "Device added: sysfs-LGE-Nexus_5"
    str_disconn = "device removed: sysfs-LGE-Nexus_5"

    if line.find(str_conn) > -1:
        print "Device connected"
        os.system('xset dpms force on && gnome-screensaver-command -d')
    if line.find(str_disconn) > -1:
        print "Device disconnected"
        os.system('gnome-screensaver-command -l && xset dpms force off')


tailed_file = '/var/log/syslog'

while True:
    try:
        with open(tailed_file) as file_:
            file_.seek(0,2)
            while True:
                curr_position = file_.tell()
                line = file_.readline()
                if not line:
                    file_.seek(curr_position)
                else:
                    LockUnlock(line)
                time.sleep(1)

    except KeyboardInterrupt:
        print "Bye"
        sys.exit()
