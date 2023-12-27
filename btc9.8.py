n = int(input("Nhập vào số N lớn hơn 0:"))
S = 0
for i in range(1, n):
    if (n % i == 0):
        S += i
if (S == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")