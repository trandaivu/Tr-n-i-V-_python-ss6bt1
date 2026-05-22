ton_kho = 100
while True:
    quantity = int(input("Nhập số lượng  "))

    if quantity < 0:
        print("Số lượng không hợp lệ. Vui lòng nhập lại.")
        continue

    elif  quantity > ton_kho:
        print("Không đủ hàng trong kho. Vui lòng nhập lại.")
        continue

    
    else:
        ton_kho -= quantity
        print("Số lượng hàng còn lại trong kho là:", ton_kho)
        break
    
     