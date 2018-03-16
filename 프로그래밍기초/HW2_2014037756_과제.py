# 특정 문자열이 들어있는 문장 모두 찾기
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.9.27
# 최종수정날짜 : 2014.10.07
# version 1.1


# totalkey = 총 나오는 횟수
# sentencecount = 나오는 문장 총 개수
# k = 문장 내에서 나오는 개수

def find_all_sentence(filename,key) :
    infile = open(filename,"r")
    midfile = open("line.txt","w")
    outfile = open("result9.txt","a")

    text = infile.read()
    text = text.replace("\n","")
    text = text.replace(". ",".\n")
    text = text.replace("?","?\n")
    midfile.write(text)

    midfile.close()
    infile.close()

    midfile = open("line.txt","r")
    linetextlist = midfile.readlines()
    midfile.close()
# 문장별줄바꿈 텍스트을 만들고 lintextlist변수에 각 문장별로 리스트를 만들어서 넣어줌    

    midfile = open("line.txt","r")
    linetext = midfile.read()
# linetext변수에 문장별줄바꿈 텍스트를 통째로 넣어줌

    totalkey = linetext.count(key)
    sentencecount = 0
    k = []
    
    for i in range(0,len(linetextlist)-1) :
        k.append(linetextlist[i].count(key))
        if int(k[i]) != 0 :
            sentencecount += 1
            outfile.write(key+"는 "+str(k[i])+"번 등장"+"\n")
            outfile.write(str(linetextlist[i])+"\n")           
            

    outfile.write(key+"는 총 "+str(sentencecount)+"개의 문장에서 "+str(totalkey)+"번 등장"+"\n")
    midfile.close()
    outfile.close()
    print("Done")



find_all_sentence("article.txt","컴퓨터")
    
