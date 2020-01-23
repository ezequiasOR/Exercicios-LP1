# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: MRU - Unidade 1

s_inicial = float(raw_input())  #Em metros
velocidade = float(raw_input()) #Em metros por segundo
tempo = float(raw_input())      #Em segundos

s_final = s_inicial + velocidade * tempo

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (tempo, s_final)
