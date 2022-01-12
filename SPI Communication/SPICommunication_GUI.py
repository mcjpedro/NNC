# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SPICommunication_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPI_Communication(object):
    def setupUi(self, SPI_Communication):
        SPI_Communication.setObjectName("SPI_Communication")
        SPI_Communication.resize(471, 296)
        SPI_Communication.setWindowTitle("SPI Communication - Raspberry Pi")
        SPI_Communication.setStyleSheet("QMainWindow{background-color:#4B4B4B;color:#FFFFFF;}")
        self.main_window = QtWidgets.QWidget(SPI_Communication)
        self.main_window.setStyleSheet("QWidget{    background-color:#353535;}")
        self.main_window.setObjectName("main_window")
        self.gridLayout = QtWidgets.QGridLayout(self.main_window)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll_area = QtWidgets.QScrollArea(self.main_window)
        self.scroll_area.setStyleSheet("QScrollArea{border:0px}QScrollBar:vertical{background:#353535;width:5px}QScrollBar::handle:vertical{background:#2C53A1;min-width:20px;}QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:#353535;}QScrollBar:horizontal{background:#353535;height:5px}QScrollBar::handle:horizontal{background:#2C53A1;min-width:20px;}QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{background:#353535;}")
        self.scroll_area.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll = QtWidgets.QWidget()
        self.scroll.setGeometry(QtCore.QRect(0, 0, 453, 278))
        self.scroll.setObjectName("scroll")
        self.communcation = QtWidgets.QFrame(self.scroll)
        self.communcation.setGeometry(QtCore.QRect(30, 0, 391, 271))
        self.communcation.setStyleSheet("QLabel{}QCheckBox{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}QCheckBox::indicator{width:15px;height:15px;background-color:#606060;border-radius:4px;}QCheckBox::indicator:checked{background-color:#A21F27;}")
        self.communcation.setObjectName("communcation")
        self.send_message = QtWidgets.QPushButton(self.communcation)
        self.send_message.setGeometry(QtCore.QRect(160, 200, 71, 21))
        self.send_message.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_message.setStyleSheet("QPushButton{font:10pt\"Century Gothic\";font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")
        self.send_message.setText("SEND")
        self.send_message.setObjectName("send_message")
        self.significant_bit = QtWidgets.QComboBox(self.communcation)
        self.significant_bit.setGeometry(QtCore.QRect(150, 110, 71, 16))
        self.significant_bit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.significant_bit.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.significant_bit.setCurrentText("MSB")
        self.significant_bit.setObjectName("significant_bit")
        self.significant_bit.addItem("MSB")
        self.significant_bit.addItem("LSB")
        self.label_1 = QtWidgets.QLabel(self.communcation)
        self.label_1.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_1.setStyleSheet("QLabel{color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}")
        self.label_1.setText("SETTINGS")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_0 = QtWidgets.QLabel(self.communcation)
        self.label_0.setGeometry(QtCore.QRect(10, 0, 291, 21))
        self.label_0.setStyleSheet("QLabel{color:#FFFFFF;font:14pt\"Century Gothic\";font-weight:bold;}")
        self.label_0.setText("SPI Communication")
        self.label_0.setObjectName("label_0")
        self.label_2 = QtWidgets.QLabel(self.communcation)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 118, 16))
        self.label_2.setStyleSheet("QLabel{color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}")
        self.label_2.setText("COMMUNICATION")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QFrame(self.communcation)
        self.image.setGeometry(QtCore.QRect(240, 0, 151, 161))
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.image_nnc = QtWidgets.QLabel(self.image)
        self.image_nnc.setGeometry(QtCore.QRect(20, 20, 111, 141))
        self.image_nnc.setText("")
        self.image_nnc.setPixmap(QtGui.QPixmap("images/NNC_logo.png"))
        self.image_nnc.setScaledContents(True)
        self.image_nnc.setAlignment(QtCore.Qt.AlignCenter)
        self.image_nnc.setObjectName("image_nnc")
        self.line_1 = QtWidgets.QFrame(self.communcation)
        self.line_1.setGeometry(QtCore.QRect(10, 146, 231, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.communcation)
        self.line_2.setGeometry(QtCore.QRect(10, 230, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.communcation)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 231, 11))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.bus = QtWidgets.QComboBox(self.communcation)
        self.bus.setGeometry(QtCore.QRect(150, 50, 71, 16))
        self.bus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bus.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.bus.setCurrentText("SPI0")
        self.bus.setObjectName("bus")
        self.bus.addItem("SPI0")
        self.bus.addItem("SPI1")
        self.bits_word = QtWidgets.QComboBox(self.communcation)
        self.bits_word.setGeometry(QtCore.QRect(150, 90, 71, 16))
        self.bits_word.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bits_word.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.bits_word.setCurrentText("8")
        self.bits_word.setObjectName("bits_word")
        self.bits_word.addItem("8")
        self.bits_word.addItem("16")
        self.message = QtWidgets.QLineEdit(self.communcation)
        self.message.setGeometry(QtCore.QRect(10, 200, 141, 20))
        self.message.setStyleSheet("QLineEdit{border:#969696;background-color:#606060;border-radius:6px;color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}")
        self.message.setText("Type here")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setDragEnabled(False)
        self.message.setReadOnly(False)
        self.message.setObjectName("message")
        self.saida = QtWidgets.QLineEdit(self.communcation)
        self.saida.setGeometry(QtCore.QRect(240, 200, 141, 20))
        self.saida.setStyleSheet("QLineEdit{border:#969696;background-color:#606060;border-radius:6px;color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;}")
        self.saida.setText("0x0000")
        self.saida.setAlignment(QtCore.Qt.AlignCenter)
        self.saida.setDragEnabled(False)
        self.saida.setReadOnly(True)
        self.saida.setObjectName("saida")
        self.msg_significant_bit = QtWidgets.QPushButton(self.communcation)
        self.msg_significant_bit.setGeometry(QtCore.QRect(20, 110, 89, 16))
        self.msg_significant_bit.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_significant_bit.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_significant_bit.setText("Bit send sequence")
        self.msg_significant_bit.setObjectName("msg_significant_bit")
        self.msg_bus = QtWidgets.QPushButton(self.communcation)
        self.msg_bus.setGeometry(QtCore.QRect(20, 50, 96, 16))
        self.msg_bus.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_bus.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_bus.setText("Communication bus")
        self.msg_bus.setObjectName("msg_bus")
        self.msg_bits_word = QtWidgets.QPushButton(self.communcation)
        self.msg_bits_word.setGeometry(QtCore.QRect(20, 90, 67, 16))
        self.msg_bits_word.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_bits_word.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_bits_word.setText("Bits per word")
        self.msg_bits_word.setObjectName("msg_bits_word")
        self.msg_send_message = QtWidgets.QPushButton(self.communcation)
        self.msg_send_message.setGeometry(QtCore.QRect(20, 180, 121, 20))
        self.msg_send_message.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_send_message.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_send_message.setText("Message to be sent")
        self.msg_send_message.setObjectName("msg_send_message")
        self.msg_output = QtWidgets.QPushButton(self.communcation)
        self.msg_output.setGeometry(QtCore.QRect(250, 180, 121, 20))
        self.msg_output.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_output.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_output.setText("Message received")
        self.msg_output.setObjectName("msg_output")
        self.clear = QtWidgets.QPushButton(self.communcation)
        self.clear.setGeometry(QtCore.QRect(300, 240, 81, 21))
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("QPushButton{font:14pt\"Century Gothic\";font-weight:bold;}QPushButton{border:2px solid #A21F27;border-radius:8px;background-color:#2C53A1;color:#FFFFFF;font:10pt\"Century Gothic\";font-weight:bold;}QPushButton:pressed{border:2px solid #A21F27;border-radius:8px;background-color:#A21F27;color:#FFFFFF;}")
        self.clear.setText("CLEAR")
        self.clear.setObjectName("clear")
        self.mode = QtWidgets.QComboBox(self.communcation)
        self.mode.setGeometry(QtCore.QRect(150, 70, 71, 16))
        self.mode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mode.setStyleSheet("QComboBox{color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#969696;border:0px;}QListView{color:#FFFFFF;font:8pt\"Century Gothic\";font-weight:bold;background-color:#606060;border:0px;border-radius:6px;}QComboBox::drop-down{width:20px;border:5px;}QComboBox::down-arrow{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #FFFFFF;width:0.5px;height:1px;border-radius:2px;}QComboBox::down-arrow:hover{border-left:2px solid none;border-right:2px solid none;border-top:2px solid #A21F27;width:0.5px;height:1px;border-radius:2px;}QAbstractItemView{border:2px solid #969696;selection-background-color:#2C53A1;}")
        self.mode.setCurrentText("0")
        self.mode.setObjectName("mode")
        self.mode.addItem("0")
        self.mode.addItem("1")
        self.mode.addItem("2")
        self.mode.addItem("3")
        self.msg_mode = QtWidgets.QPushButton(self.communcation)
        self.msg_mode.setGeometry(QtCore.QRect(20, 70, 48, 16))
        self.msg_mode.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_mode.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_mode.setText("SPI mode")
        self.msg_mode.setObjectName("msg_mode")
        self.msg_clock_frequency = QtWidgets.QPushButton(self.communcation)
        self.msg_clock_frequency.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.msg_clock_frequency.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.msg_clock_frequency.setStyleSheet("QPushButton{border:0px solid;background-color:#353535;color:#FFFFFF;font:7pt\"Century Gothic\";font-weight:bold;}")
        self.msg_clock_frequency.setText("Clock frequency")
        self.msg_clock_frequency.setObjectName("msg_clock_frequency")
        self.clock_frequency = QtWidgets.QComboBox(self.communcation)
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
        self.scroll_area.setWidget(self.scroll)
        self.gridLayout.addWidget(self.scroll_area, 0, 0, 1, 1)
        SPI_Communication.setCentralWidget(self.main_window)
        
        self.significant_bit.setCurrentIndex(0)
        self.bus.setCurrentIndex(0)
        self.bits_word.setCurrentIndex(0)
        self.mode.setCurrentIndex(0)
        self.clock_frequency.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SPI_Communication)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SPI_Communication = QtWidgets.QMainWindow()
    ui = Ui_SPI_Communication()
    ui.setupUi(SPI_Communication)
    SPI_Communication.show()
    sys.exit(app.exec_())