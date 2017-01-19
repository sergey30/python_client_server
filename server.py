import socket
import umsgpack
import multiprocessing
import psycopg2

# Сервер запускается и ждет входных данных.
socket_server = socket.socket()
socket_server.bind(("", 9090))
socket_server.listen(10)

def record_json():
    """
    Создается соединение с клиентом и принимаются данные JSON в MSGPACK, если
    данных нет, повторяется попытка принять данные, после принятия, данные
    распаковываются и записываются в файл "server.json".
    Если данные получены в неверном формате будет соответствующее сообщение.
    """

    while True:
        try:
            socket_client, address_client = socket_server.accept()
            data_from_client = socket_client.recv(1024)
            if not data_from_client:
                continue
            with open("server.json", "a") as data:
                data.write(umsgpack.unpackb(data_from_client))
            socket_client.close()
        except TypeError:
            print("data from client:", address_client, "must be json format")


def record_sql():
    """
    Создается соединение с базой "test_db" и таблица "clients" в которую будут
    записаны данные в формате JSONB. Далее в цикле создается временная таблица
    "temp_table", в которую будут записываться данные из "server.json",
    а из "temp_table" в постоянную таблицу "clients" будут записаны только
    уникальные строки. После переноса уникальных данных в "clients" таблица
    "temp_table" удаляется. С новым проходом цикла "temp_table" снова создается,
    к этому времени в "server.json" уже появились новые данные, которые будут
    перенесены через "temp_table" в "clients".
    Так сделано, потому, что, данные в "server.json" постоянно добавляются
    и необходимо одновременно принимать данные от клиентов и записывать их в базу.
    В дальнейшем данные из базы можно взять командой:
    SELECT имя_колонки->>'имя_ключа' from имя_таблицы;
    """

    # Устанавливается соединение с базой.
    connect_db = psycopg2.connect(database="test_db", user="postgres", \
     password="13", host="127.0.0.1", port="5432")
    cursor_db = connect_db.cursor()
    # Создается постоянная таблица для записи данных.
    cursor_db.execute("CREATE TABLE clients (data JSONB NOT NULL UNIQUE);")

    while True:
        # Создается временная таблица.
        cursor_db.execute("CREATE TABLE temp_table (data JSONB NOT NULL);")
        # Копируются данные из "server.json"
        cursor_db.execute("COPY temp_table(data) FROM '/Users/s/Library/Mobile Documents/com~apple~CloudDocs/programming/python_client_server/server.json';")
        # Копируются только уникальные данные в постоянную таблицу.
        cursor_db.execute("INSERT INTO clients (data) SELECT data FROM \
        temp_table ON CONFLICT DO NOTHING;")
        # Удаляется временная таблица.
        cursor_db.execute("DROP TABLE temp_table;")
        connect_db.commit()

    connect_db.close()

# Создается отдельный процесс для записи в postgresql из файла(очереди).
record = multiprocessing.Process(target = record_sql, args = ())

# Запускается отдельным процессом функция record_sql()
record.start()

record_json()
