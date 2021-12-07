a = "how kteam free education"
#tách chuỗi bằng split(giá trị muốn tách(mặc định là space), [số lần]) -> trả về kiểu list
b = a.split(" ", 1)
print(a)
print("split = ", b)
##split mặc định cắt từ bên trái. Phương thức tách từ bên phải rsplit()
b1 = a.rsplit(" ", 1)
print("rsplit = ", b1)
#Phương thức partition(giá trị): tách thành 3 chuỗi gồm trước, sau giá trị và giá trị theo trình tự-> trả về kiểu tuple
## trình tự bắt đầu trái, phải rpartition(), lpartition()
c = a.partition("e")
print("partition = ", c)
c1 = a.rpartition("e")
print("rpartition = ", c1)
#count("giá trị", [phạm vi]): đếm số giá trị chỉ định trong chuối 
##phạm vi mặc định là toàn chuối
d = a.count("e")
print("count = ", d)
d1 = a.count("e", 10, 14)
print("a[10:14] = ", a[10:14])
print("count area = ", d1)
#Kiểm tra giá trị bắt đầu bằng startswith("giá trị", [vị trí bắt đầu])
##vị trí bắt đầu mặc định là đầu chuỗi từ trái sang 
e = a.startswith("h")
print("startswith =", e)
e1 = a.startswith("h", 4)
print("startswith selection =", e1)
