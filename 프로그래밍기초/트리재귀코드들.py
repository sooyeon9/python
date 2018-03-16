# 트리재귀 모범코드들

# Tree Recursion

# Fibonacci Sequence
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n
        
def fibtail(n):
    def loop(k,old,new):
        if counter < n:
            return loop(k+1,new,old+new)
        else: # k == n
            return new
    return loop(1,1,0)

def fibwhile(n):
    k = 1
    old, new = 0, 1
    while k < n:
        k += 1
        old, new = new, old+new # �룞�떆 吏��젙
        # temp = new
        # new = old + new
        # old = temp
    return new

def fibfor(n):
    old, new = 0, 1
    for _ in range(2,n+1):
        old, new = new, old+new
    return new

def fibseq(n):
    fibs = [0,1]
    for k in range(2,n+1):
        fib = fibs[k-1]+fibs[k-2]
        fibs.append(fib)
    return fibs

def fib2(n):
    return fibseq(n).pop()

# Combination

def comb(n,r):
    if not (r == 0 or r == n):
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1

def pascal(n,r):
    table = [[]]*(n-r+1)
    table[0] = [1]*(r+1)
    for i in range(1,n-r+1):
        table[i] = [1]
    for i in range(1,n-r+1):
        for j in range(1,r+1):
            newvalue = table[i][j-1] + table[i-1][j]
            table[i].append(newvalue)
    return table[n-r][r]


# Tower of Hanoi
# assume n >= 0

def tower(n,src,dst,tmp) :
    if n > 0 :
        tower(n-1,src,tmp,dst)
        print("move from", src, "to", dst)
        tower(n-1,tmp,dst,src)
    else :
        pass

# Calulation table
def gugudan1():
    for i in range(2,10):
        for j in range(1,10):
            if j % 3 == 0:
                print(i,"x",j,"=",str(i*j).rjust(2))
            else:
                print(i,"x",j,"=",str(i*j).rjust(2),end="  ")
        if i != 9: print()

def gugudan2():
    for k in [2,6]:
        for i in range(1,10):
            for j in range(k,k+4):
                print(j,"x",i,"=",str(j*i).rjust(2),end="  ")
            print()
        if k == 2: print()

# Sliding Puzzle

def get_number():
    num = input("Type the number you want to move (Type 0 to quit): ")
    while not (num.isdigit() and 0 <= int(num) <= 15):
        num = input("Type the number you want to move (Type 0 to quit): ")
    return int(num)

def create_init_board():
    return [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]]

def set_goal_board():
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def print_board(board):
    for row in board:
        for item in row:
            if item == 0:
                print("  ", end=" ")
            elif 10 <= item <= 15:
                print(item,end=" ")
            else:
                print(str(item).rjust(2),end=" ")
        print()
        
def find_position(num,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if num == board[i][j]:
                return (i,j)

def move(pos,opened,board):
    (x,y) = pos
    if opened == (x-1,y) or opened == (x+1,y) or \
       opened == (x,y-1) or opened == (x,y+1):
        board[opened[0]][opened[1]] = board[x][y]
        board[x][y] = 0
        return (pos,board)
    else:
        print("Can't move! Try again.")
        return (opened,board)

def sliding_puzzle():
    board = create_init_board()
    goal = set_goal_board()
    opened = (3,3)
    while True:
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number() # get number between 0 and 15
        if num == 0:
            break
        pos = find_position(num,board)
        (opened,board) = move(pos,opened,board)
    print("Please come again.")
