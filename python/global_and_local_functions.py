
x = 10  # Global variable

def print_x():
    print(f"Global x: {x}")

print_x()

def change_x():
    x = 20  # Local variable
    print(f"Local x: {x}")

change_x()
print(f"Global x after change_x(): {x}")


#this shows how local and global variables work 
