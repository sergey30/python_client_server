import socket
import umsgpack
import multiprocessing
import json

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    while True:
            socket_client, address_client = socket_server.accept()
            data_from_client = socket_client.recv(1024)
            if not data_from_client:
                continue
            data = open("server.json", "a")
            data.write(umsgpack.unpackb(data_from_client))
            data.close()
            socket_client.close()

def record_sql():
    counter = 0
    while True:
        with open("server.json") as data_json, open("server.txt") as data_sql:
            result = len(list(data_json)) > len(list(data_sql))
        if result:
            with open("server.json") as data_json, open("server.txt", "a") as data_sql:
                data_sql.write(list(data_json)[counter])
            counter = counter + 1
            print("Recorded ", counter, " lines")
        else:
            continue

record = multiprocessing.Process(target = record_sql, args = ())

record.start()
record_json()
