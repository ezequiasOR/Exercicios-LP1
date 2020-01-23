#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Peso e IMC - Unidade 1

altura_parede = float(raw_input())
largura_parede = float(raw_input())

area_parede = altura_parede * largura_parede
custo_servico = 20.0 * area_parede

print 'R$ %.2f' %  custo_servico
