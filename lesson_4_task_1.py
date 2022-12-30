#Вычислить число c заданной точностью d
#Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
d = int(input("введите число, до скольки чисел округлять число pi после запятой: "))
total_pi = 3
number = 4
for i in range(2,1000000,2):
    total_pi+=number/(i*(i+1)*(i+2))
    number = number *(-1)
print(round(total_pi, d))
