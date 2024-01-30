import socket

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',  8888))

server.listen()
client, end = server.accept()

terminado = False
while not terminado:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)
    
    client.send(input('Mensagem: ').encode('utf-8'))

client.close()
Servidor.close()