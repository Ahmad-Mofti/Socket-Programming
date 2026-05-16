import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import datetime


# Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

name = input("Enter your username: ")
client.send(name.encode())


# GUI
window = tk.Tk()
window.title(f"Chat - {name}")
window.geometry("600x600")
window.configure(bg="#1e1e1e")
window.minsize(500, 500)


chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    bg="#252526",
    fg="white",
    font=("Consolas", 11)
)

chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state="disabled")


input_frame = tk.Frame(window, bg="#1e1e1e")
input_frame.pack(fill=tk.X, padx=10, pady=10)


message_input = tk.Entry(
    input_frame,
    bg="#3c3c3c",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11)
)

message_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
message_input.focus()


def add_message(msg):
    chat_area.config(state="normal")
    chat_area.insert(tk.END, msg + "\n")
    chat_area.config(state="disabled")
    chat_area.yview(tk.END)


# Receive
def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            add_message(msg)
        except:
            add_message("[SYSTEM] Disconnected from server")
            break


# Send
def send_message(event=None):

    message = message_input.get().strip()

    if message == "":
        return

    time = datetime.datetime.now().strftime("%H:%M:%S")

    # Exit
    if message == "/exit":
        try:
            client.send("/exit".encode())
            client.close()
        except:
            pass

        window.destroy()
        return

    # Users
    if message == "/users":
        client.send("/users".encode())
        message_input.delete(0, tk.END)
        return

    # Private message
    if message.startswith("@"):

        try:
            target, pm = message.split(" ", 1)

            add_message(
                f"You (pm to {target[1:]}): [{time}] {pm}"
            )

            client.send(message.encode())

        except:
            add_message("[SYSTEM] Invalid PM format")

        message_input.delete(0, tk.END)
        return

    # Normal message
    final_msg = f"[{time}] {message}"

    add_message(f"You: {final_msg}")

    try:
        client.send(final_msg.encode())
    except:
        add_message("[SYSTEM] Failed to send message")

    message_input.delete(0, tk.END)


send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#0e639c",
    fg="white",
    relief=tk.FLAT
)

send_button.pack(side=tk.RIGHT)


message_input.bind("<Return>", send_message)


# Thread
threading.Thread(
    target=receive_messages,
    daemon=True
).start()


# Close
def on_close():
    try:
        client.send("/exit".encode())
        client.close()
    except:
        pass
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)


window.mainloop()