import string
import math


def atbash_cipher(*args):
    message = ""
    for i in args:
        message += i + " "
    message = message.rstrip()
    message = message.split(" ")

    alphabet_dict = {c: i for i, c in enumerate(string.ascii_lowercase)}
    numbers_first_dict = {i: c for i, c in enumerate(string.ascii_lowercase)}
    new_message = ""

    for i in message:
        word = i.lower()
        new_word = ""
        for j in word:
            if (j == "!") or (j == "?") or (j == ",") or (j == ".") or (j == ";") or (j == ":") \
                    or (j == "_") or (j == "-") or (j == "'") or (j == '"'):
                new_word += j
            else:
                number = math.sqrt((alphabet_dict[j] - 25)**2)
                new_word += numbers_first_dict[number]

        new_message += new_word + " "
    new_message = new_message

    return new_message


print(atbash_cipher("Hello my dear friends"))
