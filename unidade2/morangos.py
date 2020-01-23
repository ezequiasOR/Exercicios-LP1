# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixas com Morangos - Unidade 2

morangos = int(raw_input())

caixas = morangos / 400.0
resto = morangos % 400.0
porc_resto = (100 * resto) / morangos  #porcentagem dos morangos perdidos

print 'Serão necessárias %d caixa(s) para embalar os morangos.' % caixas
print '%.1f%% dos morangos serão perdidos.' % porc_resto
