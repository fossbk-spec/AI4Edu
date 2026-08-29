"""
Danh mục phân phối chương trình chi tiết môn Toán Lớp 3 và Lớp 5 (Tập 1 và Tập 2)
Theo chuẩn Chương trình Giáo dục Phổ thông 2018 (Bộ sách Kết nối tri thức với cuộc sống & Cánh Diều).
"""

from typing import List, Dict, Any

MATH_GRADE_3_LESSONS = [
    # TẬP 1
    {"id": "t3_b01", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 1: Ôn tập các số đến 1 000"},
    {"id": "t3_b02", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 2: Ôn tập phép cộng, phép trừ trong phạm vi 1 000"},
    {"id": "t3_b03", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 3: Tìm thành phần trong phép cộng, phép trừ"},
    {"id": "t3_b04", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 4: Ôn tập bảng nhân 2; 5, bảng chia 2; 5"},
    {"id": "t3_b05", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 5: Bảng nhân 3, bảng chia 3"},
    {"id": "t3_b06", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 6: Bảng nhân 4, bảng chia 4"},
    {"id": "t3_b07", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 7: Ôn tập hình học và đo lường"},
    {"id": "t3_b08", "grade": 3, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 8: Luyện tập chung"},
    {"id": "t3_b09", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 9: Bảng nhân 6, bảng chia 6"},
    {"id": "t3_b10", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 10: Bảng nhân 7, bảng chia 7"},
    {"id": "t3_b11", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 11: Bảng nhân 8, bảng chia 8"},
    {"id": "t3_b12", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 12: Bảng nhân 9, bảng chia 9"},
    {"id": "t3_b13", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 13: Tìm thành phần trong phép nhân, phép chia"},
    {"id": "t3_b14", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 14: Một phần mấy (1/2, 1/3, 1/4, 1/5...)"},
    {"id": "t3_b15", "grade": 3, "volume": 1, "topic_group": "Chủ đề 2: Bảng nhân, bảng chia", "title": "Bài 15: Luyện tập chung"},
    {"id": "t3_b16", "grade": 3, "volume": 1, "topic_group": "Chủ đề 3: Làm quen hình phẳng, hình khối", "title": "Bài 16: Điểm ở giữa, trung điểm của đoạn thẳng"},
    {"id": "t3_b17", "grade": 3, "volume": 1, "topic_group": "Chủ đề 3: Làm quen hình phẳng, hình khối", "title": "Bài 17: Hình tròn. Tâm, bán kính, đường kính"},
    {"id": "t3_b18", "grade": 3, "volume": 1, "topic_group": "Chủ đề 3: Làm quen hình phẳng, hình khối", "title": "Bài 18: Góc, góc vuông, góc không vuông"},
    {"id": "t3_b19", "grade": 3, "volume": 1, "topic_group": "Chủ đề 3: Làm quen hình phẳng, hình khối", "title": "Bài 19: Hình tam giác, hình tứ giác. Hình chữ nhật, hình vuông"},
    {"id": "t3_b20", "grade": 3, "volume": 1, "topic_group": "Chủ đề 3: Làm quen hình phẳng, hình khối", "title": "Bài 20: Khối lập phương, khối hộp chữ nhật"},
    {"id": "t3_b21", "grade": 3, "volume": 1, "topic_group": "Chủ đề 4: Phép nhân, chia trong phạm vi 100", "title": "Bài 21: Gấp một số lên một số lần"},
    {"id": "t3_b22", "grade": 3, "volume": 1, "topic_group": "Chủ đề 4: Phép nhân, chia trong phạm vi 100", "title": "Bài 22: Giảm một số đi một số lần"},
    {"id": "t3_b23", "grade": 3, "volume": 1, "topic_group": "Chủ đề 4: Phép nhân, chia trong phạm vi 100", "title": "Bài 23: Nhân số có hai chữ số với số có một chữ số"},
    {"id": "t3_b24", "grade": 3, "volume": 1, "topic_group": "Chủ đề 4: Phép nhân, chia trong phạm vi 100", "title": "Bài 24: Chia số có hai chữ số cho số có một chữ số"},
    {"id": "t3_b25", "grade": 3, "volume": 1, "topic_group": "Chủ đề 4: Phép nhân, chia trong phạm vi 100", "title": "Bài 25: Phép chia hết và phép chia có dư"},
    {"id": "t3_b26", "grade": 3, "volume": 1, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích", "title": "Bài 26: Mi-li-mét (mm)"},
    {"id": "t3_b27", "grade": 3, "volume": 1, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích", "title": "Bài 27: Gam (g)"},
    {"id": "t3_b28", "grade": 3, "volume": 1, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích", "title": "Bài 28: Mi-li-lít (ml)"},
    {"id": "t3_b29", "grade": 3, "volume": 1, "topic_group": "Chủ đề 5: Đơn vị đo độ dài, khối lượng, dung tích", "title": "Bài 29: Nhiệt độ. Đo nhiệt độ bằng nhiệt kế"},
    {"id": "t3_b30", "grade": 3, "volume": 1, "topic_group": "Chủ đề 6: Phép nhân, chia trong phạm vi 1 000", "title": "Bài 30: Nhân số có ba chữ số với số có một chữ số"},
    {"id": "t3_b31", "grade": 3, "volume": 1, "topic_group": "Chủ đề 6: Phép nhân, chia trong phạm vi 1 000", "title": "Bài 31: Chia số có ba chữ số cho số có một chữ số"},
    {"id": "t3_b32", "grade": 3, "volume": 1, "topic_group": "Chủ đề 7: Ôn tập học kì I", "title": "Bài 32: Ôn tập biểu thức số và tính giá trị của biểu thức"},
    {"id": "t3_b33", "grade": 3, "volume": 1, "topic_group": "Chủ đề 7: Ôn tập học kì I", "title": "Bài 33: Ôn tập học kì I tổng hợp"},

    # TẬP 2
    {"id": "t3_b34", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số có bốn chữ số", "title": "Bài 34: Các số có bốn chữ số. Số 10 000"},
    {"id": "t3_b35", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số có bốn chữ số", "title": "Bài 35: So sánh các số có bốn chữ số"},
    {"id": "t3_b36", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số có bốn chữ số", "title": "Bài 36: Làm quen với chữ số La Mã"},
    {"id": "t3_b37", "grade": 3, "volume": 2, "topic_group": "Chủ đề 8: Các số có bốn chữ số", "title": "Bài 37: Làm tròn số đến hàng chục, hàng trăm"},
    {"id": "t3_b38", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 38: Chu vi hình tam giác, hình tứ giác"},
    {"id": "t3_b39", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 39: Chu vi hình chữ nhật, hình vuông"},
    {"id": "t3_b40", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 40: Diện tích của một hình. Xăng-ti-mét vuông (cm²)"},
    {"id": "t3_b41", "grade": 3, "volume": 2, "topic_group": "Chủ đề 9: Chu vi, diện tích một số hình phẳng", "title": "Bài 41: Diện tích hình chữ nhật, diện tích hình vuông"},
    {"id": "t3_b42", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Phép tính trong phạm vi 10 000", "title": "Bài 42: Phép cộng trong phạm vi 10 000"},
    {"id": "t3_b43", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Phép tính trong phạm vi 10 000", "title": "Bài 43: Phép trừ trong phạm vi 10 000"},
    {"id": "t3_b44", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Phép tính trong phạm vi 10 000", "title": "Bài 44: Phép nhân số có bốn chữ số với số có một chữ số"},
    {"id": "t3_b45", "grade": 3, "volume": 2, "topic_group": "Chủ đề 10: Phép tính trong phạm vi 10 000", "title": "Bài 45: Phép chia số có bốn chữ số cho số có một chữ số"},
    {"id": "t3_b46", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Thời gian, Tiền Việt Nam", "title": "Bài 46: Tháng - Năm. Xem lịch và đồng hồ"},
    {"id": "t3_b47", "grade": 3, "volume": 2, "topic_group": "Chủ đề 11: Thời gian, Tiền Việt Nam", "title": "Bài 47: Tiền Việt Nam"},
    {"id": "t3_b48", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Các số có năm chữ số", "title": "Bài 48: Các số có năm chữ số. Số 100 000"},
    {"id": "t3_b49", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Các số có năm chữ số", "title": "Bài 49: Phép cộng, phép trừ trong phạm vi 100 000"},
    {"id": "t3_b50", "grade": 3, "volume": 2, "topic_group": "Chủ đề 12: Các số có năm chữ số", "title": "Bài 50: Phép nhân, phép chia trong phạm vi 100 000"},
    {"id": "t3_b51", "grade": 3, "volume": 2, "topic_group": "Chủ đề 13: Thống kê & Xác suất", "title": "Bài 51: Bảng số liệu thống kê. Khả năng xảy ra của một sự kiện"},
    {"id": "t3_b52", "grade": 3, "volume": 2, "topic_group": "Chủ đề 14: Ôn tập cuối năm", "title": "Bài 52: Ôn tập phép tính và giải toán có lời văn"},
    {"id": "t3_b53", "grade": 3, "volume": 2, "topic_group": "Chủ đề 14: Ôn tập cuối năm", "title": "Bài 53: Ôn tập hình học, đo lường và ôn tập chung cuối năm"},
]

MATH_GRADE_5_LESSONS = [
    # TẬP 1
    {"id": "t5_b01", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 1: Ôn tập số tự nhiên"},
    {"id": "t5_b02", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 2: Ôn tập các phép tính với số tự nhiên"},
    {"id": "t5_b03", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 3: Ôn tập phân số và tính chất cơ bản của phân số"},
    {"id": "t5_b04", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 4: Phân số thập phân"},
    {"id": "t5_b05", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 5: Ôn tập các phép tính với phân số"},
    {"id": "t5_b06", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 6: Cộng, trừ hai phân số khác mẫu số"},
    {"id": "t5_b07", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 7: Hỗn số"},
    {"id": "t5_b08", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 8: Ôn tập hình học và đo lường"},
    {"id": "t5_b09", "grade": 5, "volume": 1, "topic_group": "Chủ đề 1: Ôn tập và bổ sung", "title": "Bài 9: Luyện tập chung"},
    {"id": "t5_b10", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 10: Khái niệm số thập phân. Hàng của số thập phân"},
    {"id": "t5_b11", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 11: So sánh các số thập phân"},
    {"id": "t5_b12", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 12: Làm tròn số thập phân"},
    {"id": "t5_b13", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 13: Viết số đo đại lượng dưới dạng số thập phân"},
    {"id": "t5_b14", "grade": 5, "volume": 1, "topic_group": "Chủ đề 2: Số thập phân", "title": "Bài 14: Đơn vị đo diện tích: Héc-ta (ha), Ki-lô-mét vuông (km²)"},
    {"id": "t5_b15", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 15: Phép cộng số thập phân"},
    {"id": "t5_b16", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 16: Phép trừ số thập phân"},
    {"id": "t5_b17", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 17: Phép nhân số thập phân với số tự nhiên"},
    {"id": "t5_b18", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 18: Phép nhân số thập phân với số thập phân"},
    {"id": "t5_b19", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 19: Phép chia số thập phân cho số tự nhiên"},
    {"id": "t5_b20", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 20: Phép chia một số tự nhiên cho một số thập phân"},
    {"id": "t5_b21", "grade": 5, "volume": 1, "topic_group": "Chủ đề 3: Phép tính với số thập phân", "title": "Bài 21: Phép chia một số thập phân cho một số thập phân"},
    {"id": "t5_b22", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng (Tam giác, Thang, Tròn)", "title": "Bài 22: Hình tam giác. Diện tích hình tam giác"},
    {"id": "t5_b23", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng (Tam giác, Thang, Tròn)", "title": "Bài 23: Hình thang. Diện tích hình thang"},
    {"id": "t5_b24", "grade": 5, "volume": 1, "topic_group": "Chủ đề 4: Hình phẳng (Tam giác, Thang, Tròn)", "title": "Bài 24: Chu vi và diện tích hình tròn"},
    {"id": "t5_b25", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì I", "title": "Bài 25: Ôn tập số thập phân và các phép tính"},
    {"id": "t5_b26", "grade": 5, "volume": 1, "topic_group": "Chủ đề 5: Ôn tập học kì I", "title": "Bài 26: Ôn tập hình học, đo lường và giải toán học kì I"},

    # TẬP 2
    {"id": "t5_b27", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và tỉ số phần trăm", "title": "Bài 27: Tỉ số. Tìm hai số khi biết tổng/hiệu và tỉ số"},
    {"id": "t5_b28", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và tỉ số phần trăm", "title": "Bài 28: Tỉ số phần trăm. Tìm tỉ số phần trăm của hai số"},
    {"id": "t5_b29", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và tỉ số phần trăm", "title": "Bài 29: Tìm giá trị phần trăm của một số"},
    {"id": "t5_b30", "grade": 5, "volume": 2, "topic_group": "Chủ đề 6: Tỉ số và tỉ số phần trăm", "title": "Bài 30: Tỉ lệ bản đồ và ứng dụng thực tế"},
    {"id": "t5_b31", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 31: Khái niệm thể tích. Xăng-ti-mét khối (cm³), Đề-xi-mét khối (dm³)"},
    {"id": "t5_b32", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 32: Mét khối (m³)"},
    {"id": "t5_b33", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 33: Hình hộp chữ nhật, hình lập phương"},
    {"id": "t5_b34", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 34: Diện tích xung quanh và diện tích toàn phần hình hộp chữ nhật"},
    {"id": "t5_b35", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 35: Diện tích xung quanh và diện tích toàn phần hình lập phương"},
    {"id": "t5_b36", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 36: Thể tích hình hộp chữ nhật, thể tích hình lập phương"},
    {"id": "t5_b37", "grade": 5, "volume": 2, "topic_group": "Chủ đề 7: Thể tích. Hình khối", "title": "Bài 37: Làm quen với hình trụ, hình cầu"},
    {"id": "t5_b38", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 38: Các đơn vị đo thời gian. Cộng, trừ số đo thời gian"},
    {"id": "t5_b39", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 39: Nhân, chia số đo thời gian với một số"},
    {"id": "t5_b40", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 40: Vận tốc trong chuyển động đều"},
    {"id": "t5_b41", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 41: Quãng đường trong chuyển động đều"},
    {"id": "t5_b42", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 42: Thời gian trong chuyển động đều"},
    {"id": "t5_b43", "grade": 5, "volume": 2, "topic_group": "Chủ đề 8: Thời gian & Toán chuyển động đều", "title": "Bài 43: Bài toán chuyển động ngược chiều và cùng chiều"},
    {"id": "t5_b44", "grade": 5, "volume": 2, "topic_group": "Chủ đề 9: Thống kê & Xác suất", "title": "Bài 44: Thu thập, phân loại, sắp xếp số liệu. Biểu đồ hình quạt tròn"},
    {"id": "t5_b45", "grade": 5, "volume": 2, "topic_group": "Chủ đề 9: Thống kê & Xác suất", "title": "Bài 45: Mô tả xác suất của sự kiện"},
    {"id": "t5_b46", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 46: Ôn tập số tự nhiên, phân số, số thập phân"},
    {"id": "t5_b47", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 47: Ôn tập các phép tính và giải toán thực tế"},
    {"id": "t5_b48", "grade": 5, "volume": 2, "topic_group": "Chủ đề 10: Ôn tập cuối năm", "title": "Bài 48: Ôn tập hình học, đo lường và ôn tập tổng kết K-5"},
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
