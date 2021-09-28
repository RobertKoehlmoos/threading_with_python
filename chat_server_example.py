"""
Writing a multi-threaded server can be hard. This example is provided just in case you get absolutely stuck.
Please do not just copy it, but if you are completely stuck you can check and see how certain issues were
overcome.
"""

import socket
import threading


def handle_client(conn: socket.socket, all_clients: dict[str, socket.socket], clients_lock: threading.Lock):
    name = ""
    try:
        conn.sendall(b"Welcome to my chatroom!\n")
        # this first loop gets the user's name
        while not name:
            conn.sendall(b"Please enter your name for this room: ")
            name = conn.recv(1024).decode("utf-8").strip()
            if not name:
                conn.close()
                return
            elif name in all_clients:
                conn.sendall(b"Name already in use\n")
                name = ""
        # then the user's name and connection are added to the clients dictionary
        clients_lock.acquire()
        all_clients[name] = conn
        clients_lock.release()
        # lastly, the thread loops to receive any messages from the client. It sends these messages out to
        # all the other clients, and then waits for the next one.
        while msg := conn.recv(1024):
            clients_lock.acquire()
            for client_name, connection in all_clients.items():
                if name != client_name:
                    connection.sendall(bytes(name + ": ", "utf-8") + msg)
            clients_lock.release()
    except ConnectionResetError:  # this is the error that occurs when the client socket is shut down forcefully.
        print(f"Connection with {name} closed")
    # after reaching the end, the thread closes the connection on it's end and removes it's client from the dictionary
    conn.close()
    clients_lock.acquire()
    del all_clients[name]
    clients_lock.release()


def chat_server(port: int):
    clients = {}
    clients_lock = threading.Lock()  # lock for threads accessing the clients dictionary
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"Received connection from {addr}")
            threading.Thread(target=handle_client, args=(conn, clients, clients_lock)).start()


if __name__ == "__main__":
    chat_server(7777)
