import socket
import threading

clients = []


def broadcast_msg(msg, conn):
    for c in clients:
        if c is not conn:
            try:
                c.send(msg.encode('utf-8'))
            except:
                c.close()
                if c in clients:
                    clients.remove(c)


with socket.socket() as socket:
    address, port = 'localhost', 9999

    socket.bind((address, port))

    print(f'bound ({address}, {port})')

    print('accepting connection')
    socket.listen()

    while True:
        conn, client_address = socket.accept()
        clients.append(conn)


        def handle_client_connection(conn, addr):
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    msg = f'> {addr}: {data.decode("utf-8")}'
                    print(msg)
                    broadcast_msg(msg, conn)


        threading.Thread(target=handle_client_connection, args=(conn, client_address)).start()
