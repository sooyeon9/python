# 보물찾기
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.11.21
# 최종 수정날짜 : 2014.11.23
# version 1.2

import random

def get_integer(x,a,b) : #a~b사이 정수 입력받음 (행과 열 입력받을때 사용)
    n = input(x)
    while not (n.isdigit() and a<=int(n)<=b) :
        n = input(x)
    return int(n)

def ask(message): #예스&노 입력받음 (깃발을 꽂거나 뽑을때 사용) 
    answer = input(message) 
    while not (answer == 'y' or answer == 'n'): 
        answer = input(message) 
    if answer == 'y': 
        return True 
    else: 
        return False

def get_level() : #난이도를 입력받음 (16*16인지 9*9인지 내줌)
    print("> high는 16*16보드에 지뢰60개")
    print("> normal은 9*9보드에 지뢰20개")
    lev = input("난이도 (high, normal)중 하나 선택하세요 : ")
    while lev not in {'high','normal'} :
        lev = input("난이도 (high, normal)중 하나 선택하세요 : ")
    if lev == "high" :
        return 16
    else :
        return 9

def square(n) : #기본 보드 (n에 9 or 16넣음)
    if n == 9 :
        square = [["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□"]]

    else :
        square = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
                  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
    return square

def table(n) : #유저에게 보여주도록하는 보드 (n에 9 or 16넣음)
    if n == 9 :
        table = [[False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False]]

    else :
        table = [[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]
    return table

def show_board(square,table) : #보드를 실행창에 보여주는 함수
    n = len(square)
    for i in range(n+1) :
        for j in range(n+1) :
            if i == 0 and j == 0 :
                print("+".rjust(2), end = " ")
            elif i == 0 :
                print(str(j).rjust(2), end = " ")
            elif j == 0 :
                print(str(i).rjust(2), end = " ")
            else :
                if table[i-1][j-1] == True :
                    print(str(square[i-1][j-1]).rjust(2), end = " ")
                else :
                    print("□".rjust(2),end=" ")
        print()
        
def show_true(square) : #게임 끝날때 정답보드 보여주는 함수
    n = len(square)
    for i in range(len(square)+1) :
        for j in range(n+1) :
            if i == 0 and j == 0 :
                print("+".rjust(2), end = " ")
            elif i == 0 :
                print(str(j).rjust(2), end = " ")
            elif j == 0 :
                print(str(i).rjust(2), end = " ")
            else :
                print(str(square[i-1][j-1]).rjust(2), end = " ")
        print()

def treasure(square) : #기본보드에 보물을 넣어주고 주변에 지뢰 쳐줌(보물위치 리턴)
    tlocation = []
    n = len(square)
    i = random.randint(1,n-2)
    j = random.randint(1,n-2)        
    square[i][j-1] = "X"
    square[i][j+1] = "X"
    square[i-1][j] = "X"
    square[i+1][j] = "X"
    square[i-1][j-1] = "X"
    square[i+1][j+1] = "X"
    square[i+1][j-1] = "X"
    square[i-1][j+1] = "X"
    tlocation.append(i)
    tlocation.append(j)
    return square, tlocation

def putbomb(bomb,square,tlocation) : #랜덤으로 추가 지뢰넣기 (bomb에 지뢰갯수)
    n = len(square)
    while bomb > 0 :
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        if square[i][j] == "X" :
            continue
        if i == tlocation[0] and j == tlocation[1] :
            continue
        square[i][j] = "X"
        bomb = bomb - 1
    return square

def putnumber(square) : #보물and지뢰넣은 보드에 숫자를 넣어줌
    n = len(square)
    for h in range(0,n) :
        for y in range(0,n) :
            if str(square[h][y]) != "X" :
                bombcount = 0
                if y+1<n :
                    if str(square[h][y+1]) == "X" :
                        bombcount = bombcount+1
                if y-1>=0 :
                    if str(square[h][y-1]) == "X" :
                        bombcount = bombcount+1
                if h+1<n :
                    if str(square[h+1][y]) == "X" :
                        bombcount = bombcount+1
                if h-1>=0 :
                    if str(square[h-1][y]) == "X" :
                        bombcount = bombcount+1
                if h+1<n and y+1<n :
                    if str(square[h+1][y+1]) == "X" :
                        bombcount = bombcount+1
                if h-1>=0 and y+1<n :
                    if str(square[h-1][y+1]) == "X" :
                        bombcount = bombcount+1
                if h+1<n and y-1>=0 :
                    if str(square[h+1][y-1]) == "X" :
                        bombcount = bombcount+1
                if h-1>=0 and y-1 >=0 :
                    if str(square[h-1][y-1]) == "X" :
                        bombcount = bombcount+1
                square[h][y] = bombcount
    return square
                        
def tableopen(h,y,table,square) : #칸을 열때 주변 탐색 후 연쇄적으로 열어주는 함수
    n = len(square)
    if y+1<n :
        if square[h][y+1] != "X" and table[h][y+1] == False :
            table[h][y+1] = True
            if square[h][y+1] == 0 :
                table, square = tableopen(h,y+1,table,square)
    if h+1<n :
        if square[h+1][y] != "X" and table[h+1][y] == False :
            table[h+1][y] = True
            if square[h+1][y] == 0 :
                table, square = tableopen(h+1,y,table,square)
    if y-1>=0 :
        if square[h][y-1] != "X" and table[h][y-1] == False :
            table[h][y-1] = True
            if square[h][y-1] == 0 :
                table, square = tableopen(h,y-1,table,square)
    if h-1>=0 :
        if square[h-1][y] != "X" and table[h-1][y] == False :
            table[h-1][y] = True
            if square[h-1][y] == 0 :
                table, square = tableopen(h-1,y,table,square)
    if h+1<n and y+1<n:
        if square[h+1][y+1] != "X" and table[h+1][y+1] == False :
            table[h+1][y+1] = True
            if square[h+1][y+1] == 0 :
                table, square = tableopen(h+1,y+1,table,square)			    
    if h+1<n and y-1>=0 :
        if square[h+1][y-1] != "X" and table[h+1][y-1] == False :
            table[h+1][y-1] = True
            if square[h+1][y-1] == 0 :
                table, square = tableopen(h+1,y-1,table,square)			    
    if h-1>=0 and y-1>=0 :
        if square[h-1][y-1] != "X" and table[h-1][y-1] == False :
            table[h-1][y-1] = True
            if square[h-1][y-1] == 0 :
                table, square = tableopen(h-1,y-1,table,square)			    
    if h-1>=0 and y+1<n :
        if square[h-1][y+1] != "X" and table[h-1][y+1] == False :
            table[h-1][y+1] = True
            if square[h-1][y+1] == 0 :
                table, square = tableopen(h-1,y+1,table,square)
    return table, square


def bombs(n) : #지뢰갯수
    if n == 9 :
        return 12
    else :
        return 52

# 최종함수!!!!!!!!!!!!
def treasure_hunting() :
    print("보물찾기에 오신 것을 환영합니다!")
    num = get_level()
    board_f, locate = treasure(square(num)) #보물주변에 지뢰를 넣음
    board = putnumber(putbomb(bombs(num),board_f,locate)) #추가적으로 지뢰와 숫자 넣음 
    board2 = table(num) #보여줄때 쓸 테이블받음
    flag = {} #깃발 꽂을때 그 칸의 값을 사전으로 저장해둘거
    while True :
        print()
        show_board(board, board2)
        if num == 9 :
            h = get_integer("행을 입력해주세요(1~9): ",1,9)-1
            y = get_integer("열을 입력해주세요(1~9): ",1,9)-1
        elif num == 16 :
            h = get_integer("행을 입력해주세요(1~16): ",1,16)-1
            y = get_integer("열을 입력해주세요(1~16): ",1,16)-1
        if board[h][y] == "■" :
            dab2 = ask("깃발을 뽑으시겠습니까?(y/n) : ")
            if dab2 == True :
                board2[h][y] = False
                board[h][y] = flag[h,y]
                continue
            else :
                continue
        if board2[h][y] == True :
            print("<< 이미 열려있는 칸입니다. >>")
            continue
        dab = ask("깃발을 꽂으시겠습니까?(y/n) : ")
        if dab == True :
            flag[h,y] = board[h][y]
            board[h][y] = "■"
            board2[h][y] = True
        elif dab == False :
            board2[h][y] = True
            board2, board = tableopen(h,y,board2,board) #열어준다
        if board[h][y] == "X" :
            print()
            print("※ 폭탄을 고르셨네요! Game Over. ※")
            board[locate[0]][locate[1]] = "$"
            show_true(board)
            break
        if board[h][y] == board[locate[0]][locate[1]] :
            print()
            print("★ 축하합니다. 보물을 찾았습니다! ★")
            board[locate[0]][locate[1]] = "$"
            show_true(board)
            break
         
treasure_hunting()
         
