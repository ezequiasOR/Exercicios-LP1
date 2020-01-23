# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Quadrado na Circunferência - Unidade 2

import math

raio = float(raw_input())

lado_do_quadrado = raio * math.sqrt(2)
area_quadrado = lado_do_quadrado ** 2
area_circulo = math.pi * (raio ** 2)
area_nao_comum = area_circulo - area_quadrado

print 'Área não comum: %.5f' % area_nao_comum
