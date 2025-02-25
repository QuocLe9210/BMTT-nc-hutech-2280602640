def dao_nguoc_list(list):
    return list[::-1]

input_list = input("Nhap danh sach cac so  bang dau phay : ")
numbers = list(map, (int, input_list.split(",")))
list_dao_nguoc = dao_nguoc_list(numbers)
print("Day so dao nguoc la: ", list_dao_nguoc)
