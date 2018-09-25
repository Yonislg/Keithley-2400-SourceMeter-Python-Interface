#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Keithley GUI

This script runs a GUI to extract date from the
trace buffer of the Keithley 2400 SourceMeter.

This GUI implmentation was originally inspired by the
keithley_gui on github by T. Max Robberts

author: Yonis le Grand
"""

import sys, time
from pyqtgraph.Qt import QtGui, QtCore
import keithley_control as kc
import csv

class Keithley_GUI(QtGui.QMainWindow):
    connected = False
    def __init__(self):
        super(Keithley_GUI, self).__init__()
        print("hey")

        #self.initKeithley(port, connected=connected)
        self.initUI()

    def initKeithley(self, port):
        #if connected:
        self.keithley = kc.Keithley(port)
        if self.keithley.keithleyExists == True:
            self.connected = True
        #else:
        #    self.keithley = kc.FakeKeithley()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.main_widget = QtGui.QWidget(self)
        self.main_widget.setLayout(grid)
        self.setCentralWidget(self.main_widget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy = QtGui.QSizePolicy()
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Here we define the buttons and inputs

        hbox = QtGui.QHBoxLayout()
        #hbox.addWidget(self.output)
        grid.addLayout(hbox, 0, 0)


        ### Establish Connection ###
        connectButton = QtGui.QPushButton("Connect")
        connectButton.clicked.connect(self.buttonClicked)
        grid.addWidget(connectButton, 0, 0)

        ### Connection Port ###
        self.connectPort = QtGui.QLineEdit('COM_PORT')
        self.connectPort.returnPressed.connect(connectButton.click)
        grid.addWidget(self.connectPort, 0, 1)

        ### Trace data button ###
        traceButton = QtGui.QPushButton("trace")
        traceButton.clicked.connect(self.buttonClicked)
        grid.addWidget(traceButton, 1, 0)

        ### Savefile name ###
        self.saveFile = QtGui.QLineEdit('desired_filename')
        self.saveFile.returnPressed.connect(traceButton.click)
        grid.addWidget(self.saveFile, 1, 1)

        ### Dropdown list ###
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem(".csv")
        self.comboBox.addItem(".txt")
        grid.addWidget(self.comboBox, 1, 2)

        ##############################################
        #############  Overall Layout ################
        ##############################################

        self.statusBar()

        #self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Keithley Controller')
        self.show()

    def buttonClicked(self):

        sender = self.sender()

        if sender.text() == "Connect":
            self.initKeithley(self.connectPort.text())
            time.sleep(.5)
            if self.keithley.keithleyExists == False:
                QtGui.QMessageBox.warning(self,'Message',
                                          'Port name incorrect. Could not establish connection.',
                                          QtGui.QMessageBox.Ok)
                #Write a warning that there is no valid connection
                del self.keithley
            else:
                print "Keithley Initialized"

        if sender.text() == "trace":
            #if self.connected == True:
            # trace_data = trace_data.replace(' ', '').split(',')
            csvfile = self.saveFile.text() + self.comboBox.currentText()
            if self.connected == True:
                trace_data = kc.better_parsing(self.keithley.trace_data())
                print(trace_data)
                with open(csvfile, "w") as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerow(['Time', 'Volts', 'Amps'])
                    writer.writerows(zip(*trace_data))
            else:
                print csvfile
                QtGui.QMessageBox.warning(self,'Message',
                                          'No established connection. Please connect to the correct port first.',
                                          QtGui.QMessageBox.Ok)


    """  Make sure to close the serial connection before exit """

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.keithley.set_output_off()
            time.sleep(.25)
            self.keithley.close_serial()
            time.sleep(.25)
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication([])
ex = Keithley_GUI()  ##### CHANGE THIS TO TRUE!!!
sys.exit(app.exec_())
