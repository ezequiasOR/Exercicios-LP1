#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Perímetro de Retângulo - Unidade 1

base = int(raw_input())
altura = int(raw_input())

perimetro = 2*(base + altura)         #Em milimetros
perimetro_em_cm = perimetro / 10.0    #Em centímetros

print 'O perímetro resultante (em cm) é %.2f.' % perimetro_em_cm
