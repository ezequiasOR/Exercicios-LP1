# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Depois do 13 - Unidade 3

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

if numero1 == 13:
	print 0
	
elif numero2 == 13:
	print numero1
	
elif numero3 == 13:
	soma = numero1 + numero2
	
	if soma == 13:
		print 0
	else:
		print soma
else:
	soma = numero1 + numero2 + numero3
	
	if soma == 13:
		print 0
	else:
		print soma
