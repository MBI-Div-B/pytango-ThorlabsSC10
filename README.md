# ThorlabsSC10 Tango device server

This a Tango device server written in PyTango for a Thorlabs SC10 shutter controller.

## Installation

Currently [InstrumentKit](https://github.com/Galvant/InstrumentKit) is used for communication via serial. This might be changed in future.
In order to make InstrumentKit run properly with the SC10, the is a small bug fix applied - so use the according fork+branch:

    git clone --branch stripread https://github.com/MBI-Div-B/InstrumentKit.git
    cd InstrumentKit
    pip3 install -e .

## Authors
* Daniel Schick


