# DO QUE SE TRATA?:
- É utilizado flask junto com socket, a criacao de um chat em tempo real. Criei esse projeto para estudar concorrencia e o protocolo WebSocket

# COMO RODAR?:
- Primeiro passo: instale atraves do pip ou poetry, as dependencias Flask, flask_socketio, e o psycopg
- Segundo passo: Crie uma tabela no db com usuario e messagem
- Terceiro passo: substitua suas credencias de acesso ao DB em app.py
- Quarto e ultimo pasoo: execute na pasta src, o comando python app.py e pronto, o chat está rodando
  

# Trechos do código e relação com a Concorrência:
# 1. Conexões simultâneas:

SocketIO.run(app, debug=True): Permite várias conexões de clientes ao servidor.
# 2. Manipulação assíncrona de mensagens:

@socketio.on('send_message'): Executa em paralelo para cada envio de mensagem.
emit('message_sent', ...): Envia mensagens de forma assíncrona para todos os clientes.
# 3. Eventos e callbacks:

@socketio.on('get_messages'): Permite solicitações simultâneas de mensagens.
# 4. Broadcast de mensagens:

emit('message_sent', ...): Envia a mesma mensagem para todos os clientes conectados.
# Relação com Concorrência:

Permite comunicação em tempo real para vários usuários.
Garante bom desempenho mesmo com alto volume de tráfego.
Facilita interação e comunicação em grupo.
Observação: Este código é um exemplo simples e pode ser adaptado para diferentes necessidades.
