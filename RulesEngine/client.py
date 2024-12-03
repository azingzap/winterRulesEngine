'''
This python file creates the client that subscribes to the winter application that gets an input topic with a message.
In this file the rules engine function processes the message and then publishes the processed message to an output topic.
'''

import paho.mqtt.client as mqtt
from rules_engine import *
import config

inputTopic="BRE/calculateWinterSupplementInput/"+config.topicID
outputTopic="BRE/calculateWinterSupplementOutput/"+config.topicID

#logging function, this ensures we receive the logs.
def on_log(client, userdata, paho_log_level, messages):
    print("log: " + messages)

#Callback connection function which gives us info when we subscribe to the input topic.
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(inputTopic)
        print("Connected OK")
    else:
        print("Connection failed, returned code =", reason_code)

#Function that ensures the user gets notified if it gets disconnect from the broker.
def on_disconnect(client, userdata, flags, properties, reason_code=0):
    print("Disconnected result code " + str(reason_code))

#Function that runs the rules engine and publishes the new message to the output topic.
def on_message(client, userdata, message):

    topic = message.payload.decode("utf-8")
    print("message received " + topic)
    outputMessage = implementRulesEngine(topic)
    print("Publishing message....")
    client.publish(outputTopic, outputMessage)
    print("Message has been published with message", outputMessage)

broker = "test.mosquitto.org"
client =  mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"thisIsSubscriber")

#The enabled functions.
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message

#Connects to the broker.
print("Connecting to broker...")
client.connect(broker, 1883)

#The loop processes the functions
client.loop_forever()

