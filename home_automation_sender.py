from rpi_rf import RFDevice

PULSE_LENGTH = 300
REPEAT_TRANSMIT = 10
RECEIVE_TOLERANCE = 60
PROTOCOL = 1

GROUP_NUMBER = "11100"

GPIO_PIN = 0
rfdevice = RFDevice(args.gpio)
rfdevice.enable_tx()
rfdevice.tx_repeat = REPEAT_TRANSMIT
rfdevice.tx_pulselength = PULSE_LENGTH
rfdevice.tx_repeat = REPEAT_TRANSMIT
rfdevice.tx_proto = PROTOCOL


rfdevice.tx_code(args.code, PROTOCOL, PULSE_LENGTH, args.length)
rfdevice.cleanup()


def getCodeWordB(nAddressCode, state):
   code = ["FFFF", "0FFF", "F0FF", "FF0F", "FFF0" ]
   sReturn = ''

   if nAddressCode < 1 or nAddressCode > 4 or GROUP_NUMBER < 1 or GROUP_NUMBER > 4:
    return '\0'
   for i in range(0, 4):
     sReturn += code[nAddressCode][i]

   for i in range(0, 4):
     sReturn  += code[GROUP_NUMBER][i]

   sReturn += 'F'
   sReturn += 'F'
   sReturn += 'F'

   if state:
      sReturn += 'F'
   else:
      sReturn += '0'

   sReturn += '\0'

   return sReturn
