import socket

s = socket.socket()

s.bind(('', 8989))

s.listen(2)

file = open("recv.txt", "wb")

while True:
    conn, addr = s.accept()

    conn.send("hello".encode())

    recv_data = conn.recv(1024)

    while recv_data:
        file.write(recv_data)
        recv_data = conn.recv(1024)

    file.close()

    conn.close()

    break
