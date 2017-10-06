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
        self.port = find_port(substr)
        self.disabled = self.port == None
        self.listen = False
        
    def set_listen(self, lis):
        self.listen = lis
        
    def is_listening(self):
        return self.listen
    
    def is_disabled(self):
        return self.disabled
    
    def run(self):
        if self.disabled:
            return
            
        self.ser = serial.Serial(self.port, 9600, timeout=0)
        
        while True:
            if self.ser.inWaiting() and self.listen:
                msg = self.ser.readline(s.inWaiting())
                self.queue.put(msg)

