import re
import sys

def reverse_string(text):
    if len(text) == 0:
        return ''
    return reverse_string(text[1:]) + text[0]


def strip_text(text):
    stripped_text = re.sub('[^A-Za-z]', '', text)
    return stripped_text.lower()

def is_palindrome(text):
    stripped_text = strip_text(text)

    backwards_text = reverse_string(stripped_text)

    return backwards_text == stripped_text

def get_input():
    if len(sys.argv) == 2:
        user_text_file = open(sys.argv[1])

    else:
        if len(sys.argv) > 2:
            print("I can only accept one argument from the command line.")

        user_text_file = input("What file do you want to check for palindromes? ")
        user_text_file = open(user_text_file)

    return user_text_file


def line_by_line(counter):
    return counter + 1


def main():
    user_text_file = get_input()

    line_number = 0

    for line in user_text_file:
        line_by_line(line_number)

        if is_palindrome(line):
            print(line_number, "//", "Congratulations! That's a palindrome.")

        else:
            print(line_number, "//", "That is not a palindrome.")


if __name__ == '__main__':
    main()
