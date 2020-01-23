#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Acima de - Unidade 8

def acima_de(n, l):
	L = []
	for i in range(len(l)):
		if l[i] > n:
			L.append(i)
	return L
