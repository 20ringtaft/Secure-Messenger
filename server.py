#Serverside program
#Created by: Daniel Nam, Taft Ring, and Robert Tabares
#CS 3800.01
#April 13 2024

#The purpose of this program is to provide a secure client server chat application that can queue up to 10 users. 

import threading
import socket

#local host
host = '127.0.0.1'
#unused port number
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle_clients(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
def receive():
    while True:
        print("server connection established")
        client, address = server.accept()
        print(f'connection is established with {str{address}}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'This user is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected'.encode('utf-8'))
        client.send('user connected'.encode('utf-8'))
        thread = threading.Thread(target=handle_clients, args=(client,))
        thread.start()
        
if __name__ == "__main__":
    receive()