def main():
    print("----Welcome to Email splitter-----")
    print("") #TESST

    emailInput= input("Enter your email address : ")

    (username,domain)= emailInput.split("@")
    (domain,extension)= domain.split(".")

    print("Username : ",username)
    print("Domain : ",domain)
    print("Extension : ",extension)

main()
