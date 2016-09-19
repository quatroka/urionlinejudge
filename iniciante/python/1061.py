# -*- coding: utf-8 -*-

ini_data = input().split()
ini_horario = input().split(' : ')
fim_data = input().split()
fim_horario = input().split(' : ')

ini_dia = int(ini_data[1])
fim_dia = int(fim_data[1])
ini_hora = int(ini_horario[0])
fim_hora = int(fim_horario[0])
ini_min = int(ini_horario[1])
fim_min = int(fim_horario[1])
ini_seg = int(ini_horario[2])
fim_seg = int(fim_horario[2])

dias = fim_dia - ini_dia
horas = fim_hora - ini_hora
minutos = fim_min - ini_min
segundos = fim_seg - ini_seg

if(segundos < 0):
    segundos += 60
    minutos -= 1

if(minutos < 0):
    minutos += 60
    horas -= 1

if(horas < 0):
    horas += 24
    dias -= 1

print('%s dia(s)' % dias)
print('%s hora(s)' % horas)
print('%s minuto(s)' % minutos)
print('%s segundo(s)' % segundos)
