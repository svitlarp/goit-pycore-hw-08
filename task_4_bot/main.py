import pickle 
import constants
from input_parser import parse_cmd
from phone_book import AddressBook, Record, Birthday, Phone

def save_data(book, filename='addressbook.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(book, file)

def load_data(filename='addressbook.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()        # if file not found return a new AddressBook

book = load_data()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError) as err:
            return f"Contact error: {err}"
        except Exception as err:
            return f"Unexpected error occurred: {err}"
    return inner

@input_error
def main():
    '''
    The main function which controls the main command processing loop.
    '''

    print('"How can I help you?\n"')
    print(constants.MENU)
    # Ask user which action he wants to do with a phone_book
    

    # Call parse_input() function to extract desired action from input string using python unpacking
    while True:
        user_input = input('Enter what you wonna do with your phone_book:\n')
        action, args = parse_cmd(user_input)
        # Building a simple match-case statement
        match action:
            case 'add':
                name, phone = args
                print(f"{add_contact(name, phone)}\n")
            case 'change':
                name, old, new = args
                print(f"{change_contact(name, old, new)}\n")
            case 'phone':
                print(f"{show_phone(args[0])}\n")
            case 'all':
                print(f"{show_all()}\n")
            case 'add-birthday':
                name, birthday = args
                print(f"{add_birthday(name, birthday)}\n")
            case 'show-birthday':
                print(f"{show_birthday(args[0])}\n")        
            case 'birthdays':
                print(f'{birthdays()}\n')     
            case 'exit':
                save_data(book)
                print('Good bye!')
                break
            case _:
                print(f"Command not supported: '{action}', Supported actions are: \n{constants.MENU}");

@input_error
def add_contact(name: str, phone: str) -> str:
    existing = book.find(name)
    if(not existing):
        existing = book.add_record(Record(name))
    existing.add_phone(phone)
    return f"Phone for '{name}' added"


@input_error
def change_contact(name, old_phone, phone_to_update):
    existing = book.find(name)
    if not existing:
        raise ValueError("no such contact")
    if existing.edit_phone(old_phone, phone_to_update):
        return "contact updated"
    else:
        raise ValueError("no such phone for contact")

@input_error
def show_phone(name):
    existing = book.find(name)
    if not existing:
        raise ValueError("no such contact")
    return f"Phones: {'; '.join(p.value for p in existing.phones)}"

def show_all():
    return f"All book: {book}"

@input_error
def add_birthday(name, birthday):
    existing = book.find(name)
    if not existing:
        raise ValueError("no such contact")
    existing.add_birthday(birthday)
    return "birthday added"

@input_error
def show_birthday(name):
    existing = book.find(name)
    if not existing:
        raise ValueError("no such contact")
    return existing.birthday

@input_error
def birthdays():
    # If no birthday
    return book.get_upcoming_birthdays()
   

if __name__ == "main":
    print('Hello')
    main()

main()
