from machine import Pin,I2C,ADC,SPI
from sh1106 import SH1106_I2C
import sdcard,uos,time
from ds3231_i2c import DS3231_I2C

led = Pin(25,Pin.OUT)
led.value(1)
# Initializations
wetness_in = ADC(1)
temp = ADC(0)
eva = ADC(2)

i2c = I2C(0, sda = Pin(16), scl = Pin(17), freq = 400000)
w = 128
h = 64

oled = SH1106_I2C(w, h, i2c)

ds_i2c = I2C(1,sda=Pin(14),scl = Pin(15))
ds = DS3231_I2C(ds_i2c)
cs = Pin(1,Pin.OUT)
spi = SPI(0,baudrate = 1000000,polarity = 0,
          phase = 0,bits = 8, firstbit = SPI.MSB,
          sck = Pin(2), mosi = Pin(3), miso = Pin(4))
sd = sdcard.SDCard(spi,cs)
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
file = open("/sd/sensor_data.csv", "a")

dry_value = 0.23* 65535/3.3
wet_value =  2.5 *65535/3.3
## Freq..
freq_pin = Pin(19,Pin.IN,machine.Pin.PULL_UP)
counter = 0
def pulse_counter(pin):
    global counter
    counter += 1
freq_pin.irq(trigger=Pin.IRQ_RISING, handler=pulse_counter)



def read_voltage():
    total = 0
    for _ in range(100):
        total += wetness_in.read_u16()
       
    average = total / 100
    voltage = average * (3.3 / 65535)
    return voltage, average

def calibrate_sensor(dry, wet, raw_value):
    wetness_percentage = 100 * (raw_value - dry) / (wet - dry)
    wetness_percentage = max(0, wetness_percentage)
    wetness_percentage = min(wetness_percentage,100)
    return wetness_percentage

def classify_voltage(wetness):
    if wetness < 10:
        return "Dry"
    elif 10 <= wetness < 20:
        return "Slight Moist"
    elif 20 <= wetness < 40:
        return "Moist"
    elif 40 <= wetness < 80:
         return  "Wet"
    else:
        return "Saturated"

def read_temperature_sensor():    
    total_value = 0.0
    total_value_gnd = 0.0
    for _ in range(100):
        raw_value = temp.read_u16()
        total_value += raw_value 
    avg_raw_value = float(total_value) / 100.0
    conv_rate = 3.3 / 65535.0
    voltage = (avg_raw_value ) * conv_rate
    return voltage

NUM_SAMPLES = 10

def read_moisture_sensor():
    total_value = 0
    
    for _ in range(NUM_SAMPLES):
        raw_value = eva.read_u16()
        total_value += raw_value
    
    avg_raw_value = total_value // NUM_SAMPLES
    
    voltage = avg_raw_value * (3.3 / 65535) - 0.020
    return voltage        
start_time = time.ticks_us()  
while True:
    x = time.ticks_us()
    if time.ticks_diff(x,start_time) >= 1000000:
        voltage, raw_value = read_voltage()
        wetness = calibrate_sensor(dry_value, wet_value, raw_value)
        state = classify_voltage(wetness)
        
        voltage_temp = read_temperature_sensor()
        temp_val =345.6276*voltage_temp - 537.1619
      
        voltage_eva = read_moisture_sensor()
        
        t = ds.read_time()
        timestring_day = "%02x/%02x/20%x" %(t[4],t[5],t[6])
        timestring_time="%02x:%02x:%02x" %(t[2],t[1],t[0])
        with open("/sd/sd1.txt", "a") as file:
            file.write(f"{timestring_day} {timestring_time}, Voltage = {voltage}, Wetness = {wetness}, state = {state}, Temperature = {temp_val}, Evaporation = {voltage_eva}, Frequency = {str(counter*8)}\n")
            file.flush()
       
        oled.fill(0)
        oled.text(f"Date:{timestring_day}",0,0)
        oled.text(f"Time:{timestring_time}",0,10)
        oled.text(f"Wetness:{wetness}",0,20)
        oled.text(f"Frequency = {str(counter*8)}",0,30)
        oled.text(f"Temp={temp_val}C", 0, 40)
        oled.text(f"Evap={voltage_eva} ", 0, 50)
        oled.show()
        start_time = time.ticks_us()
        counter = 0

        
