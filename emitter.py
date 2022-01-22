import time
from actor import Sender

broker_host = 'broker.emqx.io'
tcp_port = 1883
topic_1 = '/python/mqtt'
topic_2 = '/otro/topic'

emitter_client = Sender(1, broker_host, tcp_port)

while not emitter_client.client.is_connected():
    print('Esperando conexion ...')
    time.sleep(1)

opt = None
while opt != '4':
    print('1. Escribir al topic [/python/mqtt]')
    print('2. Escribir al topic [/otro/topic]')
    print('3. Chiste del dia')
    print('4. Salir')
    print()

    opt = input('Inserte una opcion: ').strip()
    print()

    if opt == '1':
        msg = input('Inserte el mensaje: ')
        emitter_client.send(topic_1, msg)

    if opt == '2':
        msg = input('Inserte el mensaje: ')
        emitter_client.send(topic_2, msg)

    if opt == '3':
        print('Why do Java programmers wear glasses?')
        time.sleep(1)
        print('Because they don\'t C#')

    print()