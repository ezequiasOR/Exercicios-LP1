# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Ciclo Trig. - Unidade 3

angulo = float(raw_input())

if 1 <= angulo <= 89:
	print 'Quadrante 1'
elif 91 <= angulo <= 179:
	print 'Quadrante 2'
elif 181 <= angulo <= 269:
	print 'Quadrante 3'
elif 271 <= angulo < 359:
	print 'Quadrante 4'
elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
	print 'Sobre eixos'
elif angulo > 360:
	voltas = angulo / 360
	angulo = angulo % 360
	if 1 <= angulo < 90:
		print 'Quadrante 1'
	elif 91 <= angulo < 180:
		print 'Quadrante 2'
	elif 181 <= angulo < 270:
		print 'Quadrante 3'
	elif 271 <= angulo < 360:
		print 'Quadrante 4'
	elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
		print 'Sobre eixos'
