import socket
import umsgpack
import multiprocessing
import psycopg2

socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    while True:
            socket_client, address_client = socket_server.accept()
            data_from_client = socket_client.recv(1024)
            if not data_from_client:
                continue
            with open("server.json", "a") as data:
                data.write(umsgpack.unpackb(data_from_client))
            socket_client.close()

def record_sql():
    connect_db = psycopg2.connect(database="test_db", user="postgres", password="13", host="127.0.0.1", port="5432")
    cursor_db = connect_db.cursor()

    cursor_db.execute("CREATE TABLE clients (id SERIAL PRIMARY KEY, data TEXT);")

    while True:
        cursor_db.execute("COPY clients(data) FROM '/Users/s/Library/Mobile Documents/com~apple~CloudDocs/programming/python_client_server/server.json'")
        connect_db.commit()

    connect_db.close()

record = multiprocessing.Process(target = record_sql, args = ())

record.start()
record_json()
