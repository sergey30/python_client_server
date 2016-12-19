import socket
import time

data = open("client_test_1.txt", "rb")
for line in data:
    socket_client = socket.socket()
    socket_client.connect(("127.0.0.1", 9090))
    socket_client.send(line)
    time.sleep(1)
    socket_client.close()
data.close()

print("Ready")
