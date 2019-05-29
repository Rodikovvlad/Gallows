from random import choice
from colorama import init
from colorama import Fore, Back
import requests, bs4
import re

init(autoreset=True)


def set_words():
    r = requests.get("http://psychologies.ru/articles/pochemu-radostnyie-sobyitiya-inogda-vyizyivayut-trevogu/")
    s = bs4.BeautifulSoup(r.text, "html.parser")
    text = s.select('.article-section.fl p')[0:10]
    f_text = []
    f_text2 = []
    f_text3 = []
    f_text4 = []
    for i in text:
        f_text.append(i.getText())
    for i in f_text:
        line = ''.join(c for c in i if c not in '!,\\.?1:«»()234567890qwertyuiopasdfghjklzxcvbnm').lower()
        f_text2.append(line)
    for i in f_text2:
        line = i.split(' ')
        f_text3.append(line)
    for i in f_text3:
        for j in i:
            if len(j) > 6:
                f_text4.append(j)
    return f_text4


# Игра
def start(word, mass_symb):
    mistakes = 0
    count = 0
    for i in range(20):
        if count == len(word):
            print(Fore.GREEN+"!!!!!!--WIN--!!!!!!")
            break
        print()
        letter = input(Fore.BLACK+Back.GREEN+"Введите букву: ")
        print()
        if letter in mass_symb:
            print(Fore.RED+"Введите другую букву!")
        else:
            for k in range(len(word)):
                if letter == word[k]:
                    mass_symb[k] = letter
                    count += 1
            for l in mass_symb:
                print(l + " ", end="")
            if letter not in mass_symb:
                mistakes += 1
            print()
            print(Fore.YELLOW+f"Кол-во неверных попыток: {mistakes}")
            print()


# Создание подчеркиваний
def set_symbols(word):
    mass_symb = []
    for let in word:
        mass_symb.append("_")
    for i in mass_symb:
        print(i + " ", end="")
    print()
    return mass_symb


# Главная функция
def main():
    print(Fore.YELLOW + "------------------------ПОДОЖДИТЕ НЕМНОГО------------------------")
    words = set_words()
    word = choice(words)
    mass_symb = set_symbols(word)
    start(word, mass_symb)
    input()


if __name__ == "__main__":
    main()
