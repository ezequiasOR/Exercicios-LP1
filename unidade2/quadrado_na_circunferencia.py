# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Quadrado inscrito na circunferência - Unidade 2

import math

lado_do_quadrado = float(raw_input())

raio = lado_do_quadrado / math.sqrt(2)
perimetro_circunferencia = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print 'Perímetro: %.5f' % perimetro_circunferencia
print 'Área: %.5f' % area
