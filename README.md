# LAN Platformer Game

This is a simple multiplayer platformer game implemented in Python using the tkinter library for the GUI and Python's built-in socket library for networking. The game features real-time player movement, gravity, and server-synchronized terrain generation.

# Features

## Multiplayer Support:

Supports multiple players over a LAN connection.

Player positions are synchronized across all clients.

## Gravity:

Gravity pulls players downward unless they are on the ground or obstacles.

## Server-Synchronized Terrain:

Terrain is generated on the server and broadcast to all clients.

Clients render the same terrain for consistent gameplay.

## Real-Time Updates:

Player movements and terrain changes are updated in real-time.

# Installation

## Requirements

Python 3.6 or later.

No external libraries are required (uses built-in Python libraries).

## Files

server.py: The server-side script for managing player positions and terrain generation.

client.py: The client-side script for player control and rendering the game.

## How to Run

**Step 1: Start the Server**

Run the server.py script on the host machine:

`python server.py`

The server will display its IP address and port (default: 12345).

**Step 2: Start the Clients**

Run the client.py script on each player's machine:

`python client.py`

Enter the server's IP address and port when prompted.

Use the arrow keys to control the player:

Left Arrow: Move left.

Right Arrow: Move right.

Gameplay

The game takes place on a 400x400 canvas.

Players can move left and right to avoid obstacles.

Gravity will pull players downward, simulating a platformer environment.

Obstacles (terrain) are randomly generated on the server and updated on all clients every 5 seconds.

# Code Structure

## Server

### Terrain Generation:

Generates random obstacles at regular intervals.

Broadcasts terrain data to all clients.

### Player Synchronization:

Receives player positions from clients.

Broadcasts player positions to all clients.

## Client

### GUI Rendering:

Uses tkinter to render the game canvas and player objects.

Displays terrain and player movements in real-time.

### Networking:

Connects to the server for receiving terrain and player data.

Sends player movement data to the server.

# 🛠️Troubleshooting

## ❓Common Issues

### Terrain Doesn't Generate:

Ensure the server is running and broadcasting terrain.

Check server logs for terrain generation messages.

### Client Cannot Connect:

Verify the server IP address and port.

Ensure the server is accessible over the network.

### Laggy Gameplay:

Ensure all machines are on the same LAN.

Minimize network congestion.

# 🌟Future Enhancements

Add collision detection for players and obstacles.

Implement jumping and more advanced physics.

Introduce a scoring system.

Expand terrain features with platforms and moving obstacles.

# License

This project is proudly released under the MIT License.

