# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Área do Cilindro - Unidade 2

import math

print 'Cálculo da Superfície de um Cilindro'
print '---'

diametro = float(raw_input('Medida do diâmetro? '))
altura = float(raw_input('Medida da altura? '))

raio = diametro / 2
area_cilindro = 2 * math.pi * raio * (raio + altura)

print '---'
print 'Área calculada: %.2f' % area_cilindro
