from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from utils import serialize_datetime
import psycopg2

app = Flask(__name__)
socketio = SocketIO(app)

# Configuração do banco de dados
db_connection = psycopg2.connect(
    database="bate_papo",
    user="ryan",
    password="rv2605rv",
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

# # Rota para enviar mensagens
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     data = request.get_json()
#     username = data['username']
#     message = data['message']

#     db_cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
#     db_connection.commit()

#     return jsonify({"status": "Message sent successfully"})


# Rota para obter mensagens
@socketio.on('get_messages')
def handle_get_messages():
    db_cursor.execute("SELECT id, username, message FROM messages ORDER BY created_at DESC LIMIT 10")
    messages = db_cursor.fetchall()
    

    emit('messages_received', {"messages": messages})

# # Rota para obter mensagens
# @app.route('/get_messages', methods=['GET'])
# def get_messages():
#     db_cursor.execute("SELECT * FROM messages ORDER BY created_at DESC LIMIT 10")
#     messages = db_cursor.fetchall()

#     return jsonify({"messages": messages})

if __name__ == '__main__':
    socketio.run(app, debug=True)
