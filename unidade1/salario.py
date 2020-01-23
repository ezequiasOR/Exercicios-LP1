#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Salário - Unidade 1

salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())

hora_bruta = salario_bruto / horas_de_trabalho
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
soma_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - soma_descontos
hora_liquida = salario_liquido / horas_de_trabalho

print 'Salário Bruto = %s\nHora Bruta = %s\nDesconto IR = %s\nDesconto INSS = %s\nDesconto Sindicato = %s\nSalário Líquido = %s\nHora Líquida = %s' % (salario_bruto, hora_bruta, desconto_ir, desconto_inss, desconto_sindicato, salario_liquido, hora_liquida)
