#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Números Iguais - Unidade 3

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

if num1 == num2 and num2 == num3:
	print 3

elif num1 == num2 or num2 == num3 or num1 == num3:
	print 2

else:
	print 0
