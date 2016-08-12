# -*- coding: utf-8 -*-

line = input()
line = line.split()

n1 = float(line[0])
n2 = float(line[1])
n3 = float(line[2])
n4 = float(line[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
print('Media: %.1f' % media)

if(media >= 7):
    print('Aluno aprovado.')
elif(media < 7 and media >= 5):
    print('Aluno em exame.')
    n_exame = float(input())
    print('Nota do exame: %.1f' % n_exame)
    media_final = (media + n_exame) / 2
    if(media_final >= 5):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % media_final)
else:
    print('Aluno reprovado.')
