# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Sensor de Ruídos - Unidade 3

ruido = str(raw_input())
hora = int(raw_input())

if ruido != '' and hora <= 6 or hora >= 22:
	print 'Perturbação Detectada!'
else:
	print 'Condomínio em Paz.'
