# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha 
#Questão: Área e Perímetro - Unidade 2

import math

diametro = int(raw_input())

raio = diametro / 2.0
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print 'A: %.5f' % area
print 'P: %.5f' % perimetro
