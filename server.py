#serverside code
import socket
import sys
import select

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STERAM)