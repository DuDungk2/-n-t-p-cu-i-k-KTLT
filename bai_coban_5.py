while True:
    try:
        n=int(input('nhap n:'))
        if n<=0:
            print('Hay nhap so nguyen duong')
        else:
            print('Tang dan: ',end='')
            for i in range(n):
                print(i,end=' ')
            print('\nGiam dan :',end=' ')
            for i in reversed(range(n)):
                print(i,end=' ')
        break
    except:
        print('dau vao khong hop le')

