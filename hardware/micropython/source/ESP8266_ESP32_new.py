import BlynkLib
import network
import machine

WIFI_SSID = 'galactic_gateway'
WIFI_PASS = '01234567'

BLYNK_AUTH = '-vDO7-8fGOnr7S71jR4kEIQ1wIG-tfme'

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.VIRTUAL_WRITE(15)
def my_write_handler(value):
    print('Current V15 value: {}'.format(value))

@blynk.VIRTUAL_READ(23)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(23, int(time.time()))

while True:
    blynk.run()
