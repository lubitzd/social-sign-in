import pip
pip.main(["install", "pyserial"])

import serial
import serial.tools.list_ports
import threading
import Queue


def find_port(substr):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if __debug__:
            print p
        if substr in p.description:
            if __debug__:
                print "^^^ This one (" + str(p.device) + ")"
            return str(p.device)
    return None


class SerialThread(threading.Thread):

    def __init__(self, substr, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.port = self.find_port(substr)
        
    
    
    def run(self):
        self.ser = serial.Serial(self.port, 9600, timeout=0)
#https://stackoverflow.com/questions/16938647/python-code-for-serial-data-to-print-on-window
        
        while True:
            if self.ser.inWaiting():
                msg = self.ser.readline(s.inWaiting())
                self.queue.put(msg)

