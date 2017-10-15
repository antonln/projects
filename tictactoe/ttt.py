# Tic tac toe version 2.0


class square:
    '''One square on the ttt board'''

    def __init__(self, val, location, density):
        self.val = val
        self.location = location
        self.density = density


a1 = square(' ', 'a1', 3)
a2 = square(' ', 'a2', 2)
a3 = square(' ', 'a3', 3)
b1 = square(' ', 'b1', 2)
b2 = square(' ', 'b2', 4)
b3 = square(' ', 'b3', 2)
c1 = square(' ', 'c1', 3)
c2 = square(' ', 'c2', 2)
c3 = square(' ', 'c3', 3)

game = True

square_list = [a1, b1, c1, a2, b2, c2, a3, b3, c3]

location_list = [a1.location, a2.location, a3.location,
                 b1.location, b2.location, b3.location,
                 c1.location, c2.location, c3.location]


def print_board():
    print("""
  1 2 3
a|{0}|{1}|{2}|
b|{3}|{4}|{5}|
c|{6}|{7}|{8}|""".format(a1.val, a2.val, a3.val,
                         b1.val, b2.val, b3.val,
                         c1.val, c2.val, c3.val))


def play_move(x_or_o, move):
    for i in square_list:
        if move == i.location:
            i.val = x_or_o
            for j in square_list:
                if move == j.location:
                    square_list.remove(j)
                    break


def refresh_win_list():
    global win_chain1
    global win_chain2
    global win_chain3
    global win_chain4
    global win_chain5
    global win_chain6
    global win_chain7
    global win_chain8
    global win_list

    win_chain1 = [a1, a2, a3]
    win_chain2 = [b1, b2, b3]
    win_chain3 = [c1, c2, c3]
    win_chain4 = [a1, b1, c1]
    win_chain5 = [a2, b2, c2]
    win_chain6 = [a3, b3, c3]
    win_chain7 = [a1, b2, c3]
    win_chain8 = [a3, b2, c1]

    win_list = [win_chain1, win_chain2, win_chain3, win_chain4,
                win_chain5, win_chain6, win_chain7, win_chain8]


def check_game():
    global game
    refresh_win_list()

    for i in win_list:
        x_counter = 0
        o_counter = 0
        for j in i:
            if j.val == 'X':
                x_counter += 1
                if x_counter == 3:
                    print_board()
                    print("X wins!")
                    game = False
                    break
            if j.val == 'O':
                o_counter += 1
                if o_counter == 3:
                    print_board()
                    print("O wins!")
                    game = False
                    break

    if len(square_list) == 0:
        print("It's a tie!")
        game = False


print("Welcome to tic tac toe!")
print("You are playing 'X'.")
print("Enter 'quit' at any time to exit.")

while game:

    print_board()

    while True:
        # Ensures that a valid move is entered.

        move = input("Please enter a move: ")
        if move in location_list:
            location_list.remove(move)
            break
        elif move == "quit":
            print("You exited the game.")
            game = False
            break
        else:
            print("Please enter a valid move, or 'quit'.")
            print()

    play_move('X', move)

    check_game()

    if not game:
        break

    while True:

        refresh_win_list()

        o_move = 0

        for i in win_list:
            x_counter = 0
            o_counter = 0

            for j in i:
                if j.val == 'X':
                    x_counter += 1
                if j.val == 'O':
                    o_counter += 1

            if x_counter == 2:
                for j in i:
                    if j.val == ' ':
                        play_move('O', j.location)
                        o_move = 1
                        break

            if o_move == 1:
                break

        if o_move == 1:
            break

        max_density = 1

        for i in square_list:
            if i.density > max_density:
                max_density = i.density

        for i in square_list:
            if i.density == max_density:
                play_move('O', i.location)
                o_move = 1
                break

        if o_move == 1:
            break

    if game:
        check_game()
