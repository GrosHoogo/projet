import socket


class Network:
    def __init__(self):
        self.interface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.110.14"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.interface.connect(self.addr)
            return self.interface.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.interface.send(str.encode(data))
            return self.interface.recv(2048).decode()
        except socket.error as e:
            print(e)