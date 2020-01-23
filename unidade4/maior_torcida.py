#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Maior Torcida - Unidade 4

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())
num4 = int(raw_input())
num5 = int(raw_input())
num6 = int(raw_input())
num7 = int(raw_input())
num8 = int(raw_input())
num9 = int(raw_input())
num10 = int(raw_input())

time1 = [num1, num2, num3, num4, num5]
time2 = [num5, num7, num8, num9, num10]

torcedores1 = 0
for i in time1:
	torcedores1 += i

torcedores2 = 0
for i in time2:
	torcedores2 += i
	
if torcedores1 > torcedores2:
	print 'O primeiro time leva mais torcedores ao estádio.'
elif torcedores1 < torcedores2:
	print 'O segundo time leva mais torcedores ao estádio.'
else:
	print 'Empate.'
