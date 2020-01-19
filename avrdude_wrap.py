#!/usr/bin/python3
""" reset an atmega32u4 and program it with a given hex file
    parsed together from bits and pieces online.
    Anyone trying to program an atmega32u4 based board is welcome to use it
"""

import sys
import subprocess
from serial import Serial, SerialException, PARITY_NONE, STOPBITS_ONE, EIGHTBITS
import argparse
import time


def avrdude_passthrough():
    # prepare argument parser to understand -P PORT
    parser = argparse.ArgumentParser()
    parser.add_argument("-P", dest="port")
    # parse only known parameters
    args = parser.parse_known_args()

    if not args[0].port:
        print("Error: no port supplied")
        sys.exit(1)

    reset_avr(args[0].port)

    count_sleep(2) # wait 2 second to ensure Arduino is ready

    avrdude_args = ['avrdude'] + args[1] + ["-P", args[0].port]
    try: # try to invoke avrdude passing all the options
        subprocess.check_call(avrdude_args)
    except subprocess.CalledProcessError as e:
        print("avrdude error:", e.output)
        sys.exit(2)


def reset_avr(ser_port):
    try: # try to initiate serial port connection on PORT with 1200 baudrate
        ser = Serial(port=ser_port, baudrate=1200, parity=PARITY_NONE,
                     stopbits=STOPBITS_ONE, bytesize=EIGHTBITS)
    except SerialException as e:
        print("pySerial error:", e)
        sys.exit(1)

    try: # try to open PORT
        ser.isOpen()
        ser.dtr=False
    except SerialException:
        print("pySerial error:", e)
        sys.exit(1)

    ser.close()


def count_sleep(seconds, increment=0.25):
    sleepytime = seconds
    print(f'wait {seconds} seconds', end='')
    while sleepytime > 0:
        print('.', end='', flush=True)
        time.sleep(increment)
        sleepytime -= increment
    print('')

if __name__ == '__main__':
   exit(avrdude_passthrough())
