while True:
    try:
        n=int(input('Nhap m: '))
        break
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên dương.')
m=[]
for i in range(n):
    m = m+ [ int(input('Nhap m[%d]='%i)) ]

print('Trung bình cộng các số là ', sum(m)/len(m))
