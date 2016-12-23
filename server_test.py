import socket
import umsgpack
import multiprocessing

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    while True:
        socket_client, address_client = socket_server.accept()
        print("Connected by:", address_client)
        data_from_client = socket_client.recv(1024)
        if not data_from_client:
            continue
        data = open("server_test.json", "a")
        data.write(umsgpack.unpackb(data_from_client))
        data.close()
        socket_client.close()

def record_sql():
    data = open("server_test.json")
    data_json = data.read()
    data.close()
    data_sql = open("server_test.txt", "a")
    data_sql.write(data_json)
    data_sql.close()

#record = multiprocessing.Process(target = record_sql, args = ())

record_json()
