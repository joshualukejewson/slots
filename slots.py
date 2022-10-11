import random
from colorama import Fore

def deposit():
    while True: 
        cash = input("How much do you want to deposit?: ")
        if cash.isdigit():
            print(f"You have ${cash} to spend at the slots! Lets see how you go ay?")
            cash = int(cash)
            return(cash)
        else:
            print("Invalid input, please re enter: ")

def slots(cash):

    symbols = ['@', '#', '%']
    while True:
 
        bet_size = int(input("How much per bet?: "))
        lines = int(input("How many lines: "))
        payoutx = 8.5
        while True:
            choice = input('Do you wish to hit? (h) for yes or (c) to change settings: ')

            if choice == 'c':
                break

            if choice == 'q':
                quit()

            wins = 0
            if choice == 'h':

                cash = cash - (bet_size * lines)

                line_1 = random.choices(symbols, k=3)
                line_2 = random.choices(symbols, k=3)
                line_3 = random.choices(symbols, k=3)

                if lines == 1:

                    print(line_1)

                    if line_1[0] == line_1[1] == line_1[2]:
                        wins+=1

                elif lines == 2:

                    print(line_1)
                    print(line_2)

                    if line_1[0] == line_1[1] == line_1[2]:
                        wins+=1
                    if line_2[0] == line_2[1] == line_2[2]:
                        wins+=1
            
                elif lines == 3:

                    print(line_1)
                    print(line_2)
                    print(line_3)

                    if line_1[0] == line_1[1] == line_1[2]:
                        wins+=1
                    if line_2[0] == line_2[1] == line_2[2]:
                        wins+=1
                    if line_3[0] == line_3[1] == line_3[2]:
                        wins+=1
                cash = cash + (bet_size * payoutx * wins)
                if wins == 1:
                    print("Well done you won! you now have $%s" % cash)
                elif wins >= 2:
                    print("Multi win! you won " + str(wins) + " lines well done! you now have $" + str(cash))
                else:
                    print("Better luck next time! you still have $%s remaining." % cash) 


def main():
    
    cash = deposit()
    slots(cash)

if __name__ == '__main__': 
    main()
