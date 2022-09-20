import os
import sys
## declaration of participants
part = ['X', 'O']

## Getting and cecking positional input
def get_postion(t, gf={}):
    correct = 0
    try:
        while correct !=1:
            inc_field = input("enter field for " + t + ":")
            if len(inc_field) != 2 or inc_field.isdecimal() == False:
                print("only 2 digits are valid")
            elif inc_field not in ['11', '12', '13', '21', '22', '23', '31', '32', '33']:
                print("field is outside game range")
            elif gf[inc_field] != '-':
                print("field is already taken")
            else:
                correct = 1
        return inc_field
    except KeyboardInterrupt:
        sys.exit(0)

## Game itself
def game():
    win = 0
    p = 0
## Initial values for gaming field
    v11 = v12 = v13 = v21 = v22 = v23 = v31 = v32 = v33 = '-'
## Declaration of game field
    gf = {'00': '\\', '01': '1', '02': '2', '03': '3', '10': '1', '11': v11, '12': v12, '13': v13, '20': '2', '21': v21, '22': v22, '23': v23, '30': '3', '31': v31, '32': v32, '33': v33}
    while win == 0:
        turn = part[p]
        os.system('cls')
        print(gf['00'] + " " + gf['01'], gf['02'], gf['03'])
        print(gf['10'] + " " + gf['11'], gf['12'], gf['13'])
        print(gf['20'] + " " + gf['21'], gf['22'], gf['23'])
        print(gf['30'] + " " + gf['31'], gf['32'], gf['33'])
        inc_field = get_postion(turn, gf)
        gf[inc_field] = turn
## declaration of victory or draw conditions
        victory_lines = [[gf['11'], gf['12'], gf['13']], [gf['21'], gf['22'], gf['23']], [gf['31'], gf['32'], gf['33']], [gf['11'], gf['21'], gf['31']], [gf['12'], gf['22'], gf['32']], [gf['13'], gf['23'], gf['33']], [gf['11'], gf['22'], gf['33']], [gf['31'], gf['22'], gf['13']]]
        if any(len(set(line)) == 1 and set(line) != {'-'} for line in victory_lines):
            win = 1
        if all(field != '-' for field in gf.values()):
            win = 2
        p = 1 if p == 0 else 0
    return win, turn

another_round = 'Y'
while another_round == 'Y':
    result = game()
    os.system('cls')
    if result[0] == 2:
        another_round = input("Game ended in a draw. Another round? Y/N").upper()
    else:
        another_round = input(result[1] + " won. Another round? Y/N ").upper()
    if another_round not in ['Y', 'N']:
        print('Unknown answer. Exiting')
        sys.exit(0)
