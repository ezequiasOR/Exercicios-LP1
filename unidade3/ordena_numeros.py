#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Ordena 3 Números - Unidade 3

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

if num1 <= num2 and num2 < num3:
	print num1, num2, num3

elif num1 <= num3 and num3 < num2:
	print num1, num3, num2

elif num2 <= num1 and num1 < num3:
	print num2, num1, num3

elif num2 <= num3 and num3 < num1:
	print num2, num3, num1

elif num3 <= num1 and num1 < num2:
	print num3, num1, num2

elif num3 <= num2 and num2 < num1:
	print num3, num2, num1

else:
	print num1, num2, num3
