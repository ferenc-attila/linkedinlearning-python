result = True

# Is there any nicer solution?
stringToTest = ""

while stringToTest != "exit":
    stringToTest = input("Enter a string to test for palindrome or 'exit':")
    stringToTest = stringToTest.lower()
    for character in stringToTest:
        if not character.isalnum():
            stringToTest = stringToTest.replace(character, "")

    print(stringToTest)

    if stringToTest == "exit":
        print("Thanks for using this software. Good bye!")
        raise SystemExit

    for indexOfCharacter in range(0, (stringToTest.__len__() / 2).__ceil__()):
        print(stringToTest[indexOfCharacter], "vs.", stringToTest[(indexOfCharacter+1)*-1])
        if stringToTest[indexOfCharacter] != stringToTest[(indexOfCharacter + 1) * -1]:
            result = False

    print(result)
