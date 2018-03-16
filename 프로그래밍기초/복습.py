def test1(xs) : #대입리스트는 바뀌지않음
    xs = xs + [6]
    return xs

def test2(xs) : #대입리스트 바뀜 -> 대입리스트를 훼손시킴
    xs.append(6)
    return xs

def test2_2(xs) : #test2를 보완시킴 (대입리스트를 복사)
    xs = xs[:]#복사!!!!
    xs.append(6)
    return xs

def test3(xs) : #대입리스트도 바뀜
    xs += [6]
    return xs

xs1 = [1,2,3,4]
xs2 = [1,2,3,4]
xs3 = [1,2,3,4]

#----------------------------


def is_list(x) : #중첩리스트니? 물어보는 함수(T or F 리턴)
    return isinstance(x,list)

def reverse(xs) : #중첩된 리스트는 뒤바뀌지않음
    xs = xs[:]#복사!!!
    xs.reverse()
    return xs

def reverse2(xs) : #위 함수의 재귀버전
    if xs != [] :
        return reverse2(xs[1:]) + [xs[0]]
    else :
        return []

def deep_reverse(xs) :
    if xs != [] :
        if is_list(xs[0]) : #중첩이면 xs[0]도 딥리버스 들어가고
            return deep_reverse(xs[1:]) + [deep_reverse(xs[0])]
        else : #아니면 보통으로
            return deep_reverse(xs[1:]) + [xs[0]]
    else :
        return []

ex = [1,[2,3,[4,[5,6]]]]


def ssm(xs) : #대칭정방행렬
    for i in range(len(xs)) :
        for j in range(len(xs)) :
            if xs[i][j] != xs[j][i] :
                return False
    return True

def check_sudok(xs) : #수독검사
    h,y = [], []
    n = len(xs)
    for i in range(n) :
        for j in range(n) :
            h.append(xs[i][j])
            y.append(xs[j][i])
        for a in range(n) :
            c = h.count(h[a]) + y.count(y[a])
            if c > 2 :
                return False
        h,y = [], []
    return True

def list_product(xs) : #정수 모두 곱하기
    product = 1
    if xs == [] :
        return product
    else :
        for i in range(len(xs)) :
            product = product * xs[i]
        return product

def bigger(x,y) :
    if x>y : return x
    else : return y
    
def greatest(xs) : #가장 큰 값 찾기
    num = 0
    if len(xs) != 0 :
        for i in range(len(xs)) :
            num = bigger(num,xs[i])
        return num
    else :
        return None
                
def longest_repetition(xs) : #가장 많이 연속적으로 반복된수와 반복횟수 내주기
    if len(xs) != 0 :
        num = 0
        times = 0
        midnum = 0
        for i in range(0,len(xs)) :
            midtimes= 1
            for j in range(i+1,len(xs)) :
                if xs[i] == xs[j] :
                    midtimes += 1
                    midnum = xs[i]
                else :
                    break
            if midtimes > times :
                times = midtimes
                num = midnum
        return num, times
    else :
        return None
        
#print(longest_repetition([2,2,3,3,3,4,4,4,2,2,2,4]))

def freq_analysis(xs) : #출연빈도 계산하기
    dic = {}
    for i in xs :
        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1
    keys = dic.keys()
    for a in keys :
        dic[a] = dic[a]/len(xs) * 100
    return dic

#s = ["s","m","a","s","h"]
#print(freq_analysis(s))

def deep_count(xs): #중첩리스트 개수세기
   count = len(xs)
   for i in xs:
       if is_list(i):
           count += deep_count(i)
   return coun

#print(deep_count([[[[[[[[1,2,3]]]]]]]]))


        



    
            
                

    

