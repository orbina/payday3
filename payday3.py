import sys
from itertools import product

def generate(digits):
    return [comb for comb in product(digits, repeat=4) if all(digit in comb for digit in digits)]

def display(combinations):
    print('Possible combinations:')
    for combination in combinations:
        print(''.join(combination))

def show_help():
    print("Payday 3 combination bruteforcer. Run as 'payday3.py INPUT'. Payday uses four digit combinations. Input can be 2, 3, or 4 digits.")

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        show_help()
        sys.exit()

    digits = sys.argv[1]
    if len(digits) not in [2, 3, 4]:
        print("Provide 2, 3, or 4 digits. Use 'payday3.py -h' for help.")
        sys.exit()

    combinations = generate(digits)
    display(combinations)
