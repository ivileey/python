import socket
host = socket.gethostname()
port = 12347
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
sock,addr = s.accept()
print('Connection built')
info = ''
while True:
    info = sock.recv(1024).decode()
    print('receive:'+info)
    send_mes = raw_input("send:")
    sock.send(send_mes.encode())
    if send_mes =='exit':
        break
sock.close()
s.close()
