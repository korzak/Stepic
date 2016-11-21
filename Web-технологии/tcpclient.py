import socket #импорт библиотеки socket, необходима, чтобы использовать функции TCP
req = "Hello tcp!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создается новый обьект сокет, причем указываес две опции: 
                                                      #AFINET  - показывает, что мы работаем с сетевыми сокетами
                                                      #SOCK_STREAM - указывает что мы будем использовать сокет для работы с протоколом TCP
s.connect(('127.0.0.1', 1234)) #подключение к удаленной машине, передаем ip-адрес и порт машины
s.send(req.encode())
rsp = s.recv(1024).decode()
print(rsp)
s.close()