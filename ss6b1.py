stock = int(input("Nhập tồn kho: "))

if stock >= 50:
    print("hàng đầy kho ")
elif (stock >= 10 and stock < 50):
    print("mức an toàn ")
elif stock <10 :
    print("Sắp hết hàng, cần báo cáo nhập thêm")
    