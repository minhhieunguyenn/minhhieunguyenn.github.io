#tính tổng các nghiệm của phương trình bậc 2 khi có 2 nghiem phan biet
def giaiptrinh (x):
    kq=0
    denta=b**2-a*a*c
    if (denta>0):
        kq=1
    else:
        kq=0
    return kq
n=int(input("nhap so n"))
for i in range (1, n+1):
    a=int(input("nhap so a"))
    b=int(input("nhap so b"))
    c=int(input("nhap so c"))
