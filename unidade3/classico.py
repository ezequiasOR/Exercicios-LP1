# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Clássico - Unidade 3

gols_campinense = int(raw_input())
gols_treze = int(raw_input())

if gols_campinense > gols_treze:
	print 'Campinense'
elif gols_treze > gols_campinense:
	print 'Treze'
else:
	print 'Empate'
