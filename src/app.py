from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from utils import serialize_datetime
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
socketio = SocketIO(app)

db_connection = psycopg2.connect(
    database="bate_papo",
    user="ryan",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port="5432"
)
db_cursor = db_connection.cursor()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para enviar mensagens
@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    message = data['message']

    db_cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
    db_connection.commit()

    emit('message_sent', {"username": username, "message": message}, broadcast=True)

# Rota para obter mensagens
@socketio.on('get_messages')
def handle_get_messages():
    db_cursor.execute("SELECT id, username, message FROM messages ORDER BY created_at DESC LIMIT 10")
    messages = db_cursor.fetchall()
    

    emit('messages_received', {"messages": messages})

if __name__ == '__main__':
    socketio.run(app, debug=True)
