import time
from machine import Pin
from neopixel import NeoPixel
np = NeoPixel(Pin(18, Pin.OUT), 8)
np.fill((0, 0, 0))
np.write()

status = 0

def write(status):
    if status=="1R":
        np[0] = (20, 0, 0)
        np.write()
    if status=="1G":
        np[0] = (0, 20, 0)
        np.write()
    if status=="1B":
        np[0] = (0, 0, 20)
        np.write()
    if status=="10":
        np[0] = (0, 0, 0)
        np.write()
    if status=="2R":
        np[1] = (20, 0, 0)
        np.write()
    if status=="2G":
        np[1] = (0, 20, 0)
        np.write()
    if status=="2B":
        np[1] = (0, 0, 20)
        np.write()
    if status=="20":
        np[1] = (0, 0, 0)
        np.write()
    if status=="3R":
        np[2] = (20, 0, 0)
        np.write()
    if status=="3G":
        np[2] = (0, 20, 0)
        np.write()
    if status=="3B":
        np[2] = (0, 0, 20)
        np.write()
    if status=="30":
        np[2] = (0, 0, 0)
        np.write()
    if status=="4R":
        np[3] = (20, 0, 0)
        np.write()
    if status=="4G":
        np[3] = (0, 20, 0)
        np.write()
    if status=="4B":
        np[3] = (0, 0, 20)
        np.write()
    if status=="40":
        np[3] = (0, 0, 0)
        np.write()
    if status=="5R":
        np[4] = (20, 0, 0)
        np.write()
    if status=="5G":
        np[4] = (0, 20, 0)
        np.write()
    if status=="5B":
        np[4] = (0, 0, 20)
        np.write()
    if status=="50":
        np[4] = (0, 0, 0)
        np.write()
    if status=="6R":
        np[5] = (20, 0, 0)
        np.write()
    if status=="6G":
        np[5] = (0, 20, 0)
        np.write()
    if status=="6B":
        np[5] = (0, 0, 20)
        np.write()
    if status=="60":
        np[5] = (0, 0, 0)
        np.write()
    if status=="7R":
        np[6] = (20, 0, 0)
        np.write()
    if status=="7G":
        np[6] = (0, 20, 0)
        np.write()
    if status=="7B":
        np[6] = (0, 0, 20)
        np.write()
    if status=="70":
        np[6] = (0, 0, 0)
        np.write()
    if status=="8R":
        np[7] = (20, 0, 0)
        np.write()
    if status=="8G":
        np[7] = (0, 20, 0)
        np.write()
    if status=="8B":
        np[7] = (0, 0, 20)
        np.write()
    if status=="80":
        np[7] = (0, 0, 0)
        np.write()
    if status == "Clear":
        np.fill((0, 0, 0))
        np.write()

def test():
    test_list=["1R", "1G", "1B", "10", "2R", "2G", "2B", "20", "3R", "3G", "3B", "30", "4R", "4G", "4B", "40",\
               "5R", "5G", "5B", "50", "6R", "6G", "6B", "60", "7R", "7G", "7B", "70", "8R", "8G", "8B", "80"]
    for i in range(len(test_list)):
        write(test_list[i])
        time.sleep_ms(200)
    

write("Clear")
