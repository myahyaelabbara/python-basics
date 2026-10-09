age = int(input("How old are you? "))
on_list = input("Are you on the guest list? (yes/no) ").lower() == "yes"

if age >= 18:
    print("Welcome in!")
elif on_list:
    print("You're on the list. Welcome in!")
else:
    print("Sorry, not tonight.")

print("Next guest, please.")
age = int(input("How old are you? "))
on_list = input("Are you on the guest list? (yes/no) ").lower() == "yes"

if age >= 18:
    print("Welcome in!")
elif on_list:
    print("You're on the list. Welcome in!")
else:
    print("Sorry, not tonight.")

print("Next guest, please.")