def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'tie': 0}
    winner = None

    if is_winner(board, 'X'):
        return scores['X']
    if is_winner(board, 'O'):
        return scores['O']
    if is_full(board):
        return scores['tie']

    if maximizing_player:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_eval = -float('inf')
    best_move = None
    for move in get_available_moves(board):
        i, j = move
        board[i][j] = 'X'
        eval = minimax(board, 0, False)
        board[i][j] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        if turn % 2 == 0:
            i, j = best_move(board)
            print("Computer plays 'X' at ({}, {})".format(i, j))
            board[i][j] = 'X'
        else:
            while True:
                i, j = map(int, input("Enter row and column (e.g., 0 1): ").split())
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    break
                else:
                    print("Invalid move. Try again.")
        
        if is_winner(board, players[turn % 2]):
            print_board(board)
            print(players[turn % 2] + " wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    main()
