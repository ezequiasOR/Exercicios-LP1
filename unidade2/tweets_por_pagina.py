# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Tweets por Página - Unidade 2

tweets = int(raw_input())

tweets_por_pagina = tweets / 400
perdidos = ((tweets % 400.0) * 100) / tweets

print 'Serão necessárias %d página(s) para visualizar os tweets.' % tweets_por_pagina
print '%.1f%% dos tweets serão perdidos.' % perdidos
