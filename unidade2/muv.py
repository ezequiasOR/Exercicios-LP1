# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Movimento Uniformemente Variado - Unidade 2

pos_inicial = float(raw_input('Posição inicial? '))
vel_inicial = float(raw_input('Velocidade inicial? '))
tempo = float(raw_input('Tempo? '))
aceleracao = float(raw_input('Aceleração? '))

vel_final = vel_inicial + aceleracao * tempo
pos_final = pos_inicial + vel_inicial* tempo + ((aceleracao * (tempo ** 2)) / 2.0)
vel_media = (vel_final + vel_inicial) / 2.0

print
print 'Dados da questão'
print '================'
print '   Posição inicial: %.2f m' % pos_inicial
print 'Velocidade inicial: %.2f m/s' % vel_inicial
print '        Aceleração: %.2f m/s2' % aceleracao
print '             Tempo: %.2f s' % tempo
print '  Velocidade final: %.2f m/s' % vel_final
print '  Velocidade média: %.2f m/s' % vel_media
print '     Posição final: %.2f m' % pos_final
