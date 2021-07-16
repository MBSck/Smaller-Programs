import string
import numpy as np

_name_ = "_CaesarCipher_"


class CaesarCipher:
    def __init__(self):

        self.alp_list = []
        for i in string.ascii_lowercase:
            self.alp_list.append(i)
        self.alp_list = np.array(self.alp_list)

    def format_message(self, *args: str):
        message = ""
        for i in args:
            message += i + " "
            message = message.rstrip()
            message = message.split(" ")

        return message

    def encrypt(self, *args: str, key=-3):
        message = self.format_message(*args)
        new_message = ""

        for i in message:
            word = i.lower()
            new_word = ""

            for j in word:
                if (j == "!") or (j == "?") or (j == ",") or (j == ".") or (j == ";") or (j == ":") \
                        or (j == "_") or (j == "-") or (j == "'") or (j == '"'):
                    new_word += j

                else:
                    index = np.where(j == self.alp_list)
                    new_word += np.array_str(np.roll(self.alp_list, key)[index])[2:-2]

            new_message += new_word + " "
        new_message = new_message

        return new_message

    def decrypt(self, *args: str, key=3, brute_force=False):
        message = self.format_message(*args)
        new_message = ""

        if brute_force:

            sentence_list = []

            # reads words document
            with open("words.txt", "r") as f:
                english_words = f.read()

            for i in range(-25, 26):
                temp = self.decrypt(*args, key=i)
                temp_formatted = self.format_message(temp)

                # Add binary search

                for i in temp_formatted:
                    if i in english_words:
                        sentence_list.append(temp)

            sentence_iterator = iter(sentence_list)
            inp = "n"

            while inp != "Y":
                print("Can this be your sentence?")
                print(next(sentence_iterator))
                inp = input("[Y/n]: ")


        else:

            for i in message:
                word = i.lower()
                new_word = ""

                for j in word:
                    if (j == "!") or (j == "?") or (j == ",") or (j == ".") or (j == ";") or (j == ":") \
                            or (j == "_") or (j == "-") or (j == "'") or (j == '"'):
                        new_word += j

                    else:
                        index = np.where(j == self.alp_list)
                        new_word += np.array_str(np.roll(self.alp_list, key)[index])[2:-2]

                new_message += new_word + " "
            new_message = new_message

        return new_message


if _name_ == "_CaesarCipher_":
    msg = "My Name is Peter Pedigrew!"
    caesar = CaesarCipher()
    ce_en = caesar.encrypt(msg, key=-14)
    print(ce_en)
    ce_de = caesar.decrypt(ce_en, brute_force=True)
    print(ce_de)



