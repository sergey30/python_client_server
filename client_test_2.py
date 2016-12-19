import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_2.txt", "rb")
for i in data:
    socket_client.send(i)
data.close()
socket_client.close()
print("Ready")
