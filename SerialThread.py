import pip
pip.main(["install", "pyserial"])

import serial
import serial.tools.list_ports
import threading
import Queue
import time


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
        self.port = find_port(substr)
        self.disabled = self.port == None
        self.listen = False
        
    def set_listen(self, lis):
        self.listen = lis
        
    def is_listening(self):
        return self.listen
    
    def is_disabled(self):
        return self.disabled

    def stop(self):
        if __debug__:
            print "Stopping thread"
        self.disabled = True
    
    def run(self):
        if not self.disabled:
            self.ser = serial.Serial(self.port, 9600, timeout=0)
        
        while not self.disabled:
            if self.ser.inWaiting():
                msg = self.ser.readline(self.ser.inWaiting())
                if self.listen:
                    self.queue.put(msg)
            time.sleep(0.75)

