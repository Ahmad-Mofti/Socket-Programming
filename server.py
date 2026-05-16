import socket

server = socket.socket()
server.bind(("127.0.0.1", 12345))
server.listen(1)
print("Server is waiting for connection...")

client_socket, client_address = server.accept()
print("Client connected:", client_address)

message = client_socket.recv(1024).decode()
print("Client says:", message)
client_socket.send("Hello Client".encode())

client_socket.close()
server.close()