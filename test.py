import socket
import json

# Define the host and port to listen on
host = 'hostip'
port = 12345

# Create a socket to listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    print(f"Listening for connections on {host}:{port}")
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")

        # Receive the data
        data = conn.recv(1024)

        # Decode the received data and load it as JSON
        received_json = json.loads(data.decode())
        print('Received JSON:', received_json)