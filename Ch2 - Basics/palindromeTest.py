def clean_text(string_to_test):
    string_to_test = string_to_test.lower()
    for char in string_to_test:
        if not char.isalnum():
            string_to_test = string_to_test.replace(char, "")
    return string_to_test


def is_palindrome(string_to_test):
    for index_of_character in range(0, (string_to_test.__len__() / 2).__ceil__()):
        print(string_to_test[index_of_character], "vs.", string_to_test[(index_of_character+1)*-1])
        if string_to_test[index_of_character] != string_to_test[(index_of_character + 1) * -1]:
            return False
    return True


def get_text_from_user():
    string_to_test = input("Enter a string to test for palindrome or 'exit':")
    if string_to_test == "exit":
        print("Thanks for using this software. Good bye!")
        raise SystemExit
    return string_to_test


stringToTest = get_text_from_user()
while stringToTest != "exit":
    stringToTest = clean_text(stringToTest)
    print(is_palindrome(stringToTest))
