import socket
import umsgpack

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_data():
    while True:
        data_from_client = socket_client.recv(1024)
        if not data_from_client:
            return
        data = open("server_test.json", "a")
        data.write(umsgpack.unpackb(data_from_client))
        data.close()

while True:
    socket_client, address_client = socket_server.accept()
    print("Connected by:", address_client)
    record_data()
    socket_client.close()
