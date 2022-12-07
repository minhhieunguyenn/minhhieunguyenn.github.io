# Viết chương trình tính tổng N số nguyên lẻ
n = int(input("nhap so n"))
s = 0
for i in range(1, n + 1):
    kq = 0
    if (i % 2 != 0):
        kq = 1
        s = s + i
        print(s)
    else:
        kq = 0
print("tong N sp nguyen le la:", s)

#cach 2: goi ham kiem tra cac so le trong N
def kiemtrachanle (i):
    kq=0
    if (i%2==0):
        print ("la so chan")
        kq=0
    else :
        print ("la so le")
        kq=1
    return kq
n=int(input("nhap so n"))
s=0
for i in range (1, n+1):
    a=kiemtrachanle(i)
    if (a==1):
       s=s+i
print (s)