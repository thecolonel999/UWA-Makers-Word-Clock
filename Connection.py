import network
from time import sleep
import sys
import machine

class Connection:

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self, ssid, pk):
        
        self.wlan.active(True)
        if not self.wlan.isconnected():
            print('connecting to network...')
            self.wlan.connect(ssid, pk)
            while not wlan.isconnected():
                pass
        print("network config: ", self.wlan.ifconfig())
    