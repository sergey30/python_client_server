import socket
import umsgpack

# Открывается файл с данными которые передадутся серверу.
data = open("client1.json")
# В цикле данные передаются порциями по одной строке.
for i in data:
    socket_client = socket.socket()
    socket_client.connect(("127.0.0.1", 9090))
    # Перед отправкой данные упаковываются в MSGPACK.
    socket_client.send(umsgpack.packb(i))
    socket_client.close()
data.close()

print("Ready")
