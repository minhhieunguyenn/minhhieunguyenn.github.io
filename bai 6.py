#. tính N! và tổng N với N nhập vào 1+2+3+4+….+n-1+n
n=int(input("nhap so n"))
giaithua=1
s=0
for i in range (1, n+1):
    giaithua=giaithua*i
    s=s+i
print (giaithua)
print("tong n la:",s)




