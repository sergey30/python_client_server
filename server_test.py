import socket

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

while True:
    question = input("Do you want to out? y/n: ")
    if question == "y":
        break
    socket_client, address_client = socket_server.accept()
    print("Connected by:", address_client)
    while True:
        data = socket_client.recv(1024)
        if not data:
            break
        socket_client.send(data.upper())
    socket_client.close()
#
