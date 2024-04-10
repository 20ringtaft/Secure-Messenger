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
    #using a stream is more secure than a datagram
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STERAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST,PORT))
    #wait for 10 possible clients
    server_socket.listen(10)
    
    SOCKET_LIST.append(server_socket)
    
    print ("Server initializing ... Success. Established on port " + str(PORT))
    
    while 1:
        ready_to_read, ready_to_wrote, in_error = select.select(SOCKET_LIST, [], [], 0)
        
        for sock in ready_to_read: 
            #handles new connections
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print ("Client (%s, %s) connected" % addr)
                
                broadcast(server_socket, sockfd, "[%s:%s] entered the chat room \n % addr")
                
            else:
                try: 
                    data = sock.recv(RECV_BUFFER)
                    if data: 
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                    else: 
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                            
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                        continue
                except: 
                    broadcast(server_socket, sock, "Client (%s,%s) is offline\n" % addr)
                    continue
    server_socket.close()  
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST: 
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except: 
                socket.close
                if socket in SOCKET_LIST: 
                    SOCKET_LIST.remove(socket)
                    
if __name__ == "__main__":
    sys.exit(server())
                