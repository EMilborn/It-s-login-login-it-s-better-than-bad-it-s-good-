def register(username, password):
    with open("data/info.csv") as f:
        lines = f.readlines()
    for line in lines:
        user = line.split(',')[0]
        if user == username:
            return False
    with open("data/info.csv", "a") as f:
        f.write(username + "," + password + "\n")
    return True

def login(username, password):
    
    with open("data/info.csv") as f:
        lines = f.readlines()
    for line in lines:
        un = line.split(',')[0]
        pw = line.split(',')[1][:-1]
        if un == username and pw == password:
            return True
    return False
    
    
