#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Passagem Aérea - Unidade 2

milhas = float(raw_input())
aliquota = float(raw_input())

preco_passagem = (milhas * aliquota) + 51.00
a_vista = preco_passagem - (preco_passagem * 0.25)
preco_seis_parcelas = preco_passagem - (preco_passagem * 0.05)
seis_parcelas = preco_seis_parcelas / 6.0
dez_parcelas = preco_passagem / 10.0

print 'Valor da passagem: R$ %.2f' % preco_passagem
print
print 'Pagamento:'
print '1. À vista. R$ %.2f' % a_vista
print '2. Em 6 parcelas. Total: R$ %.2f' % preco_seis_parcelas
print '   6 x R$ %.2f' % seis_parcelas
print '3. Em 10 parcelas. Total: R$ %.2f' % preco_passagem
print '   10 x R$ %.2f' % dez_parcelas
