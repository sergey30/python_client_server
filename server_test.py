import socket
import umsgpack

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_data():
    data_from_client = socket_client.recv(1024)
    if not data_from_client:
        return
    data = open("server_test.json", "a")
    data.write(umsgpack.unpackb(data_from_client))
    data.close()
    record_data()

while True:
    question = input("Do you want to out? y/n: ")
    if question == "y":
        break
    socket_client, address_client = socket_server.accept()
    print("Connected by:", address_client)
    record_data()

socket_client.close()
