import socket
import json


SOCKET_MAP = {
    "Wall Light": 4,
    "Bed Light": 3,
    "Music Power": 2,
    "Monitor Power": 5
}
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class ESocket:

    def __init__(self, name):
        self.name = name
        self.id = SOCKET_MAP[name]
        self.state = 0

    def __str__(self):
        return "<%s>" % self.name

    def toggle(self):
        if self.state:
            self.turn_off()
        else:
            self.turn_on()

    def turn_on(self):
        self.state = 1
        self.trigger()

    def turn_off(self):
        self.state = 0
        self.trigger()

    def trigger(self):
        print("%s set to %s" % (self, self.state))
        msg = {
            "Socket": self.id,
            "state": self.state
        }
        tcp_sock.connect(("192.168.2.10", 5005))
        tcp_sock.sendall(json.dumps(msg))
        tcp_sock.close()
