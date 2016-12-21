import socket
import umsgpack

data = open("client_test_1.json")
for i in data:
    socket_client = socket.socket()
    socket_client.connect(("127.0.0.1", 9090))
    socket_client.send(umsgpack.packb(i))
    socket_client.close()
data.close()

print("Ready")
