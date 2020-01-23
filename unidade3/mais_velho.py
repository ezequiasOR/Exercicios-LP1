#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Mais velho - Unidade 3

nome1 = str(raw_input())
dia1 = int(raw_input())
mes1 = int(raw_input())
ano1 = int(raw_input())

nome2 = str(raw_input())
dia2 = int(raw_input())
mes2 = int(raw_input())
ano2 = int(raw_input())

if ano1 < ano2:
	print nome1
elif ano1 > ano2:
	print nome2
else:
	if mes1 > mes2:
		print nome2
	elif mes1 < mes2:
		print nome1
	else:
		if dia1 < dia2:
			print nome1
		elif dia1 > dia2:
			print nome2
		else:
			print 'nenhuma'
