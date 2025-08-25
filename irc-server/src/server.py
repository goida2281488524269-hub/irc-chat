import socket
import threading
from config import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

connected_clients = {}

def broadcast(message, sender_socket = None):
    for client_socket in list(connected_clients.keys()):
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                remove_client(client_socket)

def remove_client(client_socket):
    if client_socket in connected_clients:
        nickname = connected_clients[client_socket]["nickname"]
        del connected_clients[client_socket]
        try:
            client_socket.close()
        except:
            pass
        broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
        print(f"Клиент {nickname} отключен.")

def handle_client(client_socket, address):
    client_socket.send('NICK'.encode('utf-8'))
    nickname = client_socket.recv(1024).decode('utf-8')

    connected_clients[client_socket] = {"nickname": nickname, "address": address}
    print(f"Подключился {address} с ником {nickname}")

    broadcast(f'{nickname} присоединился к чату!'.encode('utf-8'))
    client_socket.send('Подключение к серверу установлено!'.encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                raise ConnectionError("Client disconnected")
        except:
            remove_client(client_socket)
            break

def receive():
    print("Сервер запущен и слушает порт...")
    while True:
        client_socket, address = server.accept()
        print(f"Установлено соединение с {address}")

        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == '__main__':
    receive()