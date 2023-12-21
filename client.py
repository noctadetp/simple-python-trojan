import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server IP and port
server_ip = "SERVER_IP"
server_port = SERVER_PORT

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to server:", server_ip)

# Send data to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Server response:", response)

# Close the connection
client_socket.close()
