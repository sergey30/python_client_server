import socket
import umsgpack
import multiprocessing

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    while True:
        try:
            socket_client, address_client = socket_server.accept()
            data_from_client = socket_client.recv(1024)
            if not data_from_client:
                continue
            data = open("server_test.json", "a")
            data.write(umsgpack.unpackb(data_from_client))
            data.close()
            socket_client.close()
        except TypeError:
            print("Data must be in json format")

def record_sql():
    counter = 0
    while True:
        data_json = open("server_test.json")
        data_sql = open("server_test.txt")
        result = len(list(data_json)) > len(list(data_sql))
        data_json.close()
        data_sql.close()
        if result:
            data_json = open("server_test.json")
            data_sql = open("server_test.txt", "a")
            data_sql.write(list(data_json)[counter])
            counter = counter + 1
            data_json.close()
            data_sql.close()
            print("Recorded ", counter, " lines")
        else:
            continue

record = multiprocessing.Process(target = record_sql, args = ())

record.start()
record_json()
