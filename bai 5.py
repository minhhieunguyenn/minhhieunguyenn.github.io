#nhập vào một ngày tháng  nam vào cho biết tháng đó có bao nhiêu ngày
a=int(input("nhap ngay"))
b=int(input("nhap thang"))
c=int(input("nhap nam"))
kq=0
if (c%4==0):
    print ("la nam nhuan")
    kq==1
else:
    print ("la nam khong nhuan")
    kq==2
if (b==2):
    if (kq==1):
        print ("co 29 ngay")
    else:
        print("co 28 ngay")
if (b!=2):
    if (b<8):
        if (b%2==0):
            print ("co 30 ngay trong thang")
        else:
            print ("co 31 ngay trong thang")
    if (b>=8) and (b<=12):
        if (b%2!=0):
            print ("co 30 ngay trong thang")
        else :
            print ("co 31 ngay trong thang")


