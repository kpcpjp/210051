###str part 4 Phương thức chuỗi
a = "free Education"
print("a = ", a)
#Chỉ viết hoa kí tự đầu bằng capitalize()
b = a.capitalize()
print("b = ", b)
#Viết hoa toàn bộ chữ cái bằng upper()
c = a.upper()
print("c = ", c)
#Viết thường toàn bộ chữ cái bằng upper()
d = a.lower()
print("d = ", d)
#đảo ngược chữ viết hoa và viết thường bằng swapcase()
e = a.swapcase()
print("e = ", e)
#Viết hoa các chữ cái đầu của từ bằng title()
f = a.title()
print("f = ",f)
#căn giữa bằng center(width, [fillchar]) 
##fillchar có thể không điền và chỉ 1 kí tự
##tổng độ dài bằng width
g = a.center(30, "-")
print(g)
print("len(a) = ", len(a))
print("len(g) = ", len(g))
#căn trái, phải bằng rjust(), ljust()
h = a.rjust(30, "-")
i = a.ljust(30, "-")
print(h)
print(i)

