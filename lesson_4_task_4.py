#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
#и записать в файл многочлен степени k. Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
pow = int(input("Ввеедите степень: "))
def get_polynomial(k):
    polynomial =[]
    koeff = []
    end = '=0'
    unknown = '*x^'
    for i in range(pow+1):
        j = random.randrange(0,100)
        koeff.append(j)
    for i in range(pow+1):
        if koeff[i]>1:
            if i == 0:
                k = str(koeff[i])
                polynomial.insert(0,k)
            elif i == 1:
                k = str(koeff[i])+unknown[0:2]
                polynomial.insert(0,k)
            else:
                k = str(koeff[i])+unknown+str(i)
                polynomial.insert(0,k)
        elif koeff[i] == 1:
            if i == 0 or i==1:
                k = unknown[1]
                polynomial.insert(0,k)
            else:
                k = unknown[1] + str(i)
                polynomial.insert(0,k)
        else:
            continue
    polynominal_str = '+'.join(polynomial)+end
    return polynominal_str
poly_file_1 = open("poly_1.txt", "w+")
poly_file_1.write(get_polynomial(pow))
poly_file_1.close
pow = int(input("Ввеедите степень: "))
poly_file_2 = open("poly_2.txt", "w+")
poly_file_2.write(get_polynomial(pow))
poly_file_2.close