import random

def initial_state(N):
    chessboard = [[0 for _ in range(N)] for _ in range(N)]
    queens = random.sample(range(N), N)
    for i in range(N):
        chessboard[i][queens[i]] = 1
    return chessboard

def evaluation_function(chessboard):
    count = 0
    N = len(chessboard)
    for i in range(N):
        for j in range(N):
            if chessboard[i][j] == 1:
                count += diagonal_attacks(chessboard, i, j)
                count += row_attacks(chessboard, i, j)
                count += column_attacks(chessboard, i, j)
    return count

def diagonal_attacks(chessboard, i, j):
    N = len(chessboard)
    count = 0
    for d in range(1, N):
        if i - d >= 0 and j - d >= 0 and chessboard[i-d][j-d] == 1:
            count += 1
        if i - d >= 0 and j + d < N and chessboard[i-d][j+d] == 1:
            count += 1
        if i + d < N and j - d >= 0 and chessboard[i+d][j-d] == 1:
            count += 1
        if i + d < N and j + d < N and chessboard[i+d][j+d] == 1:
            count += 1
    return count

def row_attacks(chessboard, i, j):
    count = 0
    N = len(chessboard)
    for d in range(1, N):
        if i - d >= 0 and chessboard[i-d][j] == 1:
            count += 1
        if i + d < N and chessboard[i+d][j] == 1:
            count += 1
    return count

def column_attacks(chessboard, i, j):
    count = 0
    N = len(chessboard)
    for d in range(1, N):
        if j - d >= 0 and chessboard[i][j-d] == 1:
            count += 1
        if j + d < N and chessboard[i][j+d] == 1:
            count += 1
    return count

def generate_successors(chessboard):
    successors = []
    N = len(chessboard)
    for i in range(N):
        for j in range(N):
            if chessboard[i][j] == 1:
                new_board = [row.copy() for row in chessboard]
                new_board[i][j] = 0
                for k in range(N):
                    if k != j:
                        new_board[i][k] = 1
                successors.append(new_board)
    return successors

def hill_climbing(chessboard):
    steps = 0
    current_board = chessboard
    current_eval = evaluation_function(current_board)
    while True:
        steps += 1
        successors = generate_successors(current_board)
        best_successor = None
        best_eval = float('inf')
        for successor in successors:
            eval = evaluation_function(successor)
            if eval < best_eval:
                best_eval = eval
                best_successor = successor
        if best_eval >= current_eval:
            return current_board, steps
        current_eval = best_eval
        current_board = best_successor

def hill_climbing_sideways_moves(chessboard):
    steps = 0
    current_board = chessboard
    current_eval = evaluation_function(current_board)
    sideways_moves = 0
    while True:
        steps += 1
        successors = generate_successors(current_board)
        best_successor = None
        best_eval = float('inf')
        for successor in successors:
            eval = evaluation_function(successor)
            if eval < best_eval:
                best_eval = eval
                best_successor = successor
        if best_eval >= current_eval:
            if sideways_moves > 10:
                return current_board, steps
            sideways_moves += 1
        else:
            sideways_moves = 0
        current_eval = best_eval
        current_board = best_successor

N = 8
chessboard = initial_state(N)
resulting_board, steps = hill_climbing_sideways_moves(chessboard)
print(f"The final chessboard after {steps} steps is:")
for row in resulting_board:
    print(row)
