
import socket

target_host="127.0.0.1"
target_pori=9999

#建立一个sock连接
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接客户端
client.connect((target_host,target_pori))

#发送一些数据
client.send("GET /HTTP/1.1\r\nHost:baidu.com\r\n\r\n")

#接收一些数据
response=client.recv(5)
print response
