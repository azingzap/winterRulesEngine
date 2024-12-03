'''
I was having troubles subscribing to the winter supplement web app so in this file, I created a imitation of a client that
would have the same input topic as the winter supplement web app and would include a message in json format representing what the
winter supplement web app would to the input topic.
'''

import paho.mqtt.client as mqtt
import json
import config

numOfChildren = 8
familyComposition = "couple"
requiresPayStatus = "true"

#Example input data in json format.
msg=json.dumps({"id": config.topicID, "numberOfChildren": numOfChildren, "familyComposition": familyComposition, "familyUnitInPayForDecember": requiresPayStatus})
inputTopic="BRE/calculateWinterSupplementInput/"+config.topicID


#logging function.
def on_log(client, userdata, pahoLogLevel, messages):
    print("log: " + messages)

#Call back function that lets user know there was a connection and publishes the message to the topic.
def on_connect(client, userdata, flags, reasonCode, properties):
    if reasonCode == 0:
        client.publish(inputTopic, msg)
        print("Connected OK")
    else:
        print("Connection failed, returned code =", reasonCode)

#Function that allows the user to be notified if it gets disconnected from the broker.
def on_disconnect(client, userdata, flags, properties, reasonCode=0):
    print("Disconnected result code " + str(reasonCode))


broker = "test.mosquitto.org"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"thisIsPublisher")

#Functions that get called.
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect

#Connects to the broker.
print("Connecting to broker...")
client.connect(broker, 1883)
print(msg)
print(inputTopic)

#The loop processes the functions.
client.loop_forever()

