def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = "racecar"
print(is_palindrome(word))
