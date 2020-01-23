# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Ano Bissexto - Unidade 3

ano = int(raw_input())

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
	print '%d é bissexto' % ano
else:
	print '%d não é bissexto' % ano
