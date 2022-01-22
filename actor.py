from paho.mqtt import client as mqtt_client
import time

class CustomClient:
    def __init__(self, id, host, port):
        self.client = mqtt_client.Client(str(id))
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(host, port)

    def on_connect(self, client, userdata, flags, rc):
            if rc == 0:
                print('Conectado!')
            
            else:
                print(f'Error de conexion, codigo de error: {rc}')
    
    def on_message(self, client, userdata, msg):
        print(f'[{msg.topic}] -> {msg.payload.decode()}')
        
class Sender(CustomClient):

    def __init__(self, id, host, port):
        super().__init__(id, host, port)
        self.client.loop_start()

    def send(self, topic, msg):
        while not self.client.is_connected():
            print('Esperando conexion . . .')
            time.sleep(1)

        result = self.client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"[{topic}] Enviado mensaje -> {msg}")
        else:
            print(f"[{topic}] Error de envio de mensaje! [{status}]")

class Receiver(CustomClient):

    def __init__(self, id, host, port):
        super().__init__(id, host, port)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def begin(self):
        print('El cliente ha empezado a escuchar!')
        self.client.loop_forever()