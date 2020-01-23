# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Cartesiano - Unidade 3

x = float(raw_input())
y = float(raw_input())

if x > 0 and y > 0:
	print 'Primeiro quadrante.'
elif x > 0 and y < 0:
	print 'Quarto quadrante.'
elif x < 0 and y > 0:
	print 'Segundo quadrante.'
elif x < 0 and y < 0:
	print 'Terceiro quadrante.'
elif x == 0 and y > 0:
	print 'Sobre eixo.'
elif x == 0 and y < 0:
	print 'Sobre eixo.'
elif x > 0 and y == 0:
	print 'Sobre eixo.'
elif x < 0 and y == 0:
	print 'Sobre eixo.'
else:
	print 'Centro.'
