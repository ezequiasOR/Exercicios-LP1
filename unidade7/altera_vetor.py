# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Altera Vetor - Unidade 7

def altera_vetor_por_escalar(vetor, escalar):
	for i in range(len(vetor)):
		vetor[i] *= escalar
