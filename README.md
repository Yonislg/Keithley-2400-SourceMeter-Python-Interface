# Keithley 2400 SourceMeter Trace Buffer extraction Python Library 
This repo contains a python class which allows for python-based extraction of the Keithley 2400 SourceMeter trace buffer. The reason why only data extraction is performed and not device control is because the temporal resolution of measurements with a serial connection are very low. This GUI was specially designed for simple collection of Langmuir Probe Measurements at the PlasmaTEC laboratory of the Tecnólogicio of Costa Rica.

When clicking on trace_gui.exe a simple GUI pops up giving the user the ability to:
-specifiy the communication port
-save the trace data under a specified file name
-choose between .csv and .txt format


The original repository on which this is based contains a Keithley class opens a serial connection to the device through an RS232 port using the keithley_serial module. The maximum measurement resolution is about 30 Hz while the Keithley 2400 is capable of over 500 hz in manual operation.
Implemented so far is ability to:
- configure setup parameters
- configure biasing/current parameters
- configure measurements parameters
- define and configure voltage sweeps
- send general commands (given in Keithley manual)
- collect data from Keithley

Requires the pyqtgraph and numpy packages.

