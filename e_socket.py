import rf_sender

SOCKET_MAP = {
    "Wall Light": 4,
    "Bed Light": 3,
    "Music Power": 2,
    "Monitor Power": 5
}


class ESocket:

    def __init__(self, name):
        self.name = name
        self.id = SOCKET_MAP[name]
        self.state = False
        rf_sender.turn_socket_on(self.id)


    def __str__(self):
        return "< %s >" % self.name

    def toggle(self):
        if self.state:
            self.turn_off()
        else:
            self.turn_on()

    def turn_on(self):
        self.state = True
        rf_sender.turn_socket_on(self.id)
        print("%s turned on" % self)


    def turn_off(self):
        self.state = False
        rf_sender.turn_socket_off(self.id)
        print("%s turned off" % self)