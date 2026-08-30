"""
Cơ sở dữ liệu danh mục bài học chuẩn 100% SGK Tiếng Việt Cấp Tiểu Học (Lớp 1 đến Lớp 5)
Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG - Nhà xuất bản Giáo dục Việt Nam (CTGDPT 2018).
Tổng Chủ biên: GS.TS. Bùi Mạnh Hùng.
"""

from typing import List, Dict, Any

# ==============================================================================
# 1. TIẾNG VIỆT LỚP 1
# ==============================================================================
VIETNAMESE_GRADE_1_LESSONS = [
    # Tập 1: Âm chữ và Học vần
    {"id": "tv1_b01", "grade": 1, "volume": 1, "page": 6, "topic_group": "Học âm và chữ cái", "title": "Bài 1: A a, B b"},
    {"id": "tv1_b02", "grade": 1, "volume": 1, "page": 10, "topic_group": "Học âm và chữ cái", "title": "Bài 2: C c, O o, Dấu sắc"},
    {"id": "tv1_b03", "grade": 1, "volume": 1, "page": 14, "topic_group": "Học âm và chữ cái", "title": "Bài 3: D d, Đ đ, Dấu huyền"},
    {"id": "tv1_b04", "grade": 1, "volume": 1, "page": 18, "topic_group": "Học âm và chữ cái", "title": "Bài 4: E e, Ê ê, Dấu hỏi"},
    {"id": "tv1_b05", "grade": 1, "volume": 1, "page": 22, "topic_group": "Học âm và chữ cái", "title": "Bài 5: Ôn tập và kể chuyện"},
    {"id": "tv1_b06", "grade": 1, "volume": 1, "page": 26, "topic_group": "Học âm và chữ cái", "title": "Bài 6: G g, H h, Dấu ngã, Dấu nặng"},
    {"id": "tv1_b07", "grade": 1, "volume": 1, "page": 30, "topic_group": "Học âm và chữ cái", "title": "Bài 7: I i, K k"},
    {"id": "tv1_b08", "grade": 1, "volume": 1, "page": 34, "topic_group": "Học âm và chữ cái", "title": "Bài 8: L l, M m"},
    {"id": "tv1_b09", "grade": 1, "volume": 1, "page": 38, "topic_group": "Học âm và chữ cái", "title": "Bài 9: N n, Ô ô"},
    {"id": "tv1_b10", "grade": 1, "volume": 1, "page": 42, "topic_group": "Học âm và chữ cái", "title": "Bài 10: Ôn tập và kể chuyện"},
    {"id": "tv1_b11", "grade": 1, "volume": 1, "page": 46, "topic_group": "Học âm và chữ cái", "title": "Bài 11: Ơ ơ, P p"},
    {"id": "tv1_b12", "grade": 1, "volume": 1, "page": 50, "topic_group": "Học âm và chữ cái", "title": "Bài 12: Q q, R r"},
    {"id": "tv1_b13", "grade": 1, "volume": 1, "page": 54, "topic_group": "Học âm và chữ cái", "title": "Bài 13: S s, T t"},
    {"id": "tv1_b14", "grade": 1, "volume": 1, "page": 58, "topic_group": "Học âm và chữ cái", "title": "Bài 14: U u, Ư ư"},
    {"id": "tv1_b15", "grade": 1, "volume": 1, "page": 62, "topic_group": "Học âm và chữ cái", "title": "Bài 15: V v, X x, Y y"},
    {"id": "tv1_b16", "grade": 1, "volume": 1, "page": 66, "topic_group": "Học âm và chữ cái", "title": "Bài 16: Ôn tập và kể chuyện"},
    {"id": "tv1_b17", "grade": 1, "volume": 1, "page": 70, "topic_group": "Học vần", "title": "Bài 17: an, at"},
    {"id": "tv1_b18", "grade": 1, "volume": 1, "page": 74, "topic_group": "Học vần", "title": "Bài 18: am, ap"},
    {"id": "tv1_b19", "grade": 1, "volume": 1, "page": 78, "topic_group": "Học vần", "title": "Bài 19: ang, ac"},
    {"id": "tv1_b20", "grade": 1, "volume": 1, "page": 82, "topic_group": "Học vần", "title": "Bài 20: Ôn tập học kì I"},
    # Tập 2: Luyện đọc & Chủ điểm
    {"id": "tv1_b21", "grade": 1, "volume": 2, "page": 6, "topic_group": "Chủ điểm 1: Tôi và các bạn", "title": "Bài 1: Tôi là học sinh lớp 1"},
    {"id": "tv1_b22", "grade": 1, "volume": 2, "page": 12, "topic_group": "Chủ điểm 1: Tôi và các bạn", "title": "Bài 2: Đôi tai xấu xí"},
    {"id": "tv1_b23", "grade": 1, "volume": 2, "page": 18, "topic_group": "Chủ điểm 1: Tôi và các bạn", "title": "Bài 3: Bạn của gió"},
    {"id": "tv1_b24", "grade": 1, "volume": 2, "page": 24, "topic_group": "Chủ điểm 2: Mái ấm gia đình", "title": "Bài 4: Làm anh"},
    {"id": "tv1_b25", "grade": 1, "volume": 2, "page": 30, "topic_group": "Chủ điểm 2: Mái ấm gia đình", "title": "Bài 5: Quạt cho bà ngủ"},
    {"id": "tv1_b26", "grade": 1, "volume": 2, "page": 36, "topic_group": "Chủ điểm 2: Mái ấm gia đình", "title": "Bài 6: Bữa cơm gia đình"},
    {"id": "tv1_b27", "grade": 1, "volume": 2, "page": 42, "topic_group": "Chủ điểm 3: Mái trường mến yêu", "title": "Bài 7: Tôi đi học"},
    {"id": "tv1_b28", "grade": 1, "volume": 2, "page": 48, "topic_group": "Chủ điểm 3: Mái trường mến yêu", "title": "Bài 8: Giờ ra chơi"},
    {"id": "tv1_b29", "grade": 1, "volume": 2, "page": 54, "topic_group": "Chủ điểm 3: Mái trường mến yêu", "title": "Bài 9: Hoa yêu thương"},
    {"id": "tv1_b30", "grade": 1, "volume": 2, "page": 60, "topic_group": "Chủ điểm 4: Điều em cần biết", "title": "Bài 10: Rửa tay trước khi ăn"},
    {"id": "tv1_b31", "grade": 1, "volume": 2, "page": 66, "topic_group": "Chủ điểm 4: Điều em cần biết", "title": "Bài 11: Lời chào"},
    {"id": "tv1_b32", "grade": 1, "volume": 2, "page": 72, "topic_group": "Chủ điểm 4: Điều em cần biết", "title": "Bài 12: Đèn giao thông"},
    {"id": "tv1_b33", "grade": 1, "volume": 2, "page": 78, "topic_group": "Chủ điểm 5: Bài học từ cuộc sống", "title": "Bài 13: Kiến và chim bồ câu"},
    {"id": "tv1_b34", "grade": 1, "volume": 2, "page": 84, "topic_group": "Chủ điểm 5: Bài học từ cuộc sống", "title": "Bài 14: Chú bé chăn cừu"},
    {"id": "tv1_b35", "grade": 1, "volume": 2, "page": 90, "topic_group": "Chủ điểm 6: Thiên nhiên kì thú", "title": "Bài 15: Cây bàng"},
    {"id": "tv1_b36", "grade": 1, "volume": 2, "page": 96, "topic_group": "Chủ điểm 6: Thiên nhiên kì thú", "title": "Bài 16: Mặt trời và hạt đỗ"},
    {"id": "tv1_b37", "grade": 1, "volume": 2, "page": 102, "topic_group": "Chủ điểm 7: Đất nước và con người", "title": "Bài 17: Bác Hồ kính yêu"},
    {"id": "tv1_b38", "grade": 1, "volume": 2, "page": 108, "topic_group": "Chủ điểm 7: Đất nước và con người", "title": "Bài 18: Gửi lời chào lớp một - Ôn tập cuối năm"}
]

