
from itertools import product
num_dict = {
    '1':[],
    '2':['A','B','C'],
    '3':['D','E','F'],
    '4':['G','H','I'],
    '5':['J','K','L'],
    '6':['M','N','O'],
    '7':['P','Q','R','S'],
    '8':['T','U','V'],
    '9':['W','X','Y','X'],
    '0':[]
}
output = ''
ipt_str = input('Input:')
in_list = list(ipt_str)[1:-1:2]
# print(in_list)
real_letter_list=[]
for l in in_list:
    # print(l)
    real_letter_list.append(num_dict[l])
res = list(product(*tuple(real_letter_list)))
# print(res)
for t in res:
    output+= ''.join(t)+' '
print('Output:',output,sep='')

