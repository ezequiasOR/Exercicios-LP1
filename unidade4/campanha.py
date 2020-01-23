#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Campanha - Unidade 4

vitorias = 0
empates = 0
derrotas = 0
pontos_em_casa = 0
pontos_fora = 0
gols_pro = 0
gols_contra = 0


for i in range(10):
	resultado_jogos = str(raw_input()).split()    #separa o placar do local do jogo
	placar = str(resultado_jogos[0]).split('x')   #separa os gols do placar
	local_jogo = str(resultado_jogos[1])
	
	if local_jogo == '(c)':                       #local do jogo: em casa
		gols_campinense = int(placar[0])
		gols_adversario = int(placar[1])
		
		if gols_campinense > gols_adversario:     #pontos feitos em casa
			pontos_em_casa += 3
		elif gols_campinense == gols_adversario:
			pontos_em_casa += 1
	else:                                         #local do jogo: fora de casa
		gols_adversario = int(placar[0])
		gols_campinense = int(placar[1])
	
		if gols_campinense > gols_adversario:     #pontos feitos fora de casa
			pontos_fora += 3
		elif gols_campinense == gols_adversario:
			pontos_fora += 1
			
	if gols_campinense > gols_adversario:         #quantidade de vitorias
		vitorias += 1
	elif gols_campinense < gols_adversario:       #quantidade de derrotas
		derrotas += 1
	else:                                         #quantidade de empates
		empates += 1
	
	gols_pro += gols_campinense
	gols_contra += gols_adversario

pontos = (vitorias * 3) + empates
saldo = gols_pro - gols_contra

print '%dv, %de, %dd' % (vitorias, empates, derrotas)
print 'pontos: %d' % pontos
print 'saldo: %d (%d pro, %d contra)' % (saldo, gols_pro, gols_contra)
print 'pontos em casa: %d' % pontos_em_casa
print 'pontos fora: %d' % pontos_fora
