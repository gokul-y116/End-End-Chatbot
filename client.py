import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from crypto_core import encrypt_message, decrypt_message, load_public_key, load_private_key

HOST = " 192.168.56.1"
PORT = 80

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        # Load keys
        self.private_key = load_private_key(f"{username.lower().replace(' ', '_')}_private.pem")
        friend_key_file = input("Enter friend's public key file: ")
        self.friend_key = load_public_key(friend_key_file)

        # Tkinter GUI
        self.window = tk.Tk()
        self.window.title(f"Secure Chat - {username}")

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=50, height=20, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.msg_entry = tk.Entry(self.window, width=40)
        self.msg_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        send_btn = tk.Button(self.window, text="Send", command=self.send_message)
        send_btn.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.window.mainloop()

    def send_message(self):
        message = self.msg_entry.get()
        if message:
            try:
                encrypted_msg = encrypt_message(self.friend_key, f"{self.username}: {message}")
                self.sock.send(encrypted_msg)
                self.display_message(f"You: {message}")
                self.msg_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def receive_messages(self):
        while True:
            try:
                encrypted_msg = self.sock.recv(4096)
                if not encrypted_msg:
                    break
                decrypted_msg = decrypt_message(self.private_key, encrypted_msg)
                self.display_message(decrypted_msg)
            except:
                break

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    username = input("Enter your username: ")
    ChatClient(username)
