from rpi_rf import RFDevice

REPEAT_TRANSMIT = 10
RECEIVE_TOLERANCE = 60
PROTOCOL = 1

GROUP_NUMBER = "FFF00"

GPIO_PIN = 0


rfdevice = RFDevice(GPIO_PIN)
rfdevice.tx_repeat = REPEAT_TRANSMIT
rfdevice.tx_proto = PROTOCOL
rfdevice.enable_tx()


def turn_socket_on(socket_nr):
   _set_socket(socket_nr, True)


def turn_socket_off(socket_nr):
   _set_socket(socket_nr, False)


def _set_socket(socket_nr, state):
   code = _getCodeWordB(socket_nr, state)
   rfdevice.tx_length = len(code)
   # rfdevice.tx_code(code=code)
   rfdevice.tx_bin(code)


def _getCodeWordB(nChannelCode, state):
   sReturn = GROUP_NUMBER

   if nChannelCode < 1 or nChannelCode > 5:
      return '\0'

   code = ["FFFFF", "0FFFF", "F0FFF", "FF0FF", "FFF0F", "FFFF0"]
   sReturn += code[nChannelCode]

   if state:
      sReturn += '0F'
   else:
      sReturn += 'F0'

   sReturn += "\0"

   return sReturn  # int(sReturn, 16)
