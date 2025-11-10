import socket
import threading

HOST = "127.0.0.1"
PORT = 80
clients = []  # list to store all connected clients

def broadcast(message, sender):
    """Send a message to all clients except the sender."""
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client, addr):
    print(f"✅ New connection from {addr}")
    while True:
        try:
            message = client.recv(4096)
            if not message:
                break
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"🔒 Secure Chat Server Started on port {PORT}")

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
