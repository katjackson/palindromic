import re

def reverse_string(text):
    backwards_text = ''
    text = list(text)
    while text != []:
        backwards_text += text.pop()
    return backwards_text

def strip_text(text):
    stripped_text = re.sub('[^A-Za-z]', '', text)
    stripped_text = stripped_text.lower()
    return stripped_text

def is_palindrome(text):
    stripped_text = strip_text(text)

    backwards_text = reverse_string(stripped_text)

    if backwards_text == stripped_text:
        return True
    else:
        return False

def main():
    user_text = input("Enter your text: ")

    if is_palindrome(text):
        print("Congratulations! That's a palindrome.")
    else:
        print("Sorry. That is not a palindrome.")


if __name__ == '__main__':
    main()
