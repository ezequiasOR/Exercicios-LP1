# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: CSF - Unidade 3

nota_enem = float(raw_input())
creditos = float(raw_input())

porc20 = 416 * 0.2
porc90 = 416 * 0.9

if nota_enem >= 600 and porc20 < creditos < porc90:
	print 'Todas as condições satisfeitas.'
elif nota_enem < 600 and porc20 < creditos < porc90:
	print 'Condição ENEM não satisfeita.'
elif nota_enem >= 600 and creditos > porc20:
	print 'Condição CRÉDITOS não satisfeita.'
elif nota_enem >= 600 and creditos < porc90:
	print 'Condição CRÉDITOS não satisfeita.'
else:
	print 'Nenhuma condição satisfeita.'
