# 실습문제 2-1

def mult(m,n) :
    def loop(m,n,ans) :
        if n > 0 :
            return loop(m,n-1,ans+m)
        else :
            return ans
    return loop(m,n,0)



# 실습문제 2-2

def mult2(m,n) :
    ans = 0
    while n > 0 :
        n = n-1
        ans = ans + m
    return ans


# 실습문제 2-3

def double(n) :
    return n*2
def halve(n) :
    return n//2
def even(n) :
    return n%2 == 0
def odd(n) :
    return n%2 == 1


def mult3(m,n) :
    if n > 0 :
        if even(n) :
            return mult(double(m),halve(n))
        else :
            m + mult(m,n-1)
    else :
        return 0


# 실습문제 2-4

def mult4(m,n) :
    def loop(m,n,ans) :
        if n > 0 :
            if even(n) :
                return loop(double(m),halve(n),ans)
            else :
                return loop(m,n-1,m+ans)
        else :
            return ans
    return loop(m,n,0)



# 실습문제 2-5

def mult5(m,n) :
    ans = 0
    while n > 0 :
        if even(n) :
            m = double(m)
            n = halve(n)
        else :
            n = n-1
            ans = m+ans
    return ans



# 실습문제 2-6

def mult6(m,n) :
    def loop(m,n) :
        if n > 1 :
            if odd(n) :
                return m+loop(m*2,n//2)
            else :
                return loop(m*2,n//2)
        else :
             return m
    if n > 0 :
        return loop(m,n)
    else :
        return 0


# 실습문제 2-7

def mult7(m,n) :
    def loop(m,n,ans) :
        if n > 1 :
            if odd(n) :
                return loop(m*2,n//2,ans+m)
            else :
                return loop(m*2,n//2,ans)
        else :
            return ans+m
    if n > 0 :
        return loop(m,n,0)
    else :
        return 0


# 실습문제 2-8

def mult8(m,n) :
    ans = 0
    if n > 0 :
        while n > 1 :
            if odd(n) :
                ans = ans+m
                m = m*2
                n = n//2
            else :
                m = m*2
                n = n//2
        return ans+m
    else :
        return 0

print(mult8(57,86))



            
