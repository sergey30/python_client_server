import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_1.json", "rb")
socket_client.send(data.read())
data.close()
#data = socket_client.recv(1024)
socket_client.close()
print("Ready")
