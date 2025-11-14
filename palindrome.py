# check if the given string is palindrome or not
s = input("Enter a string: ")

if len(s) < 4:
    print("Error: Input must have at least 4 characters.")
else:
    if s == s[::-1]:
        print(True)
    else:
        print(False)
