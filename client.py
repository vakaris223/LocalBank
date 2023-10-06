import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Client():


    def run():
        client.connect(ADDR)
    
    #send fname, lname, password, pin to server
    def check_login_data( fname, lname, password, pin):
        data = f"{fname} {lname} {password} {pin}"
        SendData(data).encode(FORMAT)
        return bool(ADDR.recv(1024).decode(FORMAT))

    # def SendData(self, data):
    #         data = data.encode(FORMAT)
    #         data_length = len(data)
    #         send_length = str(data_length).encode(FORMAT)
    #         client.send(send_length)
    #         client.send(data)




