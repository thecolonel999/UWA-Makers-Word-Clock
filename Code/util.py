from ds3231_port import DS3231
import network
import ntptime
import os
from machine import RTC
import utime
import sys


def calibrate_time(rtc, i2c, offset):
    ds = DS3231(i2c)
    ntptime.settime()
    ds.save_time()
    tm = utime.localtime(utime.mktime(utime.localtime()) + offset*3600)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    rtc.datetime(tm)


def get_time(rtc):
    return(rtc.datetime())


def string_time(hour, minute):
    return_str = "it is"
    if hour > 12:
        hour = hour - 12

def get_config(filename):
    config = {}
    try:
        with open(filename,  "r") as infile:
            for line in infile.readlines():
                    line = line.strip().split("=")
                    config[line[0]] = line[1]
    except OSError as e:
        sys.stderr.write("OSError: config file probably not found\n")
        sys.exit(1)
    return config





    