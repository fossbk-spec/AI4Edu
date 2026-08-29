"""
Cơ sở dữ liệu danh mục bài học chuẩn 100% SGK Toán Lớp 3 và Lớp 5 (Tập 1 và Tập 2)
Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG - Nhà xuất bản Giáo dục Việt Nam (CTGDPT 2018).
"""

from typing import List, Dict, Any

# ==============================================================================
# TOÁN LỚP 3 (KẾT NỐI TRI THỨC VỚI CUỘC SỐNG - 16 CHỦ ĐỀ, 81 BÀI HỌC)
# ==============================================================================
MATH_GRADE_3_LESSONS = [
    # ------------------ TẬP 1 (BÀI 1 -> BÀI 44) ------------------
    # Chủ đề 1: Ôn tập và bổ sung
    {"id": "t3_b01", "grade": 3, "volume": 1, "page": 6, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 1: Ôn tập các số đến 1 000"},
    {"id": "t3_b02", "grade": 3, "volume": 1, "page": 9, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000"},
    {"id": "t3_b03", "grade": 3, "volume": 1, "page": 11, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 3: Tìm thành phần trong phép cộng, phép trừ"},
    {"id": "t3_b04", "grade": 3, "volume": 1, "page": 14, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 4: Ôn tập bảng nhân 2; 5, bảng chia 2; 5"},
    {"id": "t3_b05", "grade": 3, "volume": 1, "page": 16, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 5: Bảng nhân 3, bảng chia 3"},
    {"id": "t3_b06", "grade": 3, "volume": 1, "page": 19, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 6: Bảng nhân 4, bảng chia 4"},
    {"id": "t3_b07", "grade": 3, "volume": 1, "page": 21, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 7: Ôn tập hình học và đo lường"},
    {"id": "t3_b08", "grade": 3, "volume": 1, "page": 24, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 8: Luyện tập chung"},
    
    # Chủ đề 2: Bảng nhân, bảng chia
    {"id": "t3_b09", "grade": 3, "volume": 1, "page": 28, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 9: Bảng nhân 6, bảng chia 6"},
    {"id": "t3_b10", "grade": 3, "volume": 1, "page": 31, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 10: Bảng nhân 7, bảng chia 7"},
    {"id": "t3_b11", "grade": 3, "volume": 1, "page": 33, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 11: Bảng nhân 8, bảng chia 8"},
    {"id": "t3_b12", "grade": 3, "volume": 1, "page": 36, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 12: Bảng nhân 9, bảng chia 9"},
    {"id": "t3_b13", "grade": 3, "volume": 1, "page": 39, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 13: Tìm thành phần trong phép nhân, phép chia"},
    {"id": "t3_b14", "grade": 3, "volume": 1, "page": 42, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 14: Một phần mấy"},
    {"id": "t3_b15", "grade": 3, "volume": 1, "page": 46, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 15: Luyện tập chung"},
    
    # Chủ đề 3: Làm quen với hình phẳng, hình khối
    {"id": "t3_b16", "grade": 3, "volume": 1, "page": 49, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng"},
    {"id": "t3_b17", "grade": 3, "volume": 1, "page": 52, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 17: Hình tròn. Tâm, bán kính, đường kính của hình tròn"},
    {"id": "t3_b18", "grade": 3, "volume": 1, "page": 54, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 18: Góc, góc vuông, góc không vuông"},
    {"id": "t3_b19", "grade": 3, "volume": 1, "page": 56, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 19: Hình tam giác, hình tứ giác. Hình chữ nhật, hình vuông"},
    {"id": "t3_b20", "grade": 3, "volume": 1, "page": 61, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 20: Thực hành vẽ góc vuông, vẽ đường tròn, hình vuông, hình chữ nhật và vẽ trang trí"},
    {"id": "t3_b21", "grade": 3, "volume": 1, "page": 63, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 21: Khối lập phương, khối hộp chữ nhật"},
    {"id": "t3_b22", "grade": 3, "volume": 1, "page": 65, "topic_group": "Chủ đề 3: Làm quen với hình phẳng, hình khối", "title": "Bài 22: Luyện tập chung"},
    
    # Chủ đề 4: Phép nhân, phép chia trong phạm vi 100
    {"id": "t3_b23", "grade": 3, "volume": 1, "page": 67, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 23: Nhân số có hai chữ số với số có một chữ số"},
    {"id": "t3_b24", "grade": 3, "volume": 1, "page": 70, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 24: Gấp một số lên một số lần"},
    {"id": "t3_b25", "grade": 3, "volume": 1, "page": 72, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 25: Phép chia hết, phép chia có dư"},
    {"id": "t3_b26", "grade": 3, "volume": 1, "page": 75, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 26: Chia số có hai chữ số cho số có một chữ số"},
    {"id": "t3_b27", "grade": 3, "volume": 1, "page": 79, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 27: Giảm một số đi một số lần"},
    {"id": "t3_b28", "grade": 3, "volume": 1, "page": 81, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 28: Bài toán giải bằng hai bước tính"},
    {"id": "t3_b29", "grade": 3, "volume": 1, "page": 83, "topic_group": "Chủ đề 4: Phép nhân, phép chia trong phạm vi 100", "title": "Bài 29: Luyện tập chung"},
    
    # Chủ đề 5: Một số đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ
    {"id": "t3_b30", "grade": 3, "volume": 1, "page": 85, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 30: Mi-li-mét"},
    {"id": "t3_b31", "grade": 3, "volume": 1, "page": 87, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 31: Gam"},
    {"id": "t3_b32", "grade": 3, "volume": 1, "page": 89, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 32: Mi-li-lít"},
    {"id": "t3_b33", "grade": 3, "volume": 1, "page": 91, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 33: Nhiệt độ. Đơn vị đo nhiệt độ"},
    {"id": "t3_b34", "grade": 3, "volume": 1, "page": 93, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 34: Thực hành và trải nghiệm với các đơn vị mi-li-mét, gam, mi-li-lít, độ C"},
    {"id": "t3_b35", "grade": 3, "volume": 1, "page": 95, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích, nhiệt độ", "title": "Bài 35: Luyện tập chung"},
    
    # Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000
    {"id": "t3_b36", "grade": 3, "volume": 1, "page": 97, "topic_group": "Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000", "title": "Bài 36: Nhân số có ba chữ số với số có một chữ số"},
    {"id": "t3_b37", "grade": 3, "volume": 1, "page": 99, "topic_group": "Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000", "title": "Bài 37: Chia số có ba chữ số cho số có một chữ số"},
    {"id": "t3_b38", "grade": 3, "volume": 1, "page": 104, "topic_group": "Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000", "title": "Bài 38: Biểu thức số. Tính giá trị của biểu thức số"},
    {"id": "t3_b39", "grade": 3, "volume": 1, "page": 109, "topic_group": "Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000", "title": "Bài 39: So sánh số lớn gấp mấy lần số bé"},
    {"id": "t3_b40", "grade": 3, "volume": 1, "page": 111, "topic_group": "Chủ đề 6: Phép nhân, phép chia trong phạm vi 1 000", "title": "Bài 40: Luyện tập chung"},
    
    # Chủ đề 7: Ôn tập học kì 1
    {"id": "t3_b41", "grade": 3, "volume": 1, "page": 113, "topic_group": "Chủ đề 7: Ôn tập học kì 1", "title": "Bài 41: Ôn tập phép nhân, phép chia trong phạm vi 100, 1 000"},
    {"id": "t3_b42", "grade": 3, "volume": 1, "page": 116, "topic_group": "Chủ đề 7: Ôn tập học kì 1", "title": "Bài 42: Ôn tập biểu thức số"},
    {"id": "t3_b43", "grade": 3, "volume": 1, "page": 118, "topic_group": "Chủ đề 7: Ôn tập học kì 1", "title": "Bài 43: Ôn tập hình học và đo lường"},
    {"id": "t3_b44", "grade": 3, "volume": 1, "page": 120, "topic_group": "Chủ đề 7: Ôn tập học kì 1", "title": "Bài 44: Ôn tập chung"},

    # ------------------ TẬP 2 (BÀI 45 -> BÀI 81) ------------------
    # Chủ đề 8: Các số đến 10 000
    {"id": "t3_b45", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số đến 10 000", "title": "Bài 45: Các số có bốn chữ số. Số 10 000"},
    {"id": "t3_b46", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số đến 10 000", "title": "Bài 46: So sánh các số trong phạm vi 10 000"},
    {"id": "t3_b47", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số đến 10 000", "title": "Bài 47: Làm quen với chữ số La Mã"},
    {"id": "t3_b48", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số đến 10 000", "title": "Bài 48: Làm tròn số đến hàng chục, hàng trăm"},
    {"id": "t3_b49", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số đến 10 000", "title": "Bài 49: Luyện tập chung"},
    
    # Chủ đề 9: Chu vi, diện tích một số hình phẳng
    {"id": "t3_b50", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 50: Chu vi hình tam giác, hình tứ giác, hình chữ nhật, hình vuông"},
    {"id": "t3_b51", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 51: Diện tích của một hình. Xăng-ti-mét vuông"},
    {"id": "t3_b52", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 52: Diện tích hình chữ nhật, diện tích hình vuông"},
    {"id": "t3_b53", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 53: Luyện tập chung"},
    
    # Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000
    {"id": "t3_b54", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000", "title": "Bài 54: Phép cộng trong phạm vi 10 000"},
    {"id": "t3_b55", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000", "title": "Bài 55: Phép trừ trong phạm vi 10 000"},
    {"id": "t3_b56", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000", "title": "Bài 56: Nhân số có bốn chữ số với số có một chữ số"},
    {"id": "t3_b57", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000", "title": "Bài 57: Chia số có bốn chữ số cho số có một chữ số"},
    {"id": "t3_b58", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Cộng, trừ, nhân, chia trong phạm vi 10 000", "title": "Bài 58: Luyện tập chung"},
    
    # Chủ đề 11: Các số đến 100 000
    {"id": "t3_b59", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Các số đến 100 000", "title": "Bài 59: Các số có năm chữ số. Số 100 000"},
    {"id": "t3_b60", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Các số đến 100 000", "title": "Bài 60: So sánh các số trong phạm vi 100 000"},
    {"id": "t3_b61", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Các số đến 100 000", "title": "Bài 61: Làm tròn số đến hàng nghìn, hàng chục nghìn"},
    {"id": "t3_b62", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Các số đến 100 000", "title": "Bài 62: Luyện tập chung"},
    
    # Chủ đề 12: Cộng, trừ trong phạm vi 100 000
    {"id": "t3_b63", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Cộng, trừ trong phạm vi 100 000", "title": "Bài 63: Phép cộng trong phạm vi 100 000"},
    {"id": "t3_b64", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Cộng, trừ trong phạm vi 100 000", "title": "Bài 64: Phép trừ trong phạm vi 100 000"},
    {"id": "t3_b65", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Cộng, trừ trong phạm vi 100 000", "title": "Bài 65: Luyện tập chung"},
    
    # Chủ đề 13: Xem đồng hồ. Tháng - năm. Tiền Việt Nam
    {"id": "t3_b66", "grade": 3, "volume": 2, "topic_group": "Chủ đề 13: Xem đồng hồ. Tháng - năm. Tiền Việt Nam", "title": "Bài 66: Xem đồng hồ. Tháng - năm"},
    {"id": "t3_b67", "grade": 3, "volume": 2, "topic_group": "Chủ đề 13: Xem đồng hồ. Tháng - năm. Tiền Việt Nam", "title": "Bài 67: Thực hành xem đồng hồ, xem lịch"},
    {"id": "t3_b68", "grade": 3, "volume": 2, "topic_group": "Chủ đề 13: Xem đồng hồ. Tháng - năm. Tiền Việt Nam", "title": "Bài 68: Tiền Việt Nam"},
    {"id": "t3_b69", "grade": 3, "volume": 2, "topic_group": "Chủ đề 13: Xem đồng hồ. Tháng - năm. Tiền Việt Nam", "title": "Bài 69: Luyện tập chung"},
    
    # Chủ đề 14: Nhân, chia trong phạm vi 100 000
    {"id": "t3_b70", "grade": 3, "volume": 2, "topic_group": "Chủ đề 14: Nhân, chia trong phạm vi 100 000", "title": "Bài 70: Nhân số có năm chữ số với số có một chữ số"},
    {"id": "t3_b71", "grade": 3, "volume": 2, "topic_group": "Chủ đề 14: Nhân, chia trong phạm vi 100 000", "title": "Bài 71: Chia số có năm chữ số cho số có một chữ số"},
    {"id": "t3_b72", "grade": 3, "volume": 2, "topic_group": "Chủ đề 14: Nhân, chia trong phạm vi 100 000", "title": "Bài 72: Luyện tập chung"},
    
    # Chủ đề 15: Làm quen với yếu tố thống kê, xác suất
    {"id": "t3_b73", "grade": 3, "volume": 2, "topic_group": "Chủ đề 15: Làm quen với yếu tố thống kê, xác suất", "title": "Bài 73: Thu thập, phân loại, ghi chép số liệu. Bảng số liệu"},
    {"id": "t3_b74", "grade": 3, "volume": 2, "topic_group": "Chủ đề 15: Làm quen với yếu tố thống kê, xác suất", "title": "Bài 74: Khả năng xảy ra của một sự kiện"},
    {"id": "t3_b75", "grade": 3, "volume": 2, "topic_group": "Chủ đề 15: Làm quen với yếu tố thống kê, xác suất", "title": "Bài 75: Thực hành và trải nghiệm thu thập, phân loại, ghi chép số liệu, đọc bảng số liệu"},
    
    # Chủ đề 16: Ôn tập cuối năm
    {"id": "t3_b76", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 76: Ôn tập các số trong phạm vi 10 000, 100 000"},
    {"id": "t3_b77", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 77: Ôn tập phép cộng, phép trừ trong phạm vi 100 000"},
    {"id": "t3_b78", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 78: Ôn tập phép nhân, phép chia trong phạm vi 100 000"},
    {"id": "t3_b79", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 79: Ôn tập hình học, đo lường"},
    {"id": "t3_b80", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 80: Ôn tập bảng số liệu, khả năng xảy ra của một sự kiện"},
    {"id": "t3_b81", "grade": 3, "volume": 2, "topic_group": "Chủ đề 16: Ôn tập cuối năm", "title": "Bài 81: Ôn tập chung"}
]

# ==============================================================================
# TOÁN LỚP 5 (KẾT NỐI TRI THỨC VỚI CUỘC SỐNG - 12 CHỦ ĐỀ, 74 BÀI HỌC)
# ==============================================================================
MATH_GRADE_5_LESSONS = [
    # ------------------ TẬP 1 (BÀI 1 -> BÀI 35) ------------------
    # Chủ đề 1: Ôn tập và bổ sung
    {"id": "t5_b01", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 1: Ôn tập số tự nhiên"},
    {"id": "t5_b02", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 2: Ôn tập các phép tính với số tự nhiên"},
    {"id": "t5_b03", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 3: Ôn tập phân số"},
    {"id": "t5_b04", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 4: Phân số thập phân"},
    {"id": "t5_b05", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 5: Ôn tập các phép tính với phân số"},
    {"id": "t5_b06", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 6: Cộng, trừ hai phân số khác mẫu số"},
    {"id": "t5_b07", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 7: Hỗn số"},
    {"id": "t5_b08", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 8: Ôn tập hình học và đo lường"},
    {"id": "t5_b09", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 9: Luyện tập chung"},
    
    # Chủ đề 2: Số thập phân
    {"id": "t5_b10", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 10: Khái niệm số thập phân"},
    {"id": "t5_b11", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 11: So sánh các số thập phân"},
    {"id": "t5_b12", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 12: Làm tròn số thập phân"},
    {"id": "t5_b13", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 13: Viết số đo đại lượng dưới dạng số thập phân"},
    {"id": "t5_b14", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 14: Một số đơn vị đo diện tích (Héc-ta, km²)"},
    {"id": "t5_b15", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 15: Luyện tập chung"},
    
    # Chủ đề 3: Các phép tính với số thập phân
    {"id": "t5_b16", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 16: Phép cộng số thập phân"},
    {"id": "t5_b17", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 17: Phép trừ số thập phân"},
    {"id": "t5_b18", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 18: Luyện tập chung"},
    {"id": "t5_b19", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 19: Phép nhân số thập phân với số tự nhiên"},
    {"id": "t5_b20", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 20: Phép nhân số thập phân với số thập phân"},
    {"id": "t5_b21", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 21: Phép chia số thập phân cho số tự nhiên"},
    {"id": "t5_b22", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 22: Phép chia một số tự nhiên cho một số thập phân"},
    {"id": "t5_b23", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 23: Phép chia một số thập phân cho một số thập phân"},
    {"id": "t5_b24", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Các phép tính với số thập phân", "title": "Bài 24: Luyện tập chung"},
    
    # Chủ đề 4: Hình phẳng (Tam giác, Thang, Tròn)
    {"id": "t5_b25", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng", "title": "Bài 25: Hình tam giác. Diện tích hình tam giác"},
    {"id": "t5_b26", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng", "title": "Bài 26: Hình thang. Diện tích hình thang"},
    {"id": "t5_b27", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng", "title": "Bài 27: Đường tròn. Chu vi và diện tích hình tròn"},
    {"id": "t5_b28", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng", "title": "Bài 28: Thực hành và trải nghiệm vẽ hình, cắt ghép hình phẳng"},
    {"id": "t5_b29", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng", "title": "Bài 29: Luyện tập chung"},
    
    # Chủ đề 5: Ôn tập học kì 1
    {"id": "t5_b30", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 30: Ôn tập số thập phân"},
    {"id": "t5_b31", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 31: Ôn tập các phép tính với số thập phân"},
    {"id": "t5_b32", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 32: Ôn tập hình học và đo lường"},
    {"id": "t5_b33", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 33: Ôn tập giải toán có lời văn"},
    {"id": "t5_b34", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 34: Luyện tập chung"},
    {"id": "t5_b35", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì 1", "title": "Bài 35: Ôn tập học kì 1 tổng hợp"},

    # ------------------ TẬP 2 (BÀI 36 -> BÀI 74) ------------------
    # Chủ đề 6: Tỉ số và tỉ số phần trăm
    {"id": "t5_b36", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 36: Tỉ số. Tìm hai số khi biết tổng và tỉ số"},
    {"id": "t5_b37", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 37: Tìm hai số khi biết hiệu và tỉ số"},
    {"id": "t5_b38", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 38: Tìm tỉ số phần trăm của hai số"},
    {"id": "t5_b39", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 39: Tìm giá trị phần trăm của một số"},
    {"id": "t5_b40", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 40: Tỉ lệ bản đồ và ứng dụng thực tế"},
    {"id": "t5_b41", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và các bài toán liên quan", "title": "Bài 41: Luyện tập chung"},
    
    # Chủ đề 7: Thể tích. Một số đơn vị đo thể tích
    {"id": "t5_b42", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 42: Khái niệm thể tích. Xăng-ti-mét khối (cm³), Đề-xi-mét khối (dm³)"},
    {"id": "t5_b43", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 43: Mét khối (m³)"},
    {"id": "t5_b44", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 44: Hình hộp chữ nhật, hình lập phương"},
    {"id": "t5_b45", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 45: Diện tích xung quanh và diện tích toàn phần hình hộp chữ nhật"},
    {"id": "t5_b46", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 46: Diện tích xung quanh và diện tích toàn phần hình lập phương"},
    {"id": "t5_b47", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 47: Thể tích hình hộp chữ nhật, hình lập phương"},
    {"id": "t5_b48", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 48: Làm quen với hình trụ, hình cầu"},
    {"id": "t5_b49", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích & Hình khối", "title": "Bài 49: Luyện tập chung"},
    
    # Chủ đề 8: Số đo thời gian & Toán chuyển động đều
    {"id": "t5_b50", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 50: Các đơn vị đo thời gian. Cộng, trừ số đo thời gian"},
    {"id": "t5_b51", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 51: Nhân, chia số đo thời gian với một số"},
    {"id": "t5_b52", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 52: Vận tốc trong chuyển động đều"},
    {"id": "t5_b53", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 53: Quãng đường trong chuyển động đều"},
    {"id": "t5_b54", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 54: Thời gian trong chuyển động đều"},
    {"id": "t5_b55", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 55: Bài toán chuyển động ngược chiều và cùng chiều"},
    {"id": "t5_b56", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 56: Luyện tập chung"},
    
    # Chủ đề 9: Một số yếu tố thống kê và xác suất
    {"id": "t5_b57", "grade": 5, "volume": 2, "topic_group": "Chủ đề 9: Thống kê & Xác suất", "title": "Bài 57: Thu thập, phân loại, sắp xếp số liệu. Biểu đồ hình quạt tròn"},
    {"id": "t5_b58", "grade": 5, "volume": 2, "topic_group": "Chủ đề 9: Thống kê & Xác suất", "title": "Bài 58: Mô tả xác suất của sự kiện"},
    {"id": "t5_b59", "grade": 5, "volume": 2, "topic_group": "Chủ đề 9: Thống kê & Xác suất", "title": "Bài 59: Luyện tập chung"},
    
    # Chủ đề 10: Ôn tập cuối năm
    {"id": "t5_b60", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 60: Ôn tập số tự nhiên, phân số, số thập phân"},
    {"id": "t5_b61", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 61: Ôn tập các phép tính với số tự nhiên, phân số, số thập phân"},
    {"id": "t5_b62", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 62: Ôn tập tỉ số, tỉ số phần trăm"},
    {"id": "t5_b63", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 63: Ôn tập hình học"},
    {"id": "t5_b64", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 64: Ôn tập đo lường và toán chuyển động đều"},
    {"id": "t5_b65", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 65: Ôn tập thống kê và xác suất"},
    {"id": "t5_b66", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 66: Ôn tập chung cuối năm"}
]

def get_math_lessons(grade: int, volume: int = 0) -> List[Dict[str, Any]]:
    """
    Lấy danh sách bài học môn Toán theo Khối lớp (3 hoặc 5) và Tập (1, 2 hoặc 0 là cả năm).
    """
    if grade == 3:
        lessons = MATH_GRADE_3_LESSONS
    elif grade == 5:
        lessons = MATH_GRADE_5_LESSONS
    else:
        return []
        
    if volume in [1, 2]:
        return [l for l in lessons if l["volume"] == volume]
    return lessons
