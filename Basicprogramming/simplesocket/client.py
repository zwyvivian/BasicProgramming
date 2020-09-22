import socket
#1.buy phone

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print(phone)
#2.拨号
phone.connect(('127.0.0.1',8080))  #0-65535： 0-1024 os

#3.发收消息
while True:
    msg=input('>>').strip()
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print(data)
    if

#4.关闭
phone.close()

