def is_palindrome(word):
    split = list(word)
    if split == list(reversed(split)):
        print('It is a palindrome')
        return True
    else:
        print('It is not a palindrome')
        return False

is_palindrome('civic')