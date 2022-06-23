while True:
    try:
        n=int(input('Nhap m: '))
        break
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên.')
m=[]
so_chan= []
so_le= []
for i in range(n):
    m = m+ [ int(input('Nhap m[%d]='%i)) ]
for i in range (n) :
    if m[i]%2==0:
        so_chan.append(m[i])
    else:
       so_le.append(m[i])    


print('Các số chẵn là:',so_chan)
print('Các số lẻ là:',so_le)
