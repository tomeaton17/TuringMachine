tape = [1, 1, 1, 'B']
state = 'q0'
index = 0
print(index)

def print_tape(name):
    print(*name, sep='')

def print_arrow(index):
    spaces = ''
    for i in range(0,index):
        spaces += ' '
    print(spaces + '^')

while state != 'qf':
    if(state == 'q0'):
        if(tape[index] == 1):
            index += 1
            print_tape(tape)
            print_arrow(4)
        elif(tape[index] == 'B'):
            state = 'qf'

print('done')
