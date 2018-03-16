# 문제 #1 - 삼각수 구하기

def triangular(n):
    total = 0
    if n > 0 :
        for i in range(n+1) :
            total = total + i
    else :
        total = 0
    return total

# 테스트케이스
#print(triangular(1))
#print(triangular(3))
#print(triangular(6))
#print(triangular(11))
#print(triangular(-3))

# 답
# 1
# 6
# 21
# 66
# 0



# 문제#2 - flatter

def is_list(xs): return isinstance(xs,list)

def flatter(xss):
    xs = []
    for i in xss :
        if is_list(i) :
            if i != [] :
                for a in i :
                    flatter(a)
        else :
            xs.append(i)
    return xs

# 테스트케이스
#print(flatter([1,2,3]))
#print(flatter([1,[],3]))
#print(flatter([1,[1,2,[3,4]]]))
#print(flatter([[[[[[[[1,2,3]]]]]]]]))
#print(flatter([]))
#print(flatter([[[[3]],[4]],5,6,[7]]))

# 답
# [1, 2, 3]
# [1, 3]
# [1, 1, 2, 3, 4]
# [1, 2, 3]
# []
# [3, 4, 5, 6, 7]


# 문제 #3: 정방행렬 - 항등행렬 검사 

def identity(sqmat):
    size = len(sqmat)
    for i in range(size) :
        for j in range(size) :
            if i==j :
                if sqmat[i][j] != 1 :
                    return False
            elif sqmat[i][j] != 0 :
                return False
    return True

xs0 = [[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]]
xs1 = [[1,0,0,0],
       [0,2,0,0],
       [0,0,1,0],
       [0,0,0,1]]
xs2 = [[0,-3,6,4],
       [3,0,-9,8],
       [-6,9,0,2],
       [-4,-8,-2,0]]

# 테스트케이스
#print(identity(xs0))
#print(identity(xs1))
#print(identity(xs2))

# 답
# True
# False
# False

# 문제 #4: 정방행렬 - 반대칭행렬 검사

def antisymmetric(sqmat):
    size = len(sqmat)
    for i in range(size) :
        for j in range(size) :
            if sqmat[i][j] != -sqmat[j][i] :
                return False                
    return True

# 테스트케이스
#print(antisymmetric(xs0))
#print(antisymmetric(xs1))
#print(antisymmetric(xs2))

# 답
# False
# False
# True



courses = \
{'1-2': {'MAT2020': {'name': '이산수학', 'professor': '김영훈'},
         'CSE1017': {'name': '프로그래밍기초', 'professor': '도경구'}},
 '2-1': {'ELE3037': {'name': '확률과통계', 'professor': '이정규'},
         'CSE2016': {'name': '프로그램설계방법론', 'professor': '김광'},
         'CSE1007': {'name': '논리학', 'professor': '김영훈'}},
 '2-2': {'CSE2010': {'name': '자료구조론', 'professor': '조성현'},
         'ELE3029': {'name': '오토마타와형식언어론', 'professor': '김한우'},
         'CSE2018': {'name': '시스템프로그래밍기초', 'professor': '강경태'},
         'CSE3003': {'name': '디지탈논리설계', 'professor': '박성주'}},
 '3-1': {'ELE3034': {'name': '알고리즘설계와분석', 'professor': '김태형'},
         'ENE1004': {'name': '컴퓨터구조', 'professor': '박성주'},
         'COM2005': {'name': '운영체제론', 'professor': '강경태'},
         'CSE3010': {'name': '데이터베이스', 'professor': '이동호'}},
 '3-2': {'CSE4009': {'name': '시스템프로그래밍', 'professor': '이동호'},
         'CSE4007': {'name': '인공지능', 'professor': '이석복'},
         'CSE3029': {'name': '암호학', 'professor': '오희국'},
         'CSE3027': {'name': '컴퓨터네트워크', 'professor': '이석복'},
         'CSE3026': {'name': '웹애플리케이션개발', 'professor': 'Scott Lee'}},
 '4-1': {'ENE4014': {'name': '프로그래밍언어론', 'professor': '도경구'},
         'ITE4007': {'name': '컴퓨터보안', 'professor': '오희국'},
         'CSE4006': {'name': '소프트웨어공학', 'professor': 'Scott Lee'},
         'ELE4076': {'name': '정보검색론', 'professor': '김영훈'},
         'ELE3026': {'name': '객체지향개발론', 'professor': '김정선'}}}

# 문제#5: is_offered

def is_offered(courses,course,semester):
    if semester in courses :        
        if course in courses[semester] :
            return True
        else :
            return False
    else :
        return None

# 테스트케이스
#print(is_offered(courses,'CSE1017','1-2'))
#print(is_offered(courses,'CSE1017','2-1'))
#print(is_offered(courses,'CSE1017','1-1'))

# 답
# True
# False
# None


# 문제#6: when_offered

def when_offered(courses,course):
    sems = []
    semkey = courses.keys()
    for a in semkey :
        if course in courses[a] :
            sems.append(a)
    return sems

# 테스트케이스
#print(when_offered(courses,'CSE1017'))
#print(when_offered(courses,'ENE4014'))
#print(when_offered(courses,'CSE1111'))

# 답
# ['1-2']
# ['4-1']
# []

# 문제#7: involved
    
def courses_offered(courses, semester): #그 학기의 강의번호 리턴
    offered = []
    for c in courses[semester]:
        offered.append(c)
    return offered

def involved(courses,person):
    pcs = {}
    for sem in courses.keys() :
        for code in courses[sem].keys() :
            if person in courses[sem][code].values() :
                pcs[sem] = code    
    return pcs


# 테스트케이스
#print(involved(courses,'도경구'))
#print(involved(courses,'김영훈'))
#print(involved(courses,'전창호'))
#print(involved(courses,''))

# 답
# {'4-1': ['ENE4014'], '1-2': ['CSE1017']}
# {'4-1': ['ELE4076'], '2-1': ['CSE1007'], '1-2': ['MAT2020']}
# {}
# {}

# 문제#8: digit frequencies

def digit_freq(s):
    freqs = [0,0,0,0,0,0,0,0,0,0] #아무것도없을때
    dfreqs = []
    mid = []
    if len(s) != 0 :        
        for i in range(10) :
            mid.append((s.count(str(i)),str(i)))
            if s.count(str(i)) > 1 :
                mid.sort()
                mid.reverse()
        for i in range(10) :
            dfreqs.append((mid[i][1],mid[i][0]))   
    else :
        for i in range(10) :
            dfreqs.append((str(i),freqs[i]))                
    return dfreqs 

# 테스트케이스
#print(digit_freq(""))
#print(digit_freq("0987654321"))
#print(digit_freq("30774378274672034827764362738473"))

# 답
# [('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0),
#  ('5', 0), ('6', 0), ('7', 0), ('8', 0), ('9', 0)]
# [('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1),
#  ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1)]
# [('7', 9), ('3', 6), ('4', 5), ('2', 4), ('6', 3),
#  ('8', 3), ('0', 2), ('1', 0), ('5', 0), ('9', 0)]
    

