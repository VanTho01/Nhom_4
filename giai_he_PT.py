#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np

def Input1():
    #so phuong trinh
    sopt = int(input("Nhap so phuong trinh cua he: "))
    return sopt
def Input2():
    #so an 
    soan = int(input("nhap so an cua phuong trinh: "))
    return soan
sopt = Input1()
soan = Input2()
if (sopt != soan):
    print("Error! Nhap lai!")
    sopt = Input1()
    soan = Input2()

A = np.zeros((sopt, soan), dtype = float)
A1 = np.zeros((sopt, soan), dtype = float)
B = np.zeros((sopt, 1), dtype = float)
def Input3(A, B):
        for pt in range(0, sopt):
            print(f"Nhap he so cua phuong trinh thu {pt + 1}: ")
            for an in range(0, sopt):
                A[pt, an] = float(input(f"----he so thu {an + 1}: "))
            B[pt, 0] = float(input("----he so cuoi: "))
        print (A)
        print (B)
        return A, B
A, B = Input3(A, B)
def calculate(A, B):
    try:
        if (np.linalg.det(A) != 0):
            X = np.dot(np.linalg.inv(A), B)
            return X
        else: 
            calculate(A, B)
    except:
        print("Error!")
        Input3(A, B)
        calculate()
X = calculate(A, B)
print("Nghiem cua he: ", X)
A = np.array([(1,2),(3,4)])
B = np.array([5,6])
A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
print(A)
print(B)
print(A1)
X = np.dot(A1,B)
print('Nghiem cua he:',X)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print('bbbbbbbbbbbbbbbbbbbbbbb')
