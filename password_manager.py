from cryptography.fernet import Fernet

# def write_key():          # create a key  only one time then comment it
#     key=Fernet.generate_key()
#     with open("miniprojects/key.key",'wb') as f:
#         f.write(key)
# write_key()        
def load_key():           # to load the same key
    with open("miniprojects/key.key",'rb') as f:
        key=f.read()
    return key    

print("________welcome to the passwerd Manager________")

key=load_key()
ciper=Fernet(key)        # to create the object of the fernat key to encrypt and dycript
def view():              # to view the password   
    with open("miniprojects/user.txt", "r") as f:
        for line in f.readlines():
            data=line.strip()
            if " | " not in data:
                print(f"⚠️ Skipping malformed line: {data}")
                continue
            user,password=data.split(" | ")
            print("user : "+user + " | " + "password : "+ ciper.decrypt(password.encode()).decode()) # first of all encode to byte then decrypt and then decode to string

def add():              # to add the password
    name = input("Enter your name : ")
    password = input("Enter youru password : ")
    with open ("miniprojects/user.txt",'a') as f:
        passw=ciper.encrypt(password.encode()).decode()
        f.write(f"{name} | {passw}\n")    # first of all encode passw to byte then encrypt it and then decode to string 
        print("Account created successfully")


while True:
    mode=input("enter the mode you want (view/add) or q to quit ? ")
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()