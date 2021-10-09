i = ''
def Durak(a):
    global i
    if a.isdigit():
         i = int(a)
    else:
        try:
            i = float(a)
        except ValueError:
            print("пожалуйста вводите только числа")
    if type(i) == float or type(i) == int:
        if i <= 0:
            print("нельзя вводить отрицательные числа или нoль")
flag = True
while flag:
    N = input("Bведите ширину зала в метрах: ")
    Durak(N)
    if (type(i) == float or type(i) == int) and i > 0:
        flag = False
        a = i
        i = ''
flag = True
while flag:
    M = input("Введите радиус сцены в метрах: ")
    Durak(M)
    if (type(i) == float or type(i) == int) and i > 0:
        flag = False
        r = i
        i = ''
flag = True
while flag:
    P = input("Введите необходимое расстояние от стены до сцены в метрах: ")
    Durak(P)
    if (type(i) == float or type(i) == int) and i > 0:
        flag = False
        k = i
        i = ''
flag = True
S = a ** 2
Sk = 3.14 * r ** 2
D = (a - 2 * r) / 2
if Sk >= S:
    print("Нельзя поместить сцену в данный зал")
else:
    if D >= k:
        print("Можно поместить сцену в данный зал при желаемом расстоянии от стены до сцены")
    else:
        print("Нельзя поместить сцену в данный зал при желаемом расстоянии от стены до сцены")
