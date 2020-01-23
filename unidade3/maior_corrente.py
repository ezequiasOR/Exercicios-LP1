#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Maior Corrente - Unidade 3

tensao1 = float(raw_input())
resistencia1 = float(raw_input())
tensao2 = float(raw_input())
resistencia2 = float(raw_input())
tensao3 = float(raw_input())
resistencia3 = float(raw_input())

corrente1 = tensao1 / resistencia1
corrente2 = tensao2 / resistencia2
corrente3 = tensao3 / resistencia3

if corrente1 > corrente2 and corrente1 > corrente3:
	if corrente1 < 0.001:
		corrente1 = corrente1 * 1000000
		print 'condutor com maior corrente: 1'
		print 'maior corrente: %.2f µA' % corrente1
	elif 0.001 < corrente1 < 1:
		corrente1 = corrente1 * 1000
		print 'condutor com maior corrente: 1'
		print 'maior corrente: %.2f mA' % corrente1
	else:
		print 'condutor com maior corrente: 1'
		print 'maior corrente: %.2f A' % corrente1
	
elif corrente2 > corrente1 and corrente2 > corrente3:
	if corrente2 < 0.001:
		corrente2 = corrente2 * 1000000
		print 'condutor com maior corrente: 2'
		print 'maior corrente: %.2f µA' % corrente2
	elif 0.001 < corrente2 < 1:
		corrente2 = corrente2 * 1000
		print 'condutor com maior corrente: 2'
		print 'maior corrente: %.2f mA' % corrente2
	else:
		print 'condutor com maior corrente: 2'
		print 'maior corrente: %.2f A' % corrente2
	
elif corrente3 > corrente1 and corrente3 > corrente2:
	if corrente3 < 0.001:
		corrente3 = corrente3 * 1000000
		print 'condutor com maior corrente: 3'
		print 'maior corrente: %.2f µA' % corrente3
	elif 0.001 < corrente3 < 1:
		corrente3 = corrente3 * 1000
		print 'condutor com maior corrente: 3'
		print 'maior corrente: %.2f mA' % corrente3
	else:
		print 'condutor com maior corrente: 3'
		print 'maior corrente: %.2f A' % corrente3
