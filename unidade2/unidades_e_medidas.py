# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Unidades e Medidas - Unidade 2

metros = float(raw_input())

centimetros = metros * 100
polegadas = (36 * centimetros) / 91.44
pes = (3 * polegadas) / 36
jardas = pes / 3.0

print 'Jardas: %.3f yd' % jardas
print 'Pés: %.3f ft' % pes
print 'Polegadas: %.3f in' % polegadas
