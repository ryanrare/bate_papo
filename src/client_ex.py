import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8888))

terminado = False
print('Digite tt paara terminar esse o chat')

while not terminado:
    client.send(input('Mensagem: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)

client.close()