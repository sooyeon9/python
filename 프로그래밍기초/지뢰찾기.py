# -*- coding: ms949 -*-


import random


array = [	
				['O','O','O','O','O','O','O','O','O','O'], 
				['O','O','O','O','O','O','O','O','O','O'], 
				['O','O','O','O','O','O','O','O','O','O'], 
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O'],
				['O','O','O','O','O','O','O','O','O','O']	
																	]


arrst = [
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False],
				[False, False, False, False, False, False, False, False, False, False]
																										]

OpenCount = 0
JiCount = 2

def RandomInJi() : #���ڳִ°�
	ji = 0
	while ji < JiCount :
		x = random.randrange(0,10)
		y = random.randrange(0,10)
		if array[y][x] == 'O' :
			array[y][x] = 'X'
			ji+=1


def AllRealShow() : #��Ǯ� ���� �� �����ִ°�
	for i in range(0,10) :
		for j in range(0,10) :
			print(array[i][j], end = " ");
		print();
	print("\n\n----------------------------------------------------\n\n");


def AroundFind() :
	for y in range(0,10) :
		for x in range(0,10) :
			if array[y][x] != 'X' :
				jicount = 0
				if x+1 < 10 :
					if array[y][x+1] == 'X' :
						jicount += 1;
				if x-1 >= 0 :
					if array[y][x-1] == 'X' :
						jicount += 1;
				if y+1 < 10 :
					if array[y+1][x] == 'X' :
						jicount += 1;
				if y-1 >= 0 :
					if array[y-1][x] == 'X' :
						jicount += 1;
				if y+1 < 10 and x+1 < 10 :
					if array[y+1][x+1] == 'X' :
						jicount += 1;
				if y-1 >= 0 and x+1 < 10 :
					if array[y-1][x+1] == 'X' :
						jicount += 1;
				if y+1 < 10 and x-1 >= 0 :
					if array[y+1][x-1] == 'X' :
						jicount += 1;
				if y-1 >= 0 and x-1 >= 0 :
					if array[y-1][x-1] == 'X' :
						jicount += 1;
				array[y][x] = jicount;


def AllShow() : #Ʋ������ array�� �����ִ°�
	for i in range(0,10) :
		for j in range(0,10) :
			if arrst[i][j] == True :
				print(array[i][j], end = " ");
			else :

				print("*", end = " ");
		print();


def CheckAround(nY, nX) : #����ã�Ƽ� true�־��ִ°�
	global OpenCount

	if nX +1 < 10 :
		if array[nY][nX+1] != 'X' and arrst[nY][nX+1] == False :
			OpenCount += 1;
			arrst[nY][nX+1] = True;
			if array[nY][nX+1] == 0 :
				CheckAround(nY,nX+1);
	if nY+1  < 10 :
		if array[nY+1][nX] != 'X' and arrst[nY+1][nX] == False :
			OpenCount += 1;
			arrst[nY+1][nX] = True;
			if array[nY+1][nX] == 0 :
				CheckAround(nY+1,nX);
	if nX -1 >= 0 :
		if array[nY][nX-1] != 'X' and arrst[nY][nX-1] == False :
			OpenCount += 1;
			arrst[nY][nX-1] = True;
			if array[nY][nX-1] == 0 :
				CheckAround(nY,nX-1);
	if nY -1 >= 0 :
		if array[nY-1][nX] != 'X' and arrst[nY-1][nX] == False :
			OpenCount += 1;
			arrst[nY-1][nX] = True;
			if array[nY-1][nX] == 0 :
				CheckAround(nY-1,nX);

	if nY +1 < 10  and nX +1  < 10:
		if array[nY+1][nX+1] != 'X' and arrst[nY+1][nX+1] == False :
			OpenCount += 1;
			arrst[nY+1][nX+1] = True;
			if array[nY+1][nX+1] == 0 :
				CheckAround(nY+1,nX+1);
	if nY+1  < 10 and nX -1 >= 0 :
		if array[nY+1][nX-1] != 'X' and arrst[nY+1][nX-1] == False :
			OpenCount += 1;
			arrst[nY+1][nX-1] = True;
			if array[nY+1][nX-1] == 0 :
				CheckAround(nY+1,nX-1);
	if nY-1 >= 0 and nX -1 >= 0 :
		if array[nY-1][nX-1] != 'X' and arrst[nY-1][nX-1] == False :
			OpenCount += 1;
			arrst[nY-1][nX-1] = True;
			if array[nY-1][nX-1] == 0 :
				CheckAround(nY-1,nX-1);
	if nY -1 >= 0 and nX +1 < 10 :
		if array[nY-1][nX] != 'X' and arrst[nY-1][nX+1] == False :
			OpenCount += 1;
			arrst[nY-1][nX+1] = True;
			if array[nY-1][nX+1] == 0 :
				CheckAround(nY-1,nX+1);


def AllOpenJi() : #����
	for nY in range(0,10) :
		for nX in range(0,10) :
			if array[nY][nX] == 'X':
				arrst[nY][nX] = True;

#--------------------------------------------------------------------


RandomInJi()

AllRealShow()

AroundFind()

while 1: 
	
	AllShow()


	nY = int(input("Y Number input"));
	nX = int(input("X Number input"));

	print();

	if nX <= 9 and nX >= 0 and nY <= 9 and nX >= 0 and arrst[nY][nX] == False :
		arrst[nY][nX] = True;
		if array[nY][nX] != 'X' :
			OpenCount += 1;
			if array[nY][nX] == 0:
				CheckAround(nY,nX)
		else :

			AllOpenJi();
			AllShow();
			print("Game Over ");
			break;
	else :
		print("�߸��Է��Ͽ����ϴ�");

	if OpenCount == 100-JiCount :
		AllRealShow();
		print("Game Success");
		break;