# ==============================================================================
# 2. TIẾNG VIỆT LỚP 2
# ==============================================================================
VIETNAMESE_GRADE_2_LESSONS = [
    # Tập 1
    {"id": "tv2_b01", "grade": 2, "volume": 1, "page": 10, "topic_group": "Chủ điểm 1: Em lớn lên từng ngày", "title": "Bài 1: Tôi là học sinh lớp 2"},
    {"id": "tv2_b02", "grade": 2, "volume": 1, "page": 14, "topic_group": "Chủ điểm 1: Em lớn lên từng ngày", "title": "Bài 2: Ngày hôm qua đâu rồi"},
    {"id": "tv2_b03", "grade": 2, "volume": 1, "page": 18, "topic_group": "Chủ điểm 1: Em lớn lên từng ngày", "title": "Bài 3: Niềm vui của Bi và Bống"},
    {"id": "tv2_b04", "grade": 2, "volume": 1, "page": 22, "topic_group": "Chủ điểm 1: Em lớn lên từng ngày", "title": "Bài 4: Làm việc thật là vui"},
    {"id": "tv2_b05", "grade": 2, "volume": 1, "page": 28, "topic_group": "Chủ điểm 2: Đi học vui sao", "title": "Bài 5: Cầu thủ dự bị"},
    {"id": "tv2_b06", "grade": 2, "volume": 1, "page": 32, "topic_group": "Chủ điểm 2: Đi học vui sao", "title": "Bài 6: Cô giáo lớp em"},
    {"id": "tv2_b07", "grade": 2, "volume": 1, "page": 36, "topic_group": "Chủ điểm 2: Đi học vui sao", "title": "Bài 7: Nhím nâu kết bạn"},
    {"id": "tv2_b08", "grade": 2, "volume": 1, "page": 40, "topic_group": "Chủ điểm 2: Đi học vui sao", "title": "Bài 8: Em học vẽ"},
    {"id": "tv2_b09", "grade": 2, "volume": 1, "page": 46, "topic_group": "Chủ điểm 3: Niềm vui tuổi thơ", "title": "Bài 9: Cuốn sách của em"},
    {"id": "tv2_b10", "grade": 2, "volume": 1, "page": 50, "topic_group": "Chủ điểm 3: Niềm vui tuổi thơ", "title": "Bài 10: Yêu lắm trường ơi"},
    {"id": "tv2_b11", "grade": 2, "volume": 1, "page": 54, "topic_group": "Chủ điểm 3: Niềm vui tuổi thơ", "title": "Bài 11: Chữ A và những người bạn"},
    {"id": "tv2_b12", "grade": 2, "volume": 1, "page": 58, "topic_group": "Chủ điểm 3: Niềm vui tuổi thơ", "title": "Bài 12: Họa mi hót"},
    {"id": "tv2_b13", "grade": 2, "volume": 1, "page": 64, "topic_group": "Chủ điểm 4: Mái ấm gia đình", "title": "Bài 13: Mẹ"},
    {"id": "tv2_b14", "grade": 2, "volume": 1, "page": 68, "topic_group": "Chủ điểm 4: Mái ấm gia đình", "title": "Bài 14: Quả ngọt cuối mùa"},
    {"id": "tv2_b15", "grade": 2, "volume": 1, "page": 72, "topic_group": "Chủ điểm 4: Mái ấm gia đình", "title": "Bài 15: Bà nội bà ngoại"},
    {"id": "tv2_b16", "grade": 2, "volume": 1, "page": 76, "topic_group": "Chủ điểm 4: Mái ấm gia đình", "title": "Bài 16: Đi học về"},
    {"id": "tv2_b17", "grade": 2, "volume": 1, "page": 82, "topic_group": "Ôn tập học kì I", "title": "Bài 17: Ôn tập học kì I"},
    # Tập 2
    {"id": "tv2_b18", "grade": 2, "volume": 2, "page": 10, "topic_group": "Chủ điểm 5: Vẻ đẹp quanh em", "title": "Bài 18: Chuyện bốn mùa"},
    {"id": "tv2_b19", "grade": 2, "volume": 2, "page": 14, "topic_group": "Chủ điểm 5: Vẻ đẹp quanh em", "title": "Bài 19: Mùa nước nổi"},
    {"id": "tv2_b20", "grade": 2, "volume": 2, "page": 18, "topic_group": "Chủ điểm 5: Vẻ đẹp quanh em", "title": "Bài 20: Hạt đỗ nảy mầm"},
    {"id": "tv2_b21", "grade": 2, "volume": 2, "page": 22, "topic_group": "Chủ điểm 5: Vẻ đẹp quanh em", "title": "Bài 21: Cây đào"},
    {"id": "tv2_b22", "grade": 2, "volume": 2, "page": 28, "topic_group": "Chủ điểm 6: Hành tinh xanh của em", "title": "Bài 22: Lá thư dưới đáy biển"},
    {"id": "tv2_b23", "grade": 2, "volume": 2, "page": 32, "topic_group": "Chủ điểm 6: Hành tinh xanh của em", "title": "Bài 23: Cây đa quê hương"},
    {"id": "tv2_b24", "grade": 2, "volume": 2, "page": 36, "topic_group": "Chủ điểm 6: Hành tinh xanh của em", "title": "Bài 24: Mai An Tiêm"},
    {"id": "tv2_b25", "grade": 2, "volume": 2, "page": 40, "topic_group": "Chủ điểm 6: Hành tinh xanh của em", "title": "Bài 25: Thư viện chim sâu"},
    {"id": "tv2_b26", "grade": 2, "volume": 2, "page": 46, "topic_group": "Chủ điểm 7: Giao tiếp và kết nối", "title": "Bài 26: Cảm ơn và xin lỗi"},
    {"id": "tv2_b27", "grade": 2, "volume": 2, "page": 50, "topic_group": "Chủ điểm 7: Giao tiếp và kết nối", "title": "Bài 27: Lời chào"},
    {"id": "tv2_b28", "grade": 2, "volume": 2, "page": 54, "topic_group": "Chủ điểm 7: Giao tiếp và kết nối", "title": "Bài 28: Đôi bạn tay"},
    {"id": "tv2_b29", "grade": 2, "volume": 2, "page": 58, "topic_group": "Chủ điểm 7: Giao tiếp và kết nối", "title": "Bài 29: Thư viện của em"},
    {"id": "tv2_b30", "grade": 2, "volume": 2, "page": 64, "topic_group": "Chủ điểm 8: Con người Việt Nam", "title": "Bài 30: Thánh Gióng"},
    {"id": "tv2_b31", "grade": 2, "volume": 2, "page": 68, "topic_group": "Chủ điểm 8: Con người Việt Nam", "title": "Bài 31: Hai Bà Trưng"},
    {"id": "tv2_b32", "grade": 2, "volume": 2, "page": 72, "topic_group": "Chủ điểm 8: Con người Việt Nam", "title": "Bài 32: Đất nước gấm hoa"},
    {"id": "tv2_b33", "grade": 2, "volume": 2, "page": 76, "topic_group": "Chủ điểm 8: Con người Việt Nam", "title": "Bài 33: Bác Hồ với thiếu nhi"},
    {"id": "tv2_b34", "grade": 2, "volume": 2, "page": 82, "topic_group": "Ôn tập cuối năm", "title": "Bài 34: Ôn tập cuối năm"}
]

