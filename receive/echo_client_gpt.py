import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's IP and port
server = "192.168.195.134"
server_address = (server, 1234)
client_socket.connect(server_address)

try:
    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.sendall(message.encode('utf-8'))

        # Receive the response from the server
        data = client_socket.recv(1024)
        if data:
            response = data.decode('utf-8')
            print(f"Server response: {response}")

finally:
    # Clean up the connection
    client_socket.close()
