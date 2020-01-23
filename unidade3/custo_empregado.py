# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Custo Empregado - Unidade 3

salario_base = float(raw_input())
dias_trabalhados = int(raw_input())
transporte_diario = float(raw_input())

transporte_mensal = transporte_diario * dias_trabalhados   #Gasto mensal com transporte
porc6 = salario_base * (6/100.0)                           #6% do sálario bruto
fgts = salario_base * (8/100.0)                            #FGTS que o empregador paga
inss = salario_base * (12/100.0)                           #INSS que o empregador paga

if transporte_mensal > porc6:
	transporte_empregador = transporte_mensal - porc6
	transporte_empregado = transporte_mensal - transporte_empregador
else:
	transporte_empregador = 0
	transporte_empregado = 0

if salario_base <= 1317.07:
	inss_empregado = salario_base * (8/100.0)                       #Alíquota de 8%
elif 1317.08 <= salario_base <= 2195.12:
	inss_empregado = salario_base * (9/100.0)                       #Alíquota de 9%
else:
	inss_empregado = salario_base * (11/100.0)                      #Alíquota de 11%
	
print 'O salário base é R$ %.2f' % salario_base
print 'O custo mensal para o empregador é de R$ %.2f' % (salario_base + transporte_empregador + fgts + inss)
print 'O salário líquido que o trabalhador irá receber no mês é R$ %.2f' % (salario_base - transporte_empregado - inss_empregado)
