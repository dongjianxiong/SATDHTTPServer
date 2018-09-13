import socket
import sqlite3

ip_port = ('10.2.1.226', 8000)
web = socket.socket()
web.bind(ip_port)
web.listen(5)

while True:
    print 'I am waiting for the client'
    conn, addr = web.accept()
    # thread = threading.Thread(target=jonnys, args=(conn, addr))

    data = conn.recv(1024)
    print data
    conn.sendall(str('<h1>welcome nginx</h1>'))
    conn.close()