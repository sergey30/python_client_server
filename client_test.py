import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
socket_client.send("hi".encode())
data = socket_client.recv(1024)
socket_client.close()
print("Received:", data.decode())
