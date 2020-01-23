# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Divisor - Unidade 6

def divisor(num, lista):
	for i in range(len(lista)):
		if lista[i] % num == 0:
			return i

	return -1
