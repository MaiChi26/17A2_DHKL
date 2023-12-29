import datetime
nam=int(input('nhập năm: '))
thang=int(input("nhập tháng: "))
ngay=int(input("nhập ngày: "))
print("ngày tháng năm vừa nhập:",ngay,thang,nam)
import calendar
# giả sử true là năm nhuận, false không là năm nhuận
print(calendar.isleap(nam))
# giả sử giá trị số 0:thứ 2; 1:thứ 3; 2:thứ 4;......
print(calendar.weekday(nam,thang,ngay))
# giả sử phần tử thứ nhất là ngày đầu tiên trong tháng, phần tử thứ hai là số ngày trong tháng
print(calendar.monthrange(nam,thang))