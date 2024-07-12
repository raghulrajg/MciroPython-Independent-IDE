import freeIDE

##Avoid the GPIO pin number 2 because of predefine pin(Network status indicator)

#WiFi configuration
SSID = "PUT_YOUR_WIFi_NAME"
Password = "PUT_YOUR_PASSWORD"

client = freeIDE.FreeIDE(SSID, Password)

def loop():
    while True:
        #put your code here
        pass
      
if __name__ == '__main__':
    loop()
