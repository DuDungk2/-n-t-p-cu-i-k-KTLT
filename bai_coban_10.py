while True:
    try:
        r=int(input('Nhap ban kinh r: '))
        break
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên.')
cv= 2*3.14*r
dt=3.14*r*r
print('Chu vi hinh tron la :',cv)
print('Dien tich hinh tron la :',dt)
