import socket
import threading

Size = 64
PORT = 5050
FORMAT = 'UTF-8'
SERVER = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)

print(SERVER)
print(socket.gethostname())

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(Size).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                print(f"[{addr}] {msg}")
                conn.send("Sent".encode(FORMAT))
            else:
                print(f"[DISCONNECTED] {addr}")
                connected = False
        except socket.error as e:
            print(f"[DISCONNECTED] {addr}")
            connected = False
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        for thread in threading.enumerate():
            print(thread.name)

print("[STARTING] server is starting...")
start()