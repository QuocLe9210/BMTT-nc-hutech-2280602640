#Nhap so tu nguoi dung
so = int(input("Nhap mot so nguyen : "))
#kiem tra so do la so chan hay le
if so % 2 == 0:
    print(so, "So ban vua nhap la so chan.")
else:
    print(so, "So ban vua nhap la so le.")