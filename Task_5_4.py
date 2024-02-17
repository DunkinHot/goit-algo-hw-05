def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except TypeError:
            return "Wrong type of data"
        except KeyError:
            return "Wrong key value"
        except IndexError:
            return "Enter the argument for the command"
        except Exception as Error:
            return f"Error: {Error}"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contacts(args,contacts):
    name,phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contacts(args, contacts)
    else:
        return "No such name in the base"
@input_error
def show_phone(args,contacts):
    return (f"His phone number is: {contacts[args[0]]}")

@input_error
def show_all(args,contacts):
    list=''
    for key in contacts:
        list+=(f"{key:10} : {contacts[key]}\n")
    return list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args,contacts))  
        elif command == "change":
            print(change_contact(args,contacts)) 
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(args,contacts))
        else:
            print("Invalid command.")
    
if __name__ == "__main__":
    main()