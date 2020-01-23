#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Gratificação Natalina - Unidade 3

codigo_cargo = int(raw_input())

if codigo_cargo == 1:
	print 'Deverá receber em dezembro R$ 25000.00.'
	
elif codigo_cargo == 2:
	print 'Deverá receber em dezembro R$ 15000.00.'
	
elif codigo_cargo == 3:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 500.00.'
		print 'Deverá receber em dezembro R$ 8500.00.'
	else:
		gratificacao = (235 - faltas) * 2.0
		valor_total = 8000 + gratificacao
		print 'Valor da gratificação R$ %.2f.' % gratificacao
		print 'Deverá receber em dezembro R$ %.2f.' % valor_total
		
elif codigo_cargo == 4:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 300.00.'
		print 'Deverá receber em dezembro R$ 5300.00.'
	else:
		gratificacao = (235 - faltas) * 1.0
		valor_total = 5000 + gratificacao
		print 'Valor da gratificação R$ %.2f.' % gratificacao
		print 'Deverá receber em dezembro R$ %.2f.' % valor_total
		
else:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 200.00.'
		print 'Deverá receber em dezembro R$ 3000.00.'
	else:
		gratificacao = (235 - faltas) * 0.7
		valor_total = 2800 + gratificacao
		print 'Valor da gratificação R$ %.2f.' % gratificacao
		print 'Deverá receber em dezembro R$ %.2f.' % valor_total
