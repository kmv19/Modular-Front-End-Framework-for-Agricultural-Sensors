# Modular-Front-End-Framework-for-Agricultural-Sensors

## Project Overview
This project focuses on developing a modular front-end framework for agricultural sensors, specifically integrating a capacitive-based leaf wetness sensor into a standalone system. Accurate monitoring of leaf wetness is essential for effective crop management. The system aims to provide reliable and autonomous data collection and processing.
The framework incorporates a Raspberry Pi Pico microcontroller, a solar-powered battery management system (including a solar panel, solar charge controller and Li-ion batteries).

## Components
- **Raspberry Pi Pico**: RP2040 Processor Microcontroller
- **Solar Power Manager**: 5V 1A Output for system power management
- **Leaf Wetness Sensor**: 7V Capacitive Sensor
- **Lithium Ion Battery**: 3.7V, 5000mAh for backup storage
- **Solar Panel**: 6W (6V, 1A) for energy harvesting
- **DC-DC Buck Converter**: 5V to 8V for higher voltage components
- **I2C OLED Module**: 3V for displaying processed data
- **SPI Micro SD Card Reader**: 5V for data storage
- **RTC Module**: 3V for real-time timestamps

## System Architecture
The system is designed to be powered by either a solar panel or Li-ion batteries. The power is managed by a solar charge controller to provide a continuous and stable 5V, 1A output power supply. The microcontroller processes the data sent from the sensor, displays it on an OLED screen and saves it on an SD card.

![image](https://github.com/user-attachments/assets/f46112f1-c1ca-4274-9bba-16226e54ba91)

## Features
- **Sensor Data Acquisition**
- **Data Processing**
- **Data Display**
- **Data Storage**
- **Power Supply and Management**
- **Standalone Operation**
- **Testing and Validation**

## Methodology
### System Architectural Design
The system's architecture involves a Raspberry Pi Pico microcontroller, solar-powered battery management system, OLED display, SD card and RTC module. The sensors are connected and managed through a well-defined block diagram setup.

### Software Development
1. **Measuring the On-time of a PWM Wave**: The code measures the high pulse duration of a PWM signal.
2. **Interfacing Raspberry Pi Pico with OLED, SD Card Reader and RTC**: The system logs data, timestamps it, displays it on an OLED screen, and saves it to an SD card.
3. **Measuring the Voltage of a PWM Signal**: The code reads the analog voltage values from the leaf wetness sensor and maps it to a 3.3V range.

### Battery Management System (BMS)
The BMS integrates a solar panel, solar charge controller, and Li-ion batteries to ensure efficient and reliable power management. This configuration allows for autonomous and uninterrupted operation in remote agricultural environments.

## Setup and Operation
The setup involves integrating all components as per the block diagram, coding the microcontroller for data acquisition, processing, display, and storage. The system is then tested in both lab and field conditions to ensure its reliability and accuracy.

### Testing
- **Lab Testing**: Conducted to ensure system functionality in a controlled environment.
- **Field Testing**: Performed to validate the system's performance in real agricultural conditions.

![IMG-20240706-WA0004](https://github.com/user-attachments/assets/c36b7fe6-5d04-416e-92e9-e89ae2dfb69e)

## Results
The data collected from both lab and field testing is analyzed to confirm the system's accuracy and reliability. The findings support the improved decision-making in agricultural management.

## Conclusion
This project successfully demonstrates the development of a standalone module for agricultural sensors. Future work includes expanding the framework to integrate additional sensors and enhance system capabilities.
