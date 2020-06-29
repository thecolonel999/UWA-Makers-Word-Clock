from machine import Pin, I2C, RTC, ADC
from neopixel import NeoPixel
from time import sleep_ms, sleep_us
import util
from Connection import Connection
import sys


config = util.get_config("config.txt")
SSID = config["SSID"]
PK = config["PK"]
GMT_OFFSET = int(config["GMT_OFFSET"])
N_LEDS = int(config["N_LEDS"])
MAX_BRIGHT = int(config["MAX_BRIGHT"])

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
rtc = RTC()
conn = Connection()
conn.connect(SSID, PK)


util.calibrate_time(rtc, i2c, GMT_OFFSET)
current_time = util.get_time(rtc)

hour = current_time[4]
minute = current_time[5]

print(str(hour) + ":" + str(minute))

np_pin = Pin(14, Pin.OUT)
np = NeoPixel(np_pin, N_LEDS)


# Cutesy animation to cycle through all of the leds
while True:
    colour = (MAX_BRIGHT, MAX_BRIGHT, MAX_BRIGHT)
    zeroed = (0, 0, 0) 
    np[0] = colour
    for i in range(1, N_LEDS):
        np[i - 1] = zeroed
        np[i] = colour
        np.write()
        sleep_ms(500)