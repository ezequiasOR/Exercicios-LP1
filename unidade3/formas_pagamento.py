#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Formas de Pagamento - Unidade 3

area = float(raw_input())
valor_m2 = float(raw_input())
opcao_pagamento = str(raw_input())

valor_imposto = area * valor_m2

if opcao_pagamento == 'vista':
	total_pagar = valor_imposto - (valor_imposto * 0.2)
	print 'Total: R$ %.2f' % total_pagar
elif opcao_pagamento == '2x':
	total_pagar = valor_imposto - (valor_imposto * 0.1)
	parcelas = total_pagar / 2.0
	print 'Total: R$ %.2f. Parcelas: R$ %.2f' % (total_pagar, parcelas)
else:
	total_pagar = valor_imposto - (valor_imposto * 0.05)
	parcelas = total_pagar / 3.0
	print 'Total: R$ %.2f. Parcelas: R$ %.2f' % (total_pagar, parcelas)
