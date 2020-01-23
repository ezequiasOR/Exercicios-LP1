# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: É dobro - Unidade 3

numero1 = int(raw_input())
numero2 = int(raw_input())

dobro_numero1 = numero1 * 2
dobro_numero2 = numero2 * 2

if numero1 == dobro_numero2:
	print 'SIM'
elif numero2 == dobro_numero1:
	print 'SIM'
else:
	print 'NAO'
