import json

with open('data.json') as f:
    data = json.load(f)


def main():
    string = input('Choose a word to encrypt: ')
    word = []
    bw = []
    z = ''
    max = len(string)

    for letter in string:
        if letter is not 'j':
            word.extend(letter.lower())
        elif letter is 'j':
            word.extend('i')

    x = 0
    while x < max:
        for i in range(26):
            if data["alphabet"][i - 1]["letter"] == word[x]:
                bw.append(data["alphabet"][i - 1]["code"][::-1])
                
        x += 1

    print(20 * '-')

    y = 0
    while y < max:
        for i in range(26):
            if data["alphabet"][i - 1]["code"] == bw[y]:
                z += data["alphabet"][i - 1]["letter"]    
                
        y += 1

    print('Encrypted word: ' + z)
    exit = input('Do you want to quit the programm (y, n)')
    if exit.lower() == 'n':
        main()


if __name__ == "__main__":
    main()
