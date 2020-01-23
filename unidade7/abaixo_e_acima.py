# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Abaixo e Acima - Unidade 7

def calcula_media(lista):
	media = 0.0

	for e in lista:
		media += e

	media /= len(lista)

	return media

def organiza_por_media(lista):
	for e in lista:
		for i in range(len(lista)-1):
			if lista[i] > calcula_media(lista):
				lista[i], lista[i+1] = lista[i+1], lista[i]
	return lista
