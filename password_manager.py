from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    key_file = open("key.key","wb")
    key_file.write(key)
    key_file.close()
    return key

def load_key():
    key_file = open("key.key","rb")
    key = key_file.read()
    key_file.close()
    return key

print("Welcome to password manager!")
generate_pwd_prompt = input("If this is your first run, we need to generate a master key. Do you want to generate it? (y/n): ").lower() == "y"

main_pwd = ""

if generate_pwd_prompt:
    key = generate_key()
    if key:
        main_pwd = key
    else:
        print("Error: Unable to generate master key.")
        exit()  # or handle the error appropriately
else:
    key = load_key()
    if key:
        main_pwd = key
    else:
        print("Error: Unable to load master key.")
        exit()  # or handle the error appropriately

fer = Fernet(key)

def add():
    vault_file = open("vault.txt","a")
    account_site = input("Enter site name (Facebook, Google): ")
    account_name = input("Enter account name (Username/E-mail): ")
    account_password = input("Enter password: ")
    vault_file.write(account_site + "|" + fer.encrypt(account_name.encode()).decode() + "|" + fer.encrypt(account_password.encode()).decode())
    vault_file.close()
    print("Password added!" + "\n")

def view():
    vault_file = open("vault.txt","r")
    for line in vault_file.readlines():
        data = line.rstrip()
        site_name, user, passw = data.split("|")
        print("Site name: ", site_name, "| Username: ",  fer.decrypt(user.encode()).decode(), "| Password: ", fer.decrypt(passw.encode()).decode())
    print("")


while True:
    print("This is you main password vault (Find it on key.key file) (DO NOT LOSE IT!!!): " + main_pwd.decode())
    operation =  input("Select the operation (add, view): ").lower()

    if operation == "add":
        add()
    elif operation == "view":
        view()
    else:
        print("Wrong operation name")