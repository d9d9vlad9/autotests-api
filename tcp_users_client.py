import socket

def connect_and_send(message: str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

def client_1():
    connect_and_send("Привет, сервер!")

def client_2():
    connect_and_send("Как дела?")

if __name__ == '__main__':
    client_1()
    client_2()