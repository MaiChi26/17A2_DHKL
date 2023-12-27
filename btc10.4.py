x=int(input("nhập số x: "))
n=int(input("nhập số n: "))
import math
S=math.pow(pow(x,2)+x+1,n)+math.pow(pow(x,2)-x+1,n)
print("S=",S)