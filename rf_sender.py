from rpi_rf import RFDevice



GROUP_NUMBER = "FFF00"

GPIO_PIN = 0


rfdevice = RFDevice(GPIO_PIN,
                    tx_proto=1,
                    tx_pulselength=300,
                    tx_repeat=10,
                    tx_length=12,
                    rx_tolerance=60)
rfdevice.enable_tx()


def turn_socket_on(socket_nr):
   _set_socket(socket_nr, True)


def turn_socket_off(socket_nr):
   _set_socket(socket_nr, False)


def _set_socket(socket_nr, state):
   code = _getCodeWordB(socket_nr, state)
   print("length %s" % len(code))
   print(code)
   rfdevice.tx_bin(code)
   # rfdevice.tx_code(code=code)


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
