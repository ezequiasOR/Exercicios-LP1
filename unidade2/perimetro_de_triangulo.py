# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Perímetro de Triângulo - Unidade 2

import math

x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())

distancia1 = math.sqrt(((x2 - x1) ** 2.0) + ((y2 - y1) ** 2))
distancia2 = math.sqrt(((x3 - x1) ** 2.0) + ((y3 - y1) ** 2))
distancia3 = math.sqrt(((x3 - x2) ** 2.0) + ((y3 - y2) ** 2))

perimetro = distancia1 + distancia2 + distancia3

print 'O perímetro é de %.2f' % perimetro
