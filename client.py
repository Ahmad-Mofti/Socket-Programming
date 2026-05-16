import socket

client = socket.socket()
client.connect(("127.0.0.1", 12345))

client.send("Hello Server".encode())
message = client.recv(1024).decode()
print("Server says:", message)

client.close()