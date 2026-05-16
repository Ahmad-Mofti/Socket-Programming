import socket
import threading

client = socket.socket()
client.connect(("127.0.0.1", 12345))
print("Connected to server")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    message = input()

    client.send(message.encode())

    if message == "/exit":
        break

client.close()