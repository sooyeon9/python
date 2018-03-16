import random

def get_integer(x,a,b) : #a~b사이 정수 입력받음
    n = input(x)
    while not (n.isdigit() and a<=int(n)<=b) :
        n = input(x)
    return int(n)
    
def get_level() : #난이도를 입력받음
    lev = input("난이도 (상,중,하) 중에서 하나 선택하여 입력: ")
    while lev not in {'상','중','하'} :
        lev = input("난이도 (상,중,하) 중에서 하나 선택하여 입력: ")
    if lev == "상" :
        return 10
    elif lev == "중" :
        return 8
    else :
        return 6
    
def show_board(puzzle) : #퍼즐을 실행창에 보여줌
    puzzle = [['+','0',1,2,3]]+[['0']+puzzle[0]]+[[1]+puzzle[1]]+[[2]+puzzle[2]]+[[3]+puzzle[3]]
    for i in range(0,5) :
        for j in range(0,5) :
            if puzzle[i][j]==0 :
                print('.',end=" ")
            elif puzzle[i][j]=='+' :
                print('+',end=" ")
            elif puzzle[i][j]=='0' :
                print(0,end=" ")
            else :
                print(str(puzzle[i][j]).rjust(1),end=" ")
        print()
        
def create_board() : #정답보드 초안 만듦
    seed = [1,2,3,4]
    dees = []
    random.shuffle(seed)
    row0 = seed[:]
    row1 = seed[2:] + seed[:2]
    for _ in range(0,4) :
        dees.append(seed.pop())
    row2 = dees[2:] + dees[:2]
    row3 = dees[:]
    return [row0,row1,row2,row3]

def shuffle_ribons(board) : #정답보드 초안 가로줄 두줄씩 무작위로 바꿔줌
    top, bottom = board[:2],board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    board = top + bottom
    return board
                
def transpose(board) : #정답보드 초안 전치시키기
    transposed = []
    for _ in range(len(board)) :
        transposed.append([])
    for i in range(0,4) :
        for j in range(0,4) :
            transposed[j].append(board[i][j])
    return transposed

def create_solution_board() : #정답보드 섞기
    return transpose(shuffle_ribons(transpose(shuffle_ribons(create_board()))))

def copy_board(board) : #보드 복사해줌
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

def make_holes(board,no_of_holes) : #퍼즐보드 만들기
    holeset = set()
    while no_of_holes > 0 :
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] == 0 :
            continue
        board[i][j] = 0
        holeset.add((i,j))
        no_of_holes = no_of_holes - 1                   
    return board, holeset

## 최종 함수!!!!!!!!!!!!!
def sudokmini(): 
    solution = create_solution_board() 
    no_of_holes = get_level() 
    puzzle = copy_board(solution) 
    (puzzle, holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle) 
    while True: 
        i = get_integer("가로줄번호(0~3): ",0,3) 
        j = get_integer("세로줄번호(0~3): ",0,3) 
        if (i,j) not in holeset: 
            print('빈칸이 아닙니다.') 
            continue 
        n = get_integer("숫자 (1~4): ",1,4) 
        sol = solution[i][j]          
        if n == sol :                      
            puzzle[i][j] = sol 
            show_board(puzzle) 
            holeset.remove((i,j)) 
            no_of_holes -= 1 
        else : 
            print(n,"가 아닙니다. 다시 해보세요.") 
        if no_of_holes == 0 : 
            print("잘 하셨습니다. 또 들리세요.") 
            break
