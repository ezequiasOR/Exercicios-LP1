#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Busca Linear - Unidade 8

def busca(seq, valor):
	for i in range(len(seq)):
		if seq[i] == valor:
			return i
	return -1
