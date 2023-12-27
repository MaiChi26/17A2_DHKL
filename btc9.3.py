def BMI(can_nang, chieu_cao):
    BMI=can_nang/(chieu_cao*chieu_cao)
    print('chỉ số BMI:%.2f'%BMI)
    if BMI<18.5:
        print('đánh giá theo chỉ số: gầy')
    elif BMI>=18.5 and BMI<24.99:
        print('đánh giá theo chỉ số: bình thường')
    else:
        print('đánh giá theo chỉ số: thừa cân')
    return
a=float(input("nhập cân nặng(kg):"))
b=float(input("nhập chiều cao(m):"))
BMI(a,b) 
        