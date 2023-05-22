# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalGui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(994, 631)
        self.Ingroup = QGroupBox(Form)
        self.Ingroup.setObjectName(u"Ingroup")
        self.Ingroup.setGeometry(QRect(30, 120, 231, 121))
        self.OutRadio = QRadioButton(self.Ingroup)
        self.OutRadio.setObjectName(u"OutRadio")
        self.OutRadio.setGeometry(QRect(20, 30, 82, 17))
        self.OutRadio.setChecked(False)
        self.InRadio = QRadioButton(self.Ingroup)
        self.InRadio.setObjectName(u"InRadio")
        self.InRadio.setGeometry(QRect(20, 80, 82, 17))
        self.InRadio.setChecked(True)
        self.InConfig = QGroupBox(Form)
        self.InConfig.setObjectName(u"InConfig")
        self.InConfig.setEnabled(False)
        self.InConfig.setGeometry(QRect(270, 190, 291, 51))
        self.PullRadio = QRadioButton(self.InConfig)
        self.PullRadio.setObjectName(u"PullRadio")
        self.PullRadio.setGeometry(QRect(10, 20, 82, 17))
        self.HighImpRadio = QRadioButton(self.InConfig)
        self.HighImpRadio.setObjectName(u"HighImpRadio")
        self.HighImpRadio.setGeometry(QRect(160, 20, 82, 17))
        self.outConfig = QGroupBox(Form)
        self.outConfig.setObjectName(u"outConfig")
        self.outConfig.setEnabled(False)
        self.outConfig.setGeometry(QRect(270, 130, 271, 51))
        self.HighRadio = QRadioButton(self.outConfig)
        self.HighRadio.setObjectName(u"HighRadio")
        self.HighRadio.setGeometry(QRect(10, 20, 82, 17))
        self.LowRadio = QRadioButton(self.outConfig)
        self.LowRadio.setObjectName(u"LowRadio")
        self.LowRadio.setGeometry(QRect(160, 20, 82, 17))
        self.Gbtn = QPushButton(Form)
        self.Gbtn.setObjectName(u"Gbtn")
        self.Gbtn.setGeometry(QRect(330, 270, 75, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 250, 81, 16))
        self.path = QLineEdit(Form)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(30, 270, 291, 31))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 371, 81))
        self.portselection = QComboBox(self.groupBox)
        self.portselection.addItem("")
        self.portselection.addItem("")
        self.portselection.addItem("")
        self.portselection.addItem("")
        self.portselection.setObjectName(u"portselection")
        self.portselection.setGeometry(QRect(10, 40, 121, 22))
        self.pinselection = QComboBox(self.groupBox)
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.addItem("")
        self.pinselection.setObjectName(u"pinselection")
        self.pinselection.setGeometry(QRect(180, 40, 69, 22))
        self.portlabel = QLabel(self.groupBox)
        self.portlabel.setObjectName(u"portlabel")
        self.portlabel.setGeometry(QRect(10, 20, 47, 13))
        self.pinlabel = QLabel(self.groupBox)
        self.pinlabel.setObjectName(u"pinlabel")
        self.pinlabel.setGeometry(QRect(190, 20, 47, 13))
        self.fileName = QLineEdit(Form)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(30, 340, 381, 31))
        self.loadBtn = QPushButton(Form)
        self.loadBtn.setObjectName(u"loadBtn")
        self.loadBtn.setGeometry(QRect(330, 380, 81, 31))
        self.saveBtn = QPushButton(Form)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(220, 380, 91, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 320, 47, 13))

        self.retranslateUi(Form)
        # self.OutRadio.clicked.connect(self.InConfig.setDisabled)
        # self.OutRadio.clicked.connect(self.outConfig.setEnabled)
        # self.InRadio.clicked.connect(self.InConfig.setEnabled)
        # self.InRadio.clicked.connect(self.OutRadio.setDisabled)
        # self.Gbtn.clicked.connect(Form.close)
        QObject.connect(self.OutRadio,SIGNAL("clicked(bool)"),self.InConfig.setDisabled)
        QObject.connect(self.OutRadio,SIGNAL("clicked(bool)"),self.outConfig.setEnabled)
        QObject.connect(self.InRadio,SIGNAL("clicked(bool)"),self.outConfig.setDisabled)
        QObject.connect(self.InRadio,SIGNAL("clicked(bool)"),self.InConfig.setEnabled)
        self.Gbtn.clicked.connect(self.GenerateFunction)

        self.saveBtn.clicked.connect(self.SaveFunction)
        self.loadBtn.clicked.connect(self.LoadFunction)
       
        self.portselection.highlighted.connect(self.UpdatingPins)
        self.pinselection.highlighted.connect(self.UpdatingPins)
        self.portselection.currentIndexChanged.connect(self.updateHandle)
        self.pinselection.currentIndexChanged.connect(self.updateHandle)
        
        
        
        
        
        QMetaObject.connectSlotsByName(Form)


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Ingroup.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.OutRadio.setText(QCoreApplication.translate("Form", u"Output", None))
        self.InRadio.setText(QCoreApplication.translate("Form", u"Input", None))
        self.InConfig.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullRadio.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.HighImpRadio.setText(QCoreApplication.translate("Form", u"High Impedence", None))
        self.outConfig.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.HighRadio.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowRadio.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Gbtn.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.path.setText(QCoreApplication.translate("Form", u"Enter Path to add output file", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"config", None))
        self.portselection.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.portselection.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.portselection.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.portselection.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.pinselection.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.pinselection.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.pinselection.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.pinselection.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.pinselection.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.pinselection.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.pinselection.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.pinselection.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))

        self.portlabel.setText(QCoreApplication.translate("Form", u"Port", None))
        self.pinlabel.setText(QCoreApplication.translate("Form", u"Pin", None))
        self.loadBtn.setText(QCoreApplication.translate("Form", u"Load", None))
        self.saveBtn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"File Name", None))
    # retranslateUi
      # self.OutRadio.clicked.connect(self.InConfig.setDisabled)
        # self.OutRadio.clicked.connect(self.outConfig.setEnabled)
        # self.InRadio.clicked.connect(self.InConfig.setEnabled)
        # self.InRadio.clicked.connect(self.OutRadio.setDisabled)
    def updateHandle(self):
      if (PortSele[self.portselection.currentText()][1][self.pinselection.currentText()].strip() == "DIO_HIGH"):
        self.OutRadio.setChecked(True)
        self.InConfig.setDisabled(True)
        self.outConfig.setEnabled(True)
        self.HighRadio.setChecked(True)
      
      elif (PortSele[self.portselection.currentText()][1][self.pinselection.currentText()].strip() == "DIO_LOW"):
        self.OutRadio.setChecked(True)
        self.InConfig.setDisabled(True)
        self.outConfig.setEnabled(True)
        self.LowRadio.setChecked(True)
        
      elif (PortSele[self.portselection.currentText()][1][self.pinselection.currentText()].strip() == "DIO_HIGH_IMPEDANCE"):
        self.InRadio.setChecked(True)
        self.InConfig.setEnabled(True)
        self.outConfig.setDisabled(True)
        self.HighImpRadio.setChecked(True)
      
      else:
        self.InRadio.setChecked(True)
        self.InConfig.setEnabled(True)
        self.outConfig.setDisabled(True)
        self.PullRadio.setChecked(True)
      return
      
      
    def GenerateFunction(self):
      self.UpdatingPins()
      if self.path.text() != '':
        File_Handler = open(self.path.text() + '\DIO.h', 'w')
        File_CHandler = open(self.path.text() + '\DIO_config.h', 'w')
      else:
        File_CHandler = open('DIO_config.h', 'w')
        File_Handler = open('DIO.h', 'w')
        
      File_Handler.write("#ifndef DIO_H\n")
      File_Handler.write("#define DIO_H\n\n\n")
      File_Handler.write("#define DIO_IN                   0\n")
      File_Handler.write("#define DIO_OUT                  1\n\n")
      File_Handler.write("#define DIO_PULL_UP              1\n")
      File_Handler.write("#define DIO_HIGH_IMPEDANCE       0\n\n")
      File_Handler.write("#define DIO_HIGH                 1\n")
      File_Handler.write("#define DIO_LOW                  0\n\n")
      File_Handler.write("#endif\n")
      File_Handler.close()
      
      File_CHandler.write("#ifndef _DIO_CONFIG_H\n")
      File_CHandler.write("#define _DIO_CONFIG_H\n")
      File_CHandler.write("\n")
      File_CHandler.write("\n")
      
      for port in PortSele:
        for pin in PortSele[port][1]:
          if PortSele[port][1][pin].strip() == "DIO_HIGH" or PortSele[port][1][pin].strip() == "DIO_LOW":
            File_CHandler.write('#define DIO_'+PortSele[port][0]+'_'+pin+'        '+"DIO_OUT\n")
          else:
            File_CHandler.write('#define DIO_'+PortSele[port][0]+'_'+pin+'        '+"DIO_IN\n")
      
      File_CHandler.write('\n\n\n')
      
      for port in PortSele:
        for pin in PortSele[port][1]:
            File_CHandler.write('#define DIO_'+port+'_'+pin+'     '+PortSele[port][1][pin])
      
      File_CHandler.write("#endif /_DIO_CONFIG_H/\n")
      File_CHandler.close()
      return
      
      
      
    def SaveFunction(self):
      self.UpdatingPins()
      if self.fileName.text() != '':
        ConfigFileName = self.fileName.text()
      else:
        ConfigFileName = 'DefaultConfig.txt'
      SaveFile = open(ConfigFileName, 'w')
      for port in PortSele:
        for pin in PortSele[port][1]:
          SaveFile.write('\n'+port + ' ' + pin + ' ' + PortSele[port][1][pin])
      SaveFile.close()
      return
      
      
      
    def LoadFunction(self):
      if self.fileName.text() != '':
        ConfigFileName = self.fileName.text()
      else:
        return
      LoadFile = open(ConfigFileName,'r')
      for line in LoadFile:
        configList = line.split()
        PortSele[configList[0]][1][configList[1]] = configList[2]
      self.updateHandle()
      LoadFile.close()
      return
      
      
    def UpdatingPins(self): 
      if self.OutRadio.isChecked():
        if self.HighRadio.isChecked():
          PortSele[self.portselection.currentText()][1][self.pinselection.currentText()]="DIO_HIGH\n"
        else:
          PortSele[self.portselection.currentText()][1][self.pinselection.currentText()]="DIO_LOW\n"

      else:
        if self.PullRadio.isChecked():
          PortSele[self.portselection.currentText()][1][self.pinselection.currentText()]="DIO_PULL_UP\n"
        else:
          PortSele[self.portselection.currentText()][1][self.pinselection.currentText()]="DIO_HIGH_IMPEDANCE\n"
      return


#Dictionaries that save pin values
PORTA={"PIN0":"DIO_PULL_UP\\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTB={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTC={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTD={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PortSele = {"PORTA": ["DDRA",PORTA], "PORTB": ["DDRB",PORTB], "PORTC": ["DDRC",PORTC], "PORTD": ["DDRD",PORTD]}


app=QApplication(sys.argv) 
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
