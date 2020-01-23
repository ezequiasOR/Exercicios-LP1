# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Altera Consecutivos - Unidade 6

def inverte2a2(seq):
	if len(seq) % 2 == 0:
		for i in range(0, len(seq)-1, 2):
			seq[i], seq[i+1] = seq[i+1], seq[i]
	
	else:
		for i in range(0, len(seq)-2, 2):
			seq[i], seq[i+1] = seq[i+1], seq[i]
	
	return seq
