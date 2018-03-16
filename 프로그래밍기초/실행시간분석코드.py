#열한째날 - 실행시간 분석


# linear search

def linear_search_while(key,xs):
    i = 0
    while i < len(xs) and key != xs[i]:
        i += 1
    return i

def linear_search_for(key,xs):
    i = 0
    for x in xs:
        if key == x:
            return i
        i += 1
    return i

def binary_search(key,xs):
    low = 0              
    high = len(xs) - 1   
    index = -1           
    while low <= high and index == -1:
        mid = (high + low) // 2
        if key == xs[mid]:
            index = mid
        elif key < xs[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return index

import time
def search_time():
    def timer(search,key,xs): 
        t1 = time.clock()
        search(key,xs)
        t2 = time.clock()
        return (t2 - t1) * 1000000
    xs = [x for x in range(100000)]
    print("선형검색(while 버전)")
    print("first:",int(timer(linear_search_while,0,xs)),"micro sec")
    print("middle:",int(timer(linear_search_while,50000,xs)),"micro sec")
    print("last:",int(timer(linear_search_while,99999,xs)),"micro sec")
    print()
    print("선형검색(for 버전)")
    print("first:",int(timer(linear_search_for,0,xs)),"micro sec")
    print("middle:",int(timer(linear_search_for,50000,xs)),"micro sec")
    print("last:",int(timer(linear_search_for,99999,xs)),"micro sec")
    print()
    print("Python 라이브러리 메소드")
    t1 = time.clock()
    xs.index(0)
    t2 = time.clock()
    print("first:",int((t2-t1)*1000000),"micro sec")
    t1 = time.clock()
    xs.index(50000)
    t2 = time.clock()
    print("middle:",int((t2-t1)*1000000),"micro sec")
    t1 = time.clock()
    xs.index(99999)
    t2 = time.clock()
    print("last:",int((t2-t1)*1000000),"micro sec")
    print()
    print("이분검색")
    print("first:",int(timer(binary_search,0,xs)),"micro sec")
    print("middle:",int(timer(binary_search,66666,xs)),"micro sec")
    print("last:",int(timer(binary_search,99999,xs)),"micro sec")
    print("none:",int(timer(binary_search,-1,xs)),"micro sec")


# insertion sort

def insert(x,ss):
    rs = []
    while ss != []:
        if x <= ss[0]:
            rs.append(x)
            return rs + ss
        else:
            rs.append(ss[0])
            ss = ss[1:]
    rs.append(x)
    return rs

def insert(x,ss):
    rs = []
    for s in ss:
        if x <= s:
            rs.append(x)
            return rs + ss
        else:
            rs.append(s)
    rs.append(x)
    return rs

def isort_w(xs) :
    ss = []
    while xs != [] :
        ss = insert(xs[0],ss)
        xs = xs[1:]
    return ss

def isort(xs):
    ss = []
    for x in xs:
        ss = insert(x,ss)
    return ss

# selection sort

def smaller(x,y) :
    if x < y : return x
    else : return y

def smallest(xs) :
    (x,xs) = (xs[0],xs[1:])
    while xs != [] :
        x = smaller(xs[0],x)
        xs = xs[1:]
    return x

def ssort(xs) :
    ss = []
    while xs != []:
        x = smallest(xs)
        xs.remove(x)
        ss.append(x)
    return ss

# merge sort

def merge(xs,ys):
    rs = []
    while xs != [] and ys!= []:
        if xs[0] <= ys[0]:
            rs.append(xs[0])
            xs = xs[1:]
        else:
            rs.append(ys[0])
            ys = ys[1:]
    return rs + xs + ys

def msort(xs):
    if xs != [] and xs[1:] != []:
        mid = len(xs) // 2
        return merge(msort(xs[:mid]),msort(xs[mid:]))
    else:
        return xs

# Quicksort

def partition(pivot,xs):
    left = []
    right = []
    for x in xs:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left,right

def qsort(xs):
    if xs != []:
        pivot = xs[0]
        left, right = partition(pivot,xs[1:])
        return qsort(left) + [pivot] + qsort(right)
    else:
        return []

# Sort testing

import random
def ascending_list():
    return [x for x in range(100)]

def descending_list():
    return [x for x in range(100,0,-1)]

def random_list():
    xs = [x for x in range(100)]
    random.shuffle(xs)
    return xs

import time
def sort_time():
    def timer(sort,xs): 
        t1 = time.clock()
        sort(xs)
        t2 = time.clock()
        return (t2 - t1) * 1000000
    up = ascending_list()
    down = descending_list()
    ran = random_list()
    ran1 = ran[:]
    ran2 = ran[:]
    ran3 = ran[:]
    ran4 = ran[:]
    ran5 = ran[:]
    print("삽입정렬")
    print("오름차순:",int(timer(isort,up)),"micro sec")
    print("내림차순:",int(timer(isort,down)),"micro sec")
    print("랜덤:",int(timer(isort,ran1)),"micro sec")
    print()
    up = ascending_list()
    down = descending_list()
    print("선택정렬")
    print("오름차순:",int(timer(ssort,up)),"micro sec")
    print("내림차순:",int(timer(ssort,down)),"micro sec")
    print("랜덤:",int(timer(ssort,ran2)),"micro sec")
    print()
    up = ascending_list()
    down = descending_list()
    print("합병정렬")
    print("오름차순:",int(timer(msort,up)),"micro sec")
    print("내림차순:",int(timer(msort,down)),"micro sec")
    print("랜덤:",int(timer(msort,ran3)),"micro sec")
    print()
    up = ascending_list()
    down = descending_list()
    print("퀵정렬")
    print("오름차순:",int(timer(qsort,up)),"micro sec")
    print("내림차순:",int(timer(qsort,down)),"micro sec")
    print("랜덤:",int(timer(qsort,ran4)),"micro sec")
    print()
    up = ascending_list()
    down = descending_list()
    print("Python 라이브러리 메소드")
    t1 = time.clock()
    up.sort()
    t2 = time.clock()
    print("오름차순:",int((t2-t1)*1000000),"micro sec")
    t1 = time.clock()
    down.sort()
    t2 = time.clock()
    print("내림차순:",int((t2-t1)*1000000),"micro sec")
    t1 = time.clock()
    ran5.sort()
    t2 = time.clock()
    print("랜덤:",int((t2-t1)*1000000),"micro sec")
    


sort_time()

