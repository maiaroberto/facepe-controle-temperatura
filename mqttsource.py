# python3.6
from datetime import datetime
import sqlite3
import json
import random

from paho.mqtt import client as mqtt_client



broker = 'broker.emqx.io'
port = 1883
topic = "laco_test_7261_temp"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client.Client):
    def on_message(client, userdata, msg):
        rec = json.loads(msg.payload.decode())

        print(f"Received `{rec}` from `{msg.topic}` topic, type {type(rec)}")

        # con = sqlite3.connect("control.db")
        # tp = rec["varType"]
        # mac = rec["id"]
        # data_e_hora = datetime.fromiso(rec["timestamp"])
        # vl = rec["value"]

        # script = "INSERT INTO leituras (tipo_leitura, id_mac, data_hora, leitura) VALUES (?, ?, ?, ?);"
        # con.execute(script, (tp, mac, data_e_hora, vl)) # execute the script
        # con.commit()
        # con.close()

    client.subscribe(topic)
    client.on_message = on_message
    print("sub ok")


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
