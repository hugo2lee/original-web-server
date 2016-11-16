import socket

with socket.socket() as s:

    s.bind(('0.0.0.0', 80))

    while True:
        s.listen(5)
        connection, address = s.accept()

        response = b'HTTP/1.1 200 OK\r\n\r\n<!DOCTYPE html><html><head><meta charset="utf-8"><title>CODEE</title></head><body><h1>WELCOME TO CODEE\r\n\r\n</h1>\r\n\r\n<h2>by hugo</h2></body></html>'
        connection.sendall(response)
        connection.close()
