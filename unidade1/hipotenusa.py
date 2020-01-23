# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Hipotenusa - Unidade 1

cateto1 = float(raw_input('Medida do Cateto 1? '))
cateto2 = float(raw_input('Medida do Cateto 2? '))

hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5

print 'Medida da Hipotenusa: %.2f' % hipotenusa
