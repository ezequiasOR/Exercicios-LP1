#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: B2 para B10 - Unidade 4

binario = str(raw_input())

tamanho = len(binario) - 1
soma = 0

for i in binario:
	resultado =  int(i) * 2 ** tamanho
	print '%d * %d = %d' % (int(i), (2 ** tamanho), resultado)
	tamanho -= 1
	soma += resultado

print '%s(2) = %d(10)' % (binario, soma)
