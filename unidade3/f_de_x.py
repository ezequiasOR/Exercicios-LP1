# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: f(x) - Unidade 3

x = int(raw_input())

if abs(x) <= 1:
	print 1
elif 1 < abs(x) <= 2:
	print 2
elif 2 < abs(x) <= 3:
	print x ** 2
elif abs(x) > 3:
	print x ** 3
