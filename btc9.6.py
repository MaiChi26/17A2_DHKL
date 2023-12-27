x=int(input("nhập số x: "))
def kiem_tra_so_nguyen_to(x):
    if x<=1:
        print(x,"không phải là số nguyên tố")
    else:
        for i in range(1, x):
            if x % i ==0:
                print(x,"không phải là số nguyên tố")
            else:
                print(x,"là số nguyên tố")
    return




        
    