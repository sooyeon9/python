# 숙제4 - 블랙잭(+추가)
# 작성인 : 2014037756 구수연
# 작성날짜 : 2014.11.24
# 최종수정날짜 : 2014.11.29
# version 2.1

import random

def fresh_deck():  #새로운 카드 1벌을 섞어서 내줌 
    suits = {"Spade", "Heart", "Diamond", "Club"} 
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"} 
    deck = []
    for key in suits :
        for num in ranks :
            deck.append({"suit":key, "rank":num})
    random.shuffle(deck)
    return deck

def hit(deck): #앞장이랑 나머지카드 내줌 
    if deck == []: 
        deck = fresh_deck() 
    return deck[0], deck[1:]

def count_score(hand): #카드 점수의 합을 내줌 
    score = 0
    number_of_ace = 0
    for card in hand:
        rank = card['rank']
        if rank == 'A':
            score += 11
            number_of_ace += 1
        elif rank in {'J', 'Q', 'K'}: 
            score += 10
        else: 
            score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

def show_cards(cards,message): #카드보여줌 
    print(message) 
    for card in cards: 
        print(" ", card["suit"], card["rank"])

def more(message): #예스&노 입력받음 
    answer = input(message) 
    while not (answer == 'y' or answer == 'n'): 
        answer = input(message) 
    if answer == 'y': 
        return True 
    else: 
        return False

#--------------------------------------------------

def load_members() : #텍스트파일로부터 members사전을 불러옴
    file = open("members.txt","r")
    members = {}
    for line in file :
        name, passwd, tries, wins, chips = line.strip("\n").split(",")
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members) : #members사전으로부터 텍스트파일을 저장
    file = open("members.txt","w")
    names = members.keys()
    for name in names :
        passwd, tries, wins, chips = members[name]
        line = name + "," + passwd + "," + \
               str(tries) + "," + str(wins) + "," + str(chips) + "\n"
        file.write(line)
    file.close()

def divide(x,y) : #승률구하는거
    if y > 0 :
        r = "{0:.2f}".format(x/y)
        return int(float(r)*100) 
    else :
        0

def login(members): #로그인함수
    username = input("Enter your name:(4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys() :
        if str(trypasswd) == str(members[username][0]) :
            print("You played",members[username][1],"games and won",members[username][2],"of them.")            
            print("your all-time winning percentage is",divide(members[username][2],members[username][1]),"%")
            if members[username][3] > 0 :
                print("You have",members[username][3],"chips.")
            elif members[username][3] < 0:
                print("You owe",members[username][3]*-1,"chips.")
            else:
                print("no chips")
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            return username, int(tries), float(wins), int(chips), members           
        else :
            login(members)
    else:
        members[str(username)]=(trypasswd,0,0,0)
        return username, 0, 0, 0, members

def show_top5(members): #랭킹함수
    print("-----")
    sorted_members = sorted(members.items(),key =lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    for i in range(5) :
        if sorted_members[i][1][3] > 0 :       
            print(sorted_members[i][0],":",sorted_members[i][1][3],"chips")

# 최종함수!!!!!!!!!!
def blackjack():
    print("Welcome to SMaSH Casino!")
    username, tries, wins, chips, members = login(load_members())
    deck = fresh_deck()
    while True :
        tries += 1
        print("-----")
        dealer = []  
        player = []
        card, deck = hit(deck)   # 1장 뽑아서
        player.append(card)      # 손님에게 주고
        card, deck = hit(deck)   # 1장 뽑아서
        dealer.append(card)      # 딜러에게 주고
        card, deck = hit(deck)   # 1장 뽑아서
        player.append(card)      # 손님에게 주고
        card, deck = hit(deck)   # 1장 뽑아서
        dealer.append(card)      # 딜러에게 준다.
        print("My cards are:") 
        print(" ", "****", "**") 
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        #카드분배가 끝났음
        if int(score_player) == 21 : #블랙잭일때
            chips += 2
            wins += 1
            print("Blackjack! You won.")
            print("Chips =",chips)
        else :
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card["suit"], card["rank"])
            if score_player > 21:
                chips -= 1
                print("You bust! I won.")
                print("Chips =",chips)
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    chips += 1
                    wins += 1
                    print("I bust! You won.")
                elif score_dealer == score_player:
                    wins += 0.5
                    print("We draw.")
                elif score_dealer > score_player:
                    chips -= 1
                    print("I won.")
                else:
                    print("You won.")
                    chips += 1
                    wins += 1
                print("Chips =",chips)
        if not more("Play more? (y/n) "):
            break
    print("Bye!")
    print("-----")
    members[username] = (members[username][0],tries,wins,chips)
    store_members(members)
    print("You played",tries,"games and won",wins,"of them.")
    print("Your winning percentage today is",divide(wins,tries),"%")
    show_top5(members)

blackjack()         
