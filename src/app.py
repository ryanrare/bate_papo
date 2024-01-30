from flask import Flask, request  # Import request object
import asyncio

app = Flask(__name__)

async def enviar_mensagem(message):
    reader, writer = await asyncio.open_connection('localhost', 8080)  # Unpack the tuple
    try:
        await writer.write(message.encode())  # Use writer for sending
        await writer.drain()  # Wait for data to be sent

    except:
        print('fudeu tudooooo')
        writer.close() 

@app.route('/mensagem', methods=['POST'])
def mensagem():  # Make the view function synchronous
    message = request.form['message']  # Access POST data using request.form
    asyncio.run(enviar_mensagem(message))  # Run async function within Flask
    return 'Mensagem enviada!'

if __name__ == '__main__':
    app.run(host='localhost', port=8001)
