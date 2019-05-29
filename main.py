from random import choice
from colorama import init
from colorama import Fore
import requests, bs4
from time import sleep
import sys


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
    inp_letters = set([])
    for i in range(20):
        if count == len(word):
            print(Fore.GREEN+"!!!!!!----------ПОБЕДА---------!!!!!!")
            break
        print()
        letter = input("Введите букву: ").lower()
        print()
        if len(letter) == 1 and letter.isalpha() and letter not in "qwertyuiopasdfghjklzxcvbnm":
            inp_letters.add(letter)
            print()
            if letter in mass_symb:
                print(Fore.RED+"ЭТА БУКВА УЖЕ ЕСТЬ В СЛОВЕ!")
                print(Fore.RED+"ВВЕДИТЕ ДРУГУЮ БУКВУ!")
                print(Fore.YELLOW + "КОЛ-ВО НЕВЕРНЫХ ПОПЫТОК: " + Fore.GREEN + str(mistakes), end="")
                print(" | " + Fore.YELLOW + f"ОСТАЛОСЬ ХОДОВ: ", end="")
                print(Fore.GREEN + f"{19 - i}")
                print(Fore.YELLOW + "ВВЕДЕННЫЕ БУКВЫ: ", end="")
                print(Fore.GREEN, end="")
                print(inp_letters)
                print()
                for l in mass_symb:
                    print(l + " ", end="")
                print()
            else:
                for k in range(len(word)):
                    if letter == word[k]:
                        mass_symb[k] = letter
                        count += 1
                for l in mass_symb:
                    print(l + " ", end="")
                print(Fore.CYAN+"  <------ СЛОВО, КОТОРОЕ НАДО УГАДАТЬ")
                if letter not in mass_symb:
                    mistakes += 1
                print()
                if 19 - i == 0:
                    print(Fore.RED + "ВЫ ПРОИГРАЛИ!")
                    print(Fore.RED + "СЛОВО, КОТОРОЕ ВЫ НЕ СМОГЛИ ОТГАДАТЬ: " + Fore.GREEN + word)
                    input()
                    sys.exit()
                print(Fore.YELLOW+"КОЛ-ВО НЕВЕРНЫХ ПОПЫТОК: "+Fore.GREEN+str(mistakes), end="")
                print(" | "+ Fore.YELLOW+f"ОСТАЛОСЬ ХОДОВ: ", end="")
                print(Fore.GREEN + f"{19-i}")
                print(Fore.YELLOW+"ВВЕДЕННЫЕ БУКВЫ: ", end="")
                print(Fore.GREEN,end="")
                print(inp_letters)
                print()
        elif letter in "qwertyuiopasdfghjklzxcvbnm":
            if 19 - i == 0:
                print(Fore.RED + "ВЫ ПРОИГРАЛИ!")
                print(Fore.RED + "СЛОВО, КОТОРОЕ ВЫ НЕ СМОГЛИ ОТГАДАТЬ: "+ Fore.GREEN + word)
                input()
                sys.exit()
            mistakes += 1
            print(Fore.RED+"ВЫ ВВЕЛИ АНГЛИЙСКУЮ БУКВУ, ОТГАДАВЫЕМОЕ СЛОВО НА РУССКОМ ЯЗЫКЕ!")
            print(Fore.YELLOW + "КОЛ-ВО НЕВЕРНЫХ ПОПЫТОК: " + Fore.GREEN + str(mistakes), end="")
            print(" | " + Fore.YELLOW + f"ОСТАЛОСЬ ХОДОВ: ", end="")
            print(Fore.GREEN + f"{19 - i}")
            if len(inp_letters) > 0:
                print(Fore.YELLOW + "ВВЕДЕННЫЕ БУКВЫ: ", end="")
                print(Fore.GREEN, end="")
                print(inp_letters)
            print()
            for l in mass_symb:
                print(l + " ", end="")
            print()
        else:
            if 19 - i == 0:
                print(Fore.RED + "ВЫ ПРОИГРАЛИ!")
                print(Fore.RED + "СЛОВО, КОТОРОЕ ВЫ НЕ СМОГЛИ ОТГАДАТЬ: "+ Fore.GREEN + word)
                input()
                sys.exit()
            mistakes += 1
            print(Fore.RED+"НЕВЕРНЫЙ ВВОД!")
            print(Fore.YELLOW + "КОЛ-ВО НЕВЕРНЫХ ПОПЫТОК: " + Fore.GREEN + str(mistakes), end="")
            print(" | " + Fore.YELLOW + f"ОСТАЛОСЬ ХОДОВ: ", end="")
            print(Fore.GREEN + f"{19 - i}")
            if len(inp_letters) > 0:
                print(Fore.YELLOW + "ВВЕДЕННЫЕ БУКВЫ: ", end="")
                print(Fore.GREEN, end="")
                print(inp_letters)
            print()
            for l in mass_symb:
                print(l + " ", end="")
            print()


# Создание подчеркиваний
def set_symbols(word):
    mass_symb = []
    for let in word:
        mass_symb.append("_")
    print()
    for i in mass_symb:
        print(i + " ", end="")
    print(Fore.CYAN + "  <------ СЛОВО, КОТОРОЕ НАДО УГАДАТЬ")
    print()
    return mass_symb


# Главная функция
def main():
    print(Fore.GREEN + "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\------ ВИСЕЛИЦА ------////////////////////////")
    sleep(1)
    print()
    print(Fore.BLUE + "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\------ БЕТА ВЕРСИЯ ------/////////////////////")
    sleep(1)
    print()
    print(Fore.YELLOW + "------------------------------------ ПРАВИЛА ---------------------------------")
    print(Fore.YELLOW+"|                                                                            |")
    print(Fore.YELLOW+"|"+Fore.GREEN + "   1 - ВАМ НАДО УГАДАТЬ СЛОВО, БУКВЫ КОТОРОГО СКРЫТЫ СИМВОЛОМ ПОДЧЕРКИВАНИЯ "
          +Fore.YELLOW+"|")
    print(Fore.YELLOW + "|" + Fore.GREEN + "   2 - У вас есть 20 попыток                                              "
                                           "  " + Fore.YELLOW + "|")
    print(Fore.YELLOW + "|" + Fore.GREEN + "   3 - Вводите по одной букве                                            "
                                           "   " + Fore.YELLOW + "|")
    print(Fore.YELLOW + "------------------------------------------------------------------------------")
    words = set_words()
    word = choice(words)
    mass_symb = set_symbols(word)
    start(word, mass_symb)



if __name__ == "__main__":
    main()
