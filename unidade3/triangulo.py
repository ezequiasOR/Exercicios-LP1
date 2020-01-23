# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: É triangulo - Unidade 3

a = int(raw_input())   #Lado a do triângulo
b = int(raw_input())   #Lado b do triângulo
c = int(raw_input())   #Lado c do triângulo

condicao1 = ((b - c) < a < (b + c))
condicao2 = ((a - c) < b < (a + c))
condicao3 = ((a - b) < c < (a + b))

if condicao1 and condicao2 and condicao3:
	perimetro = a + b + c
	print 'triangulo valido. %d' % perimetro
else:
	print 'triangulo invalido.'
