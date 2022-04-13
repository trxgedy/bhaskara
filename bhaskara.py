import os, math

def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def main():
    cls()
    print(f'x = -b ± √b² - 4.a.c\n--------------------\n        2.a\n\n')

    try:
        a = float(input("Value A: "))
        b = float(input("Value B: "))
        c = float(input("Value C: "))

        delta = (b ** 2) - (4 * a) * c

        y1 = (- b) + delta ** (1/2)
        y2 = (- b) - delta ** (1/2)

        x1 = y1 / (2 * a)
        x2 = y2 / (2 * a)

        if delta >= 0:
            print("\n{} & {}".format(x1,x2))
        else: 
            print('\nDelta negativo.')

    except:
        print("\nErro! Morra coder viadinho.")

if __name__ == '__main__':
    while 1:
        main()
        os.system("pause > nul")
