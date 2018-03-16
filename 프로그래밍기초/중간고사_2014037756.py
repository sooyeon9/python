# -*- coding: cp949 -*-
# 프로그래밍기초 시험 코드 양식
# 한양대학교 ERICA 컴퓨커공학과
# 2014년 1학기
# 학번: 2014037756
# 이름: 구수연
# 반: 금

# 1-가 [10점]

def grade(message) :
    s = input(message)
    while not (s.isdigit() and 0<=int(s)<=100 ) :
        s = input(message)
    s = int(s)
    if 0<=s<=59 :
        print("학점: F")
    elif 60<=s<=69 :
        print("학점: D")
    elif 70<=s<=79 :
        print("학점: C")
    elif 80<=s<=89 :
        print("학점: B")
    else :
        print("학점: A")
    return print("1-가 프로그램 안녕")

print(grade("백분위 점수: "))


# 1-나 [10점]

def grade(message) :
    s = input(message)
    while not (s.isdigit() and 0<=int(s)<=100 ) :
        s = input(message)
    s = int(s)
    if 0<=s<=59 :
        print("학점: F")
    elif 60<=s<=69 :
        print("학점: D")
    elif 70<=s<=79 :
        print("학점: C")
    elif 80<=s<=89 :
        print("학점: B")
    else :
        print("학점: A")
    return print(grade2("더할래?(y/n) "))

def grade2(message) :
    a = input(message)
    while a != "y" and a != "n" :
        a = input(message)
    if a == "y" :
        return print(grade("백분위 점수: "))
    else :
        return print("1-나 프로그램 안녕")

print(grade("백분위 점수: "))


# 2 [10점]

def bigger(a,b) :
    if a > b :
        return a
    else :
        return b

def biggest(a,b,c):
    return bigger(bigger(a,b),c)

def median(a,b,c):
    n = biggest(a,b,c)
    if a==n:
        dad = bigger(b,c)
    elif b==n:
        dad = bigger(a,c)
    elif c==n:
        dad = bigger(a,b)
    return dad

    
# 3 [10점]

def fillwith_(sentence):
    text = sentence.split(" ")
    a = []
    dad = ""
    for i in range(0,len(text)-1) :
        a.append(str(text[i])+"_")
        dad = dad + str(a[i])
    dad = dad + str(text[len(text)-1])
    return print(dad)

print(fillwith_("나는 한양대학교 컴퓨터공학과 학생이 되어 너무 행복하다."))



# 4 [15점]

def sum(lower,upper) :
    if lower <= upper :
        return lower + sum(lower+1,upper)
    else :
        return 0
    
def sum(lower,upper) :
    def loop(lower,total) :
        if lower <= upper :
            return loop(lower+1,total+lower)
        else :
            return total
    return loop(lower,0)
	
def sum(lower,upper) :
    total = 0
    while lower <= upper :
        total = total+lower
        lower = lower+1
    return total

# List functions
nil = []
def null(xs): return xs == []
def cons(x,xs): return [x]+xs
def head(xs): return xs[0]
def tail(xs): return xs[1:]
def snoc(xs,x): return xs+[x]
def concat(xs,ys): return xs+ys

# 5 [15점]
def take(n,xs):
    if n > 0 and not null(xs):
        return cons(head(xs),take(n-1,tail(xs)))
    else:
        return nil

def take(n,xs):
    def loop(n,xs,rs):
        if n > 0 and not null(xs):
            return loop(n-1,tail(xs),snoc(rs,head(xs)))
        else:
            return rs
    return loop(n,xs,nil)

def take(n,xs):
    rs = nil
    while n > 0 and not null(xs):
        n = n-1
        rs = snoc(rs,head(xs))
        xs = tail(xs)
    return rs
        

"""
ns = cons(1,cons(2,cons(3,cons(4,cons(5,nil)))))
print(take(10,ns))
print(take(3,ns))
print(take(0,ns))
print(take(-2,ns))
print(take(3,nil))

"""

# 6 [30점]
def member(x,xs):
    return not null(xs) and (x == head(xs) or member(x,tail(xs)))

def remove(x,xs):
    if not null(xs) :
        if x == head(xs) :
            return tail(xs)
        else :
            return cons(head(xs),remove(x,tail(xs)))
    else :
        return nil
            
def union(xs,ys) :
    pass

def intersection(xs,ys) :
    dad = nil
    if not null(xs) and not null(ys) :
        while member(head(xs),ys) :
            dad = snoc(dad,head(xs))
            xs = tail(xs)
        return dad
    elif null(xs) and not null(ys) :
        return ys
    elif not null(xs) and null(ys) :
        return xs
    else :
        return nil
    
def difference(xs,ys) :
    if not null(xs) and not null(ys) :
        return difference(remove(head(ys),xs),tail(ys))
    elif null(xs) and not null(ys) :
        return nil
    elif not null(xs) and null(ys) :
        return xs
    else :
        return nil



