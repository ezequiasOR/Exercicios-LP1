#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Assembleia - Unidade 4

quant_professores = int(raw_input())

quant_sim = 0
quant_nao = 0
quant_abstencao = 0

for i in range(quant_professores):
	votos = str(raw_input())
	if votos == 'sim':
		quant_sim += 1
	elif votos == 'não':
		quant_nao += 1
	else:
		quant_abstencao += 1

if (quant_sim + quant_nao) <= (quant_professores / 2):
	print 'Quorum insuficiente.'
else:
	if quant_sim > (quant_nao + quant_abstencao):
		print 'Decisão a favor da greve.'
	elif quant_nao > (quant_sim + quant_abstencao):
		print 'Decisão contrária à greve.'
	else:
		print 'Empate.'
