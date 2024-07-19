from machine import Pin
import time

pwm = Pin(15, Pin.IN)

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

while True:      
    l = []
    
    for _ in range(1000):
        on_time = measure_pwm(pwm)
        if on_time > 0:  # Valid measurements
            l.append(on_time)
 
    if l:
        avg_on_time = sum(l) / len(l)
        print("Average On_Time =", avg_on_time/1000)