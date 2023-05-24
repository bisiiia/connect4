import os
from colorama import Fore


def printWhite(data, ends):
    print(Fore.WHITE, data, end=ends, sep="")

def printRed(data):
    print(Fore.RED,data,Fore.WHITE,end=" │ ",sep="")

def printGreen(data):
    print(Fore.GREEN,data,Fore.WHITE,end=" │ ",sep="")

tab = [0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0]

def below(adres):
    try:
        if(tab[adres+7]==0):
            return True
        else:
            return False
    except:
        return False

def change(adres):
    value=True
    while value:
        if(below(adres)):
            adres+=7
        else:
            value=False
    return adres



def draw(argument):
    os.system('clear')
    printWhite("┌───┬───┬───┬───┬───┬───┬───┐", "\n")
    for j in range(0, 6):
        printWhite("│ ", "")
        for i in range(0, 7):
            if argument[j*7+i] == 1:
                printGreen("●")
            elif argument[j*7+i] == 2:
                printRed("●")
            else:
                printWhite(" ", " │ ")
        if j != 5:
            printWhite("\n├───┼───┼───┼───┼───┼───┼───┤", "\n")
        else:
            printWhite("\n└───┴───┴───┴───┴───┴───┴───┘", "\n")


draw(tab)

gracz = 1
value = True
while value:
    draw(tab)
    if gracz == 1:
        print("Gracz 1 wybierz pole(1-7) w które chcesz wrzucić żeton:")
    else:
        print("Gracz 2 wybierz pole(1-7) w które chcesz wrzucić żeton:")
    value2 = True
    while value2:
        wsp = input()
        try:
            wsp = int(wsp)
        except:
            continue
        if(wsp>0 and wsp<8):
            wsp-=1
            if(tab[wsp]==0):
                value2=False
            else:
                print("Wyrzuciłeś żeton poza planszę :C")
                print("Podaj inne pole :>")
    tab[change(wsp)]=gracz
    if(gracz==1):
        gracz=2
    else:
        gracz=1
