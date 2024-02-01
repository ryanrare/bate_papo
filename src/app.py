from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
db_connection = psycopg2.connect(
    database="bate_papo",
    user="ryan",
    password="/////",
    host="localhost",
    port="5432"
)
db_cursor = db_connection.cursor()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para enviar mensagens
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    username = data['username']
    message = data['message']

    db_cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
    db_connection.commit()

    return jsonify({"status": "Message sent successfully"})

# Rota para obter mensagens
@app.route('/get_messages', methods=['GET'])
def get_messages():
    db_cursor.execute("SELECT * FROM messages ORDER BY created_at DESC LIMIT 10")
    messages = db_cursor.fetchall()

    return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(debug=True)
