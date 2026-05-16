import socket

client = socket.socket()
client.connect(("127.0.0.1", 12345))

print("Connected to server")

while True:

    message = input("You: ")
    client.send(message.encode())

    if message == "/exit":
        break

    response = client.recv(1024).decode()
    print("Server:", response)

client.close()