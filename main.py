import os
from colorama import Fore, Back

def printWhite(data,ends):
    print(Fore.WHITE,data,end=ends,sep="")

tab = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def draw(argument):
    os.system('clear')
    printWhite("┌───┬───┬───┬───┬───┬───┬───┐","\n")
    for j in range(0, 6):
        printWhite("│ ","")
        for i in range(0,7):
            if argument[i]!=0:
                print(argument[i],end=" │ ")
            else:
                printWhite(" "," │ ")
        if j!=5:
            printWhite("\n├───┼───┼───┼───┼───┼───┼───┤","\n")
        else:
            printWhite("\n└───┴───┴───┴───┴───┴───┴───┘","\n")

draw(tab)
