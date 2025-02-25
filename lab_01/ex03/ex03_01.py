def tinh_tong_so_chan(list):
    tong = 0 
    for num in list:
        if num % 2 ==0:
            tong += num
            return tong
    input_list = input("Nhap danh sach cac so  bang dau phay : ")
    numbers = input_list.split(",")
    tong_chan = tinh_tong_so_chan(numbers)
    print("Tong cac so chan trong day la: ", tong_chan)