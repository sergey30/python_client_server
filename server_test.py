import socket
import umsgpack
import multiprocessing

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    while True:
        socket_client, address_client = socket_server.accept()
        data_from_client = socket_client.recv(1024)
        if not data_from_client:
            continue
        data = open("server_test.json", "a")
        data.write(umsgpack.unpackb(data_from_client))
        data.close()
        socket_client.close()

def record_sql():
    counter = 0
    while True:
        data_json = open("server_test.json")
        data_sql = open("server_test.txt")
        data_json_list = list(data_json)
        data_sql_list = list(data_sql)
        result = len(data_json_list) > len(data_sql_list)
        data_json.close()
        data_sql.close()

        if result:
            data_json = open("server_test.json")
            data_sql = open("server_test.txt", "a")
            data_json_list = list(data_json)
            data_sql.write(data_json_list[counter])
            counter = counter + 1
            data_json.close()
            data_sql.close()
            print("Recorded ", counter, " lines")
        else:
            continue

record = multiprocessing.Process(target = record_sql, args = ())

record.start()
record_json()
