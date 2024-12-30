import socket
import threading
import tkinter as tk

# Global variables
player_positions = {"player1": (50, 50), "player2": (150, 150)}
player = "player1"
other_player = "player2"
terrain = []

def receive_messages(client_socket, canvas, players):
    global player_positions, terrain
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data.startswith("TERRAIN:"):
                terrain_data = data.split(":")[1]
                terrain = [
                    tuple(map(int, obs.split(":")))
                    for obs in terrain_data.split(",")
                ]
                update_terrain(canvas)
            else:
                parts = data.split(":")
                if parts[0] in player_positions:
                    key, x, y = parts[:3]
                    player_positions[key] = (int(x), int(y))
                    update_canvas(canvas, players)
        except:
            client_socket.close()
            break

def update_terrain(canvas):
    """Render terrain from server data."""
    canvas.delete("terrain")  # Clear old terrain
    for x, y, w, h in terrain:
        canvas.create_rectangle(x, y, x + w, y + h, fill="black", tags="terrain")

def update_canvas(canvas, players):
    canvas.coords(players[player], *player_positions[player], player_positions[player][0] + 20, player_positions[player][1] + 20)
    canvas.coords(players[other_player], *player_positions[other_player], player_positions[other_player][0] + 20, player_positions[other_player][1] + 20)

def move_player(event, canvas, players):
    global player_positions
    x, y = player_positions[player]

    if event.keysym == "Left":
        x = max(0, x - 10)
    elif event.keysym == "Right":
        x = min(400, x + 10)

    player_positions[player] = (x, y)
    update_canvas(canvas, players)

def connect_to_server(canvas, players):
    host = input("Enter server IP address: ")
    port = int(input("Enter server port: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_messages, args=(client_socket, canvas, players)).start()

def main():
    global player, other_player

    # Create the GUI window
    root = tk.Tk()
    root.title("LAN Platformer")
    root.geometry("500x500")

    # Canvas for the game area
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

    # Create player objects on the canvas
    players = {
        "player1": canvas.create_rectangle(50, 50, 70, 70, fill="blue"),
        "player2": canvas.create_rectangle(150, 150, 170, 170, fill="red"),
    }

    # Start networking
    threading.Thread(target=connect_to_server, args=(canvas, players)).start()

    # Bind key events for player movement
    root.bind("<KeyPress>", lambda event: move_player(event, canvas, players))

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
