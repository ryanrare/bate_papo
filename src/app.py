from flask import Flask, request
import asyncio

app = Flask(__name__)

async def enviar_mensagem(message):
    reader, writer = await asyncio.open_connection('localhost', 8080)
    try:
        await writer.write(message.encode())
        await writer.drain()

    except:
        print('fudeu tudooooo')
        writer.close() 

@app.route('/mensagem', methods=['POST'])
def mensagem():
    message = request.form['message']
    asyncio.run(enviar_mensagem(message))
    return 'Mensagem enviada!'

if __name__ == '__main__':
    app.run(host='localhost', port=8001)
