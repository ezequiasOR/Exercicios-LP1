#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Bubble - Unidade 8

def bubble(seq):
	trocas = 0
	for i in range(len(seq)-1):
		if seq[i] > seq[i+1]:
			seq[i], seq[i+1] = seq[i+1], seq[i]
			trocas += 1
	return trocas
