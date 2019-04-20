from rpi_rf import RFDevice

PULSE_LENGTH = 300
REPEAT_TRANSMIT = 10
RECEIVE_TOLERANCE = 60
PROTOCOL = 1

GROUP_NUMBER = "11100"

GPIO_PIN = 0


rfdevice = RFDevice(GPIO_PIN)
rfdevice.enable_tx()
rfdevice.tx_repeat = REPEAT_TRANSMIT
rfdevice.tx_pulselength = PULSE_LENGTH
rfdevice.tx_repeat = REPEAT_TRANSMIT
rfdevice.tx_proto = PROTOCOL


def turn_socket_on(socket_nr):
   _set_socket(socket_nr, True)

def turn_socket_off(socket_nr):
   _set_socket(socket_nr, False)


def _set_socket(socket_nr, state):
   code = _getCodeWordB(socket_nr, state)
   rfdevice.tx_code(code=code)
   rfdevice.cleanup()


def _getCodeWordB(nChannelCode, state):
   sReturn = ''
   code = ["11111", "01111", "10111", "11011", "11101", "11110"]

   if nChannelCode < 1 or nChannelCode > 5:
      return '\0'

   for i in range(0, 5):
      if GROUP_NUMBER[i] == '0':
         sReturn += 'F'
      elif GROUP_NUMBER[i] == '1':
         sReturn += '0'
      else:
         return '\0'

   sReturn += code[nChannelCode]

   if state:
      sReturn += '01'
   else:
      sReturn += '10'

   sReturn += '\0'
   return int(sReturn, 2)
