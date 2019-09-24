possible_notes = [2, 5, 10, 20, 50, 100]
possible_choices = []
for note in possible_notes:
    for join_note in possible_notes:
        possible_choices.append(note + join_note)

line = input()
while line != '0 0':
    value, payed = line.split()
    change = int(payed) - int(value)
    if change in possible_choices:
        print('possible')
    else:
        print('impossible')
    line = input()
