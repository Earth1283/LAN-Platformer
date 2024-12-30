import socket
import threading
import random
import time

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345
clients = []
terrain_data = []

def generate_terrain():
    """Generate random terrain periodically."""
    global terrain_data
    while True:
        terrain_data = [
            (random.randint(0, 350), random.randint(200, 350), 50, 10)
            for _ in range(5)  # Generate 5 obstacles
        ]
        broadcast_terrain()
        time.sleep(5)  # Update terrain every 5 seconds

def handle_client(client_socket, address):
    print(f"New connection: {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            broadcast(data, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def broadcast_terrain():
    """Send terrain data to all clients."""
    terrain_message = "TERRAIN:" + ",".join(
        f"{x}:{y}:{w}:{h}" for x, y, w, h in terrain_data
    )
    for client in clients:
        try:
            client.send(terrain_message.encode())
        except:
            clients.remove(client)

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print(f"Server started on {HOST}:{PORT}")
    
    threading.Thread(target=generate_terrain).start()  # Start terrain generation

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    server()
