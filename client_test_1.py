import socket

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_1.txt", "rb") # читаю из файла в байтах
socket_client.send(data.read()) # не использую encode() т.к. прочитано из файла в байтах
data.close()
data = socket_client.recv(1024)
socket_client.close()
print("Received:", data.decode())
