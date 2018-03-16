# <실습문제 코딩>
# 기본적 정의 함수
nil = []
def head(xs) : return xs[0]
def tail(xs) : return xs[1:]
def null(xs) : return xs == nil #리스트가 빈리스트이면 T
def cons(x,xs) : return [x] + xs #리스트 앞에 원소 하나 추가해줌
def snoc(xs,x) : return xs + [x] #리스트 마지막에 원소 하나 추가해줌
def concat(xs,ys) : return xs + ys #리스트끼리 합쳐줌

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ns = [2,4,5,7,8] # 끼워넣는 1-2,1-3사용 print(insert(6,ns))
ns2 = [4,7,5,2,8] # 정렬하는 1-4,1-5,2-3,2-4사용 print(isort(ns2))
ns3 = [2,5,4] # 작은수찾는 2-1,2-2사용 print(smallest(ns3))


# 실습 1-1 재귀
def insert(x,ss) : #기본틀-정렬된 리스트에 알맞은 위치에다 새 원소 삽입
    if not null(ss) :
        if x <= head(ss) :
            return cons(x,ss)
        else :
            return cons(head(ss),insert(x,tail(ss)))
    else :
        return cons(x,nil)



# 실습 1-2 꼬리재귀 ★★★
def insert2(x,ss) :
    def loop(ss,rs) :
        if not null(ss) :
            if x <= head(ss) :
                return concat(rs,cons(x,ss))
            else :
                return loop(tail(ss),snoc(rs,head(ss)))
        else :
            return snoc(rs,x)
    return loop(ss,nil)


# 실습 1-3 반복
def insert3(x,ss) :
    rs = nil
    while not null(ss) :
        if x <= head(ss) :
            return concat(rs,cons(ss))
        else :
            rs = snoc(rs,head(ss))
            ss = tail(ss)
    return snoc(rs,x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 실습 1-4 꼬리재귀 ★★★
def isort(xs) : #기본틀-정렬함수
    if not null(xs) :
        return insert(head(xs),isort(tail(xs)))
    else :
        return nil 

def isort2(xs) :
    def loop(xs,ss) :
        if not null(xs) :
            return loop(tail(xs),insert(head(xs),ss)) #??왜 loop???
        else :
            return ss
    return loop(xs,nil)


# 실습 1-5 반복
def isort3(xs) :
    ss = nil
    while not null(xs) :
        ss = insert(head(xs),ss)
        xs = tail(xs)
    return ss

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 2-1 꼬리재귀
def smaller(x,y) : #두 수 중에 작은 수 찾기
    if x < y : return x
    else : return y

def smallest(xs) : #리스트중에 가장 작은 수 찾기
    if length(xs) > 1 :
        x = smallest(tail(xs))
        return smaller(head(xs),x)
    else :
        return head(xs)

def length(xs) : #리스트 길이 구하는 함수
    if not null(xs) :
        return 1 + length(tail(xs))
    else :
        return 0

def smallest2(xs) :
    def loop(xs,x) :
        if not null(xs) :
            return loop(tail(xs),smaller(head(xs),x)) #??왜 loop???
        else :
            return x
    return loop(tail(xs),head(xs))

# 실습 2-2 반복
def smallest3(xs) :
    (xs, x) = (tail(xs), head(xs))
    while not null(xs) :
        x = smaller(head(xs),x)
        xs = tail(xs)
    return x

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 실습 2-3 꼬리재귀 ★★★
def ssort(xs) : #기본틀-작은수대로 정렬함수
    if not null(xs) :
        x = smallest(xs)
        return cons(x,ssort(removeone(x,xs)))
    else :
        return nil

def removeone(x,xs) : #원소 하나만 제거하기
    if not null(xs) :
        if x == head(xs) :
            return tail(xs)
        else :
            return cons(head(xs),removeone(x,tail(xs)))

    else :
        return nil

def ssort2(xs) :
    def loop(xs,x) :
        if not null(xs) :
            return loop(removeone(smallest(xs),xs),snoc(x,smallest(xs)))
        else :
            return x 
    return loop(xs,[])
            
# 실습 2-4 반복
def ssort3(xs) :
    x = []
    while not null(xs) :
        x = snoc(x,smallest(xs))
        xs = removeone(smallest(xs),xs)
    return x

