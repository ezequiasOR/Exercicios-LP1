#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Fli Flai - Unidade 3

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

if numero1 % 10 ==0 or numero2 % 10 == 00 or numero3 % 10 ==0:
	print 'Tumba'
else:
	if numero1 % 2 == 0:
		print 'Fli'
	if numero2 % 3 == 0:
		print 'Flai'
	if numero3 % 5 == 0:
		print 'Flu'
