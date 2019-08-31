import socket
import json
import config

SOCKET_MAP = {
    config.WALL_LIGHT_SOCKET: 4,
    config.BED_LIGHT_SOCKET: 3,
    config.MUSIC_POWER_SOCKET: 2,
    config.MONITOR_POWER_SOCKET: 5
}

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect((config.IP, config.RF_PORT))


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
            "State": self.state
        }
        tcp_sock.sendall(json.dumps(msg).encode())
