# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: IPTU - Unidade 2

area_casa = float(raw_input('Área construída? '))
aliquota = float(raw_input('Alíquota? '))

iptu = area_casa * aliquota + 35.0
cota_unica = iptu - (iptu * 0.25)
desconto6 = iptu - (iptu * 0.05)
parcela6 = desconto6 / 6.0
parcela10 = iptu / 10.0

print 'IPTU: R$ %.2f' % iptu
print
print 'Pagamento:'
print '1. Quota única. R$ %.2f' % cota_unica
print '2. Em 6 parcelas. Total: R$ %.2f' % desconto6
print '   6 x R$ %.2f' % parcela6
print '3. Em 10 parcelas. Total: R$ %.2f' % iptu
print '   10 x R$ %.2f' % parcela10
