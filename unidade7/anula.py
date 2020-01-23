#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Anula - Unidade 7

def anula(lista):
	for j in range(len(lista)):
		for i in range(len(lista)-1,-1,-1):
			if lista[i] + lista[i-1] == 0:
				lista.pop(i)
				lista.pop(i-1)
				break
