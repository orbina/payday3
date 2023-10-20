import sys
from itertools import product

def generate(digits):
    return [comb for comb in product(digits, repeat=4) if all(digit in comb for digit in digits)]

def display(combinations):
    print('Possible combinations:')
    for combination in combinations:
        print(''.join(combination))

def show_help():
    print("Payday3 combination bruteforcer. Run as 'payday3.py INPUT'. Payday3 uses four digit combinations.")

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        show_help()
        sys.exit()

    digits = sys.argv[1]
    if len(digits) != 4:
        print("Provide exactly four digits or use 'payday3.py -h' for help.")
        sys.exit()

    combinations = generate(digits)
    display(combinations)
