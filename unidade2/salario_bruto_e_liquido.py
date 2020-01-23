# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Salário Bruto e Líquido - Unidade 2

nome = str(raw_input())
quant_horas_extras = float(raw_input())
salario_minimo = float(raw_input())
valor_hora_extra = float(raw_input())

salario_hora_extra = quant_horas_extras * valor_hora_extra
salario_bruto = 4 * salario_minimo + salario_hora_extra
desconto_inss = salario_bruto * 0.12
desconto_ir = salario_bruto * 0.2
salario_liquido = salario_bruto - (desconto_inss + desconto_ir)

print 'O Salário Bruto de %s é de R$ %.2f' % (nome, salario_bruto)
print 'O Salário Líquido de %s é de R$ %.2f' % (nome, salario_liquido)
