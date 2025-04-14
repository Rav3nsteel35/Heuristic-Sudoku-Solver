from collections import deque
import time

def is_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def read_board():
    board = []
    for _ in range(9):
        line = input().strip().split()
        board.append([int(num) for num in line])
    return board

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_neighbors(i, j):
    neighbors = set()
    for x in range(9):
        if x != j:
            neighbors.add((i, x))
    for y in range(9):
        if y != i:
            neighbors.add((y, j))
    box_x = j // 3
    box_y = i // 3
    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):
            if x != i or y != j:
                neighbors.add((x, y))
    return list(neighbors)

def initialize_domains(board):
    domains = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domains[(i, j)] = set(range(1, 10))
            else:
                domains[(i, j)] = {board[i][j]}
    return domains

def ac3(board, domains):
    queue = deque()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for (x, y) in get_neighbors(i, j):
                    queue.append(((i, j), (x, y)))

    while queue:
        (xi, xj), (yi, yj) = queue.popleft()
        if revise(board, domains, xi, xj, yi, yj):
            if not domains[(xi, xj)]:
                return False
            for (xk, xl) in get_neighbors(xi, xj):
                queue.append(((xk, xl), (xi, xj)))
    return True

def revise(board, domains, xi, xj, yi, yj):
    revised = False
    if board[yi][yj] != 0 and board[yi][yj] in domains[(xi, xj)]:
        domains[(xi, xj)].remove(board[yi][yj])
        revised = True
    return revised

def select_unassigned_variable(board, domains):
    min_domain_size = float('inf')
    selected_cell = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domain_size = len(domains[(i, j)])
                if domain_size < min_domain_size:
                    min_domain_size = domain_size
                    selected_cell = (i, j)
    return selected_cell

def order_domain_values(board, domains, cell):
    i, j = cell
    domain = list(domains[(i, j)])
    constraint_counts = []
    for value in domain:
        count = 0
        for (x, y) in get_neighbors(i, j):
            if board[x][y] == 0 and value in domains[(x, y)]:
                count += 1
        constraint_counts.append((value, count))
    constraint_counts.sort(key=lambda x: x[1])
    return [x[0] for x in constraint_counts]

def solve(board, domains, start_time, timeout=10):
    if time.time() - start_time > timeout:
        return False
    if not ac3(board, domains):
        return False
    find = select_unassigned_variable(board, domains)
    if not find:
        return True
    row, col = find
    for value in order_domain_values(board, domains, (row, col)):
        board[row][col] = value
        old_domains = {k: v.copy() for k, v in domains.items()}
        if solve(board, domains, start_time, timeout):
            return True
        board[row][col] = 0
        domains = old_domains
    return False

def is_valid(board):
    for row in board:
        if len(set(row)) != 9:
            return False
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(subgrid)) != 9:
                return False
    return True

def main():
    board = read_board()
    domains = initialize_domains(board)
    start_time = time.time()
    if solve(board, domains, start_time, timeout=10):
        if is_valid(board):
            print_board(board)
        else:
            print("No solution.")
    else:
        print("No solution.")

if __name__ == "__main__":
    main()