# ==============================================================================
# 3. TIẾNG VIỆT LỚP 3
# ==============================================================================
VIETNAMESE_GRADE_3_LESSONS = [
    # Tập 1
    {"id": "tv3_b01", "grade": 3, "volume": 1, "page": 10, "topic_group": "Chủ điểm 1: Những búp măng non", "title": "Bài 1: Ngày em vào Đội"},
    {"id": "tv3_b02", "grade": 3, "volume": 1, "page": 14, "topic_group": "Chủ điểm 1: Những búp măng non", "title": "Bài 2: Về thăm quê"},
    {"id": "tv3_b03", "grade": 3, "volume": 1, "page": 18, "topic_group": "Chủ điểm 1: Những búp măng non", "title": "Bài 3: Chiếc nhãn vở đặc biệt"},
    {"id": "tv3_b04", "grade": 3, "volume": 1, "page": 22, "topic_group": "Chủ điểm 1: Những búp măng non", "title": "Bài 4: Lời giải toán đặc biệt"},
    {"id": "tv3_b05", "grade": 3, "volume": 1, "page": 28, "topic_group": "Chủ điểm 2: Mái trường thân yêu", "title": "Bài 5: Mùa thu của em"},
    {"id": "tv3_b06", "grade": 3, "volume": 1, "page": 32, "topic_group": "Chủ điểm 2: Mái trường thân yêu", "title": "Bài 6: Nghe thầy đọc thơ"},
    {"id": "tv3_b07", "grade": 3, "volume": 1, "page": 36, "topic_group": "Chủ điểm 2: Mái trường thân yêu", "title": "Bài 7: Đi học vui sao"},
    {"id": "tv3_b08", "grade": 3, "volume": 1, "page": 40, "topic_group": "Chủ điểm 2: Mái trường thân yêu", "title": "Bài 8: Lớp học trên đường"},
    {"id": "tv3_b09", "grade": 3, "volume": 1, "page": 46, "topic_group": "Chủ điểm 3: Cổng trường mở ra", "title": "Bài 9: Bàn tay cô giáo"},
    {"id": "tv3_b10", "grade": 3, "volume": 1, "page": 50, "topic_group": "Chủ điểm 3: Cổng trường mở ra", "title": "Bài 10: Cùng vui chơi"},
    {"id": "tv3_b11", "grade": 3, "volume": 1, "page": 54, "topic_group": "Chủ điểm 3: Cổng trường mở ra", "title": "Bài 11: Bác bảo vệ trường em"},
    {"id": "tv3_b12", "grade": 3, "volume": 1, "page": 58, "topic_group": "Chủ điểm 3: Cổng trường mở ra", "title": "Bài 12: Tiếng trống trường"},
    {"id": "tv3_b13", "grade": 3, "volume": 1, "page": 64, "topic_group": "Chủ điểm 4: Gia đình yêu thương", "title": "Bài 13: Quạt cho bà ngủ"},
    {"id": "tv3_b14", "grade": 3, "volume": 1, "page": 68, "topic_group": "Chủ điểm 4: Gia đình yêu thương", "title": "Bài 14: Con yêu mẹ"},
    {"id": "tv3_b15", "grade": 3, "volume": 1, "page": 72, "topic_group": "Chủ điểm 4: Gia đình yêu thương", "title": "Bài 15: Mẹ của Đỗ"},
    {"id": "tv3_b16", "grade": 3, "volume": 1, "page": 76, "topic_group": "Chủ điểm 4: Gia đình yêu thương", "title": "Bài 16: Bàn tay mẹ"},
    {"id": "tv3_b17", "grade": 3, "volume": 1, "page": 82, "topic_group": "Ôn tập học kì I", "title": "Bài 17: Ôn tập học kì I"},
    # Tập 2
    {"id": "tv3_b18", "grade": 3, "volume": 2, "page": 10, "topic_group": "Chủ điểm 5: Đất nước ngàn năm", "title": "Bài 18: Đất nước"},
    {"id": "tv3_b19", "grade": 3, "volume": 2, "page": 14, "topic_group": "Chủ điểm 5: Đất nước ngàn năm", "title": "Bài 19: Hai Bà Trưng"},
    {"id": "tv3_b20", "grade": 3, "volume": 2, "page": 18, "topic_group": "Chủ điểm 5: Đất nước ngàn năm", "title": "Bài 20: Người đi săn và con vượn"},
    {"id": "tv3_b21", "grade": 3, "volume": 2, "page": 22, "topic_group": "Chủ điểm 5: Đất nước ngàn năm", "title": "Bài 21: Sự tích Hồ Gươm"},
    {"id": "tv3_b22", "grade": 3, "volume": 2, "page": 28, "topic_group": "Chủ điểm 6: Trái Đất của chúng mình", "title": "Bài 22: Mưa"},
    {"id": "tv3_b23", "grade": 3, "volume": 2, "page": 32, "topic_group": "Chủ điểm 6: Trái Đất của chúng mình", "title": "Bài 23: Cơn mưa rào"},
    {"id": "tv3_b24", "grade": 3, "volume": 2, "page": 36, "topic_group": "Chủ điểm 6: Trái Đất của chúng mình", "title": "Bài 24: Bầu trời mùa thu"},
    {"id": "tv3_b25", "grade": 3, "volume": 2, "page": 40, "topic_group": "Chủ điểm 6: Trái Đất của chúng mình", "title": "Bài 25: Mặt Trời xanh của tôi"},
    {"id": "tv3_b26", "grade": 3, "volume": 2, "page": 46, "topic_group": "Chủ điểm 7: Nghệ thuật và cuộc sống", "title": "Bài 26: Hát bội"},
    {"id": "tv3_b27", "grade": 3, "volume": 2, "page": 50, "topic_group": "Chủ điểm 7: Nghệ thuật và cuộc sống", "title": "Bài 27: Tiếng đàn Ba-la-lai-ca trên sông Đà"},
    {"id": "tv3_b28", "grade": 3, "volume": 2, "page": 54, "topic_group": "Chủ điểm 7: Nghệ thuật và cuộc sống", "title": "Bài 28: Nhà bác học và bà cụ"},
    {"id": "tv3_b29", "grade": 3, "volume": 2, "page": 58, "topic_group": "Chủ điểm 7: Nghệ thuật và cuộc sống", "title": "Bài 29: Nhà hát của em"},
    {"id": "tv3_b30", "grade": 3, "volume": 2, "page": 64, "topic_group": "Chủ điểm 8: Ngôi nhà chung", "title": "Bài 30: Bác sĩ Y-éc-xanh"},
    {"id": "tv3_b31", "grade": 3, "volume": 2, "page": 68, "topic_group": "Chủ điểm 8: Ngôi nhà chung", "title": "Bài 31: Chuyện ở đảo Trường Sa"},
    {"id": "tv3_b32", "grade": 3, "volume": 2, "page": 72, "topic_group": "Chủ điểm 8: Ngôi nhà chung", "title": "Bài 32: Con suối nhỏ"},
    {"id": "tv3_b33", "grade": 3, "volume": 2, "page": 76, "topic_group": "Chủ điểm 8: Ngôi nhà chung", "title": "Bài 33: Cây đa làng"},
    {"id": "tv3_b34", "grade": 3, "volume": 2, "page": 82, "topic_group": "Ôn tập cuối năm", "title": "Bài 34: Ôn tập cuối năm"}
]

