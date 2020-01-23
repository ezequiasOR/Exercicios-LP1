# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Roleta 360 - Unidade 3

numero = int(raw_input())

if numero == 0 or numero == 90 or numero == 180 or numero == 270 or numero == 360:
	print 'Sobre eixos'
elif 0 < numero < 90:
	print 'Quadrante 1'
elif 90 < numero < 180:
	print 'Quadrante 2'
elif 180 < numero < 270:
	print 'Quadrante 3'
elif 270 < numero < 360:
	print 'Quadrante 4'
else:
	resto = numero % 360
	if resto == 0 or resto == 90 or resto == 180 or resto == 270 or resto == 360:
		print 'Sobre eixos'
	elif 0 < resto < 90:
		print 'Quadrante 1'
	elif 90 < resto < 180:
		print 'Quadrante 2'
	elif 180 < resto < 270:
		print 'Quadrante 3'
	elif 270 < resto < 360:
		print 'Quadrante 4'
