#put your filename has "main.py" 
import freeIDE
from machine import Pin
from time import sleep

##Avoid the GPIO pin number 2 because of predefine pin(Network status indicator)

#WiFi configuration
SSID = "PUT_YOUR_WIFi_NAME"
Password = "PUT_YOUR_PASSWORD"

client = freeIDE.FreeIDE(SSID, Password)

#put your variable here
led = Pin(2, Pin.OUT)

def loop():
    while True:
        #put your code here
        led.value(not led.value())
        sleep(1)

if __name__ == '__main__':
    loop()
