from paho.mqtt import publish
import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'Ouyv74FtY5rcVxoNaAKr'

INTERVAL = 2
sensor_data = {'temperature': 0, 'humidity':0}
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()



try:
    while True:

        sensor_data['temperature'] = 32
        sensor_data['humidity'] = 30
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data),1)


except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect
