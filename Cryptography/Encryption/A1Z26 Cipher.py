import string
import math


def a1z26_cipher(*args):
    message = ""
    for i in args:
        message += i + " "
    message = message.rstrip()
    message = message.split(" ")

    alphabet_dict = {c: i for i, c in enumerate(string.ascii_lowercase)}
    new_message = ""

    for i in message:
        word = i.lower()
        new_word = ""
        for j in word:
            if (j == "!") or (j == "?") or (j == ",") or (j == ".") or (j == ";") or (j == ":") \
                    or (j == "_") or (j == "-") or (j == "'") or (j == '"'):
                new_word += j
            else:
                number = alphabet_dict[j] + 1
                new_word += str(int(number)) + "-"
        new_word = new_word[:-1]

        new_message += new_word + " "
    new_message = new_message

    return new_message


print(a1z26_cipher("Hello my dear friends"))
print(a1z26_cipher("ah, hh"))
