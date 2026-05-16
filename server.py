import socket
import threading

server = socket.socket()
server.bind(("127.0.0.1", 12345))
server.listen()

print("Server is running...")


def handle_client(client_socket, client_address):

    print(f"{client_address} Connected")

    try:
        while True:

            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message == "/exit":
                break

            print(f"{client_address}: {message}")

            response = f"I received your message, client {client_address[0]}:{client_address[1]}"
            client_socket.send(response.encode())

    except Exception as e:
        print(f"[ERROR] {client_address}: {e}")

    finally:
        client_socket.close()
        print(f"{client_address} Disconnected")


while True:
    client_socket, client_address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    thread.start()