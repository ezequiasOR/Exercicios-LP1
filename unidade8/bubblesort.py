#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Bubblesort - Unidade 8

def bubblesort(dados):
	for e in dados:
		swapped = False
		for i in range(len(dados)-1):
			if dados[i] > dados[i+1]:
				dados[i], dados[i+1] = dados[i+1], dados[i]
				swapped = True
		if not swapped: break
