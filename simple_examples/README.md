# Simple Examples

In this section are simple examples for basic Raspberry Pi GIPO functionality.

## Make a LED blick

### About
The code LED_Blink_Example.py makes the LED of the circuit below blink. To build it use a LED diode connected to a resistor (470 Ohms is enough).

### Circuit

![LED_Blink_Example_image](https://user-images.githubusercontent.com/53011744/140577519-8586f117-4924-4453-9f56-fd6fd7508ff5.png)

## SPI Communication

### About
The SPI_Communication_Example.py code introduces simple SPI communication. To test it use a digital analyzer or an oscilloscope. 
You can also test it by short-circuiting the MOSI and MISO connections so that the Raspberry Pi receives the message it sent. 
- obs: Note that on Raspberry Pi there are 2 buses for SPI communication (SPI0 and SPI10), however only SPI0 is natively enabled. To activate SPI1, follow the steps:
    - Open the Terminal
    - Go to the "boot" directory: cd /boot
    - Open the "config.txt": sudo nano config.txt
    - Insert one line on the text: "dtoverlay=spi1-1cs"
    - Save it: "Ctrl+X", "s" and "Enter"
    - Reboot the system

### Circuit

![SPI_Communication_Example_image](https://user-images.githubusercontent.com/53011744/140578589-240a0914-f9b4-4ecd-b68f-d5c20f168015.png)

## Threaded Callback Interrupt - LED Frequency Controller 

### About
The Interrupt_Example.py code is a simple example of chained interrupt callback functions. It is possible to control by buttons (switches) the frequency of an LED
inserted in a circuit with a resistor (470 Ohms is enough). The button 1 increase the frequency, the button 2 decrease the frequency and the button 3 reset the frequency
to 5Hz.

### Circuit

![Interrupt_Example_image](https://user-images.githubusercontent.com/53011744/140579157-5c19bff4-5651-45bb-b6ef-4e1012ecd470.png)

## CONTACT
Núcleo de Neurociências - NNC\
Universidade Federal de Minas Gerais - UFMG\
Author: João Pedro Carvalho Moreira (mcjpedro@gmail.com)\
Advisor: Márcio Flávio Dutra Moraes (marcionnc@gmail.com)
