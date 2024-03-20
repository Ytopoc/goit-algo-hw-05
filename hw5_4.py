#Декоратири 
def input_error_add_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner
    

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Invalid command."

    return inner
def input_error_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError,IndexError):
            return "Give me name please."
        except KeyError: 
            return "No contacts found."  
    return inner

#Внутрішні функції

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_add_change
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Such a contact already exists, you can change the phone number using the \"change\" "
    contacts[name] = phone
    return "Contact added."

@input_error_add_change
def change_phone(args, contacts):
    name, phone = args
    if name not in contacts:
        return "No contacts found."
    contacts[name] = phone
    return "Contact changed."

@input_error_phone
def phone_contact(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(contacts, args=None):
    if args:
        return "I need only command \"all\" "
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts:"
        for name, phone in contacts.items():
            result += f"\n{name}: {phone}"
        return result
 

    
#Головна функція

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello" or command=="hi":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args,contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all" or command=="show":
            print(show_all(contacts, args)) 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()