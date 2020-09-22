import socket
#1.buy phone

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print(phone)
#2.bind sim card
phone.bind(('127.0.0.1',8080))  #0-65535： 0-1024 os

#3.开机

phone.listen(5) #最大挂起链接数

#4.等电话链接
conn,client=phone.accept()  #conn 就好像是线

#5. recieve /send message
while True: #通信循环
    data=conn.recv(1024)  #threshold bytes 1024 最大接受
    print("client's data",data)

    conn.send(data.upper())

#6.挂电话
conn.close()
#7.关机
phone.close()