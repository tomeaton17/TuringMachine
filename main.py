tape = [1, 1, 1, 'B']
state = 'q0'
index = 0
print(index)

while state != 'qf':
    if(state == 'q0'):
        if(tape[index] == 1):
            index += 1
            print(index)
        elif(tape[index] == 'B'):
            state = 'qf'

print('done')
