# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Dia Normal - Unidade 3

dia_da_semana = str(raw_input())
numero_de_clientes = int(raw_input())

if dia_da_semana == 'segunda' or dia_da_semana == 'terça' or dia_da_semana == 'quarta' or dia_da_semana == 'quinta' or dia_da_semana == 'sexta':
	if 40 <= numero_de_clientes <= 60:
		print 'normal'
	else:
		print 'atípico' 
elif dia_da_semana == 'sábado' or dia_da_semana == 'domingo':
	if numero_de_clientes >= 40:
		print 'normal'
	else:
		print 'atípico'
