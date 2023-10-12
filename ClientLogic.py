import re

def ageValid(age):
    if(age >= 18):
        return True
    else:
        return False
    
    
def gmailValid(gmail):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.match(pat, gmail)):
        return True
    else:
        return False
    
    
def FnameValid(Fname):
    if(len(Fname) >= 1 and len(Fname) <= 747):
        return True
    else:
        return False
    

def LnameValid(Lname):
    if(len(Lname) >= 1 and len(Lname) <= 747):
        return True
    else:
        return False
    
# def addressValid(address)
#     if
    
    