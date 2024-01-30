import asyncio
import json
import threading

from flask import Flask, request
from websockets import serve

app = Flask(__name__)

clients = set()

@app.route("/")
def index():
    return "Chat em tempo real"

@app.route("/ws")
async def ws():
    async with websockets.serve(
        handle_websocket,
        host="0.0.0.0",
        port=8080,
    ):
        await asyncio.sleep(1)
        print("Servidor iniciado na porta 8080")

async def handle_websocket(websocket, path):
    clients.add(websocket)

    while True:
        message = await websocket.recv()
        print("Mensagem recebida:", message)

        for client in clients:
            await client.send(message)

def lock():
    global lock
    if not lock:
        lock = threading.Lock()
    lock.acquire()

def unlock():
    global lock
    if lock:
        lock.release()

@app.route("/send")
def send():
    global lock
    message = request.args.get("message")

    lock()
    for client in clients:
        await client.send(message)
    unlock()
    return "Mensagem enviada"