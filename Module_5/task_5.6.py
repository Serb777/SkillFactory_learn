# Крестики-нолики

print("Крестики-нолики\n")

board = list(range(1, 10))


def draw_field(field):
    print("-" * 13)
    for i in range(3):
        print(f'| {field[0 + i * 3]} | {field[1 + i * 3]} | {field[2 + i * 3]} |')
        print("-" * 13)


def player_turn(key_player):
    valid = False

    while not valid:
        try:
            key_input = int(input(f"\nВведите номер ячейки {key_player}: "))
        except ValueError:
            print("\nНомер ячейки - число от 1 до 9")
            continue
        if key_input in range(1, 9):
            if str(board[key_input - 1]) not in "XO":
                board[key_input - 1] = key_player
                valid = True
            else:
                print("Эта клетка уже занята!")


def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            player_turn("X")
        else:
            player_turn("0")
        counter += 1
        if counter > 4:
            winner = check_win(field)
            if winner:
                print(winner, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_field(field)


main(board)

input("Нажмите Enter для выхода!")