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
        direction = conn.recv(Size).decode(FORMAT)
        if(direction == "Login"):
            loginData = conn.recv(Size).decode(FORMAT)
            loginData = loginData.split()
            
            if logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]):
                print(logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]))
                conn.send("True".encode(FORMAT))
            else:
                print(logic.checkdata(loginData[0], loginData[1], loginData[2], loginData[3]))
                conn.send("False".encode(FORMAT))  
        elif (direction == "Reg"):
            regData = conn.recv(Size).decode(FORMAT)
            regData = regData.split()
            
            #Fname, Lname, Pass, Gmail, Address, Mobile, Age
            
            if logic.checkdata(regData[0], regData[1], regData[2], regData[4], regData[5], regData[6]):
                print(logic.checkdata(regData[0], regData[1], regData[2], regData[4], regData[5], regData[6]))
                conn.send("True".encode(FORMAT))
            else:
                print(logic.checkdata(regData[0], regData[1], regData[2], regData[4], regData[5], regData[6]))
                conn.send("False".encode(FORMAT))
                
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