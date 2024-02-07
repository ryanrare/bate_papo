# ///server
# import socket

# import asyncio

# async def handle_client(reader, writer):
#     # while True:
#     data = await reader.read(1024)
#     mensagem = data.decode('utf-8')
#     if mensagem == 'tt':
#         pass
#     print(f"Mensagem recebida: {mensagem}")

#     # Aqui sera a logica para subir pro banco de dados, com possivel id do cliente e message, opu ate mandar para outros clientes

#     await writer.drain()

#     writer.close()

# async def main():
#     server = await asyncio.start_server(handle_client, 'localhost', 8080, backlog=10000)

#     async with server:
#         await server.serve_forever()

# if __name__ == '__main__':
#     asyncio.run(main())


# /// app 
# from flask import Flask, request
# import asyncio

# app = Flask(__name__)

# async def enviar_mensagem(message):
#     reader, writer = await asyncio.open_connection('localhost', 8080)
#     try:
#         await writer.write(message.encode())
#         await writer.drain()

#     except:
#         print('ta no except')
#         writer.close() 

# @app.route('/mensagem', methods=['POST'])
# def mensagem():
#     message = request.form['message']
#     asyncio.run(enviar_mensagem(message))
#     return 'Mensagem enviada!'

# if __name__ == '__main__':
#     app.run(host='localhost', port=8001)