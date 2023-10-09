import socket
import threading
import logic

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
        # try:
        loginData = conn.recv(Size).decode(FORMAT)
        loginData = loginData.split()
        
        if logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]):
            print(logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]))
            conn.send("True".encode(FORMAT))
        else:
            print(logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]))
            conn.send("False".encode(FORMAT))
        # except socket.error as e:
        #     print(f"[DISCONNECTED] {addr}")
        #     connected = False
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