#Serverside program
#Created by: Daniel Nam, Taft Ring, and Robert Tabares
#CS 3800.01
#April 13 2024

#The purpose of this program is to provide a secure client server chat application that can queue up to 10 users. 
import socket
import sys
import select

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STERAM)