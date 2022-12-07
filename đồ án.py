#để hiển thị cho người dùng biết ngày giờ hiện tại
from datetime import datetime  # hàm lấy giờ hệ thống
now = datetime.now()
current_year = now.strftime("%Y")
current_month = now.strftime("%m")
current_day = now.strftime("%d")
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
current_second = now.strftime("%S")
print('năm hiện tại: ', current_year)
print('tháng hiện tại: ', current_month)
print('ngày hiện tại: ', current_day)
print('giờ hiện tại: ', current_hour)
print('phút hiện tại: ', current_minute)
print('giây hiện tại: ', current_second)

nbt =int(input("nhap nam bao thuc"))
while (nbt < int(current_year)) :
  nbt= int(input("moi nhap lai nam bao thuc"))
else :
  tbt = int(input("nhap thang bao thuc"))
  if (tbt<1) or (tbt>12):    #if or
      tbt=int(input("vui lòng nhập lại tháng báo thức"))
  else:
      ngbt = int(input("nhap ngay bao thuc"))
      kq=0
      if (nbt % 4==0): # la năm nhuần
          kq=1
      else :
          kq=2
      if (tbt==2): # == : là để so sánh
          if (kq==1):
              if (ngbt<1) or (ngbt>29):   #if or
                  ngbt=int(input("vui lòng nhập lại ngày báo thức"))
              else:
                  kq=3 # = :là để gán
          else :
              if (ngbt<1) or (ngbt>28):   #if or
                  ngbt =int(input("vui lòng nhập lại ngày báo thức"))
              else :
                  kq=3
      if (tbt!=2):
          if (tbt<8):
              if (tbt%2==0):
                  if (ngbt<1) or (ngbt>30): #if or nha
                      ngbt=int(input("vui lòng nhập lại ngày báo thức"))
                  else :
                      kq=3
              else:
                  if (ngbt<1) or (ngbt>31): #if or
                      ngbt= int(input("vui lòng nhập lại ngày báo thức"))
                  else:
                      kq=3
          else:   #thiếu nè
              if ngbt<1 or ngbt>31:
                  ngbt=int(input('vui lòng nhập lại ngày báo thức'))
              else:
                  kq=3
                  if kq==3:
                          gbt = int(input("nhap gio bao thuc"))
                          if (gbt<0) or (gbt>23): #if or và sửa thành 0 đến 23 giờ
                              gbt=int(input("vui lòng nhập lại giờ báo thức"))
                          else:
                              pbt = int(input("nhap phút bao thuc"))
                              if (pbt<0) or (pbt>60):    #if or
                                  pbt =int(input("vui lòng nhập lại phút báo thức"))
                              else:
                                  giaybt= int(input("nhập giây báo thức"))
                                  if (giaybt<0) or (giaybt>60):  #if or
                                       giaybt= int(input("vui lòng nhập lại giây báo thức"))

flag=False
while flag==False :
  from datetime import datetime #hiển thị thời gian trong python
  now = datetime.now()
  current_year = now.strftime ("%Y")
  current_month = now.strftime ("%m")
  current_day = now.strftime("%d")
  current_hour = now.strftime("%H")
  current_minute = now.strftime("%M")
  current_second = now.strftime("%S")
  print('năm hiện tại: ', current_year)
  print('tháng hiện tại: ', current_month)
  print('ngày hiện tại: ', current_day)
  print('giờ hiện tại: ', current_hour)
  print('phút hiện tại: ', current_minute)
  print('giây hiện tại: ', current_second)
  if  int(current_year)==nbt and int(current_month) == tbt and int(current_day)== ngbt and int(current_hour) == gbt and int(current_minute) == pbt and int(current_second)==giaybt:  # đổi về int
      print('wake up')
      flag = True
  else:
      flag = False
      print('ngủ tiếp')

