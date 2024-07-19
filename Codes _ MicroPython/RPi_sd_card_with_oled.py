from machine import Pin, I2C, SPI, RTC
import time, sdcard, os
from sh1106 import SH1106_I2C

led = Pin(25,Pin.OUT)
led.value(1)

spi = SPI(0,baudrate=40000000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
sd = sdcard.SDCard(spi, Pin(5))

vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print(os.listdir('/sd'))

pwm = Pin(15, Pin.IN)
w = 128
h = 64
i2c = I2C(0, sda = Pin(16), scl = Pin(17), freq = 400000)

oled = SH1106_I2C(w, h, i2c)

rtc = RTC()

def measure_pwm(pwm):
    on_time = 0
    
    if pwm.value() == 0:
    
        while pwm.value() == 0:
            pass
        start_pwm = time.ticks_us()
        
        while pwm.value() == 1:
            pass
        end_pwm = time.ticks_us()
        
        on_time = time.ticks_diff(end_pwm, start_pwm)
    
    return on_time

with open ("/sd/sd1.txt","w") as file:
    file.write("")

while True:      
    l = []
    
    for _ in range(100):
        on_time = measure_pwm(pwm)
        if on_time > 0:  # Valid measurements
            l.append(on_time)
        
    avg_on_time = sum(l) / len(l)
    print("Average On_Time =", avg_on_time)
     
    timestamp = rtc.datetime()

    timestamp_read = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}:{:02d}".format(timestamp[0], timestamp[1], timestamp[2],
    timestamp[3], timestamp[4], timestamp[5],timestamp[6])
   
    timestamp_read_day = "{}-{:02d}-{:02d} ".format(timestamp[0], timestamp[1], timestamp[2])

    timestamp_read_time = "{:02d}:{:02d}:{:02d}:{:02d}".format(timestamp[3], timestamp[4], timestamp[5],timestamp[6])

    oled.fill(0)
    oled.text(f"Day:{timestamp_read_day}",0,0)
    oled.text(f"Time:{timestamp_read_time}",0,10)
    oled.text(f"On Time={str(on_time/1000)} ms ",0,20)
    oled.show()
    
    with open ("/sd/sd1.txt","a") as file:
        file.write(f"{timestamp_read}, On_Time={on_time/1000}ms\n")
        file.flush()
        
    time.sleep(.1)