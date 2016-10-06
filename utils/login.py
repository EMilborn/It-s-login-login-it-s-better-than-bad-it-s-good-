def register(username, password):
    with open("info.csv") as f:
        lines = f.readlines()
    for line in lines:
        user = line.split(',')[0]
        if user == username:
            return false
    with open("info.csv", "a") as f:
        f.write(username + "," + password)
    return true

def login(username, password):
    
    with open("info.csv") as f:
        lines = f.readlines()
    for line in lines:
        un = line.split(',')[0]
        pw = line.splt(',')[1]
        if un == username:
            if pw == password:
                return true
    return false
    
    
