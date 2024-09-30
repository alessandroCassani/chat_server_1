import socket
from sys import argv

HOST = "0.0.0.0"
DEFAULT_PORT = 8080


def main():
    try:
        port = int(argv[1])
    except:
        port = DEFAULT_PORT

    print(f"Server started on port {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen()
        
        print("Waiting for a client...")
        conn, addr = s.accept()
        print('new connection established!')
        
        with conn:
            data = conn.recv(1024)
            if not data:
                print('empty string received!')
            else:
                print(f'data received form the client {data}')
            
            print('connection closed')
        
        print('socket closed')
    


if __name__ == "__main__":
    main()