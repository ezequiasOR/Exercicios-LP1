# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Perda de Tempo no Trânsito - Unidade 2

tempo1 = int(raw_input())
tempo2 = int(raw_input())
tempo3 = int(raw_input())
tempo4 = int(raw_input())
tempo5 = int(raw_input())

soma = tempo1 + tempo2 + tempo3 + tempo4 + tempo5
media = (tempo1 + tempo2 + tempo3 + tempo4 + tempo5) / 5.0
porcentagem_semana_produtiva = (soma * 100) / (5 * 1440.0)
ep_house = soma / 50

print 'Você perdeu %d min na semana (média de %.1f min por dia).' % (soma, media)
print 'Isso significa %.2f%% da sua semana produtiva.' % porcentagem_semana_produtiva
print 'Daria para assistir %d episódio(s) de House.' % ep_house
