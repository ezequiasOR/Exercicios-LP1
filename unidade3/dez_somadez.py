# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Dez ou soma dez - Unidade 3

numero1 = int(raw_input())
numero2 = int(raw_input())

soma = numero1 + numero2

if numero1 == 10:
	print 'SIM'
elif numero2 == 10:
	print 'SIM'
elif soma == 10:
	print 'SIM'
else:
	print 'NAO'
