# 실습문제 4번
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.9.22

# 주석 제거 함수

def remove_comments(message) :
    a=input(message)
    if a.startswith("(") :
        (f,m,b)=a.partition(")")
        a=b
        return a
    elif a.endswith(")") :
        (f,m,b)=a.partition("(")
        a=f
        return a
    else :
        return a
print (remove_comments("입력하시오.\n "))
