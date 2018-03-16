# 1번문제 deep_reverse
#is_list를 사용.

def is_list(x):
   return isinstance(x,list)

def reverse(xs) :
   if xs == [] :
       return []
   elif is_list(xs[0]):
       return reverse(xs[1:])+[reverse(xs[0])]
   else:
       return reverse(xs[1:])+[xs[0]]

print(reverse([1,[2,3,[4,[5,6]]]]))



#대칭정방행렬
x1=[[1,9,5,11],[9,4,7,3],[5,7,-7,8],[11,3,8,6]]
x2=[[1,9,5,1],[9,4,2,3],[5,7,2,8],[11,3,8,6]]
def symmetric_square_matrix(xs):
   for i in range(len(xs)):
       for j in range(len(xs)):
           if xs[i][j] != xs[j][i]:
               return False
   return True
print(symmetric_square_matrix(x1))
print(symmetric_square_matrix(x2))


#수독검사하기
s1=[[1,2,3],[2,3,1],[3,1,2]]
s2=[[1,2,3],[1,2,3],[1,2,3]]
def check_sudok(xs) : 
   def transpose(board) :
       transposed = []
       for i in range(len(board)) :
           transposed.append([])
       for i in range(len(board)) :
           for j in range(len(board)) :
               transposed[j].append(board[i][j])
       return transposed
   check = len(xs)
   for i in range(len(xs)) :
       for j in range(1,len(xs)+1) :
           if not j in xs[i] :
               return False
   xs = transpose(xs)
   for i in range(len(xs)) :
       for j in range(1,len(xs)+1) :
           if not j in xs[i] :
               return False
   return True
print (check_sudok(s1))
print (check_sudok(s2))


"""리스트"""
k1=[3,5,2,8]
#리스트에 있는 정수 모두 곱하기
def list_product(xs) :
   mul = 1
   for i in range(len(xs)) :
       mul *= xs[i]
   return mul

print (list_product(k1))

#리스트에서 가장 큰값찾기
b1=[3,4,5,1,2,22,33,4]
def greatest(xs) :
   if xs == [] :
       return None
   else :
       m = xs[0]
       for y in xs :
           if m < y :
               m = y
       return m

print (greatest(b1))


#리스트에서 연속적으로 가장 많이 반복된 수와 반복회수 내주기
def longest_repetition(xs) :
   if xs == [] :
       return None
   numm = 0
   times = 0
   numsave = 0
   for i in range(0,len(xs)) :
       count = 1
       for j in range(i+1,len(xs)) :
           if xs[i] == xs[j] :
               count = count + 1
               numm = xs[i]
           else :
               break
       if count >= times :
           numsave = numm
           times = count
       i = i+count-1
   return numsave , times
print(longest_repetition ([5,5,4,4,4,4,4,2,2,2,2,7,8,4,4,3,3,3,]))
#빈도계산하기
def freq_analysis(xs) :
   dic = {}
   for i in xs :
       if not (i in dic) :
           dic[i] = 1
       else :
           dic[i] += 1
   keys = dic.keys()
   for i in keys :
       dic[i] = dic[i]/len(xs)*100
   return dic

print(freq_analysis(["s","m","a","s","h"]))


def deep_count(xs):
   count = len(xs)
   for i in xs:
       if is_list(i):
           count += deep_count(i)
   return count
   
print (deep_count([[[[[[[[1,2,3]]]]]]]]))