# 실습문제 3번
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.9.21

# 주민등록번호 입력 확인



def format_ok(front,mid,back) :
    if len(front)==6 and front.isdigit() and mid == "-" and len(back)==7 and back.isdigit()) :
        return True


def last_digit_ok(s) :
    a = 11 -((2*int(s[0])+3*int(s[1])+4*int(s[2])+5*int(s[3])+6*int(s[4])+7*int(s[5])+8*int(s[7])+9*int(s[8])+2*int(s[9])+3*int(s[10])+4*int(s[11])+5*int(s[12])) % 11)
    if a == int(s[12]) :
        return True

def isRNN(message) :
    s = input(message)
    (front,mid,back) = s.partition("-")
    while not (format_ok(front,mid,back) and last_digit_ok(front+back)) :
        print ("Invalid number")
        s = input(message)
        (front,mid,back) = s.partition("-")
    return s
