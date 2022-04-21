#!/usr/bin/python3
import datetime
import logging
# import json package
import logging.handlers
import time
import json
import datetime

import paho.mqtt.client as mqtt
from random import randint

PORT = 1883  # MQTT data listening port
SubTopic = "tracking"

# BROKER_ENDPOINT = "192.168.0.3"
BROKER_ENDPOINT = "astrazeneca.vacustech.in"
SLAVE_ADDR = "5a-c2-15-0a-00-01"
print(SLAVE_ADDR)


def processDataFrame():
    """
    function to process data array
    :param data_array:
    :return: none
    """

    # {"master": "5a-c2-15-08-00-01", "assets": [
    #     {"macaddress": "5a-c2-15-01-05-01", "X": 115.89, "Y": 7.88, "temp": 0.0, "humidity": 0.0, "airflow": 0.0,
    #      "iaq": 0.0, "alert": 4.0, "battery": 88.0, "slaveaddress": "5a-c2-15-0a-00-03"}]}

    assetpayload = []
    sensorpayload = []
    iaqpayload = []
    iaqpayload2 = []
    statpayload = []

    for i in range(1, 5):
        dummy = {}
        dummy["id"] = "5a-c2-15-" + "{0:02x}-{1:02x}-{2:02x}".format(2, 0, i)
        dummy["LAT"] = "{0:d}.{1:d}".format(12, 93140500)
        dummy["LONG"] = "{0:d}.{1:d}".format(77, 62311500)
        dummy["temp"] = "{0:d}.{1:d}".format(randint(0, 0), randint(0, 0))
        dummy["Hum"] = "{0:d}.{1:d}".format(randint(0, 0), randint(0, 0))
        dummy["alert"] = int(randint(2, 5))
        dummy["bt"] = int(randint(88, 96))
        dummy["gateway"] = "5a-c2-15-0d-00-35"
        print(dummy)
        # client.publish("LnTtracking", payload=json.dumps(dummy), qos=0)

    time.sleep(10)

    for i in range(1, 5):
        dummy = {}
        dummy["id"] = "5a-c2-15-" + "{0:02x}-{1:02x}-{2:02x}".format(1, 0, i)
        dummy["LAT"] = "{0:d}.{1:d}".format(12, 93140500)
        dummy["LONG"] = "{0:d}.{1:d}".format(77, 62311500)
        dummy["temp"] = "{0:d}.{1:d}".format(randint(0, 0), randint(0, 0))
        dummy["Hum"] = "{0:d}.{1:d}".format(randint(0, 0), randint(0, 0))
        dummy["alert"] = int(randint(0, 5))
        dummy["bt"] = int(randint(88, 96))
        dummy["gateway"] = "5a-c2-15-0d-00-35"
        print(dummy)
        client.publish("LnTtracking", payload=json.dumps(dummy), qos=0)

    for i in range(1, 5):
        dummy= {}
        dummy["id"] = "5a-c2-15-" + "{0:02x}-{1:02x}-{2:02x}".format(5, 0, i)
        print(dummy)
        # client.publish("LnTtracking", payload=json.dumps(dummy), qos=0)
    # assetpayload.append(dummy)

    # {"id": "5a-c2-15-02-00-01", "LAT": 12.93140500, "LONG": 77.62311500, "temp": 0.00, "Hum": 0.00,
    #  "gateway": "5a-c2-15-0d-00-35", "bt": 100, "alert": 0, "timestamp": 2022 - 04 - 07T10: 39: 7
    # Z, "gpsstatus": 1}

    # ret = client.publish("LnTtracking", payload=json.dumps(assetpayload), qos=0)

    print("published")
    # ret = client.publish("esp/test1",payload=json.dumps(sensor), qos=0)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, user_data, flags, rc):
    print("Connected with result code " + str(rc))


def systemcon():
    st = 0
    try:
        st = client.connect(BROKER_ENDPOINT, PORT)  # establishing connection

    except:
        st = 1

    finally:
        if st != 0:
            time.sleep(5)
            systemcon()


def on_connect(client, userdata, flags, rc):
    print("Connected to broker")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        # logging.info("Unexpected disconnection.")
        systemcon()


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
systemcon()
# Connecting to both MQTT brokers
client.loop_start()

while True:
    try:
        # process serial data
        processDataFrame()
        time.sleep(1)
    except KeyboardInterrupt:
        Data_port.close()
        client.loop_stop()
        break
