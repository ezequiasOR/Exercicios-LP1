# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Conta Alertas - Unidade 6

def conta_alertas_acude(medicoes):
	conta = 0
	for i in range(1, len(medicoes)):
		if medicoes[i] < 17:
			if 10 > abs(medicoes[i-1] - medicoes[i]):
				conta += 1
	return conta
