import socket
import threading
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen()

print("Server started...")

clients = {}  


def broadcast(message, sender_socket=None):
    for client in list(clients.keys()):
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove_client(client)


def remove_client(client_socket):
    if client_socket in clients:
        name, addr = clients[client_socket]
        print(f"{name} disconnected -> {addr[0]}:{addr[1]}")
        del clients[client_socket]
        client_socket.close()


def handle_client(client_socket, address):

    try:
        name = client_socket.recv(1024).decode()
        clients[client_socket] = (name, address)

        print(f"{name} connected -> {address[0]}:{address[1]}")

        time = datetime.datetime.now().strftime("%H:%M:%S")
        broadcast(f"[{time}] {name} joined the chat".encode())

        while True:

            message = client_socket.recv(1024)

            if not message:
                break

            text = message.decode()

            # Exit
            if text == "/exit":
                break

            # Users list
            if text == "/users":

                users = [
                    f"{n} -> {a[0]}:{a[1]}"
                    for c, (n, a) in clients.items()
                ]

                msg = "[Connected Users]\n" + "\n".join(users)
                client_socket.send(msg.encode())
                continue

            # Private message
            if text.startswith("@"):

                try:
                    target_name, private_msg = text.split(" ", 1)
                    target_name = target_name[1:]

                    sender_name = clients[client_socket][0]

                    sent = False

                    for c, (n, a) in clients.items():
                        if n == target_name:
                            c.send(
                                f"{sender_name} (pm): {private_msg}".encode()
                            )
                            sent = True
                            break

                    if not sent:
                        client_socket.send(
                            "[SYSTEM] User not found".encode()
                        )

                except:
                    client_socket.send(
                        "[SYSTEM] Invalid PM format".encode()
                    )

                continue

            # Normal Broadcast
            sender_name = clients[client_socket][0]

            broadcast(
                f"{sender_name}: {text}".encode(),
                client_socket
            )

    except:
        pass

    time = datetime.datetime.now().strftime("%H:%M:%S")
    broadcast(f"[{time}] {name} left the chat".encode())
    remove_client(client_socket)


while True:
    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )
    thread.start()