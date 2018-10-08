import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)


def main():
    string = input('Choose a word to encrypt: ')
    word = []
    bw = []
    password = ''
    max = len(string)

    for letter in string:
        word.extend(letter.lower())

    index = 0
    while index < max:
        for i in range(26):
            if data["alphabet"][i - 1]["letter"] == word[index]:
                bw.append(data["alphabet"][i - 1]["code"][::-1])

        index += 1

    print(20 * '-')

    counter = 0
    while counter < max:
        for i in range(26):
            if data["alphabet"][i - 1]["code"] == bw[counter]:
                password += data["alphabet"][i - 1]["letter"]

        counter += 1

    print('Encrypted word: ' + password)
    exit = input('Do you wanna quit (y, n)')
    if exit.lower() == 'n':
        main()


if __name__ == "__main__":
    main()
