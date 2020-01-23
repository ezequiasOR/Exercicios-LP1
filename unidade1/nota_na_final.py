# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Nota na Final - Unidade 1

print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))

media_parcial = (peso1*nota1 + peso2*nota2 + peso3*nota3)
media5 = (media_parcial * 0.6 - 5.0) / -0.4
media7 = (media_parcial * 0.6 - 7.0) / -0.4

print '== Resultados =='
print 'Média parcial: %.1f' % media_parcial
print 'Nota na final, pra média 5.0 = %.1f' % media5
print 'Nota na final, pra média 7.0 = %.1f' % media7
