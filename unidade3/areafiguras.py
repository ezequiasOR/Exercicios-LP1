# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Área Figuras - Unidade 3

import math

figura = str(raw_input())

if figura == 'triângulo':
	base = float(raw_input())
	altura = float(raw_input())
	area_tri = (base * altura) / 2
	print 'Área do triângulo: %.2f (cm2)' % area_tri
elif figura == 'círculo':
	raio = float(raw_input())
	area_circulo = math.pi * raio ** 2
	print 'Área do círculo: %.2f (cm2)' % area_circulo
elif figura == 'quadrado':
	lado = float(raw_input())
	area_qua = lado ** 2
	print 'Área do quadrado: %.2f (cm2)' % area_qua
else:
	base = float(raw_input())
	altura = float(raw_input())
	area_ret = base * altura
	print 'Área do retângulo: %.2f (cm2)' % area_ret
