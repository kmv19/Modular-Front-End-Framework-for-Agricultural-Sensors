from machine import Pin, ADC
import utime

pin = ADC(2)

def read_voltage():
    total = 0
    for _ in range(100):
        total += pin.read_u16()
        
    average = total / 100
    voltage = average * (3.3 / 65535)
    return voltage, average

while True:    
    voltage, raw_value = read_voltage()
    print("Voltage: {:.5f} V".format(voltage))
    
    utime.sleep(1)
