
total_error = 0

# Vòng lặp nhập dữ liệu
while True:
    quantity = int(input("Nhập số lượng hàng lỗi của quầy (-1 để kết thúc): "))

    
    if quantity == -1:
        break

   
    total_error += quantity


print("Tổng số hàng lỗi thu hồi trong ngày là:", total_error)
        