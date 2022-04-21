import paho.mqtt.client as paho
import json
import datetime
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging.config
from tables import *

dt = datetime.datetime.now()
print(dt)

engine = create_engine(
    "mysql+pymysql://vacus:vacus@localhost/vertivedb", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
BROKER_ENDPOINT = "psa.vacustech.in"
# BROKER_ENDPOINT = "192.168.1.102"

PORT = 1883
topic = "#"


def on_message(client, userdata, message):
    # logger.info("Data received")
    print("data received from the broker ")

    serializedJson = message.payload.decode('utf-8')
    if len(serializedJson) > 20:
        jsonData = json.loads(serializedJson)
        # print(jsonData)
        storeData(jsonData, message.topic)


def storeData(jsonData, topic):
    try:
        # time.sleep(2)
        timeStamp = datetime.datetime.now()
        if topic == "esp/test1":
            print("Data Received", jsonData["id"])
            epoch = jsonData["timestamp"]
            a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

            # for elem in jsonData:
            """ Retrieving Temperature/Humidity object"""
            temp = session.query(Sensor).filter(Sensor.macid == jsonData["id"]).first()
            print("----------------", temp, jsonData["temp"], type(temp))
            if temp:
                """ Updating sensors data """
                temp.temperature = jsonData["temp"]
                temp.lastseen = timeStamp
                temp.battery = jsonData["bt"]
                session.commit()
                print("temperature data updated", temp.id)

                """Inserting Daily Temp/Humidity Data"""
                dailydata = SensorDailyTempHumi(
                    temperature=jsonData["temp"],
                    asset_id=temp.id,
                    timestamp=timeStamp)
                session.add(dailydata)
                session.commit()
                print("daily temperature data inserted")

                # sys = session.query(System).filter(System.id == temp.systemid_id).first()
                # print(sys.name)
                # if sys:
                #     if jsonData["temp"] > sys.temp:
                #         alertTemp = alert_alert(id=alert_alert.id, value=jsonData["temp"], lastseen=timeStamp, macid_id=temp.id)
                #         session.add(alertTemp)
                #         session.commit()

                print(temp.min, jsonData["temp"], temp.max)
                if jsonData["temp"] <= temp.min or jsonData["temp"] >= temp.max:
                    """Inserting Alert data """
                    alert = alert_alert(id=alert_alert.id, value=jsonData["temp"], lastseen=timeStamp,
                                        macid_id=temp.id)
                    session.add(alert)
                    session.commit()
                    print("alert data inserted")
            # else:
                # temp = session.query(Sensor).filter(Sensor.macid == jsonData["id"]).first()
                # if temp:
                    # temp.temperature = jsonData["temp"]
                    # temp.humidity = jsonData["humidity"]
                    # temp.lastseen = timeStamp
                    # temp.battery = jsonData["bt"]

                    # """Inserting Daily Temp/Humidity Data"""
                    # dailydata = SensorDailyTempHumi(
                    #     temperature=jsonData["temp"], humidity=jsonData["humidity"]
                    #     asset_id=temp.id,
                    #     timestamp=timeStamp)
                    # session.add(dailydata)
                    # session.commit()

    except Exception as err:
        # logger.info("Error: ", str(err))
        print("error : ", err)
        # Session.rollback()


def on_connect(client, userdata, flags, rc):
    # logger.info("Connected to broker")
    print("connected to broker ")
    client.subscribe(topic)  # subscribe topic test


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("disconnected to the broker ")

        # logger.info("Disconnection from broker, Reconnecting...")
        systemcon()
        client.subscribe(topic)  # subscribe topic test


def systemcon():
    st = 0
    try:
        st = client.connect(BROKER_ENDPOINT, PORT)  # establishing connection
    except:
        st = 1
    finally:
        if st != 0:
            # logger.info("Connection failed, Reconnecting...")
            time.sleep(5)
            systemcon()


if __name__ == "__main__":

    # with open('/home/ubuntu/logs/logging_tracking.yaml', 'r') as stream:
    #     logger_config = yaml.load(stream, yaml.FullLoader)
    # logging.config.dictConfig(logger_config)
    logger = logging.getLogger('Tracking -')

    client = paho.Client()  # create client object
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    systemcon()
    client.subscribe(topic)  # subscribe topic test
    client.loop_forever()

    while True:
        pass
