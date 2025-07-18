import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count =  {
    "A": 2,
    "B": 4,
    "C": 6,
}

symbol_value =  {
    "A": 10,
    "B": 8,
    "C": 3,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #Check lines bet on. Looping through every row user bet on
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols): #Generate outcome of slot machine 
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #Gives key and item associated with key. Key here is Letter, Value is number (frequency)
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #Lesson: [:] is copy of list not a refernce. 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)#add value to column

        columns.append(column)

    return columns

def print_slot_machine(columns): #Transposing the 'matrix'
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):  #Looping over every item in columns. Lesson - i is index from iteration of columns.
            if i != len(columns) -1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter amount desired to put into account $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than zero")
        else:
            print("Please enter amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter amount of lines desired to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter valid amount of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet_amount(amount):
    while True:
        print(f"Your account balance is: ${amount}")
        bet = input("Enter amount desired to bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print("Enter bet valid amount ")
        else:
            print("Please enter a number")
    return bet



def get_total_bet(bet, lines):
    total_bet = bet * lines
    return total_bet
    
def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet_amount(balance)
    total_bet = get_total_bet(bet, lines)
    if total_bet > balance:     #
        print("You do not have requisite funds.")
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
        print(f"Your current balance is {balance} \nPlease add more funds or allocate bets within funds range.")
    else:
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count) #Generate slot machine dependent on bet validation
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        print(f"You won on line(s): ", *winning_lines) #*variable is the unpack operator 

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: {balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with {balance}")

main()