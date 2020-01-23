#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Coluna - Unidade 9

def coluna(matriz, i):
	valores = []
	for coluna in range(len(matriz)):
		valores.append(matriz[coluna][i])
		
	return valores
