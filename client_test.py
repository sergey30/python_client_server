import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
#data = input("Write number:")
socket_client.send(str.encode("hi"))
data = socket_client.recv(1024)
socket_client.close()
print("Received:", bytes.decode(data))
