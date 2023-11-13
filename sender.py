import socket
import json

# Define the host and port to connect to on the host computer
host = 'your_host_ip'
port = 12345

# Sample JSON object to send
data_to_send = {'key': 'value', 'another_key': 42}

# Convert JSON to string
json_string = json.dumps(data_to_send)

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    # Send the JSON string
    s.sendall(json_string.encode())

print('JSON sent successfully')
