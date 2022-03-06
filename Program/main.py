from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app=QtWidgets.QApplication([])
ui = uic.loadUi("GUI.ui")


serial = QSerialPort()
serial.setBaudRate(115200)
def updateCOMlist():
    COMPortList = []
    ports=QSerialPortInfo().availablePorts()
    for port in ports:
        COMPortList.append(port.portName())
    print(COMPortList)
    if (not COMPortList):
        ui.openCOM.setEnabled(False)
        ui.closeCOM.setEnabled(False)
    else:
        ui.openCOM.setEnabled(True)
        ui.closeCOM.setEnabled(True)

    ui.listCOM.addItems(COMPortList)
updateCOMlist()
ui.pushButton_UPD_COM.clicked.connect(updateCOMlist)

listCOM_Steps=["100","200","300","400","500"]
ui.listCOM_Steps.addItems(listCOM_Steps)

def openCOM():
    serial.setPortName(ui.listCOM.currentText())
    serial.open(QIODevice.ReadWrite)
    ui.listCOM.setEnabled(False)

def clsoeCOM():
    serial.close()
    ui.listCOM.setEnabled(True)

ui.openCOM.clicked.connect(openCOM)
ui.closeCOM.clicked.connect(clsoeCOM)

flag=True
def readCOM():
    global flag
    rx = serial.readLine()
    if flag:
        rx=rx[1:]
        flag=False
    rxs = str(rx, 'utf-8')#.strip()
    print(rxs)

def sendData(val1, val2):
    print("sendData>",end='')
    sval=""
    sval += str(val1)
    sval += " "
    sval += str(val2)
    sval += " "
    sval += ui.listCOM_Steps.currentText()
    print(sval)
    serial.write(sval.encode())

serial.readyRead.connect(readCOM)

def buttonA1():
    print("Button A1")
    sendData('A',1)

def buttonA2():
    print("Button A2")
    sendData('A',2)

ui.pushButton_A1.clicked.connect(buttonA1)
ui.pushButton_A2.clicked.connect(buttonA2)

def buttonB1():
    print("Button B1")
    sendData('B',1)

def buttonB2():
    print("Button B2")
    sendData('B',2)

ui.pushButton_B1.clicked.connect(buttonB1)
ui.pushButton_B2.clicked.connect(buttonB2)

def buttonC1():
    print("Button C1")
    sendData('C',1)

def buttonC2():
    print("Button C2")
    sendData('C',2)

ui.pushButton_C1.clicked.connect(buttonC1)
ui.pushButton_C2.clicked.connect(buttonC2)

def buttonD1():
    print("Button D1")
    sendData('D',1)

def buttonD2():
    print("Button D2")
    sendData('C',2)

ui.pushButton_D1.clicked.connect(buttonD1)
ui.pushButton_D2.clicked.connect(buttonD2)

ui.show()
app.exec()