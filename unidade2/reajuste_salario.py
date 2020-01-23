# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Reajuste do Salário Mínimo - Unidade 2

salario_minimo = float(raw_input('Valor atual? '))
novo_salario = float(raw_input('Novo valor? '))

diferenca = novo_salario - salario_minimo
reajuste = (diferenca * 100) / salario_minimo

print 'Reajuste de %.1f%%' % reajuste
