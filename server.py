import socket
import threading

server = socket.socket()
server.bind(("127.0.0.1", 12345))
server.listen()
print("Server is running...")

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                pass


def handle_client(client_socket, client_address):

    print(f"{client_address} Connected")
    clients.append(client_socket)

    try:
        while True:

            message = client_socket.recv(1024)

            if not message:
                break

            text = message.decode()

            if text == "/exit":
                break

            msg = f"{client_address}: {text}".encode()
            print(msg.decode())

            broadcast(msg, client_socket)

    except:
        pass

    clients.remove(client_socket)
    client_socket.close()
    print(f"{client_address} Disconnected")


while True:
    client_socket, client_address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    thread.start()