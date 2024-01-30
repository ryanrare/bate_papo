import socket

import asyncio

async def handle_client(reader, writer):
    # while True:
    data = await reader.read(1024)
    mensagem = data.decode('utf-8')
    if mensagem == 'tt':
        pass
    print(f"Mensagem recebida: {mensagem}")

    # Aqui sera a logica para subir pro banco de dados, com possivel id do cliente e message, opu ate mandar para outros clientes

    await writer.drain()

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8080, backlog=10000)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())