import os
import time
tape = [1, 1, 1, 'B']
state = 'q0'
index = 0

def print_arrow_tape(name, index):
    spaces = ''
    tape_string = ''
    for i in range(0,index):
        spaces += ' '

    for i in name:
        if i == 1 or i == 0:
            tape_string += str(i)

    os.system('cls')
    print(tape_string)
    print(spaces + '^')



def oneStateInversion(index, state):
    print_arrow_tape(tape, index)
    time.sleep(1)
    while state != 'qf':
        if(tape[index] == 'B'):
            state = 'qf'
        elif(tape[index] == 0):
            tape[index] = 1
            index += 1
            print_arrow_tape(tape, index)
            time.sleep(1)
        else:
            tape[index] = 0
            index += 1
            print_arrow_tape(tape, index)
            time.sleep(1)


oneStateInversion(0, 0)