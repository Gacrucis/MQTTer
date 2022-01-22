from paho.mqtt import client as mqtt_client
from random import randint

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

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()