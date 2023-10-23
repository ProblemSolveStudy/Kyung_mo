name = 'JAZ'
cursor_move = len(name) - 1
spell_move = 0
answer = 0
for i, spell in enumerate(name):
    spell_move += min(ord(spell) - ord("A"), ord("Z") - ord(spell) + 1)
    
    next = i + 1
    while next<len(name) and name[next] == 'A':
        next += 1
    
    cursor_move = min([cursor_move, 2*i + len(name) - next, i+2 * (len(name) - next)])

answer = spell_move + cursor_move
print(answer)