# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Imprime Nota Fiscal - Unidade 1

valor_total = float(raw_input())
data = str(raw_input())
quantidade_de_produtos = int(raw_input())

media = valor_total / quantidade_de_produtos

print 'Data: %s' % data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f.' % (valor_total, media)
