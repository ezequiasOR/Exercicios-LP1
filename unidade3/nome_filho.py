#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Nome do Filho - Unidade 3

nome_pai = str(raw_input()).strip()
nome_avo_paterno = str(raw_input()).strip()
nome_avo_materno = str(raw_input()).strip()

if nome_pai != nome_avo_paterno and nome_avo_paterno != nome_avo_materno and nome_pai != nome_avo_materno:
	print nome_pai + ' ' + nome_avo_paterno + ' ' + nome_avo_materno

elif nome_pai == nome_avo_paterno and nome_pai != nome_avo_materno:
	print nome_avo_materno

elif nome_pai == nome_avo_materno and nome_pai != nome_avo_paterno:
	print nome_avo_paterno

elif nome_avo_paterno == nome_avo_materno and nome_pai != nome_avo_paterno:
	print nome_pai

else:
	print 'Rafael'
