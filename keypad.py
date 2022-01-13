from machine import Pin
import time

# KeyPad
col1 = Pin(15, Pin.OUT)
col2 = Pin(17,Pin.OUT)
col3 = Pin(13,Pin.OUT)
row1 = Pin(16, Pin.IN, Pin.PULL_DOWN)
row2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
row3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
row4 = Pin(14, Pin.IN, Pin.PULL_DOWN)


last = "x"
history = ["x", "x", "x", "x", "x"]
keypad=10


def read():
    global last
    global key_history
    global keypad
    keypad = " "
    col1.value(1)
    time.sleep_ms(1)
    if row1.value()==1:
        keypad=1
    elif row2.value()==1:
        keypad=4
    elif row3.value()==1:
        keypad=7
    elif row4.value()==1:
        keypad="*"
    col1.value(0)
    time.sleep_ms(1)
    
    col2.value(1)
    time.sleep_ms(1)
    if row1.value()==1:
        keypad=2
    elif row2.value()==1:
        keypad=5
    elif row3.value()==1:
        keypad=8
    elif row4.value()==1:
        keypad=0
    col2.value(0)
    time.sleep_ms(1)
    
    col3.value(1)
    time.sleep_ms(1)
    if row1.value()==1:
        keypad=3
    elif row2.value()==1:
        keypad=6
    elif row3.value()==1:
        keypad=9
    elif row4.value()==1:
        keypad="#"
    col3.value(0)
    time.sleep_ms(1)
    if keypad!=" ":
       last=keypad
    if keypad != last and last != None:
        print("in cikle", keypad)
        print("last", last)
        history.append(last)
        history.pop(0)
        last = keypad
   
    

