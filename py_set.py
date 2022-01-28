#kieu du lieu set
"""set_1 = {69, 96}
print(set_1)
print(type(set_1))"""

"""set_2 = {"how Kteam"}
print(set_2)"""

"""set_3 = {(69, 'Free Education'), (1,2,3)}
print(set_3)"""

#kieu set khong luu duoc unhashable object nhu mot set khac hay list
"""
set_4 = {1,2,{"a"}}
set_5 = {[22]}
print(set_4, set_5)"""

#set khong quan tam den vi tri cac phan tu
"""set6 = {'khanh', 'nguyen', 14, 'Thanh'}
print(set6)"""

#set chi luu 1 gia tri giong nhau
"""set7 = {1, 1, 1}
print(set7)"""
#khong the tao 1 set rong boi no la 1 dictionary
"""set8 = {}
print(type(set8))"""

#su dung constructor cho set. Khi do no se tao ra 1 set
"""set9 = set((1, 2, 3))
set10 = set(("Khanh"))
set11 = set()
print(set9, set10, set11)
print(type(set9))
print(type(set11))"""

#toan tu trong set

#toan tu in (chi kiem tra duoc 1 phan tu)
"""print(1 in {1, 2, 4})   #True
print({1, 2} in {1, 2, 3})  #False
print((1, 2) in {(1, 2), 3})   #True"""
#toan tu - (ket qua la gia tri chi ton tai trong set dau tien, neu khong co tra ve set rong)
"""print({1, 2, 3, 4} - {2, 3})
print({1, 2} - {1, 3, 4})
print({1} - {1})"""
#toan tu & (ket qua la phan tu ton tai trong ca 2 set, neu khong tra ve set())
'''print({1, 2} & {3, 4})
print({1, 2, 5, 6} & {2, 5, 7})'''
#toan tu | (ket qua tra ve cac phan tu ca 2 set deu co)
#print({1, 2, 5, 6} | {2, 5, 7})
#toan tu ^ (XOR) Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại ở một trong hai Set
       #  ^ = | - &
"""print({1, 2, 3} ^ {3, 4})"""

#phuong thuc voi set
#clear() - tra ve set()
"""set12 = {1, 2, 3}
set12.clear()
print(set12)"""
#pop() (khong giong nhu list pop() trong set lay ra gia tri dau tien trong set va khong su dung doi so)
"""
set13 = {1, 2, 3}
set13.pop()
print(set13)"""
#pop() voi set rong se bi KeyError
"""
set14 = set()
set14.pop()"""
#remove() : lay ra gia tri o trung voi doi so chi dinh trong set
"""
set15 = {1, 2, 3, 7, 5, 4}
set15.remove(7)
print(set15)
"""
#discard(): giong nhu remove() nhung khong bao loi voi cac gia tri khong nam trong set
"""
set16 = {1, 2, 3, 7, 5, 4}
set16.discard(9)
print(set16)
"""
#copy(): sao chep set
"""
set17 = {1, 2, 3}
set18 = set17.copy()
print(set18)
"""
#add() : them phan tu trong doi so vao set
set19 = {1, 2, 3}
set19.add(5)
print(set19)