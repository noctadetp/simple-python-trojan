import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server IP and port
server_ip = "SERVER_IP"
server_port = SERVER_PORT

# Bind the server to the IP and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Receive and send data to the client
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("Received from client:", data)
    response = "Server received your message: " + data
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
