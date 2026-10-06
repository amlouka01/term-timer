import sys, os, time

def get_num(num):
    try: x = int(num)
    except Exception as e:
        print(f"Error : {e}")
        exit(1)
    return x

def print_line(x):
    match x:
        case 7: print("+    +", end="")
        case 2: print("+----+", end="")
        case 1: print("     +", end="")
        case 3: print("+     ", end="")
        case 4: print("|    |", end="")
        case 5: print("|     ", end="")
        case 6: print("     |", end="")

def solve(num):
    solve_print = {
        "0": [2, 4, 7, 4, 2],
        "1": [1, 6, 1, 6, 1],
        "2": [2, 6, 2, 5, 2],
        "3": [2, 6, 2, 6, 2], 
        "4": [7, 4, 2, 6, 1],
        "5": [2, 5, 2, 6, 2],
        "6": [2, 5, 2, 4, 2],
        "7": [2, 6, 1, 6, 1],
        "8": [2, 4, 2, 4, 2],
        "9": [2, 4, 2, 6, 2]
    }
    n = get_num(num)
    while (n >= 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, 5):
            for index, number in enumerate(str(n)):
                print_line(int(solve_print[number][i]))
                if (len(str(n)) - 1 == index): print("\n", end="")
                else: print(" ", end="")
        bar = "\u2588" * int(((int(num) - n) * 100 / int(num)))
        print(f"[ {bar} ] {len(bar)}%")
        time.sleep(1)
        n = n - 1

if (len(sys.argv) != 2):
    print("Invalid input ! Please enter a number from 0 to 9 .")
else:
    solve(sys.argv[1])