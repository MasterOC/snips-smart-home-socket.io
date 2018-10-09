#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from socketIO-client-2 import SocketIO

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{0}:{1}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intentMessage):
    sentence = 'You asked for '

    if intent_message.intent.intent_name == 'onOffIntent':
        print('searchWeatherForecast')
    else:
        return

    device = intentMessage.slots.device.first().value
    state = intentMessage.slots.state.first().value

    if len(intentMessage.slots.room) > 0:
      room = intentMessage.slots.room.first().value

    if len(intentMessage.slots.location) > 0:
      location = intentMessage.slots.location.first().value

      for i,c in enumerate(location):
        if c.isupper():
          print i
          locationObject = location[i:len(location)]
          print locationObject
          break

    result_sentence = "Schalte {0} {1}".format(str(device), str(state))


    #socket.io
    socketIO = SocketIO('192.168.2.121', 3000)
    socketIO.emit('snips')
    socketIO.wait(seconds=1)

    #tts + end_session
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()


########


