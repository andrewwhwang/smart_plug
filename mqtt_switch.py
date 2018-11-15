#!/usr/bin/python
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

output_GPIO = [7, 11]

def setup_board():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_GPIO, GPIO.OUT)
    GPIO.output(output_GPIO, 1)

def on_connect(client, userdata, rc):
    client.subscribe("switch/+")
    print("connected")

def on_message(client, userdata, msg):
    message = int(msg.payload.decode("utf-8"))
    outlet_id = int(msg.topic.split("/")[1])
    GPIO.output(output_GPIO[outlet_id], message)

if __name__ == '__main__':
    try:
        setup_board()
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set("username", password="password")
        client.connect("BROKER IP ADDRESS", 1883, 60)
        client.loop_forever()
    except Exception as e:
        print(e)
        GPIO.cleanup()
    except:
        GPIO.cleanup()
