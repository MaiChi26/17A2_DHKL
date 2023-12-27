def tinh_can(nam):
    a=nam%10
    if a==0:
        can="canh"
    if a==1:
        can="tân"
    if a==2:
        can="Nhâm"
    if a==3:
        can="quý"
    if a==4:
        can="giáp"
    if a==5:
        can="ất"
    if a==6:
        can="bính"
    if a==7:
        can="đinh"
    if a==8:
        can="mậu"
    if a==9:
        can="kỷ"
    return can
def tinh_chi(nam):
    a=nam%12
    if a==0:
        chi="thân"
    if a==1:
        chi="dậu"
    if a==2:
        chi="tuất"
    if a==3:
        chi="hợi"
    if a==4:
        chi="tý"
    if a==5:
        chi="sửu"
    if a==6:
        chi="dần"
    if a==7:
        chi="mão"
    if a==8:
        chi="thìn"
    if a==9:
        chi="tỵ"
    if a==10:
        chi="ngọ"
    if a==11:
        chi="mùi"
    return chi
nam=int(input("nhập năm:"))
print('năm' ,nam,"lịch âm là năm",tinh_can(nam),tinh_chi(nam))