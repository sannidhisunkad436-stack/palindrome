# check if the given string is palindrome or not
def is_palindrome(s):
    if len(s) < 4:
        raise ValueError("Input must have at least 4 characters.")
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    try:
        result = is_palindrome(user_input)
        print(result)
    except ValueError as e:
        print("Error:", e)
