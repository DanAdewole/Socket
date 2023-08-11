import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (1 connection at a time)
server_socket.listen(1)

print("Server is up and listening...")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print("Connection established with:", client_address)

        while True:
            data = connection.recv(1024)
            if data:
                message = data.decode('utf-8')
                print(f"Received: {message}")

                # Echo back the message to the client
                connection.sendall(data)
            else:
                print("Connection closed by the client.")
                break

    finally:
        # Clean up the connection
        connection.close()
