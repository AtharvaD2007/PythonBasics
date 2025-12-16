contacts = {}
print("1. Check a contact")
print("2. Add contacts")
choice = input("Choose an option: ")
if choice == "1":
    name = input("Enter name to check: ")
    if name in contacts:
        print("Number:", contacts[name])
    else:
        print("Contact not found")
elif choice == "2":
    while True:
        name = input("Enter name (or stop): ")
        if name == "stop":
            break
        number = input("Enter number: ")
        contacts[name] = number