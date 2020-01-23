# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixas de Cerâmica - Unidade 2

revestimento = float(raw_input('Capacidade de revestimento? '))

print
print '== Dados do vão a revestir =='
comprimento = float(raw_input('Comprimento? '))
largura = float(raw_input('Largura? '))
altura = float(raw_input('Altura? '))

area_coberta = (comprimento * altura * 2) + (largura * altura * 2) + (comprimento * largura)
num_caixas = area_coberta / revestimento
print
print '== Resultados =='
print 'Área total a revestir: %.1f m2' % area_coberta
print 'Número de caixas: %d' % num_caixas
