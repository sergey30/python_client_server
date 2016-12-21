import socket
import umsgpack

socket_client = socket.socket()
socket_client.connect(("127.0.0.1", 9090))
data = open("client_test_1.json")
data_read = data.read()
socket_client.send(umsgpack.packb(data_read))
data.close()
socket_client.close()
print("Ready")


# большой объем не получается отправить через msgpack, только маленький, пробовал не только json, но и txt
