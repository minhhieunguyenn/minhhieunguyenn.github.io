#nhập vào 3 cạnh của tam giác !
#kiểm tra hợp lệ về tam giác ! và tính chu vi và diện tích
a =int(input("nhap canh a"))
b=int(input("nhap canh b"))
c=int(input("nhap canh c"))
kq=0
#abs: gia tri tuyet doi
if (a+b>c) and (abs(a-b)<c):
    kq=1
if (a+c>b) and (abs(a-c)<b):
    kq=kq+1
if (b+c>a) and (abs(b-c)<a):
    kq=kq+1
if kq==3 :
    print ("3 canh thoa man hinh tam giac")
    d=0
    s=0
    d=(a+b+c)
    print ("chu vi tam giac la:",d)
    p=(a+b+c)/2
    import math
    s=math. sqrt(p*(p-a)*(p-b)*(p-c))
    print ("dien tich tam giac la:",s)
else:
    print ("3 canh tam giac khong hop le")


#cach 2 : su dung ham de kiem tra 3 canh tam giac
def kiemtra3canhtamgiac(a,b,c):
    kq=0
    if (a + b > c) and (abs(a - b) < c):
        kq = 1
    if (a + c > b) and (abs(a - c) < b):
        kq = kq + 1
    if (b + c > a) and (abs(b - c) < a):
        kq = kq + 1
    return kq
a =int(input("nhap canh a"))
b=int(input("nhap canh b"))
c=int(input("nhap canh c"))
e = kiemtra3canhtamgiac(a,b,c)
if (kq==3):
    print ("tam giac hop le")
    d = 0
    s = 0
    d = (a + b + c)
    print("chu vi tam giac la:", d)
    p = (a + b + c) / 2
    import math
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print ("dien tich tam giac la:",s)
else :
    print ("tam giac khong hop le")


