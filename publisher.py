from paho.mqtt import client as mqtt_client
from random import randint
import time

broker_host = 'broker.emqx.io'
tcp_port = 1883
websocket_port = 8083
topic = '/python/mqtt'
client_id = f'python-mqtt-{randint(0, 1000)}'

username = 'gacrucis'
password = '1234'

def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Conectado!')
            return
        
        print(f'Error de conexion, codigo de error: {rc}')
    
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_host, tcp_port)
    return client

def publish(client):
     msg_count = 0
     while True:
         time.sleep(1)
         msg = f"Mensajes: {msg_count}"
         result = client.publish(topic, msg)
         # result: [0, 1]
         status = result[0]
         if status == 0:
             print(f"Send `{msg}` to topic `{topic}`")
         else:
             print(f"Failed to send message to topic {topic}")
         msg_count += 1

def run():
    client = connect()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()