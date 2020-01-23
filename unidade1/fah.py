#coding: utf-8

# UFGC - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Fahrenheit Celsius - Unidade 1

fah = float(raw_input())
cel = (fah - 32) * 5 / 9
kel = cel + 273.15
print "Fahrenheit: %.3f F" % fah
print "Celsius: %.3f C" % cel
print "Kelvin: %.3f K" % kel
