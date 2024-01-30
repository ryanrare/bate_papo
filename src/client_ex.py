# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect(('localhost', 8888))

# terminado = False
# print('Digite tt paara terminar esse o chat')

# while not terminado:
#     client.send(input('Mensagem: ').encode('utf-8'))
#     msg = client.recv(1024).decode('utf-8')
#     if msg == 'tt':
#         terminado = True
#     else:
#         print(msg)

# client.close()


# ///
# from flask import Flask
# import socket

# app = Flask(__name__)

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect(('localhost', 8888))

# terminado = False
# print('Dígite tt para terminar esse o chat')

# while not terminado:
#     client.send(input('Mensagem: ').encode('utf-8'))
#     msg = client.recv(1024).decode('utf-8')
#     if msg == 'tt':
#         terminado = True
#     else:
#         print(msg)

# client.close()

# @app.route('/mensagem', methods=['POST'])
# def mensagem(request):
#     mensagem = request.json['mensagem']
#     client.send(mensagem.encode('utf-8'))
#     return 'Mensagem enviada!'

# app.run(host='localhost', port=8888)



# /////
# import socket

# server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost',  8888))

# server.listen()
# client, end = server.accept()

# terminado = False
# while not terminado:
#     msg = client.recv(1024).decode('utf-8')
#     if msg == 'tt':
#         terminado = True
#     else:
#         print(msg)
    
#     client.send(input('Mensagem: {msg}').encode('utf-8'))

# client.close()
# server.close()