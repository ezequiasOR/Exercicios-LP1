# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Ajeita Lista - Unidade 7

def ajeita_lista(lista):
	for e in lista:
		for i in range(len(lista)-1):
			if lista[i] % 2 != 0:
				lista[i], lista[i+1] = lista[i+1], lista[i]

	for e in lista:
		for i in range(len(lista)-1):
			if lista[i+1] % 2 == 0:
				if lista[i] < lista[i+1]:
					lista[i], lista[i+1] = lista[i+1], lista[i]
			elif lista[i] % 2 != 0:
				if lista[i] > lista[i+1]:
					lista[i], lista[i+1] = lista[i+1], lista[i]
