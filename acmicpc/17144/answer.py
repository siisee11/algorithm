import copy

def __print_board(board):
    for row in board:
        print(row)
    print("----------------------------------")

def __copy(board):
    matrix = [row for row in board]
    return matrix


def direction(board, r, c):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    nr_direction = 4
    row = len(board) - 1 
    col = len(board[0]) - 1

    if (r - 1 < 0 or board[r - 1][c] < 0) :
        dr[2] = 0
        nr_direction = nr_direction - 1
    if (r + 1 > row or board[r + 1][c] < 0) :
        dr[3] = 0
        nr_direction = nr_direction - 1
    if (c - 1 < 0 or board[r][c - 1] < 0 ) :
        dc[1] = 0
        nr_direction = nr_direction - 1
    if (c + 1 > col or board[r][c + 1] < 0 ) :
        dc[0] = 0
        nr_direction = nr_direction - 1

    return dr, dc, nr_direction

def __spread(board, R, C):
    copy_board = copy.deepcopy(board)

    for i in range(R):
        for j in range(C):
            A_ij = copy_board[i][j]
            if (A_ij < 0) : continue
            dr, dc, nr_direction = direction(board, i, j)
            spread_A = A_ij // 5

            for k in range(4):
                if (dr[k] == 0 and dc[k] == 0):
                    continue
                board[i + dr[k]][j + dc[k]] += spread_A

            board[i][j] = board[i][j] - nr_direction * spread_A
        
def __circulation(board, R, C, air_r):
    for j in range(air_r - 1, 0, -1):
        board[j][0] = board[j - 1][0]
    for i in range(0, C - 1, 1):
        board[0][i] = board[0][i + 1]
    for j in range(0, air_r, 1):
        board[j][C - 1] = board[j + 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[air_r][i] = board[air_r][i - 1]
    board[air_r][1] = 0

    air_r = air_r + 1
    for j in range(air_r + 1, R - 1, 1):
        board[j][0] = board[j + 1][0]
    for i in range(0, C - 1, 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for j in range(R -  1, air_r, -1):
        board[j][C - 1] = board[j - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[air_r][i] = board[air_r][i - 1]
    board[air_r][1] = 0


def __do_one_step(board, R, C, air_r) :

    __spread(board, R, C)
    __circulation(board, R, C , air_r)
    
    return board

def __answer(R, C, T, board):

    col0 = [i[0] for i in board]
    for i in range(len(col0)) :
        if col0[i] == -1 :
            air_r = i
            break

    for i in range(T):
        __do_one_step(board, R, C, air_r)

    answer = int(sum([sum(row) for row in board])) + 2

    return answer

def main():

    R,C,T = map(int,input().split())

    board = []

    for i in range(R):
        board.append(list(map(int,list(input().split()))))

    answer = __answer(R, C, T, board)

    print(answer)

    return answer

if __name__ == "__main__":
    main()