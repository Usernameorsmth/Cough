# Python program to demonstrate
# exit()

for i in range(10):
    # If the value of i becomes
    # 5 then the program is forced
    # to exit
    if i == 5:
        # prints the exit message
        print(exit) # Note: This will print the exit function object, not a message
        exit()
    print(i)