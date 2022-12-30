#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
with open('poly_1.txt', 'r') as text:
    poly_1 = text.readline()
with open('poly_2.txt', 'r') as text:
    poly_2 = text.readline()
def adaptation(poly):
    poly = poly.replace('=0','').replace('x+', 'x^1+')
    num_list = []
    num = ''
    for i in poly:
        if i.isdigit():
            num = num + i
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list 
poly_list_1 = adaptation(poly_1)
poly_list_2 = adaptation(poly_2)
sum_poly_list = []
for i in range(len(poly_list_1)):
    if i%2 == 0:
        sum_poly_list.append(poly_list_1[i]+poly_list_2[i])
    else:
        sum_poly_list.append(poly_list_1[i])

end = '=0'
unknown = '*x^'
sum_poly_list2 = []
for i in range(len(sum_poly_list)-1):
    if i%2 == 0:
        sum_poly_list2.append(str(sum_poly_list[i]) + unknown + str(sum_poly_list[i+1]))
    elif i == ((len(sum_poly_list))-2):
        sum_poly_list2.append(str(sum_poly_list[i+1]))
    else:
        continue  
sum_poly_str = '+'.join(sum_poly_list2)+end
poly_sum_file = open("poly_sum.txt", "w+")
poly_sum_file.write(sum_poly_str)
poly_sum_file.close
