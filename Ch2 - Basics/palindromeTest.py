def clean_text(string_to_test):
    string_to_test = string_to_test.lower()
    for char in string_to_test:
        if not char.isalnum():
            string_to_test = string_to_test.replace(char, "")
    return string_to_test


def is_palindrome(string_to_test):
    if string_to_test == string_to_test[::-1]:
        return True
    return False


def get_text_from_user():
    string_to_test = input("Enter a string to test for palindrome or 'exit': ")
    if clean_text(string_to_test) == "exit":
        print("Thanks for using this software. Good bye!")
        raise SystemExit
    return string_to_test


stringToTest = get_text_from_user()
while stringToTest != "exit":
    stringToTest = clean_text(stringToTest)
    print("The result of palindrome test for text '", stringToTest, "': ", is_palindrome(stringToTest))
    stringToTest = get_text_from_user()
