# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Pedágio (qualitativa) - Unidade 3

tipo_do_veiculo = str(raw_input())

if tipo_do_veiculo == 'Automóvel utilitário':
	preco_do_pedagio  = 11.40
	print 'Valor a pagar: R$ %.2f.' % preco_do_pedagio
	
elif tipo_do_veiculo == 'Ônibus':
	quantidade_de_eixos = int(raw_input())
	preco_do_pedagio = quantidade_de_eixos * 11.40
	print 'Valor a pagar: R$ %.2f.' % preco_do_pedagio
	
elif tipo_do_veiculo == 'Caminhão':
	quantidade_de_eixos = int(raw_input())
	preco_do_pedagio = quantidade_de_eixos * 9.60
	print 'Valor a pagar: R$ %.2f.' % preco_do_pedagio
	
elif tipo_do_veiculo == 'Motocicleta':
	preco_do_pedagio = 5.70
	print 'Valor a pagar: R$ %.2f.' % preco_do_pedagio
	
else:
	print 'Veículo não cadastrado.'
