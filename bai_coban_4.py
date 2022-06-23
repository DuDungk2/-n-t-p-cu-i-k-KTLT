def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)
def bscnn(a, b):
    return int((a * b) / uscln(a, b))
while True:
    try:
        a = int(input("Nhập số nguyên dương a = "))
        break
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên dương.')
while True:
    try:
        b = int(input("Nhập số nguyên dương b = "))
        break
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên dương.')

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b))
