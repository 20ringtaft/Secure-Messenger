import sys
import socket
import select
 
def client():
    if(len(sys.argv) < 3) :
        print('Usage : python chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()
     
    print('Connected to remote host. You can start sending messages')
    print('[Me] ', end='', flush=True)
     
    while True:
        socket_list = [s]
         
        ready_to_read, _, _ = select.select(socket_list, [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:
                    print(data.decode(), end='', flush=True)
                    print('[Me] ', end='', flush=True)
            
        try:
            msg = sys.stdin.readline()
            s.send(msg.encode())
        except KeyboardInterrupt:
            print("\nClosing connection...")
            s.close()
            sys.exit()

if __name__ == "__main__":
    client()
