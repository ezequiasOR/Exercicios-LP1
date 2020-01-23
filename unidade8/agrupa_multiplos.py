#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Agrupa Múltiplos - Unidade 8

def agrupa_multiplos(seq, k):
	for e in seq:
		for i in range(len(seq)-1):
			if seq[i] % k == 0:
				seq[i], seq[i+1] = seq[i+1], seq[i]

	for ele in seq:
		for j in range(len(seq)-1, -1, -1):
			if seq[j] % k == 0:
				if j-1 != -1:
					seq[j], seq[j-1] = seq[j-1], seq[j]
