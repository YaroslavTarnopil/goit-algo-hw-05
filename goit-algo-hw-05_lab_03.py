def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Enter user name"
            elif isinstance(e, ValueError):
                return "Give me name and phone please"
            elif isinstance(e, IndexError):
                return "Index out of range"
    return wrapper

contacts = {}

@input_error
def add_contact(command):
    parts = command.split()
    if len(parts) < 2:
        raise ValueError
    name, *phone = parts[1:]
    phone = " ".join(phone)
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(command):
    name = command.split()[1]
    return contacts.get(name, "Contact not found.")

@input_error
def get_all_contacts(command):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

while True:
    command = input("Enter a command: ").strip()
    if not command:
        break

    if command.startswith("add"):
        print(add_contact(command))
    elif command.startswith("phone"):
        print(get_contact(command))
    elif command.startswith("all"):
        print(get_all_contacts(command))