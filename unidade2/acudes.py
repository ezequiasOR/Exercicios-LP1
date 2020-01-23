# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Açudes - Unidade 2

capacidade_total = float(raw_input('capacidade? '))   #Em metros cubicos
volume_atual = float(raw_input('percentual hoje? '))  #Percentual
consumo_diario = float(raw_input('gasto diário? '))   #Em metros cubicos

volume = capacidade_total * volume_atual / 100
dias_restantes = volume / consumo_diario

print 'volume: %.2f' % volume
print 'dias restantes: %d' % dias_restantes
