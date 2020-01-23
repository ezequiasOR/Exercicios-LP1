#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Bolsa do CNPq - Unidade 4

saldo = 500
maior_saldo = 0
cont = 0
posicao = 0

for i in range(12):
	gastos_mensais = int(raw_input())
	saldo -= gastos_mensais
	if saldo >= maior_saldo:
		maior_saldo = saldo
		posicao = cont
	saldo += 500
	cont += 1

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

cont2 = 0

for c in meses:
	if cont2 == posicao:
		print c
	cont2 += 1
	
