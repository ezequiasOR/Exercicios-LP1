# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Controle de Qualidade - Unidade 3

#Peso do produto, antes e depois de descongelado, em kg
produto_congelado = float(raw_input())
produto_descongelado = float(raw_input())

peso_agua = produto_congelado - produto_descongelado      #Peso da água
porc_peso_agua = peso_agua / produto_congelado            #Porcentagem do peso da água
porc5 = produto_congelado * (5/100.0)                     #5% do peso do produto congelado
porc10 = produto_congelado * (10/100.0)                   #10% do peso do produto congelado

if porc5 <= peso_agua < porc10:                                                   #Peso da água entre 5 e 10% do peso do produto congelado
	print '%.1f%% do peso do produto é de água congelada.' % (porc_peso_agua * 100.0)
	print 'Produto em conformidade.'
elif peso_agua < porc5:                                                          #Peso da água abaixo de 5% do peso do produto congelado
	print '%.1f%% do peso do produto é de água congelada.' % (porc_peso_agua * 100.0)
	print 'Produto qualis A.'
elif peso_agua >= porc10:                                                          #Peso da água acima de 10% do peso do produto congelado
	print '%.1f%% do peso do produto é de água congelada.' % (porc_peso_agua * 100.0)
	print 'Produto não conforme.'
