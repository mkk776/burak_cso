# checks one digit changes
def diff(x, y):
    diff=0
    output=''
    for i in range(len(x)):
        if x[i]==y[i]:
            output+=x[i]
        else:
            diff+=1
            output+='-'

    if diff==1:
        return [True, output]
    else:
        return [False, '']

# finds all one digit changes and replecas them with '-'
def get_new_layer(input_grouped, n):
    output = []
    for i in range(len(input_grouped)-1):
        for x in range(len(input_grouped[i])):
            for y in range(x+1, len(input_grouped[i])):
                is_one, differed = diff(input_grouped[i][x],input_grouped[i][y])
                if is_one and (differed not in output):
                    output.append(differed)

    output_grouped = []
    index = -1
    changed = -1
    for i in sorted(output, key=lambda x:int(x.replace('1', '0').replace('-', '1'), 2)):
        if not changed==int(i.replace('1', '0').replace('-', '1'), 2):
            changed = int(i.replace('1', '0').replace('-', '1'), 2)
            output_grouped = output_grouped+[[]]
            index+=1
        output_grouped[index] = output_grouped[index]+[i]

    output_grouped_prinable = []
    for i in output_grouped:
        output_grouped_prinable = output_grouped_prinable+i+[' '*n]
    output_grouped_prinable = output_grouped_prinable[:-1]

    return [output, output_grouped, output_grouped_prinable]

def print_table(array_of_arrays, n):
    max_lines = max([len(i) for i in array_of_arrays])

    width = 3*len(array_of_arrays)-1
    for i in array_of_arrays:
        try:
            width+=len(i[0])
        except IndexError:
            width+=n

    print('/'+'-'*(width)+'\\')
    for line in range(max_lines):
        print('| ', end='')
        for i in range(len(array_of_arrays)):
            try:
                print(array_of_arrays[i][line], end=' | ')
            except IndexError:
                try:
                    array_of_arrays[i][0]
                    print(' '*len(array_of_arrays[i][0])+' | ', end='')
                except IndexError:
                    print(' '*n+' | ', end='')
        print('')
    print('\\'+'-'*(width)+'/')
