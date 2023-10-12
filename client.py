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
    def check_login_data(fname, lname, password, pin):
        #to redirect server to do login() function
        rederaction = "Login"
        client.send(rederaction.encode(FORMAT))
        
        data = f"{fname} {lname} {password} {pin}"
        client.send(data.encode(FORMAT))
        if(client.recv(64).decode(FORMAT) == "True"):
            print("Login True")
            return True
        else:
            print("Login False")
            return False
        
    def send_reg_data(Fname, Lname, Pass, Gmail, Address, Mobile, Age):
        #to redirect server to do Registration() function
        rederaction = "Reg"
        client.send(rederaction.encode(FORMAT))
        
        data = f"{Fname} {Lname} {Pass} {Gmail} {Address}, {Mobile}, {Age}"
        client.send(data.encode(FORMAT))
        if(client.recv(64).decode(FORMAT) == "True"):
            print("Reg True")
            return True
        else:
            print("Reg False")
            return False
        

    # def SendData(self, data):
    #         data = data.encode(FORMAT)
    #         data_length = len(data)
    #         send_length = str(data_length).encode(FORMAT)
    #         client.send(send_length)
    #         client.send(data)