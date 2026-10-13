# times.py: prints the multiplication table of any number
number = int(input("Which table? "))
for i in range(1, 21):
    print(f"{number} x {i} = {number * i}")