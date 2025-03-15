
from utilis import greet_user

def main():
    name = input("Enter your Name: ")
    message = greet_user(name)
    print(message)

if  __name__ == "__main__": 
    main()
