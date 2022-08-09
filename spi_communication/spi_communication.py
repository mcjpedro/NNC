"""
SPI Communication Interface for Raspberry Pi

Created on Wed Oct 20 10:27:27 2021

Author: João Pedro Carvalho Moreira
Universidade Federal de Minas Gerais, Brazil
Núcleo de Neurociências (NNC)
"""

from PyQt5 import QtCore, QtGui, QtWidgets      # Interface library
from PyQt5.QtWidgets import QMessageBox         # Warning message library
import spidev                                   # SPI communicatio library (only for linux)
import os                                       # Image directory library
import sys                                      # Import the system library

# Program interface 
class Ui_SPI_Communication(object):    
    def setupUi(self, SPI_Communication):
        # The following function defines the interface aspects such as buttons, texts, images, etc.
        # The code that creates these elements was generated using QtDesigner, so it won't be commented
        # in full, only in blocks. At the end of this section there are the application actions, these
        # connect an interaction with the interface to functions that define the functionality of this
        # program.
        
        # Create the main window
        SPI_Communication.setObjectName("SPI_Communication")
        SPI_Communication.resize(471, 296)
        SPI_Communication.setWindowTitle("SPI Communication - Raspberry Pi")
        SPI_Communication.setWindowIcon(QtGui.QIcon(self.resource_path("images/icon.ico")))
        SPI_Communication.setStyleSheet("QMainWindow{background-color:#4B4B4B;color:#FFFFFF;}")
        self.main_window = QtWidgets.QWidget(SPI_Communication)
        self.main_window.setStyleSheet("QWidget{background-color:#353535;}")
        self.main_window.setObjectName("main_window")
        
        # Create a scroll area
        self.gridLayout = QtWidgets.QGridLayout(self.main_window)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll_area = QtWidgets.QScrollArea(self.main_window)
        self.scroll_area.setStyleSheet("QScrollArea{border:0px}QScrollBar:vertical{background:#353535;width:5px}QScrollBar::handle:vertical{background:#2C53A1;min-width:20px;}QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:#353535;}QScrollBar:horizontal{background:#353535;height:5px}QScrollBar::handle:horizontal{background:#2C53A1;min-width:20px;}QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{background:#353535;}")
        self.scroll_area.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll = QtWidgets.QWidget()
        self.scroll.setGeometry(QtCore.QRect(0, 0, 453, 278))
        self.scroll.setObjectName("scroll")
        
        # Create a frame inside main window
        self.communication = QtWidgets.QFrame(self.scroll)
        self.communication.setGeometry(QtCore.QRect(30, 0, 391, 271))
        self.communication.setStyleSheet("QLabel{}QCheckBox{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}QCheckBox::indicator{width:15px;height:15px;background-color:#606060;border-radius:4px;}QCheckBox::indicator:checked{background-color:#A21F27;}")
        self.communication.setObjectName("communication")
        self.send_message = QtWidgets.QPushButton(self.communication)
        self.send_message.setGeometry(QtCore.QRect(160, 200, 71, 21))
        self.send_message.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_message.setStyleSheet("QPushButton{font:10pt\"Century Gothic\";font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")
        self.send_message.setText("SEND")
        self.send_message.setObjectName("send_message")
        self.significant_bit = QtWidgets.QComboBox(self.communication)
        self.significant_bit.setGeometry(QtCore.QRect(150, 110, 71, 16))
        self.significant_bit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.significant_bit.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.significant_bit.setCurrentText("MSB")
        self.significant_bit.setObjectName("significant_bit")
        self.significant_bit.addItem("MSB")
        self.significant_bit.addItem("LSB")
        
        # Create the labels in the interface
        self.label_1 = QtWidgets.QLabel(self.communication)
        self.label_1.setGeometry(QtCore.QRect(10, 30, 72, 16))
        self.label_1.setStyleSheet("QLabel{color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}")
        self.label_1.setText("SETTINGS")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_0 = QtWidgets.QLabel(self.communication)
        self.label_0.setGeometry(QtCore.QRect(10, 0, 291, 21))
        self.label_0.setStyleSheet("QLabel{color:#FFFFFF;font:14pt\"Century Gothic\";font-weight:bold;}")
        self.label_0.setText("SPI Communication")
        self.label_0.setObjectName("label_0")
        self.label_2 = QtWidgets.QLabel(self.communication)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 131, 21))
        self.label_2.setStyleSheet("QLabel{color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}")
        self.label_2.setText("COMMUNICATION")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # Create the NNC image 
        self.image = QtWidgets.QFrame(self.communication)
        self.image.setGeometry(QtCore.QRect(240, 0, 151, 161))
        self.image.setStyleSheet("QFrame{border:0px}")
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.image_nnc = QtWidgets.QLabel(self.image)
        self.image_nnc.setGeometry(QtCore.QRect(20, 20, 111, 141))
        self.image_nnc.setPixmap(QtGui.QPixmap(self.resource_path("images/NNC_logo.png")))
        self.image_nnc.setScaledContents(True)
        self.image_nnc.setAlignment(QtCore.Qt.AlignCenter)
        self.image_nnc.setObjectName("image_nnc")
        
        # Create the bus selection
        self.bus = QtWidgets.QComboBox(self.communication)
        self.bus.setGeometry(QtCore.QRect(150, 50, 71, 16))
        self.bus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bus.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.bus.setCurrentText("SPI0")
        self.bus.setObjectName("bus")
        self.bus.addItem("SPI0")
        self.bus.addItem("SPI1")
        
        # Create the bits per word selection
        self.bits_word = QtWidgets.QComboBox(self.communication)
        self.bits_word.setGeometry(QtCore.QRect(150, 90, 71, 16))
        self.bits_word.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bits_word.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.bits_word.setCurrentText("8")
        self.bits_word.setObjectName("bits_word")
        self.bits_word.addItem("8")
        self.bits_word.addItem("16")
        
        # Create the input line edit
        self.message = QtWidgets.QLineEdit(self.communication)
        self.message.setGeometry(QtCore.QRect(10, 200, 141, 20))
        self.message.setStyleSheet("QLineEdit{border:#969696;background-color:#606060;border-radius:6px;color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}")
        self.message.setText("Type here")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setDragEnabled(False)
        self.message.setReadOnly(False)
        self.message.setObjectName("message")
        
        # Create the output viewer
        self.output = QtWidgets.QLineEdit(self.communication)
        self.output.setGeometry(QtCore.QRect(240, 200, 141, 20))
        self.output.setStyleSheet("QLineEdit{border:#969696;background-color:#606060;border-radius:6px;color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}")
        self.output.setText("0x0000")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setDragEnabled(False)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        
        # Create the info button for bit sequence selection
        self.msg_significant_bit = QtWidgets.QPushButton(self.communication)
        self.msg_significant_bit.setGeometry(QtCore.QRect(19, 110, 95, 16))
        self.msg_significant_bit.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_significant_bit.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_significant_bit.setText("Bit send sequence")
        self.msg_significant_bit.setObjectName("msg_significnt_bit")
        
        # Create the info button for bus selection
        self.msg_bus = QtWidgets.QPushButton(self.communication)
        self.msg_bus.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.msg_bus.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_bus.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_bus.setText("Communication bus")
        self.msg_bus.setObjectName("msg_bus")
        
        # Create the info button for bits per word selection
        self.msg_bits_word = QtWidgets.QPushButton(self.communication)
        self.msg_bits_word.setGeometry(QtCore.QRect(20, 90, 69, 16))
        self.msg_bits_word.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_bits_word.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_bits_word.setText("Bits per word")
        self.msg_bits_word.setObjectName("msg_bits_word")
        
        # Create the info button for input lie edit
        self.msg_send_message = QtWidgets.QPushButton(self.communication)
        self.msg_send_message.setGeometry(QtCore.QRect(19, 180, 124, 20))
        self.msg_send_message.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_send_message.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_send_message.setText("Messge to be sent")
        self.msg_send_message.setObjectName("msg_send_message")
        
        # Create the info button for output viewew
        self.msg_output = QtWidgets.QPushButton(self.communication)
        self.msg_output.setGeometry(QtCore.QRect(250, 180, 121, 20))
        self.msg_output.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_output.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_output.setText("Message received")
        self.msg_output.setObjectName("msg_output")
        
        # Create the clear button
        self.clear = QtWidgets.QPushButton(self.communication)
        self.clear.setGeometry(QtCore.QRect(300, 240, 81, 21))
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("QPushButton{font:14pt\"Century Gothic\";font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")
        self.clear.setText("CLEAR")
        self.clear.setObjectName("clear")
        
        # Create the mode selection
        self.mode = QtWidgets.QComboBox(self.communication)
        self.mode.setGeometry(QtCore.QRect(150, 70, 71, 16))
        self.mode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mode.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.mode.setCurrentText("0")
        self.mode.setObjectName("mode")
        self.mode.addItem("0")
        self.mode.addItem("1")
        self.mode.addItem("2")
        self.mode.addItem("3")
        
        # Create the info button for mode selection
        self.msg_mode = QtWidgets.QPushButton(self.communication)
        self.msg_mode.setGeometry(QtCore.QRect(20, 70, 48, 16))
        self.msg_mode.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_mode.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_mode.setText("SPI mode")
        self.msg_mode.setObjectName("msg_mode")
        
        # Creae the info button for clock frequency selection
        self.msg_clock_frequency = QtWidgets.QPushButton(self.communication)
        self.msg_clock_frequency.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.msg_clock_frequency.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_clock_frequency.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_clock_frequency.setText("Clock frequency")
        self.msg_clock_frequency.setObjectName("msg_bitsignificativo_2")
        
        # Create the clock frequency selection
        self.clock_frequency = QtWidgets.QComboBox(self.communication)
        self.clock_frequency.setGeometry(QtCore.QRect(150, 130, 71, 16))
        self.clock_frequency.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clock_frequency.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.clock_frequency.setCurrentText("30MHz")
        self.clock_frequency.setObjectName("clock_frequency")
        self.clock_frequency.addItem(" 30MHz")
        self.clock_frequency.addItem(" 10MHz")
        self.clock_frequency.addItem("  5MHz")
        self.clock_frequency.addItem("  1MHz")
        self.clock_frequency.addItem("500kHz")
        self.clock_frequency.addItem("200kHz")
        self.clock_frequency.addItem("100kHz")
        self.clock_frequency.addItem(" 50kHz")
        self.clock_frequency.addItem(" 10kHz")
        
        # Create the iterface lines 
        self.line_1 = QtWidgets.QFrame(self.communication)
        self.line_1.setGeometry(QtCore.QRect(10, 152, 231, 11))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.communication)
        self.line_2.setGeometry(QtCore.QRect(10, 225, 371, 11))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.communication)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 231, 11))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        # Set the scroll area end the main window
        self.scroll_area.setWidget(self.scroll)
        self.gridLayout.addWidget(self.scroll_area, 0, 0, 1, 1)
        SPI_Communication.setCentralWidget(self.main_window)
        
        # Define the initial values for the interface selections
        self.significant_bit.setCurrentIndex(0)
        self.bus.setCurrentIndex(0)
        self.bits_word.setCurrentIndex(0)
        self.mode.setCurrentIndex(0)
        self.clock_frequency.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SPI_Communication)
        
        # Interface actions
        self.send_message.clicked.connect(self.communicate)                    # When send button is clicked, it connects the commuication() function 
        self.msg_bus.clicked.connect(self.info_bus)                            # When info text is clecked,  it connects the corresponding info function
        self.msg_significant_bit.clicked.connect(self.info_significant_bit)    # When info text is clecked,  it connects the corresponding info function
        self.msg_mode.clicked.connect(self.info_mode)                          # When info text is clecked,  it connects the corresponding info function
        self.msg_bits_word.clicked.connect(self.info_bits_word)                # When info text is clecked,  it connects the corresponding info function
        self.msg_send_message.clicked.connect(self.info_send)                  # When info text is clecked,  it connects the corresponding info function
        self.msg_output.clicked.connect(self.info_output)                      # When info text is clecked,  it connects the corresponding info function
        self.msg_clock_frequency.clicked.connect(self.info_clock_frequency)    # When info text is clecked,  it connects the corresponding info function
        self.clear.clicked.connect(self.clear_interface)                       # When clear button is clicked, it connects the clear_interface() function 
        
    def communicate(self):
        # This function will set the parameters and make SPI communication
        
        # Set SPI connection
        spi = spidev.SpiDev()                                                   # Set SPI communication variable
        
        # Set the GPIO bus
        if self.bus.currentIndex() == 0:                                        # If SPI0 is selected
            spi.open(0,0)                                                       # Open SPI communication, bus 0 e CS 0
        else:                                                                   # If SPI1 is selected
            spi.open(1,0)                                                       # Open SPI communication, bus 1 e CS 0
        
        # Set clock frequency
        frequency = [30e6, 10e6, 5e6, 1e6, 500e3, 200e3, 100e3, 50e3, 10e3]     # Vector of possible clock frequencies
        spi.max_speed_hz = int(frequency[self.clock_frequency.currentIndex()])  # Set clock frequency according to interface selection
              
        # Set the SPI connection mode
        if self.mode.currentIndex() == 0:                                       # If mode 0 is selected 
            spi.mode = 0                                                        # Set polarity 0 an phase 0
        elif self.mode.currentIndex() == 1:                                     # If mode 1 is selected
            if self.bus.currentIndex() == 1:                                    # If SPI1 is selected
                self.error_message("On Raspberry pi, the SPI1 bus doesn't have mode 1 and 3") # Display error message
                self.mode.setCurrentIndex(0)                                    # Set polarity 0 and phase 0
            else:                                                               # If SPI0 is selected
                spi.mode = 1                                                    # Set polarity 0 and phase 1        
        elif self.mode.currentIndex() == 2:                                     # If mode 2 is selected
            spi.mode = 2                                                        # Set polarity 1 and phase 0
        else:                                                                   # If mode 3 is selected
            if self.bus.currentIndex() == 1:                                    # If SPI1 is selected
                self.error_message("On Raspberry pi, the SPI1 bus doesn't have mode 1 and 3") # Display error message
                self.mode.setCurrentIndex(0)                                    # Set polarity 0 and phase 0
            else:                                                               # If SPI0 is selected
                spi.mode = 3                                                    # Set polarity 1 and phase 1
            
        # Sets the message in hexadecimal
        bits_length = self.bits_word.currentIndex()                             # Set the bit length according to interface selection
        mosi = self.read_message(bits_length)                                   # Call the read_message() fuction    
        
        # Send the message
        if mosi != 'Invalid input' and bits_length == 0:                        # If the message is in the correct format and has 8 bits
            if self.significant_bit.currentIndex() == 0:                        # If the bit sequence is the most bit first (MSB)                
                miso = spi.xfer2(mosi)                                          # Make the SPI transfer, send a message and get another one
                miso = str(hex(miso[0]))                                        # Covert output in hexadecimal string
                miso = '0x' + miso[2:].upper()                                  # Edit the string to be uppercase
                self.output.setText(miso)                                       # Display the result in the interface
            else:                                                               # If the bit sequence is the last bit first (LSB)
                reverse_mosi = [self.reverse_bits(mosi[0])]                     # Call the reverse_bits() fuction to reverse the bits sequence
                miso = spi.xfer2(reverse_mosi)                                  # Make the SPI transfer, send a message and get another one
                miso = str(hex(miso[0]))                                        # Covert output in hexadecimal string
                miso = '0x' + miso[2:].upper()                                  # Edit the string to be uppercase
                self.output.setText(miso)                                       # Exibe o resultado na interface
        elif mosi != 'Invalid input' and bits_length == 1:                      # If the message is in the correct format and has 16 bits
            if self.significant_bit.currentIndex() == 0:                        # If the bit sequence is the most bit first (MSB)        
                miso = spi.xfer2(mosi)                                          # Make the SPI transfer, send a message and get another one
                miso = str(hex(miso[0])) + str(hex(miso[1]))[2::]               # Covert output in hexadecimal string
                miso = '0x' + miso[2:].upper()                                  # Edit the string to be uppercase
                self.output.setText(miso)                                       # Display the result in the interface
            else:                                                               # If the bit sequence is the last bit first (LSB)
                reverse_mosi = []
                reverse_mosi.append(self.reverse_bits(mosi[1]))                 # Call the reverse_bits() fuction to reverse the bits sequence
                reverse_mosi.append(self.reverse_bits(mosi[0]))                 # Call the reverse_bits() fuction to reverse the bits sequence
                miso = spi.xfer2(reverse_mosi)                                  # Make the SPI transfer, send a message and get another one
                miso = str(hex(miso[0])) + str(hex(miso[1]))[2::]               # Covert output in hexadecimal string
                miso = '0x' + miso[2:].upper()                                  # Edit the string to be uppercase
                self.output.setText(miso)                                       # Display the result in the interface
        else:                                                                   # If the message isn't in the correct format
            self.output.setText(mosi)                                           # Display 'innvalid input' in the interface

    def clear_interface(self):
        # This function clear all selections
        self.significant_bit.setCurrentIndex(0)                                  # Clear the bit send sequence selection 
        self.bus.setCurrentIndex(0)                                              # Clear the bus selection 
        self.bits_word.setCurrentIndex(0)                                        # Clear the bits per word selection 
        self.mode.setCurrentIndex(0)                                             # Clear the SPI mode selection
        self.clock_frequency.setCurrentIndex(0)                                  # Clear the SPI mode selection
        self.message.setText("Type here")                                        # Clear the input message
        self.output.setText("0x0000")                                            # Clear the output message                    

    def read_message(self,bits_length):
        # This function reads the message entered by the user
        mosi = self.message.text()                                               # Read the text
        if mosi[:2] == '0x' and 2 < len(mosi) <= 4 and bits_length == 0:         # If the message starts with "0x" and has less than 4 characters
            mosi_8bits = [int(mosi, 16)]                                         # Reads message as integer in base 16                                                                                             
            return mosi_8bits                                                    # Return the message
        elif mosi[:2] == '0x' and 2 < len(mosi) <= 6 and bits_length == 1:       # If the message starts with "0x" and has less than 6 characters
            mosi = int(mosi, 16)                                                 # Reads message as integer in base 16                                                                                          
            mosi_16bits = [int(hex(mosi >> 8),16)]                               # Create 2-position vector to split 16-bit word, containing 1 byte
            mosi_16bits.append(int(hex(mosi & 0xFF),16))                         # Add second byte
            return mosi_16bits                                                   # Return the message
        else:                                                                    # Else
            self.error_message('Enter a message in hexadecimal format 0x0000 for 16 bits or 0x00 for 8 bits')  # Display error message
            mosi = 'Invalid input'                                               # Display error message on output
            return mosi                                                          # Return error message
    
    def reverse_bits(self, byte):
        # This function reverse the sequece of 16 or 8 bits word
        byte = ((byte & 0x5555) << 1) | ((byte & 0xAAAA) >> 1)                  # Reverse double bits
        byte = ((byte & 0x3333) << 2) | ((byte & 0xCCCC) >> 2)                  # Reverse bit quad
        byte = ((byte & 0x0F0F) << 4) | ((byte & 0xF0F0) >> 4)                  # Change the sequence of the bit quad 
        return byte                                                             # Return the reverse word
     
    def error_message(self, text):
        # This function call a message pop-up
        warning = QMessageBox(SPI_Communication)                                # Create message box
        warning.setWindowTitle("Warning")                                       # Message box title
        warning.setText(text)                                                   # Message box text
        warning.setIcon(QMessageBox.Warning)                                    # Message box icon
        warning.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        warning.setStandardButtons(QMessageBox.Yes)                             # Message box Button
        option_ok = warning.button(QMessageBox.Yes)                             # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        warning.exec_()                                                         # Message box execution
        
    def info_send(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("The message to be sent to the slave by the Raspberry Pi must be in hexadecimal, in the format 0x0000 for 16 bits per word or 0x00 for 8 bits per word")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution

    def info_output(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("The message sent by the slave to the Raspberry Pi will be represented in hexadecimal. Note that in some peripheral equipment the SPI responses are delayed, that is, the message of interest will only appear after successive communications (Intan RHD2000 chips respond with 2 delay messages)")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution

    def info_bus(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("The Raspberry Pi 3B+/4 has two sets of SPI communication ports (for more information type 'pinout' in Terminal):\n\n - SPI0: MOSI (pin 19), MISO (pin 21), SCLK (pin 23) , CS0 (pin 24) and CS1 (pin 26)\n - SPI1: MOSI (pin 38), MISO (pin 35), SCLK (pin 40), CS0 (pin 36), CS1 (pin 11) and CS2 (pin 36)")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution

    def info_significant_bit(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("The communication can be done by the Raspberry Pi in two ways, sending the bit in the position of highest value first (MSB) or sending the bit in position of least value first (LSB)")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution

    def info_bits_word(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("Word, in computing, is the basic unit of information in binary. Thus, the number of bits per word is the number of bits to be sent in each communication")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution
        
    def info_clock_frequency(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("Clock frequency is the number of cycles per second of the sync signal used by the SPI communication driver.")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution

    def info_mode(self):
        # This function call a message pop-up
        info = QMessageBox(SPI_Communication)                                   # Create message box
        info.setWindowTitle("Information")                                      # Message box title
        info.setText("SPI communication can take 4 modes depending on the so called clock phase and polarity:\n - 0: polarity 0 and phase 0\n - 1: polarity 0 and phase 1\n - 2: polarity 1 and phase 0\n - 3: polarity 1 and phase 1")   # Message box text
        info.setIcon(QMessageBox.Information)                                   # Message box icon
        info.setStyleSheet("QMessageBox{background:#353535;}QLabel{color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt/Century Gothic/;font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")   # Pop-up style
        info.setStandardButtons(QMessageBox.Yes)                                # Message box Button
        option_ok = info.button(QMessageBox.Yes)                                # Define "yes" button
        option_ok.setText('    OK    ')                                         # Rename "yes" buton
        info.exec_()                                                            # Message box execution    

    def resource_path(self, relative_path):
        # This function search the correct path to build the insterface images (pulled from the internet)
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path =os.path.abspath(".")
        return os.path.join(base_path, relative_path)
            

# Interface execution (Generated by QtDesigner)
if __name__ == "__main__":
    # This structure run the insterface
    QtWidgets.QApplication.setStyle("fusion")                                   # Adapt the interface layout to Linux
    app = QtWidgets.QApplication(sys.argv)                                      # Set the application variable
    SPI_Communication = QtWidgets.QMainWindow()                                 # Define the main window
    ui = Ui_SPI_Communication()                                                 # Set the UI variable
    ui.setupUi(SPI_Communication)                                               # Define UI setup
    SPI_Communication.show()                                                    # Show the interface
    sys.exit(app.exec_())                                                       # Exit function
    
'''
INTERFACE PRODUCTION OBSERVATIONS

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
    1. Open the Terminal
    2. Go to the "boot" directory: cd /boot
    3. Open the "config.txt": sudo nano config.txt
    4. Insert two lines on the text: "core_freq=500" and "core_freq_min=500"
    5. Save it: "Ctrl+X", "s" and "Enter"
    6. Reboot the system
    
- Turn ON the SPI1 bus: the pins referring to the SPI 1 bus are natively 
turned off, so it is necessary to turn them on through the "config.txt" file:
    1. Open the Terminal
    2. Go to the "boot" directory: cd /boot
    3. Open the "config.txt": sudo nano config.txt
    4. Insert one line on the text: "dtoverlay=spi1-1cs"
    5. Save it: "Ctrl+X", "s" and "Enter"
    6. Reboot the system
    
- Layout deconfiguration in linux: when transferring the windows interface 
(where it was conceived) to linux, some elements were misconfigured. To solve 
this, we manually repositioned some labels and used the function below
    1. QtWidgets.QApplication.setStyle("fusion")

- Executable file: to make an executable file from the .py code it is 
necessary to use the PyInstaller library and attach the interface images in the 
executable creation directory. For that, the command "pyinstaller --windowed 
--onefile program.py" is used, the function research_path( ) removed from the 
internet and a modification in the file ".spec" generated after the process of 
building the executable. 
'''