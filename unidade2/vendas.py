# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Vendas - Unidade 2

brinquedos_vendidos = int(raw_input())
teresa = int(raw_input())
carla = int(raw_input())

joaquim = brinquedos_vendidos - (teresa + carla)
porc_teresa = (teresa * 100.0) / brinquedos_vendidos
porc_joaquim = (joaquim * 100.0) / brinquedos_vendidos
porc_carla = (carla * 100.0) / brinquedos_vendidos

print 'Teresa vendeu %d (de %d) brinquedos. (%.2f%%)' % (teresa, brinquedos_vendidos, porc_teresa)
print 'Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)' % (joaquim, brinquedos_vendidos, porc_joaquim)
print 'Carla vendeu %d (de %d) brinquedos. (%.2f%%)' % (carla, brinquedos_vendidos, porc_carla)