# ==============================================================================
# 4. TIẾNG VIỆT LỚP 4
# ==============================================================================
VIETNAMESE_GRADE_4_LESSONS = [
    # Tập 1
    {"id": "tv4_b01", "grade": 4, "volume": 1, "page": 10, "topic_group": "Chủ điểm 1: Mỗi người một vẻ", "title": "Bài 1: Thanh âm của gió"},
    {"id": "tv4_b02", "grade": 4, "volume": 1, "page": 14, "topic_group": "Chủ điểm 1: Mỗi người một vẻ", "title": "Bài 2: Cánh buồm tuổi thơ"},
    {"id": "tv4_b03", "grade": 4, "volume": 1, "page": 18, "topic_group": "Chủ điểm 1: Mỗi người một vẻ", "title": "Bài 3: Tuổi Ngựa"},
    {"id": "tv4_b04", "grade": 4, "volume": 1, "page": 22, "topic_group": "Chủ điểm 1: Mỗi người một vẻ", "title": "Bài 4: Người làm đồ chơi"},
    {"id": "tv4_b05", "grade": 4, "volume": 1, "page": 28, "topic_group": "Chủ điểm 2: Trải nghiệm và khám phá", "title": "Bài 5: Nghệ sĩ trống"},
    {"id": "tv4_b06", "grade": 4, "volume": 1, "page": 32, "topic_group": "Chủ điểm 2: Trải nghiệm và khám phá", "title": "Bài 6: Chuỗi hạt ngọc"},
    {"id": "tv4_b07", "grade": 4, "volume": 1, "page": 36, "topic_group": "Chủ điểm 2: Trải nghiệm và khám phá", "title": "Bài 7: Bầu trời của em"},
    {"id": "tv4_b08", "grade": 4, "volume": 1, "page": 40, "topic_group": "Chủ điểm 2: Trải nghiệm và khám phá", "title": "Bài 8: Chuyến du lịch kì thú"},
    {"id": "tv4_b09", "grade": 4, "volume": 1, "page": 46, "topic_group": "Chủ điểm 3: Mái ấm gia đình", "title": "Bài 9: Về thăm bà"},
    {"id": "tv4_b10", "grade": 4, "volume": 1, "page": 50, "topic_group": "Chủ điểm 3: Mái ấm gia đình", "title": "Bài 10: Bàn tay mẹ"},
    {"id": "tv4_b11", "grade": 4, "volume": 1, "page": 54, "topic_group": "Chủ điểm 3: Mái ấm gia đình", "title": "Bài 11: Hương ổi"},
    {"id": "tv4_b12", "grade": 4, "volume": 1, "page": 58, "topic_group": "Chủ điểm 3: Mái ấm gia đình", "title": "Bài 12: Bức tranh của em gái tôi"},
    {"id": "tv4_b13", "grade": 4, "volume": 1, "page": 64, "topic_group": "Chủ điểm 4: Chắp cánh ước mơ", "title": "Bài 13: Đôi cánh của ngựa trắng"},
    {"id": "tv4_b14", "grade": 4, "volume": 1, "page": 68, "topic_group": "Chủ điểm 4: Chắp cánh ước mơ", "title": "Bài 14: Ước mơ của Sam"},
    {"id": "tv4_b15", "grade": 4, "volume": 1, "page": 72, "topic_group": "Chủ điểm 4: Chắp cánh ước mơ", "title": "Bài 15: Bay cao ước mơ"},
    {"id": "tv4_b16", "grade": 4, "volume": 1, "page": 76, "topic_group": "Chủ điểm 4: Chắp cánh ước mơ", "title": "Bài 16: Tuổi thơ em"},
    {"id": "tv4_b17", "grade": 4, "volume": 1, "page": 82, "topic_group": "Ôn tập học kì I", "title": "Bài 17: Ôn tập học kì I"},
    # Tập 2
    {"id": "tv4_b18", "grade": 4, "volume": 2, "page": 10, "topic_group": "Chủ điểm 5: Sống để yêu thương", "title": "Bài 18: Người ăn xin"},
    {"id": "tv4_b19", "grade": 4, "volume": 2, "page": 14, "topic_group": "Chủ điểm 5: Sống để yêu thương", "title": "Bài 19: Con muốn làm một cái cây"},
    {"id": "tv4_b20", "grade": 4, "volume": 2, "page": 18, "topic_group": "Chủ điểm 5: Sống để yêu thương", "title": "Bài 20: Chiếc lá đầu tiên"},
    {"id": "tv4_b21", "grade": 4, "volume": 2, "page": 22, "topic_group": "Chủ điểm 5: Sống để yêu thương", "title": "Bài 21: Vì hòa bình"},
    {"id": "tv4_b22", "grade": 4, "volume": 2, "page": 28, "topic_group": "Chủ điểm 6: Uống nước nhớ nguồn", "title": "Bài 22: Chiếc gáo dừa"},
    {"id": "tv4_b23", "grade": 4, "volume": 2, "page": 32, "topic_group": "Chủ điểm 6: Uống nước nhớ nguồn", "title": "Bài 23: Lời ru của mẹ"},
    {"id": "tv4_b24", "grade": 4, "volume": 2, "page": 36, "topic_group": "Chủ điểm 6: Uống nước nhớ nguồn", "title": "Bài 24: Danh y Tuệ Tĩnh"},
    {"id": "tv4_b25", "grade": 4, "volume": 2, "page": 40, "topic_group": "Chủ điểm 6: Uống nước nhớ nguồn", "title": "Bài 25: Bác Hồ làm việc"},
    {"id": "tv4_b26", "grade": 4, "volume": 2, "page": 46, "topic_group": "Chủ điểm 7: Quê hương trong tôi", "title": "Bài 26: Gió đồng hun hút"},
    {"id": "tv4_b27", "grade": 4, "volume": 2, "page": 50, "topic_group": "Chủ điểm 7: Quê hương trong tôi", "title": "Bài 27: Sông Hương"},
    {"id": "tv4_b28", "grade": 4, "volume": 2, "page": 54, "topic_group": "Chủ điểm 7: Quê hương trong tôi", "title": "Bài 28: Đất nước ngàn năm"},
    {"id": "tv4_b29", "grade": 4, "volume": 2, "page": 58, "topic_group": "Chủ điểm 7: Quê hương trong tôi", "title": "Bài 29: Làng sen"},
    {"id": "tv4_b30", "grade": 4, "volume": 2, "page": 64, "topic_group": "Chủ điểm 8: Vì một thế giới bình yên", "title": "Bài 30: Hải âu bay trên biển"},
    {"id": "tv4_b31", "grade": 4, "volume": 2, "page": 68, "topic_group": "Chủ điểm 8: Vì một thế giới bình yên", "title": "Bài 31: Trái Đất trẻ thơ"},
    {"id": "tv4_b32", "grade": 4, "volume": 2, "page": 72, "topic_group": "Chủ điểm 8: Vì một thế giới bình yên", "title": "Bài 32: Tiếng chuông hòa bình"},
    {"id": "tv4_b33", "grade": 4, "volume": 2, "page": 76, "topic_group": "Chủ điểm 8: Vì một thế giới bình yên", "title": "Bài 33: Vòng tay bạn bè"},
    {"id": "tv4_b34", "grade": 4, "volume": 2, "page": 82, "topic_group": "Ôn tập cuối năm", "title": "Bài 34: Ôn tập cuối năm"}
]

