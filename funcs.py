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