import socket


url = input("Please input address you would like to connect:")

discard1,discard2,host,discard3 = url.split('/')

print(host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))

cmd = "GET" ,url, "HTTP/1.0\r\n\r\n".encode()#encodes HTTP request to UTF-8
mysock.send(cmd)

#while True just runs until you tell it to break.
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close