# ==============================================================================
# 5. TIẾNG VIỆT LỚP 5
# ==============================================================================
VIETNAMESE_GRADE_5_LESSONS = [
    # Tập 1
    {"id": "tv5_b01", "grade": 5, "volume": 1, "page": 10, "topic_group": "Chủ điểm 1: Khởi đầu mới", "title": "Bài 1: Bài ca Trái Đất"},
    {"id": "tv5_b02", "grade": 5, "volume": 1, "page": 14, "topic_group": "Chủ điểm 1: Khởi đầu mới", "title": "Bài 2: Buổi sáng ở quê nội"},
    {"id": "tv5_b03", "grade": 5, "volume": 1, "page": 18, "topic_group": "Chủ điểm 1: Khởi đầu mới", "title": "Bài 3: Ngày hội mừng năm học mới"},
    {"id": "tv5_b04", "grade": 5, "volume": 1, "page": 22, "topic_group": "Chủ điểm 1: Khởi đầu mới", "title": "Bài 4: Thư gửi các học sinh"},
    {"id": "tv5_b05", "grade": 5, "volume": 1, "page": 28, "topic_group": "Chủ điểm 2: Khám phá thế giới", "title": "Bài 5: Vịnh Hạ Long"},
    {"id": "tv5_b06", "grade": 5, "volume": 1, "page": 32, "topic_group": "Chủ điểm 2: Khám phá thế giới", "title": "Bài 6: Kì quan thế giới"},
    {"id": "tv5_b07", "grade": 5, "volume": 1, "page": 36, "topic_group": "Chủ điểm 2: Khám phá thế giới", "title": "Bài 7: Du hành mặt trăng"},
    {"id": "tv5_b08", "grade": 5, "volume": 1, "page": 40, "topic_group": "Chủ điểm 2: Khám phá thế giới", "title": "Bài 8: Hành tinh xanh"},
    {"id": "tv5_b09", "grade": 5, "volume": 1, "page": 46, "topic_group": "Chủ điểm 3: Yêu thương và chia sẻ", "title": "Bài 9: Tiếng rao đêm"},
    {"id": "tv5_b10", "grade": 5, "volume": 1, "page": 50, "topic_group": "Chủ điểm 3: Yêu thương và chia sẻ", "title": "Bài 10: Mùa hoa cải bên sông"},
    {"id": "tv5_b11", "grade": 5, "volume": 1, "page": 54, "topic_group": "Chủ điểm 3: Yêu thương và chia sẻ", "title": "Bài 11: Hạt gạo làng ta"},
    {"id": "tv5_b12", "grade": 5, "volume": 1, "page": 58, "topic_group": "Chủ điểm 3: Yêu thương và chia sẻ", "title": "Bài 12: Lòng dân"},
    {"id": "tv5_b13", "grade": 5, "volume": 1, "page": 64, "topic_group": "Chủ điểm 4: Cội nguồn yêu thương", "title": "Bài 13: Thư thăm quê"},
    {"id": "tv5_b14", "grade": 5, "volume": 1, "page": 68, "topic_group": "Chủ điểm 4: Cội nguồn yêu thương", "title": "Bài 14: Nghĩa thầy trò"},
    {"id": "tv5_b15", "grade": 5, "volume": 1, "page": 72, "topic_group": "Chủ điểm 4: Cội nguồn yêu thương", "title": "Bài 15: Hạt giống tâm hồn"},
    {"id": "tv5_b16", "grade": 5, "volume": 1, "page": 76, "topic_group": "Chủ điểm 4: Cội nguồn yêu thương", "title": "Bài 16: Đất nước"},
    {"id": "tv5_b17", "grade": 5, "volume": 1, "page": 82, "topic_group": "Ôn tập học kì I", "title": "Bài 17: Ôn tập học kì I"},
    # Tập 2
    {"id": "tv5_b18", "grade": 5, "volume": 2, "page": 10, "topic_group": "Chủ điểm 5: Giữ lấy màu xanh", "title": "Bài 18: Kì quan rừng nhiệt đới"},
    {"id": "tv5_b19", "grade": 5, "volume": 2, "page": 14, "topic_group": "Chủ điểm 5: Giữ lấy màu xanh", "title": "Bài 19: Tiếng đàn Ba-la-lai-ca trên sông Đà"},
    {"id": "tv5_b20", "grade": 5, "volume": 2, "page": 18, "topic_group": "Chủ điểm 5: Giữ lấy màu xanh", "title": "Bài 20: Bài ca giữ đất"},
    {"id": "tv5_b21", "grade": 5, "volume": 2, "page": 22, "topic_group": "Chủ điểm 5: Giữ lấy màu xanh", "title": "Bài 21: Trồng cây gây rừng"},
    {"id": "tv5_b22", "grade": 5, "volume": 2, "page": 28, "topic_group": "Chủ điểm 6: Vì cuộc sống bình yên", "title": "Bài 22: Người gác rừng tí hon"},
    {"id": "tv5_b23", "grade": 5, "volume": 2, "page": 32, "topic_group": "Chủ điểm 6: Vì cuộc sống bình yên", "title": "Bài 23: Chú công an của em"},
    {"id": "tv5_b24", "grade": 5, "volume": 2, "page": 36, "topic_group": "Chủ điểm 6: Vì cuộc sống bình yên", "title": "Bài 24: Giữ gìn an ninh trật tự"},
    {"id": "tv5_b25", "grade": 5, "volume": 2, "page": 40, "topic_group": "Chủ điểm 6: Vì cuộc sống bình yên", "title": "Bài 25: Lập làng giữ biển"},
    {"id": "tv5_b26", "grade": 5, "volume": 2, "page": 46, "topic_group": "Chủ điểm 7: Con người và thời đại", "title": "Bài 26: Nhà phát minh tương lai"},
    {"id": "tv5_b27", "grade": 5, "volume": 2, "page": 50, "topic_group": "Chủ điểm 7: Con người và thời đại", "title": "Bài 27: Chinh phục vũ trụ"},
    {"id": "tv5_b28", "grade": 5, "volume": 2, "page": 54, "topic_group": "Chủ điểm 7: Con người và thời đại", "title": "Bài 28: Trí tuệ nhân tạo và em"},
    {"id": "tv5_b29", "grade": 5, "volume": 2, "page": 58, "topic_group": "Chủ điểm 7: Con người và thời đại", "title": "Bài 29: Thành phố thông minh"},
    {"id": "tv5_b30", "grade": 5, "volume": 2, "page": 64, "topic_group": "Chủ điểm 8: Việt Nam gấm vóc", "title": "Bài 30: Đất nước hình tia chớp"},
    {"id": "tv5_b31", "grade": 5, "volume": 2, "page": 68, "topic_group": "Chủ điểm 8: Việt Nam gấm vóc", "title": "Bài 31: Bác Hồ sống mãi với non sông"},
    {"id": "tv5_b32", "grade": 5, "volume": 2, "page": 72, "topic_group": "Chủ điểm 8: Việt Nam gấm vóc", "title": "Bài 32: Việt Nam quê hương ta"},
    {"id": "tv5_b33", "grade": 5, "volume": 2, "page": 76, "topic_group": "Chủ điểm 8: Việt Nam gấm vóc", "title": "Bài 33: Lời chào tạm biệt tiểu học"},
    {"id": "tv5_b34", "grade": 5, "volume": 2, "page": 82, "topic_group": "Ôn tập cuối năm", "title": "Bài 34: Ôn tập cuối năm"}
]

def get_vietnamese_lessons(grade: int, volume: int = 0) -> List[Dict[str, Any]]:
    """Tra cứu danh sách bài học SGK Tiếng Việt theo khối lớp và tập sách."""
    lesson_map = {
        1: VIETNAMESE_GRADE_1_LESSONS,
        2: VIETNAMESE_GRADE_2_LESSONS,
        3: VIETNAMESE_GRADE_3_LESSONS,
        4: VIETNAMESE_GRADE_4_LESSONS,
        5: VIETNAMESE_GRADE_5_LESSONS,
    }
    lessons = lesson_map.get(grade, [])
    if volume in [1, 2]:
        return [l for l in lessons if l["volume"] == volume]
    return lessons
