#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Plif Plof - Unidade 3

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

soma = num1 + num2 + num3

if soma % 3 == 0 and soma % 5 == 0:
	print 'plifplof'
elif soma % 3 == 0:
	print 'plif'
elif soma % 5 == 0:
	print 'plof'
else:
	print soma
