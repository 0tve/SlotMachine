import random

REEL_CONTENT = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 8,
}

ROWS = 3
COLS = 3


def get_reel_content_list():
    reel_content_list = []

    for el in REEL_CONTENT.items():
        for _ in range(el[1]):
            reel_content_list.append(el[0])

    return reel_content_list


def get_row():
    row = []

    for _ in range(COLS):
        field = random.choice(get_reel_content_list())
        row.append(field)

    return row


def get_all_rows():
    all_rows = []

    for _ in range(ROWS):
        all_rows.append(get_row())

    return all_rows


def print_all_rows(all_rows):
    for row in all_rows:
        for i, el in enumerate(row):
            if i == len(row) - 1:
                print(f"{el}")
            else:
                print(f"{el} | ", end='')


def get_matches(all_rows):
    matches = []
    for i, row in enumerate(all_rows):
        row_distinct_values = set(row)
        if len(row_distinct_values) == 1:
            matches.append(i + 1)

    return matches


def get_balance(prompt):
    balance = input(prompt)

    if not balance.isdigit():
        balance = get_balance('Please enter a number! $')

    return int(balance)


def get_rows_bet(prompt):
    rows_bet = input(prompt)

    if not rows_bet.isdigit():
        rows_bet = get_rows_bet('Please enter a number! ')

    if int(rows_bet) not in range(1, ROWS + 1):
        rows_bet = get_rows_bet(f'Please enter a number in range 1-{ROWS}: ')

    return int(rows_bet)


def get_money_bet(prompt, rows_bet, balance):
    money_bet = input(prompt)

    if not money_bet.isdigit():
        money_bet = get_money_bet(
            'Please enter a number! $', rows_bet, balance)

    total_bet = int(money_bet) * rows_bet

    if total_bet > balance:
        money_bet = get_money_bet(
            f"Your balance: ${balance}, your total bet: ${total_bet}. Please bet less money! $", rows_bet, balance)

    return int(money_bet)


def play_game():
    balance = get_balance("How much money would you like to deposit? $")
    rows_bet = get_rows_bet(
        f'How many rows would you like to bet on (1-{ROWS})? ')
    money_bet = get_money_bet(
        'How much money would you like to bet on a row? $', rows_bet, balance)
    all_rows = get_all_rows()
    matches = get_matches(all_rows)
    winnings = len(matches) * money_bet
    losses = money_bet * rows_bet - winnings
    balance += winnings - losses
    print_all_rows(all_rows)

    if winnings == 0:
        print('There are no matches')
    else:
        print(
            f"There are {len(matches)} matches on rows {','.join(str(x) for x in matches)}")

    print(f"Your winnings: {winnings}")
    print(f"Your losses: {losses}")
    print(f"Your new balance: {balance}")


def main():
    while True:
        want_to_play = input("Do you want to play the game? (y|n): ")
        if want_to_play == "y":
            play_game()
        else:
            break


main()
