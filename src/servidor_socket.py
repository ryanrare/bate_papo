import socket

import asyncio

async def handle_client(reader, writer):
    # while True:
    data = await reader.read(1024)
    mensagem = data.decode('utf-8')
    if mensagem == 'tt':
        pass
    print(f"Mensagem recebida: {mensagem}")

    # Aqui você pode adicionar a lógica para processar a mensagem,
    # como por exemplo, salvar no banco de dados ou enviar para outros clientes.

    await writer.drain()  # Aguarda o envio completo dos dados

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8080, backlog=10000)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())