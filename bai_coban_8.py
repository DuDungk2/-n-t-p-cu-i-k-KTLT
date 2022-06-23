def tienlaisuat(t,n,k):
    for i in range(k):
     n=n+n*t/100
     print('Tong so tien nhan duoc la: ')
     print(n)
if __name__=='__main__':
    t=float(input('Nhap lai suat: '))
    n=float(input('Nhap so tien gui ban dau: '))
    k=int(input('Nhap so thang gui: '))
tienlaisuat(t,n,k)
