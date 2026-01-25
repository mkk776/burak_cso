from funcs import *
import random
import os


# random.seed(1337)
# os.system('clear')

n=4 # random.randint(1,8)

probab = 0.70

numbers = []
for i in range(2**n):
    if random.random()<probab:
        numbers.append(i)

if len(numbers)==0:
    numbers.append(random.randint(0, 2**n-1))

# numbers = [0,1,2,4,6,8,9]
numbers = [0,1,2,3,4,6,12,14]

invert_numbers = True
invert_numbers = False
numbers2 = []
for i in range(2**n):
    if not (i in numbers):
        numbers2.append(i)

if invert_numbers:
    numbers = numbers2

assert max(numbers)<2**n # you should increase n

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


# creating L1
# we must look for below group since we dont have -
L1 = []
for i in range(len(groups)-1):
    for x in groups[i]:
        for y in groups[i+1]:
            is_one, differed = diff(x,y)
            if is_one and (differed not in L1):
                L1.append(differed)

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
# end of creating L1

# creating other layers
layers = [[L1, L1_grouped, L1_grouped_prinable]]
for i in range(1, n):
    layers.append(get_new_layer(layers[-1][1], n=n))
# end of creating other layers

# IN HERE IT INCLUDES UNNDECESARY PRIMES SO I GUESS WE NEED A TABLE AND IM BORED
# # finding primes
# def does_prime_has_it(prime, x):
#     print('################ ', prime, x)
#     for i in range(n):
#         if not prime[i]=='-':
#             if not x[i]==prime[i]:
#                 return False
#     return True

# prime_candidates = []
# for i in layers[::-1]+[[numbers_binary]]:
#     for j in i[0]:
#         is_new_prime = True
#         for prime in prime_candidates:
#             if does_prime_has_it(prime, j):
#                 is_new_prime = False
#                 break
#         if is_new_prime:
#             prime_candidates.append(j)

# print('primes:', ', '.join(primes).replace('\'', ''))
# # end of finding primes


# testing
# f_numbers = []
# for i in range(2**n):
#     i_bin = (n*'0'+bin(i)[2:])[-n:]
#     included = False
#     for prime in primes:
#         if does_prime_has_it(prime, i_bin):
#             included = True
#             break

#     if included:
#         f_numbers.append(i)

# if not f_numbers==numbers:
#     print('BAZINGA... bug') # I tested thausands of numbers to make sure, it works...
#     print(numbers)
#     print(f_numbers)
#     exit(1)
# end of testing


# printing
printed_layers = [numbers_printable, numbers_binary, groups_prinable]
for i in layers:
    printed_layers.append(i[0])
    printed_layers.append(i[2])

header = ('N,'+''.join(['L'+str(i)+',,' for i in range(n+1)]))[:-1]
assert len(header.split(','))==len(printed_layers)
splitter = [' '*len(str(2**n-1)),]+[' '*n]*(len(printed_layers)-1)
for i in range(len(printed_layers)):
    if i==0:
        printed_layers[i] = [(header.split(',')[i]+' '*n)[:len(str(2**n-1))]]+[splitter[i]]+printed_layers[i]
    else:
        printed_layers[i] = [(header.split(',')[i]+' '*n)[:n]]+[splitter[i]]+printed_layers[i]

print_table(printed_layers, n=n)
# end of printing

