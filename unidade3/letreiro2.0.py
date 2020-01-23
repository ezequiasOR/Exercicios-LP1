#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Lei Estadual - Unidade 3

palavra1 = str(raw_input())
palavra2 = str(raw_input())
palavra3 = str(raw_input())

if palavra1 < palavra2 and palavra2 < palavra3:
	print palavra1, palavra2, palavra3
elif palavra1 < palavra3 and palavra3 < palavra2:
	print palavra1, palavra3, palavra2
elif palavra2 < palavra1 and palavra1 < palavra3:
	print palavra2, palavra1, palavra3
elif palavra2 < palavra3 and palavra3 < palavra1:
	print palavra2, palavra3, palavra1
elif palavra3 < palavra1 and palavra1 < palavra2:
	print palavra3, palavra1, palavra2
elif palavra3 < palavra2 and palavra2 < palavra1:
	print palavra3, palavra2, palavra1
elif palavra1 == palavra2 and palavra2 < palavra3:
	print palavra1, palavra2, palavra3
elif palavra1 == palavra2 and palavra2 > palavra3:
	print palavra3, palavra1, palavra2
elif palavra1 == palavra3 and palavra1 < palavra2:
	print palavra1, palavra3, palavra2
elif palavra1 == palavra3 and palavra1 > palavra2:
	print palavra2, palavra1, palavra3
elif palavra2 == palavra3 and palavra2 < palavra1:
	print palavra2, palavra3, palavra1
elif palavra2 == palavra3 and palavra2 > palavra1:
	print palavra1, palavra2, palavra3

