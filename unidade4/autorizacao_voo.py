#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Autorização voos - Unidade 4

tempo_disponivel = int(raw_input())
quant_avioes = int(raw_input())

cont = 0

for i in range(quant_avioes):
	tempo_aviao = int(raw_input())
	if tempo_aviao <= tempo_disponivel:
		cont += 1
		tempo_disponivel -= tempo_aviao
	else:
		cont = cont
		tempo_disponivel = tempo_disponivel

print '%d voo(s) autorizados.' % cont
