# 숙제3 - 9*9수독만들기
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.11.7
# 최종수정날짜 : 2014.11.9
# version 1.1


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
        return 40
    elif lev == "중" :
        return 34
    else :
        return 28
    
def show_board(puzzle) : #퍼즐을 실행창에 보여줌
    wait = []
    wait = [['+','0',1,2,3,4,5,6,7,8]]+[['0']+puzzle[0]]
    for a in range(1,9) :
        wait.append([a]+puzzle[a])
    for i in range(0,10) :
        for j in range(0,10) :
            if wait[i][j]==0 :
                print('.',end=" ")
            elif wait[i][j]=='+' :
                print('+',end=" ")
            elif wait[i][j]=='0' :
                print(0,end=" ")
            else :
                print(str(wait[i][j]).rjust(1),end=" ")
        print()

def create_board() : #정답보드 초안 만듦
    seed = [1,2,3,4,5,6,7,8,9]
    random.shuffle(seed)
    row0 = seed[:]
    row1 = seed[3:6] + seed[6:] + seed[:3]
    row2 = seed[6:] + seed[:3] + seed[3:6]
    row3 = [seed[1] , seed[2] , seed[0] , seed[4] , seed[5] , seed[3] , seed[7] , seed[8] , seed[6]]
    row4 = [seed[4] , seed[5] , seed[3] , seed[7] , seed[8] , seed[6] , seed[1] , seed[2] , seed[0]]
    row5 = [seed[7] , seed[8] , seed[6] , seed[1] , seed[2] , seed[0] , seed[4] , seed[5] , seed[3]]
    row6 = [seed[2] , seed[0] , seed[1] , seed[5] , seed[3] , seed[4] , seed[8] , seed[6] , seed[7]]
    row7 = [seed[5] , seed[3] , seed[4] , seed[8] , seed[6] , seed[7] , seed[2] , seed[0] , seed[1]]
    row8 = [seed[8] , seed[6] , seed[7] , seed[2] , seed[0] , seed[1] , seed[5] , seed[3] , seed[4]]
    return [row0,row1,row2,row3,row4,row5,row6,row7,row8]

print(create_board()) 

def shuffle_ribons(board) : #정답보드 초안 가로줄 무작위로 바꿔줌
    one = board[:3]
    one3 = [one[0],one[2]]
    random.shuffle(one3)
    one = [one3[0],one[1],one3[1]]
    one2_1 = one[:2]
    random.shuffle(one2_1)
    one = [one2_1[0],one2_1[1],one[2]]
    one2_2 = one[1:]
    random.shuffle(one2_2)
    one = [one[0],one2_2[0],one2_2[1]]

    two = board[3:6]
    two3 = [two[0],two[2]]
    random.shuffle(two3)
    two = [two3[0],two[1],two3[1]]
    two2_1 = two[:2]
    random.shuffle(two2_1)
    two = [two2_1[0],two2_1[1],two[2]]
    two2_2 = two[1:]
    random.shuffle(one2_2)
    two = [two[0],two2_2[0],two2_2[1]]

    three = board[6:]
    three3 = [three[0],three[2]]
    random.shuffle(three3)
    three = [three3[0],three[1],three3[1]]
    three2_1 = three[:2]
    random.shuffle(three2_1)
    three = [three2_1[0],three2_1[1],three[2]]
    three2_2 = three[1:]
    random.shuffle(three2_2)
    three = [three[0],three2_2[0],three2_2[1]]   
    
    board = one + two + three
    return board

def transpose(board) : #정답보드 전치시키기
    transposed = []
    for _ in range(len(board)) :
        transposed.append([])
    for i in range(0,9) :
        for j in range(0,9) :
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
        i = random.randint(0,8)
        j = random.randint(0,8)
        if board[i][j] == 0 :
            continue
        board[i][j] = 0
        holeset.add((i,j))
        no_of_holes = no_of_holes - 1                   
    return board, holeset

## 최종 함수!!!!!!!!!!!!!
def sudokbig(): 
    solution = create_solution_board() 
    no_of_holes = get_level() 
    puzzle = copy_board(solution) 
    (puzzle, holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle) 
    while True: 
        i = get_integer("가로줄번호(0~8): ",0,8) 
        j = get_integer("세로줄번호(0~8): ",0,8) 
        if (i,j) not in holeset: 
            print('빈칸이 아닙니다.') 
            continue 
        n = get_integer("숫자 (1~9): ",1,9) 
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

