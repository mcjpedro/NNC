# SPI COMMUNICATION - RASPBERRY PI
This application was designed to make SPI communication between the Raspberry Pi and any peripheral system. Through a programmable interface the user is able to modify:
- The connection bus
- The number of bits sent with each message
- The bits sequence (MSB and LSB)
- The clock frequency

At each communication command, the interface returns the word read through the SPI protocol to the user.

![image](https://user-images.githubusercontent.com/53011744/149071143-57814850-a257-4673-a1f9-0e6660b25c9c.png)

## IMPORTANT NOTE
To run the interface with all its functionality, please read the notes below. It is necessary to change some native Raspberry Pi protocols, located in the "/boot/confi.txt" file.

## INTERFACE PRODUCTION OBSERVATIONS
Interface design: to build the interface layout the QtDesigner program was
used, after the design was finished, a .ui file was generated which was 
converted to .py through the command "pyui5 -x program.ui -o program.py" in
the file directory.

- Bits per word on Raspberry Pi: on the Raspberry Pi only 8-bits are sent at a 
time, so to make a communication with 16-bits it is necessary to use the 
xfer2( ) (SpiDev library) function with a list of bytes. In this way, two 8-bit 
words will be sent without the CS returning to the idle state.

- Correct clock frequency: on the Raspberry Pi processor there is a limitation 
on the dedicated clock. Therefore, for the clock frequency to reach the 
programmed value and not a percentage of it, it is necessary to overclock the 
processor, to do so, follow the steps:
    - Open the Terminal
    - Go to the "boot" directory: cd /boot
    - Open the "config.txt": sudo nano config.txt
    - Insert two lines on the text: "core_freq=500" and "core_freq_min=500"
    - Save it: "Ctrl+X", "s" and "Enter"
    - Reboot the system

- Turn ON the SPI1 bus: the pins referring to the SPI 1 bus are natively 
turned off, so it is necessary to turn them on through the "config.txt" file:
    - Open the Terminal
    - Go to the "boot" directory: cd /boot
    - Open the "config.txt": sudo nano config.txt
    - Insert one line on the text: "dtoverlay=spi1-1cs"
    - Save it: "Ctrl+X", "s" and "Enter"
    - Reboot the system
    
- Layout deconfiguration in linux: when transferring the windows interface 
(where it was conceived) to linux, some elements were misconfigured. To solve 
this, we manually repositioned some labels and used the function below
    - QtWidgets.QApplication.setStyle("fusion")

- Executable file: to make an executable file from the .py code it is 
necessary to use the PyInstaller library and attach the interface images in the 
executable creation directory. For that, the command "pyinstaller --windowed 
--onefile program.py" is used, the function research_path( ) removed from the 
internet and a modification in the file ".spec" generated after the process of 
building the executable. 

## CONTACT
Núcleo de Neurociências - NNC\
Universidade Federal de Minas Gerais - UFMG\
Author: João Pedro Carvalho Moreira (mcjpedro@gmail.com)\
Advisor: Márcio Flávio Dutra Moraes (marcionnc@gmail.com)
