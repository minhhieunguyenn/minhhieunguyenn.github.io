#chương trình nhập vào một con số ứng với con số đó là
#1 thì in ra màn hình dòng “tôi là người việt nam”
#2 in ra màn hình dòng “tôi là người hàn quốc”
#3 in ra “tôi là người  campuchia “
#Khac 1,2,3 “toi khong phai la nguoi ”
n=int(input("nhap so n"))
kq=0
if (n==1):
    print ("toi la nguoi viet nam")
    kq=1
else :
    kq=0
if (n==2):
    print ("toi la nguoi han quoc")
else:
    kq=0
if (n==3):
    print ("toi la nguoi campuchia")
else:
    kq=0
if kq==0 :
    print ("toi khong phai la nguoi")

