# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calcula Preço de Venda - Unidade 2

entrada = float(raw_input())
despesas = float(raw_input()) /100*entrada
lucro = float(raw_input()) /100*entrada
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

soma = entrada + despesas + lucro
venda = 100 * soma / (100 - impostos - comissoes - descontos - encargos)
resto = venda % 1

print 'Preço de venda é R$ %.2f (R$ %d.00 + R$ %.2f)' % (venda, int(venda), resto)
