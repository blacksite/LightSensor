##!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import random


if __name__ == '__main__':
    # This is the Publisher
    wait_interval = 60
    BROKER_URL = "broker.mqttdashboard.com"
    BROKER_PORT = 1883

    while True:
        status = random.randint(0, 1)
        amount = random.random() * 1000

        client = mqtt.Client()
        client.connect(BROKER_URL, BROKER_PORT)
        # client.publish("topic/test", "Hello world!")
        client.publish("light", status)
        client.publish("light", amount)
        client.disconnect()
        time.sleep(wait_interval)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
