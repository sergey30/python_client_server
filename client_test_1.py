import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_1.txt", "rb")
for line in data:
    socket_client.send(line)
data.close()
socket_client.close()
print("Ready")
