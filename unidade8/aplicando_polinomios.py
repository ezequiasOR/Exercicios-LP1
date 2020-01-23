#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Aplicação Polinômios - Unidade 8

while True:
	calculo = 0
	exp = 0
	entrada = str(raw_input()).split()              #Pode ser os polinômios, o valor de x ou a condição de parada
	if entrada[0] == 'fim': break
	elif entrada[0] == 'p:':
		polinomios = entrada
		print 'novo polinomio'
	else:
		for i in range(1, len(polinomios)):
			calculo += int(polinomios[i])*int(entrada[0])**exp
			exp += 1
		print calculo
