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
    '9':['W','X','Y','Z'],
    '0':[]
}
output = ''
while True:
    ipt_str = input('请输入0-9的列表格式（每位用逗号隔开）:')

    # print(len(list(ipt_str)))
    if len(list(ipt_str)) <=5:
        in_list = list(ipt_str)[1:-1:2]
    # print(in_list)
        real_letter_list = []
        for l in in_list:
            # print(l)
            if not(l=='1' or l=='0'):
                real_letter_list.append(num_dict[l])
    # print(real_letter_list)
        res = list(product(*tuple(real_letter_list)))
    # print(res)
        for t in res:
            output+= ''.join(t)+' '
        print('Output:',output,sep='')
        break
    else:
        print('只支持输入两位数字，请重新输入')
