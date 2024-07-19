from machine import Pin, ADC
import utime

pin = ADC(2)

dry_value = 0.23* 65535/3.3
wet_value =  65535

def read_voltage():
    total = 0
    for _ in range(100):
        total += pin.read_u16()
        
    average = total / 100
    voltage = average * (3.3 / 65535)
    return voltage, average

def calibrate_sensor(dry, wet, raw_value):
    wetness_percentage = 100 * (raw_value - dry) / (wet - dry)
    wetness_percentage = max(0, wetness_percentage)
    return wetness_percentage

while True:    
    voltage, raw_value = read_voltage()
    wetness = calibrate_sensor(dry_value, wet_value, raw_value)
    print("Voltage: {:.5f} V, Wetness: {:.2f}%".format(voltage, wetness))
    
    utime.sleep(1)