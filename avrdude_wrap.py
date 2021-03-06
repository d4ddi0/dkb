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
from os import path


def avrdude_passthrough():
    # prepare argument parser to understand -P PORT
    parser = argparse.ArgumentParser()
    parser.add_argument("-P", dest="port")
    # parse only known parameters
    args = parser.parse_known_args()

    if not args[0].port:
        print("Error: no port supplied")
        sys.exit(1)

    if path.exists(args[0].port):
        reset_avr(args[0].port)
        count_sleep(1.5) # wait 1.5 second to ensure Arduino is ready
    else:
        print(f'{args[0].port} not found. Plug in or reset Microcontroller')
        if not count_sleep(5, test_func=lambda: path.exists(args[0].port)):
            print(f'Error: port {args[0].port} not present')
            exit(1)

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


def count_sleep(seconds, increment=0.25, test_func=lambda: False):
    sleepytime = seconds
    print(f'wait {seconds} seconds', end='')
    while sleepytime > 0:
        if test_func():
            return True
        print('.', end='', flush=True)
        time.sleep(increment)
        sleepytime -= increment
    print('')
    return False

if __name__ == '__main__':
   exit(avrdude_passthrough())
