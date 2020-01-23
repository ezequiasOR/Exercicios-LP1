#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Colheita - Unidade 4

quantidade = int(raw_input())
soma_total = 0
mes1 = 0
mes2 = 0
mes3 = 0
mes4 = 0
mes5 = 0
mes6 = 0
mes7 = 0
mes8 = 0
mes9 = 0
mes10 = 0
mes11 = 0
mes12 = 0

for i in range(quantidade):
	registros_das_colheitas = str(raw_input()).split(',')
	mes = int(registros_das_colheitas[0])
	colheita = int(registros_das_colheitas[1])
	soma_total += colheita
	
	if mes == 1:
		mes1 += colheita
	elif mes == 2:
		mes2 += colheita
	elif mes == 3:
		mes3 += colheita
	elif mes == 4:
		mes4 += colheita
	elif mes == 5:
		mes5 += colheita
	elif mes == 6:
		mes6 += colheita
	elif mes == 7:
		mes7 += colheita
	elif mes == 8:
		mes8 += colheita
	elif mes == 9:
		mes9 += colheita
	elif mes == 10:
		mes10 += colheita
	elif mes == 11:
		mes11 += colheita
	else:
		mes12 += colheita

media_colheitas = soma_total / float(quantidade)
meses = [mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11, mes12]
cont = 1

for i in meses:
	if i >= media_colheitas:
		print 'O mês %d teve boa colheita.' % cont
	cont += 1
