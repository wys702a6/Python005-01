import socket
import sys

if len(sys.argv) > 1:
    server_ip = sys.argv[1]
else:
    exit(1)


s = socket.socket()

s.connect((server_ip, 8989))

with open("sample.txt", "rb") as f:
    send_data = f.read(1024)

    while send_data:
        s.send(send_data)
        send_data = f.read(1024)

s.close()
