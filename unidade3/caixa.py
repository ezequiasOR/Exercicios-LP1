# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixas em Banco - Unidade 3

from math import pi

cpf = int(raw_input())

caixas = 1 + (25 * (cpf * pi % 1))

if 1 <= caixas <= 8:
	print 'Caixa %d, térreo' % (caixas)
elif 9 <= caixas <= 20:
	print 'Caixa %d, primeiro andar' % (caixas)
else:
	print 'Caixa %d, segundo andar' % (caixas)

