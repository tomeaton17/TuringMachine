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

print_arrow_tape(tape, index)
time.sleep(1)

while state != 'qf':
    if(state == 'q0'):
        if(tape[index] == 1):
            index += 1
            print_arrow_tape(tape,index)
        elif(tape[index] == 'B'):
            state = 'qf'
        time.sleep(1)


