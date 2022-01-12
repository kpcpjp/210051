a = int(input("a = "))
b = int(input("b = "))
def ucln(a, b):
    if a == 0 or b == 0:
        ucln = a + b
    else:
        while a != b:
            if a > b:
                a = a -b
            elif a < b:
                b = b -a
        ucln = a
    return ucln
print(a, b)
Uocchung = ucln(a, b)
print("So a = ", a)
print("So b = ", b)
print("UCLN cua a va b la: ", Uocchung)