from funcs import *
import random
import os


# random.seed(1337)
os.system('clear')

n=4

while True:
    probab = 0.80

    numbers = []
    for i in range(0, 2**n):
        if random.random()<probab:
            numbers.append(i)

    numbers = [1,4,7,9,15,16,17,20,21,24,25,28,29]

    numbers_printable = [str(i)+' '*(len(str(2**n-1))-len(str(i))) for i in numbers]

    numbers_binary = []
    for i in numbers:
        numbers_binary.append((n*'0'+bin(i)[2:])[-n:])


    groups = []
    index = -1
    changed = -1
    for i in sorted(numbers_binary, key=lambda x:len(x.replace('0', ''))):
        if not changed==len(i.replace('0', '')):
            changed = len(i.replace('0', ''))
            index+=1
            groups = groups+[[]]
        groups[index] = groups[index]+[i]


    groups_prinable = []
    for i in groups:
        if not i==[]:
            groups_prinable = groups_prinable+i+[' '*n]
    groups_prinable = groups_prinable[:-1]




    L1 = []
    for i in range(len(groups)-1):
        for x in groups[i]:
            for y in groups[i+1]:
                is_one, output = diff(x,y)
                if is_one:
                    L1.append(output)

    L1_grouped = []
    index = -1
    changed = -1
    for i in sorted(L1, key=lambda x:int(x.replace('1', '0').replace('-', '1'), 2)):
        if not changed==int(i.replace('1', '0').replace('-', '1'), 2):
            changed = int(i.replace('1', '0').replace('-', '1'), 2)
            L1_grouped = L1_grouped+[[]]
            index+=1
        L1_grouped[index] = L1_grouped[index]+[i]

    L1_grouped_prinable = []
    for i in L1_grouped:
        L1_grouped_prinable = L1_grouped_prinable+i+[' '*n]
    L1_grouped_prinable = L1_grouped_prinable[:-1]




    def get_new_layer(L1_grouped):
        L2 = []
        for i in range(len(L1_grouped)-1):
            for x in range(len(L1_grouped[i])):
                for y in range(x+1, len(L1_grouped[i])):
                    is_one, output = diff(L1_grouped[i][x],L1_grouped[i][y])
                    if is_one and (output not in L2):
                        L2.append(output)

        L2_grouped = []
        index = -1
        changed = -1
        for i in sorted(L2, key=lambda x:int(x.replace('1', '0').replace('-', '1'), 2)):
            if not changed==int(i.replace('1', '0').replace('-', '1'), 2):
                changed = int(i.replace('1', '0').replace('-', '1'), 2)
                L2_grouped = L2_grouped+[[]]
                index+=1
            L2_grouped[index] = L2_grouped[index]+[i]

        L2_grouped_prinable = []
        for i in L2_grouped:
            L2_grouped_prinable = L2_grouped_prinable+i+[' '*n]
        L2_grouped_prinable = L2_grouped_prinable[:-1]

        return [L2, L2_grouped, L2_grouped_prinable]


    layers = [[L1, L1_grouped, L1_grouped_prinable]]
    for i in range(1, n):
        layers.append(get_new_layer(layers[-1][1]))

    printed_layers = [numbers_printable, numbers_binary, groups_prinable]
    for i in layers:
        printed_layers.append(i[0])
        printed_layers.append(i[2])

    header = ('N,bin,,'+''.join(['L'+str(i)+',,' for i in range(1, n+1)]))[:-1]
    assert len(header.split(','))==len(printed_layers)
    splitter = [' '*len(str(2**n-1)),]+[' '*n]*(len(printed_layers)-1)
    for i in range(len(printed_layers)):
        if i==0:
            printed_layers[i] = [(header.split(',')[i]+' '*n)[:len(str(2**n-1))]]+[splitter[i]]+printed_layers[i]
        else:
            printed_layers[i] = [(header.split(',')[i]+' '*n)[:n]]+[splitter[i]]+printed_layers[i]

    if len(printed_layers[-3])>2:
        break
print_table(printed_layers, n=n)