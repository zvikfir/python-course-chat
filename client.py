import os
import socket
import sys
import threading

from select import select

with socket.socket() as socket:
    socket.connect(('localhost', os.environ['PORT']))


    def read_input(socket):
        while True:
            message = input('> ')
            socket.send(message.encode('utf-8'))


    read_input_thread = threading.Thread(target=read_input, args=(socket,))
    read_input_thread.start()

    while True:
        data = socket.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

