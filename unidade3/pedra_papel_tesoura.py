# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Pedra, Papel, Tesoura - Unidade 3

jogador1 = str(raw_input('j1? '))
jogador2 = str(raw_input('j2? '))

if jogador1 == 'pedra' and jogador2 == 'papel':
	print 'j2 vence: papel ganha de pedra'
elif jogador1 == 'pedra' and jogador2 == 'tesoura':
	print 'j1 vence: pedra ganha de tesoura'
elif jogador1 == 'pedra' and jogador2 == 'pedra':
	print 'empate: pedra empata com pedra'

elif jogador1 == 'papel' and jogador2 == 'pedra':
	print 'j1 vence: papel ganha de pedra'
elif jogador1 == 'papel' and jogador2 == 'tesoura':
	print 'j2 vence: tesoura ganha de papel'
elif jogador1 == 'papel' and jogador2 == 'papel':
	print 'empate: papel empata com papel'

elif jogador1 == 'tesoura' and jogador2 == 'pedra':
	print 'j2 vence: pedra ganha de tesoura'
elif jogador1 == 'tesoura' and jogador2 == 'papel':
	print 'j1 vence: tesoura ganha de papel'
elif jogador1 == 'tesoura' and jogador2 == 'tesoura':
	print 'empate: tesoura empata com tesoura'
