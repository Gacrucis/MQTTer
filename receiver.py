import time
from actor import Receiver

broker_host = 'broker.emqx.io'
tcp_port = 1883
topic_1 = '/python/mqtt'
topic_2 = '/otro/topic'

receiver_client = Receiver(2, broker_host, tcp_port)

opt = None
while opt != '3':
    print('1. Suscribirse al topic [/python/mqtt]')
    print('2. Suscribirse al topic [/otro/topic]')
    print('3. Empezar a escuchar los topics')
    print('4. Chiste del dia')
    print()

    opt = input('Inserte una opcion: ').strip()
    print()

    if opt == '1':
        receiver_client.subscribe(topic_1)

    if opt == '2':
        receiver_client.subscribe(topic_2)

    if opt == '3':
        receiver_client.begin()

    if opt == '4':
        print('What do computers air conditioners have in common?')
        time.sleep(1)
        print('They both become useless when you open windows')

    print()