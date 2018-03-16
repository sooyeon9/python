# 숙제 : 이메일 주소 입력 확인
# 작성인 : 2014037756 컴퓨터공학과 구수연
# 작성날짜 : 2014.9.24
# version 1.0




# 주석 제거 함수

def remove_comments(x) :
    if x.startswith("(") :
        (f,m,b)=x.partition(")")
        x = b
        return x
    elif x.endswith(")") :
        (f,m,b)=x.partition("(")
        x = f
        return x
    else :
        return x

# 특수문자 함수

def special_ok(a) :
    specials = ["!","#","$","%","&","'","*","+","-","/","=","?","^","_","`","{","|","}","~"]
    for i in range(0,19) :
        if a.count(specials[i]) >= 1 :
            return 1

# 로컬 이름 함수                    

def local_ok(l) :
    l = remove_comments(l)
    if l.isalnum() or special_ok(l) == 1 :
        return True
    elif l.count("..") >= 1 :
        return False
    elif l.startswith(".") or l.endswith(".") :
        return False
    else :
        return True

# 호스트 이름 함수

def hostname_ok(h) :
    if h.count("..") >= 1 or h.startswith(".") or h.endswith(".") :
        return False
    elif len(h) > 256 :
        return False
    elif h.startswith("[") and h.endswith("]") :
        return True
    else :
        return True    

    

# 최종 점검 함수

def get_email(message) :
    s = input(message)
    s = remove_comments(s)
    (l,m,h) = s.partition("@")
    while not (s.count("@")==1 and local_ok(l) and hostname_ok(h)) :
        print ("잘못된 이메일 주소이므로 다시 입력 부탁.")
        s = input(message)
        s = remove_comments(s)
        (l,m,h) = s.partition("@")
    return s

print("<프기과제 - 이메일 주소 입력확인>\n")
a = get_email("이메일 주소를 입력해라.\n")
print (a)
