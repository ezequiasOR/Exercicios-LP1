# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Encontra Menores - Unidade 6

def encontra_menores(num, lista):
	for e in lista:
		if e < num:
			return e
	return -1
