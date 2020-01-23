#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calcula Áreas com Funções - Unidade 8

from math import pi

def area_do_quadrado(lado):
	area = lado ** 2
	return area
	
def area_do_circulo(raio):
	area = pi * raio ** 2
	return area

def area_do_triangulo(base, altura):
	area = (base * altura)/2
	return area

while True:
	entrada = str(raw_input()).split()
	if entrada[0] == 'fim': break
	
	if entrada[0] == 'Q':
		print 'A área do quadrado é %.2f' % area_do_quadrado(float(entrada[1]))
	elif entrada[0] == 'C':
		print 'A área do círculo é %.2f' % area_do_circulo(float(entrada[1]))
	elif entrada[0] == 'T':
		print 'A área do triangulo é %.2f' % area_do_triangulo(float(entrada[1]), float(entrada[2]))
