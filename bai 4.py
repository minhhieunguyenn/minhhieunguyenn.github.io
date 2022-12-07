# Giải phương trình bậc nhất ax+b=0
def giaiphuongtrinhbacnhat(a,b):
    kq=0
    if (a==0) and (b!=0):
        kq=1
    if (a==0) and (b==0):
        kq=2
    if a!=0 :
        kq=3
    return kq
a=int(input ("nhap so a"))
b=int(input("nhap so b"))
x=0
s=giaiphuongtrinhbacnhat (a,b)
print (s)
if (s==1):
    print ("phuong trinh vo nghiem")
if (s==2):
    print ("phuong trinh co vo so nghiem")
else :
    x=-b/a
    print("phuong trinh co mot nghiem la:",x)

