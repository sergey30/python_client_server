import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_2.txt", "rb")
data = data.read()
socket_client.send(data)
data = socket_client.recv(1024)
socket_client.close()
print("Received:", data.decode())
