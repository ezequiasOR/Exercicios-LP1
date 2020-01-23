# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Custo INSS - Unidade 3

salario = float(raw_input())

inss_empregador = salario * (12/100.0)

if salario <= 1317.07:
	inss_empregado = salario * (8/100.0)
elif 1317.08 <= salario <= 2195.12:
	inss_empregado = salario * (9/100.0)
else:
	inss_empregado = salario * (11/100.0)

print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador
print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado
