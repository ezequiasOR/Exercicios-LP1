#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Limpeza - Unidade 3

servico = int(raw_input())

if servico == 1:
	tamanho = int(raw_input())
	preco_do_servico = tamanho * 80
	print 'R$ %d,00' % preco_do_servico
	if preco_do_servico >= 200:
		print 'Brinde!'

elif servico == 2:
	tamanho = int(raw_input())
	preco_do_servico = tamanho * 50
	print 'R$ %d,00' % preco_do_servico
	if preco_do_servico >= 200:
		print 'Brinde!'
	
else:
	print 'R$ 50,00'
