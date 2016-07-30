import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from time import sleep

# GPIO Setup
chan_list = [11,13,15,12]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, GPIO.LOW)  
GPIO.output(11, GPIO.HIGH)  

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("BEACON/1")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    GPIO.output(chan_list, GPIO.LOW)
    GPIO.output(chan_list[int(msg.payload)], GPIO.HIGH)
    if int(msg.payload) > 0
        GPIO.output(chan_list, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(chan_list, GPIO.LOW)
        sleep(0.1)
        GPIO.output(chan_list, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(chan_list, GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.62.201.125", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
