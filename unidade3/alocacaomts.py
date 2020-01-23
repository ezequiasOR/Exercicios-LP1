# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Alocação MTs - Unidade 3

num_identificador = int(raw_input())

if 1 <= num_identificador <= 10:
	print 'LCC1-1'
elif 11 <= num_identificador <= 20:
	print 'LCC1-2'
elif 21 <= num_identificador <= 30:
	print 'LCC2-1'
elif 31 <= num_identificador <= 40:
	print 'LCC2-2'
else:
	print 'Aluno inexistente.'
