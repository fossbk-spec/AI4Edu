import os
import sys
import json
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from dotenv import load_dotenv

# Đảm bảo UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

# Import các service từ ai4edu package
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.core.llm_provider import UnifiedLLMClient, SUPPORTED_PROVIDERS
from ai4edu.data.math_curriculum import (
    get_math_lessons, 
    MATH_GRADE_1_LESSONS, 
    MATH_GRADE_2_LESSONS, 
    MATH_GRADE_3_LESSONS, 
    MATH_GRADE_4_LESSONS, 
    MATH_GRADE_5_LESSONS
)
from ai4edu.data.vietnamese_curriculum import (
    get_vietnamese_lessons, 
    VIETNAMESE_GRADE_1_LESSONS, 
    VIETNAMESE_GRADE_2_LESSONS, 
    VIETNAMESE_GRADE_3_LESSONS, 
    VIETNAMESE_GRADE_4_LESSONS, 
    VIETNAMESE_GRADE_5_LESSONS
)
from ai4edu.data.math_grade3_textbook_content import get_textbook_lesson_detail
from ai4edu.services.hoang_mai_service import (
    generate_lesson_plan_2345,
    generate_differentiated_taskset,
    generate_tt27_assessment
)
from ai4edu.services.ai_tutor import tutor_chat
from ai4edu.services.docx_exporter import create_lesson_plan_docx
from ai4edu.services.quizizz_exporter import generate_quizizz_questions, export_quiz_to_excel
from ai4edu.services.gdocs_exporter import export_lesson_plan_to_rich_html

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="AI4Edu Hub - Tiểu học Hoàng Mai",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS cho giao diện hiện đại, cao cấp với độ tương phản màu chuẩn xác
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0b57d0 0%, #1e40af 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(11, 87, 208, 0.15);
    }
    
    .main-header h1 {
        color: white !important;
        margin: 0;
        font-size: 26px;
        font-weight: 700;
    }
    
    .main-header p {
        color: #e0e7ff;
        margin-top: 6px;
        margin-bottom: 0;
        font-size: 14px;
    }
    
    .badge-hm {
        background-color: #fef3c7;
        color: #92400e;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* Box Thử thách mở rộng cho HS khá giỏi với màu nổi bật, dễ đọc trên mọi nền */
    .advanced-challenge-box {
        background-color: #fffbeb !important;
        border: 1.5px solid #fde68a !important;
        border-left: 6px solid #d97706 !important;
        padding: 14px 18px !important;
        border-radius: 8px !important;
        margin-top: 12px !important;
        margin-bottom: 8px !important;
        color: #0f172a !important;
        box-shadow: 0 2px 6px rgba(217, 119, 6, 0.08);
    }
    
    .advanced-challenge-title {
        color: #b45309 !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        display: inline-block;
        margin-right: 6px;
    }
    
    .advanced-challenge-content {
        color: #1e293b !important;
        font-weight: 500 !important;
        font-size: 14.5px !important;
        line-height: 1.5;
    }
    
    /* Các thẻ 4 Tầng Phân Hóa với chữ đậm nét, tương phản cao */
    .tier-card-1 { 
        border-left: 6px solid #10b981; 
        background-color: #f0fdf4; 
        padding: 16px; 
        border-radius: 8px; 
        margin-bottom: 14px; 
        color: #0f172a !important;
        border: 1px solid #bbf7d0;
    }
    .tier-card-2 { 
        border-left: 6px solid #0284c7; 
        background-color: #f0f9ff; 
        padding: 16px; 
        border-radius: 8px; 
        margin-bottom: 14px; 
        color: #0f172a !important;
        border: 1px solid #bae6fd;
    }
    .tier-card-3 { 
        border-left: 6px solid #8b5cf6; 
        background-color: #f5f3ff; 
        padding: 16px; 
        border-radius: 8px; 
        margin-bottom: 14px; 
        color: #0f172a !important;
        border: 1px solid #ddd6fe;
    }
    .tier-card-4 { 
        border-left: 6px solid #f59e0b; 
        background-color: #fffbeb; 
        padding: 16px; 
        border-radius: 8px; 
        margin-bottom: 14px; 
        color: #0f172a !important;
        border: 1px solid #fde68a;
    }
    
    .tier-card-1 h4, .tier-card-2 h4, .tier-card-3 h4, .tier-card-4 h4 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    
    .tier-card-1 p, .tier-card-2 p, .tier-card-3 p, .tier-card-4 p {
        color: #1e293b !important;
        margin-bottom: 6px;
    }
    
    .tier-card-1 strong, .tier-card-2 strong, .tier-card-3 strong, .tier-card-4 strong {
        color: #0f172a !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: #f1f5f9;
        border-radius: 8px 8px 0 0;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
        font-size: 13.5px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #0b57d0 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function tra cứu danh mục bài học SGK chuẩn
def get_subject_curriculum_lessons(subject_id: str, grade: int, volume: int = 0):
    sub_lower = (subject_id or "").lower()
    if any(k in sub_lower for k in ["toán", "math"]):
        return get_math_lessons(grade, volume)
    elif any(k in sub_lower for k in ["tiếng việt", "vietnamese", "văn"]):
        return get_vietnamese_lessons(grade, volume)
    return []

# Helper function để đồng bộ tức thì giá trị bài học khi chọn dropdown SGK
def sync_sgk_topic(pick_key: str, input_key: str):
    pick_val = st.session_state.get(pick_key, "")
    if pick_val and not pick_val.startswith("✏️"):
        st.session_state[input_key] = pick_val.split("  (")[0]

# Các Dialog Modal Cẩm Nang Sư Phạm Tương Tác 100%
@st.dialog("🚀 Quy Trình 3 Bước Soạn Bài Chuẩn Sư Phạm", width="large")
def show_quickstart_dialog():
    st.markdown("""
    ### 🎯 Quy Trình 3 Bước Soạn Giáo Án & Học Liệu Tự Động:
    ---
    #### 🔹 Bước 1: Thiết lập cấu hình tại Sidebar (Thanh bên trái)
    1. **Chọn Khối Lớp:** Chọn lớp giảng dạy (Khối Lớp 1, 2, 3, 4 hoặc 5).
    2. **Chọn Môn Học:** Chọn môn tương ứng (Toán học, Tiếng Việt, Tự nhiên & Xã hội, Khoa học...).
    3. **Chọn Mô hình AI:** Khuyên dùng `Gemini 3.5 Flash` (Rất nhanh & ổn định).

    #### 🔹 Bước 2: Chọn Bài Học từ Danh Mục SGK Chuẩn
    1. Chọn **Tập sách** (Tập 1 hoặc Tập 2).
    2. Chọn **Bài học chính thức từ SGK** (Ví dụ: `Bài 18: Góc, góc vuông, góc không vuông`).
    3. Kiểm tra khung **Trích dẫn nguyên văn từ SGK** (Số trang, định nghĩa, bài tập gốc).
    4. Tích chọn `Thử thách HS khá giỏi` để AI tích hợp các câu hỏi mở, nhiệm vụ liên môn.

    #### 🔹 Bước 3: Sinh Kế Hoạch Bài Dạy & Xuất File
    1. Bấm **`🚀 Tự Động Sinh Kế Hoạch Bài Dạy 2345`**.
    2. **Xuất sang Google Docs (Khuyên dùng):** Bấm nút màu xanh **`📋 SAO CHÉP GOOGLE DOCS`** ➔ Mở Google Docs ➔ Nhấn **`Ctrl + V`** (Giữ nguyên bảng 5 cột có màu sắc).
    3. **Tải File Word:** Bấm nút **`📥 Tải Kế Hoạch Bài Dạy (.docx)`** để lưu về máy tính.
    """)

@st.dialog("🎒 Hướng Dẫn Sư Phạm Chi Tiết Từng Khối Lớp (1-5)", width="large")
def show_grade_guide_dialog():
    st.markdown("""
    ### 🎒 Hướng Dẫn Sư Phạm Theo Tâm Lý Nhận Thức Lớp 1 Đến Lớp 5:
    ---
    * 🧸 **Khối Lớp 1 & Lớp 2 (Trực quan - Cảm tính):**
      - **Đặc điểm:** Tư duy dựa trên đồ vật thật (que tính, viên bi, ngón tay), hình ảnh màu sắc.
      - **Môn Toán:** Đếm, so sánh, phép cộng trừ có nhớ phạm vi 20 & 100, nhận biết hình phẳng đơn giản.
      - **Môn Tiếng Việt:** Âm, chữ cái, ghép vần, đọc trơn đoạn văn ngắn 20-30 chữ.
      - **Trợ giảng AI (Tab 4):** Chọn `🐰 Thỏ Trắng Dễ Thương` với lời khuyên ngắn gọn, vui vẻ.

    * 📘 **Khối Lớp 3 (Bảng cửu chương & Tư duy Số học sơ cấp):**
      - **Đặc điểm:** Chuyển từ đếm cộng sang tư duy phép nhân/chia và cấu tạo số 4-5 chữ số.
      - **Môn Toán:** Bảng nhân chia 6, 7, 8, 9; Điểm ở giữa, Trung điểm; Góc vuông (thước ê-ke); Bán kính, Đường kính; Bài toán 2 bước tính.
      - **Môn Tiếng Việt:** Mở rộng vốn từ, Biện pháp Tu từ So sánh và Nhân hóa.

    * 🔬 **Khối Lớp 4 (Tư duy Trừu tượng & Khám phá Khoa học):**
      - **Đặc điểm:** Bắt đầu hình thành các khái niệm trừu tượng, phân tích và tổng hợp.
      - **Môn Toán:** Khái niệm phân số, quy đồng mẫu số, 4 phép tính phân số, hình bình hành, hình thoi.
      - **Khoa học / Lịch sử - Địa lý:** Kịch bản thí nghiệm nước, không khí; tìm hiểu lược đồ địa lý.

    * 🎓 **Khối Lớp 5 (Tổng kết Tiểu học & Chuẩn bị Chuyển cấp):**
      - **Đặc điểm:** Hoàn thiện tư duy logic, tính toán đại số và hình học không gian.
      - **Môn Toán:** Số thập phân, Tỉ số phần trăm, Diện tích hình thang/hình tròn, Thể tích, Chuyển động đều ($v, s, t$).
      - **Quizizz (Tab 5):** Tạo đề trắc nghiệm ma trận 4 mức độ Bloom ôn thi vào lớp 6.
    """)

@st.dialog("📑 Mục Lục Bài Học Toán & Tiếng Việt Lớp 1 - 5 (SGK Kết Nối Tri Thức)", width="large")
def show_curriculum_dialog():
    st.markdown("""
    ### 📑 Mục Lục Chi Tiết Môn Toán & Tiếng Việt Lớp 1 - 5 (Bộ Kết Nối Tri Thức Với Cuộc Sống):
    *Tổng Chủ biên môn Toán: GS.TSKH. Hà Huy Khoái • Chủ biên: PGS.TS. Lê Anh Vinh*  
    *Tổng Chủ biên môn Tiếng Việt: GS.TS. Bùi Mạnh Hùng (NXB Giáo Dục Việt Nam)*
    ---
    """)
    tab_g1, tab_g2, tab_g3, tab_g4, tab_g5 = st.tabs([
        "🧸 Khối Lớp 1",
        "🎒 Khối Lớp 2",
        "📘 Khối Lớp 3",
        "🔬 Khối Lớp 4",
        "🎓 Khối Lớp 5"
    ])
    
    with tab_g1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📐 TOÁN LỚP 1 (39 Bài Học)")
            st.markdown("**Tập 1 (Bài 1 - 17):**")
            for l in MATH_GRADE_1_LESSONS[:17]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 (Bài 18 - 39):**")
            for l in MATH_GRADE_1_LESSONS[17:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
        with c2:
            st.markdown("#### 📖 TIẾNG VIỆT LỚP 1 (38 Bài Học)")
            st.markdown("**Tập 1 - Âm chữ & Vần (Bài 1 - 20):**")
            for l in VIETNAMESE_GRADE_1_LESSONS[:20]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 - Chủ điểm Luyện đọc (Bài 1 - 18):**")
            for l in VIETNAMESE_GRADE_1_LESSONS[20:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")

    with tab_g2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📐 TOÁN LỚP 2 (67 Bài Học)")
            st.markdown("**Tập 1 (Bài 1 - 35):**")
            for l in MATH_GRADE_2_LESSONS[:35]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 (Bài 36 - 67):**")
            for l in MATH_GRADE_2_LESSONS[35:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
        with c2:
            st.markdown("#### 📖 TIẾNG VIỆT LỚP 2 (34 Bài Học)")
            st.markdown("**Tập 1 - Chủ điểm 1 đến 4 (Bài 1 - 17):**")
            for l in VIETNAMESE_GRADE_2_LESSONS[:17]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 - Chủ điểm 5 đến 8 (Bài 18 - 34):**")
            for l in VIETNAMESE_GRADE_2_LESSONS[17:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")

    with tab_g3:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📐 TOÁN LỚP 3 (81 Bài Học)")
            st.markdown("**Tập 1 (Bài 1 - 44):**")
            for l in MATH_GRADE_3_LESSONS[:44]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 (Bài 45 - 81):**")
            for l in MATH_GRADE_3_LESSONS[44:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
        with c2:
            st.markdown("#### 📖 TIẾNG VIỆT LỚP 3 (34 Bài Học)")
            st.markdown("**Tập 1 - Chủ điểm 1 đến 4 (Bài 1 - 17):**")
            for l in VIETNAMESE_GRADE_3_LESSONS[:17]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 - Chủ điểm 5 đến 8 (Bài 18 - 34):**")
            for l in VIETNAMESE_GRADE_3_LESSONS[17:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")

    with tab_g4:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📐 TOÁN LỚP 4 (70 Bài Học)")
            st.markdown("**Tập 1 (Bài 1 - 35):**")
            for l in MATH_GRADE_4_LESSONS[:35]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 (Bài 36 - 70):**")
            for l in MATH_GRADE_4_LESSONS[35:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
        with c2:
            st.markdown("#### 📖 TIẾNG VIỆT LỚP 4 (34 Bài Học)")
            st.markdown("**Tập 1 - Chủ điểm 1 đến 4 (Bài 1 - 17):**")
            for l in VIETNAMESE_GRADE_4_LESSONS[:17]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 - Chủ điểm 5 đến 8 (Bài 18 - 34):**")
            for l in VIETNAMESE_GRADE_4_LESSONS[17:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")

    with tab_g5:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 📐 TOÁN LỚP 5 (66 Bài Học)")
            st.markdown("**Tập 1 (Bài 1 - 35):**")
            for l in MATH_GRADE_5_LESSONS[:35]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 (Bài 36 - 66):**")
            for l in MATH_GRADE_5_LESSONS[35:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
        with c2:
            st.markdown("#### 📖 TIẾNG VIỆT LỚP 5 (34 Bài Học)")
            st.markdown("**Tập 1 - Chủ điểm 1 đến 4 (Bài 1 - 17):**")
            for l in VIETNAMESE_GRADE_5_LESSONS[:17]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")
            st.markdown("**Tập 2 - Chủ điểm 5 đến 8 (Bài 18 - 34):**")
            for l in VIETNAMESE_GRADE_5_LESSONS[17:]:
                st.markdown(f"- **{l['title']}** (Tr.{l['page']}) - *{l['topic_group']}*")

@st.dialog("📚 Kho Tải File PDF Sách Giáo Khoa Lớp 1 - 5 (Bộ Kết Nối Tri Thức)", width="large")
def show_pdf_library_dialog():
    st.markdown("""
    ### 📚 Tổng Hợp File PDF Sách Giáo Khoa Lớp 1 Đến Lớp 5 (NXB Giáo Dục Việt Nam):
    ---
    * 🌐 **Cổng đọc online chính thức NXBGDVN:** [Hành Trang Số (hanhtrangso.nxbgd.vn)](https://hanhtrangso.nxbgd.vn/)
    * 📂 **Kho Google Drive Tổng Hợp (Tất cả các lớp):** [Mở Thư Viện Google Drive](https://drive.google.com/drive/folders/1OfOZQW4SVQA3VjFp_bkf84U1_zgR473t?usp=sharing)
    ---
    #### 🎒 Liên Kết Tải Trọn Bộ Theo Từng Khối Lớp:
    * 🧸 **Khối Lớp 1:** [Tải trọn bộ PDF SGK Lớp 1 (Toán, Tiếng Việt, TN&XH, Đạo đức, HĐTN...)](https://drive.google.com/drive/folders/169N_qc2yAINJ3QLibudU2bQsro0mv26q?usp=sharing)
    * 🎒 **Khối Lớp 2:** [Tải trọn bộ PDF SGK Lớp 2 (Toán, Tiếng Việt, TN&XH, Đạo đức, HĐTN...)](https://drive.google.com/drive/folders/1TUkLbCcAYDYopEsicPR7FweoiHhMwcBK?usp=sharing)
    * 📘 **Khối Lớp 3:** [Tải trọn bộ PDF SGK Lớp 3 (Toán, Tiếng Việt, TN&XH, Tin học, Công nghệ...)](https://drive.google.com/drive/folders/1aLHxjgpYsvcR54JGlYlb7PgW3v3Wkhy0?usp=sharing)
    * 🔬 **Khối Lớp 4:** [Tải trọn bộ PDF SGK Lớp 4 (Toán, Tiếng Việt, Khoa học, Lịch sử - Địa lý, Tin học...)](https://drive.google.com/drive/folders/1EyJEo4JuVxvOBHwdVpwZkbCayvrFwvHu?usp=sharing)
    * 🎓 **Khối Lớp 5:** [Tải trọn bộ PDF SGK Lớp 5 (Toán, Tiếng Việt, Khoa học, Lịch sử - Địa lý, Tin học...)](https://drive.google.com/drive/folders/1kw3n1xGwdgCa8RPgLRb_g6d4hADDei98?usp=sharing)
    """)

@st.dialog("🌐 Chuẩn UNESCO & Đạo Đức Ứng Dụng AI Trong Giáo Dục", width="large")
def show_unesco_standards_dialog():
    st.markdown("""
    ### 🌐 Hướng Dẫn Ứng Dụng AI Giáo Dục Theo UNESCO & Chuẩn Quốc Tế
    *Căn cứ Khung Năng Lực AI Cho Giáo Viên (UNESCO AI Competency Framework - 2024) & Tiêu chuẩn ISTE / OECD*
    ---
    
    #### ⚠️ 1. KHUYẾN CÁO QUAN TRỌNG KHI SỬ DỤNG CÔNG CỤ (DISCLAIMER):
    > 🔴 **Tính chất Demo & Trợ lý:** Ứng dụng mang tính chất **trình diễn công nghệ (Demo) và hỗ trợ sư phạm**, không thay thế vai trò chuyên môn của nhà giáo.  
    > 🔴 **Trách nhiệm thẩm định:** Giáo viên giữ vai trò quyết định chuyên môn cao nhất (**Teacher-in-the-loop**) và **bắt buộc phải kiểm tra, rà soát và thẩm định lại toàn bộ tính chính xác khoa học, tính chuẩn mực ngôn ngữ và độ phù hợp lứa tuổi** của các nội dung do AI sinh ra trước khi đưa vào giảng dạy thực tế.

    ---
    
    #### 🏛️ 2. 5 Trụ Cột Khung Năng Lực AI Giáo Viên Của UNESCO (2024):
    1. **Tư duy Lấy Con Người Làm Trung Tâm (Human-Centred Mindset):**  
       AI chỉ đóng vai trò trợ lý khuếch đại năng lực sư phạm. Người thầy luôn là người truyền cảm hứng, thấu cảm và trực tiếp dẫn dắt tương tác xã hội - cảm xúc (Social-Emotional Learning) của học sinh.
    2. **Đạo Đức AI & Bảo Vệ Quyền Riêng Tư Của Trẻ Em (AI Ethics & Child Privacy):**  
       Tuyệt đối không nhập thông tin định danh cá nhân nhạy cảm, hình ảnh riêng tư hoặc học bạ của học sinh lên các nền tảng AI công cộng. Tuân thủ nghiêm ngặt Luật An toàn Thông tin và Quyền trẻ em.
    3. **Sư Phạm Số & Dạy Học Phân Hóa (AI Pedagogy & Differentiation):**  
       Sử dụng AI để thiết kế các kịch bản học tập cá nhân hóa, giàn giáo hỗ trợ 4 tầng (Scaffolding) giúp học sinh chậm tiến bộ và mở rộng thử thách sáng tạo (STEM/STEAM) cho học sinh năng khiếu.
    4. **Năng Lực Thẩm Định & Phản Biện (Critical AI Literacy & Fact-Checking):**  
       Giáo viên cần nắm vững kỹ năng kiểm tra chéo (Cross-verification), phát hiện hiện tượng "ảo giác" (Hallucination) hoặc thiên kiến thông tin (Bias) từ mô hình ngôn ngữ lớn.
    5. **Học Tập Suốt Đời & Sinh Hoạt Chuyên Môn (Continuous Professional Learning):**  
       Chủ động cập nhật tri thức công nghệ mới, tích cực chia sẻ các kịch bản và Prompt mẫu hiệu quả trong tổ chuyên môn nhà trường.

    ---
    
    #### 🌍 3. Tiêu Chuẩn Quốc Tế ISTE & OECD:
    * **ISTE Standards for Educators & Students:** Khuyến khích học sinh trở thành **Nhà kiến tạo số (Digital Creators)**, sử dụng công nghệ để giải quyết các vấn đề thực tiễn của cuộc sống địa phương.
    * **OECD Digital Education Outlook:** Đảm bảo tính công bằng (Equity) trong tiếp cận giáo dục số, không để bất kỳ học sinh nào bị bỏ lại phía sau trong thời đại số.
    """)

# Nạp danh mục chương trình từ PromptEngine
engine = PromptEngine()

# Header Banner
st.markdown("""
<div class="main-header">
    <div class="badge-hm">🏫 TRƯỜNG TIỂU HỌC HOÀNG MAI • CHẤT LƯỢNG CAO & ĐỔI MỚI SÁNG TẠO</div>
    <h1>🎓 AI4Edu Hub - Trợ Lý AI Giáo Dục Đa Mô Hình (Gemini / Claude / GPT)</h1>
    <p>Tích hợp trọn bộ 323 bài Toán & 174 bài Tiếng Việt (Lớp 1-5 KNTT) • Soạn KHBD 5 cột • Phân hóa 4 tầng • Chuẩn UNESCO.</p>
</div>
""", unsafe_allow_html=True)

# Khung Hướng Dẫn Sử Dụng Chi Tiết Hiện Đại (Interactive User Guide Banner)
with st.expander("📖 HƯỚNG DẪN SỬ DỤNG CHI TIẾT THEO TỪNG KHỐI LỚP, MÔN HỌC & BÀI HỌC (BẤM ĐỂ MỞ/ĐÓNG)", expanded=False):
    g_tab1, g_tab2, g_tab3, g_tab4, g_tab5, g_tab6 = st.tabs([
        "🚀 1. Quy Trình 3 Bước",
        "🎒 2. Hướng Dẫn Từng Khối Lớp (1-5)",
        "📐 3. Hướng Dẫn Từng Bài Học SGK",
        "📋 4. Xuất Google Docs & Word",
        "🌐 5. Cẩm Nang Trực Tuyến",
        "🏛️ 6. Chuẩn UNESCO & Khuyến Cáo Demo"
    ])
    
    with g_tab1:
        st.markdown("""
        #### 🚀 Quy Trình 3 Bước Soạn Giáo Án & Học Liệu Tự Động:
        1. **Bước 1 (Sidebar trái):** Chọn **Khối Lớp** (ví dụ: `Khối Lớp 3`) $\rightarrow$ Chọn **Môn Học** (ví dụ: `Toán học`) $\rightarrow$ Chọn **Mô hình AI** (`Gemini 3.5 Flash` khuyên dùng).
        2. **Bước 2 (Giao diện chính):** Chọn **Tập sách** (Tập 1 hoặc 2) $\rightarrow$ Chọn **Bài học chính thức từ SGK** (Ví dụ: `Bài 18: Góc, góc vuông, góc không vuông`). Kiểm tra khung trích dẫn nguyên văn SGK.
        3. **Bước 3:** Bấm **`🚀 Tự Động Sinh Kế Hoạch Bài Dạy 2345`** $\rightarrow$ Bấm nút màu xanh **`📋 SAO CHÉP GOOGLE DOCS`** hoặc tải file Word `.docx`.
        """)
        
    with g_tab2:
        st.markdown("""
        #### 🎒 Hướng Dẫn Sư Phạm Chi Tiết Cho Từng Khối Lớp:
        * 🧸 **Khối Lớp 1 & 2 (Trực quan - Cảm tính):**
          - **Toán:** Tập trung đếm que tính, hình học trực quan, phép tính có nhớ phạm vi 20 & 100.
          - **Tiếng Việt:** Nhận diện âm vần, ghép chữ, tập đọc trơn đoạn văn ngắn 20-30 chữ.
          - **Trợ giảng AI (Tab 4):** Chọn nhân vật `🐰 Thỏ Trắng Dễ Thương` với lời khen ngợi vui tươi.
        * 📘 **Khối Lớp 3 (Bảng cửu chương & Đại số sơ cấp):**
          - **Toán:** Bảng nhân chia 6, 7, 8, 9; Làm quen Góc, Bán kính/Đường kính; Bài toán 2 bước tính.
          - **Tiếng Việt:** Mở rộng vốn từ, nhận biết hình ảnh so sánh, nhân hóa, viết đoạn văn ngắn.
        * 🔬 **Khối Lớp 4 (Tư duy Trừu tượng & Khám phá):**
          - **Toán:** Khái niệm phân số, quy đồng mẫu số, diện tích hình bình hành & hình thoi.
          - **Khoa học / Lịch sử - Địa lý:** Kịch bản thí nghiệm nước, không khí; tìm hiểu lược đồ địa lý.
        * 🎓 **Khối Lớp 5 (Tổng kết Tiểu học & Chuyển cấp):**
          - **Toán:** Số thập phân, Tỉ số phần trăm, Thể tích, Toán chuyển động đều ($v, s, t$).
          - **Quizizz (Tab 5):** Tự động tạo 10-15 câu trắc nghiệm ma trận 4 mức độ ôn thi chuyển cấp.
        """)
        
    with g_tab3:
        st.markdown("""
        #### 📐 Hướng Dẫn Khớp Chính Xác Từng Bài Học Từ Sách Giáo Khoa:
        * **100% Không Bịa Đặt:** Hệ thống đã nạp sẵn toàn bộ 323 bài Toán và 174 bài Tiếng Việt (Lớp 1-5) chuẩn sách *Kết nối tri thức với cuộc sống*.
        * **Trích Dẫn Nguyên Bản:** Khi chọn bài (ví dụ `Bài 18`), hệ thống hiển thị ngay:
          - Số trang chính xác trong SGK (Trang 54 - 55).
          - Định nghĩa cốt lõi: Góc đỉnh O; cạnh OA, OB; Thước ê-ke kiểm tra góc vuông.
          - Bài tập mẫu và tình huống khám phá gốc của Mai, Việt, Rô-bốt.
        * **Tùy chỉnh linh hoạt:** Giáo viên có thể chỉnh sửa thêm ghi chú riêng vào ô Tên bài học trước khi bấm sinh.
        """)
        
    with g_tab4:
        st.markdown("""
        #### 📋 Hướng Dẫn Đồng Bộ Sang Google Docs & In Ấn:
        * **Cách 1: Sao chép sang Google Docs (Khuyên dùng - Nhanh nhất):**
          1. Bấm nút màu xanh **`📋 BẤM VÀO ĐÂY ĐỂ SAO CHÉP ĐỊNH DẠNG GOOGLE DOCS`**.
          2. Bấm nút **`🌐 Mở Google Docs Mới (docs.new)`**.
          3. Tại trang Google Docs, nhấn **`Ctrl + V`** (Dán) $\rightarrow$ Bảng 5 cột có màu sắc, tiêu đề và kẻ viền xuất hiện hoàn hảo!
        * **Cách 2: Tải File Word (.docx):**
          - Bấm nút **`📥 Tải Kế Hoạch Bài Dạy (.docx)`** để lưu file về máy tính chỉnh sửa và in ấn.
        """)
        
    with g_tab5:
        st.markdown("""
        #### 🌐 Cẩm Nang & Tài Liệu Sư Phạm Trực Tuyến:
        * 📖 **Cẩm nang Tổng quan:** [Xem tài liệu trực tuyến](https://ai4edu-hm.streamlit.app/)
        * 🏫 **Chuyên trang Tiểu học Hoàng Mai:** Hướng dẫn Công văn 2345, Phân hóa 4 tầng & Thông tư 27.
        * 📐 **Mục lục Toàn diện Toán & Tiếng Việt (1-5):** Tra cứu số trang và trọng tâm sư phạm.
        """)

    with g_tab6:
        st.markdown("""
        #### 🏛️ Chuẩn UNESCO & Khuyến Cáo Khi Sử Dụng (Disclaimer):
        * ⚠️ **Khuyến Cáo Sử Dụng:** Hệ thống mang tính chất **trình diễn công nghệ (Demo) và hỗ trợ sư phạm**. Giáo viên giữ vai trò chuyên môn chủ đạo và **phải kiểm tra, thẩm định lại tính chính xác** của kết quả do AI sinh ra trước khi áp dụng vào lớp học.
        * 🌐 **Khung UNESCO 2024:** Lấy con người làm trung tâm, tôn trọng đạo đức AI, bảo vệ bí mật thông tin học sinh và rèn luyện năng lực phản biện thẩm định dữ liệu.
        """)

# Sidebar điều khiển
with st.sidebar:
    st.markdown("## 🏫 Tiểu Học Hoàng Mai")
    st.title("⚙️ Cấu Hình Giảng Dạy")
    
    scope_option = st.radio(
        "Phạm vi áp dụng:",
        ["🏫 Tiểu học Hoàng Mai (Lớp 1 - 5)", "🌐 Toàn bộ K-12 (Lớp 1 - 12)"],
        index=0
    )
    
    if "Tiểu học" in scope_option:
        grade_options = [1, 2, 3, 4, 5]
    else:
        grade_options = list(range(1, 13))
        
    selected_grade_num = st.selectbox(
        "Chọn Khối Lớp:",
        grade_options,
        index=2 if 3 in grade_options else 0, # Mặc định chọn Lớp 3
        format_func=lambda x: f"Khối Lớp {x}"
    )
    
    grade_info = engine.get_grade(selected_grade_num)
    
    subject_map = {s.id: s.name for s in grade_info.subjects} if grade_info else {}
    selected_subject_id = st.selectbox(
        "Chọn Môn Học:",
        list(subject_map.keys()),
        format_func=lambda x: subject_map.get(x, x)
    )
    
    # -------------------------------------------------------------
    # 📖 CẨM NANG SƯ PHẠM (ĐƯỢC ĐƯA LÊN TRƯỚC CHỌN AI MODEL)
    # -------------------------------------------------------------
    st.markdown("---")
    st.markdown("### 📖 Cẩm Nang Sư Phạm")
    if st.button("🚀 Quy Trình 3 Bước", use_container_width=True, key="btn_dlg1"):
        show_quickstart_dialog()
    if st.button("🎒 Hướng Dẫn Từng Khối Lớp", use_container_width=True, key="btn_dlg2"):
        show_grade_guide_dialog()
    if st.button("📑 Mục Lục Bài Học Toán & Tiếng Việt (Lớp 1 - 5)", use_container_width=True, key="btn_dlg3"):
        show_curriculum_dialog()
    if st.button("📚 Tải File PDF SGK Lớp 1 - 5", use_container_width=True, key="btn_dlg4"):
        show_pdf_library_dialog()
    if st.button("🌐 Chuẩn UNESCO & Đạo Đức AI", use_container_width=True, key="btn_dlg5"):
        show_unesco_standards_dialog()

    st.info("⚠️ **Khuyến cáo:** Ứng dụng mang tính chất thử nghiệm Demo & hỗ trợ sư phạm. Thầy cô cần kiểm tra, thẩm định lại tính chính xác của kết quả do AI sinh ra trước khi giảng dạy.")

    st.markdown("---")
    st.markdown("### 🤖 Chọn AI Model & API Key")
    
    provider_options = list(SUPPORTED_PROVIDERS.keys())
    selected_provider = st.selectbox("Nhà cung cấp AI:", provider_options, index=0)
    
    model_list = SUPPORTED_PROVIDERS[selected_provider]
    model_ids = [m["id"] for m in model_list]
    model_labels = {m["id"]: m["name"] for m in model_list}
    
    selected_model_id = st.selectbox(
        "Mô hình AI:",
        model_ids,
        format_func=lambda x: model_labels.get(x, x)
    )
    
    # Hàm tiện ích lấy Secret từ os.getenv hoặc st.secrets trên Streamlit Cloud
    def _get_key(key_name: str) -> Optional[str]:
        val = os.getenv(key_name)
        if val and val.strip():
            return val.strip()
        try:
            if key_name in st.secrets:
                return str(st.secrets[key_name]).strip()
        except Exception:
            pass
        return None

    # Quản lý API Key cho từng Provider
    active_api_key = None
    if "Gemini" in selected_provider:
        env_key = _get_key("GEMINI_API_KEY")
        if env_key:
            st.success("✅ Gemini API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có GEMINI_API_KEY")
            active_api_key = st.text_input("Nhập Gemini API Key:", type="password")
            if active_api_key:
                os.environ["GEMINI_API_KEY"] = active_api_key
    elif "Claude" in selected_provider or "Anthropic" in selected_provider:
        env_key = _get_key("ANTHROPIC_API_KEY")
        if env_key:
            st.success("✅ Anthropic Claude API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có ANTHROPIC_API_KEY")
            active_api_key = st.text_input("Nhập Claude API Key:", type="password")
            if active_api_key:
                os.environ["ANTHROPIC_API_KEY"] = active_api_key
    elif "OpenAI" in selected_provider:
        env_key = _get_key("OPENAI_API_KEY")
        if env_key:
            st.success("✅ OpenAI API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có OPENAI_API_KEY")
            active_api_key = st.text_input("Nhập OpenAI API Key:", type="password")
            if active_api_key:
                os.environ["OPENAI_API_KEY"] = active_api_key

    st.caption(f"**Giai đoạn nhận thức:** {grade_info.cognitive_stage if grade_info else 'N/A'}")
    st.caption(f"**Văn bản pháp quy:** Công văn 2345/BGDĐT-GDTH & Thông tư 27/2020/TT-BGDĐT")

# Khởi tạo Unified LLM Client hiện tại
llm_client = UnifiedLLMClient(
    provider=selected_provider,
    model_id=selected_model_id,
    api_key=active_api_key
)

# 5 Tabs Chuyên Biệt
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📑 1. Soạn KHBD 5 Cột (CV 2345)",
    "🎯 2. Phân Hóa Nhiệm Vụ 4 Tầng",
    "📊 3. Nhận Xét Học Sinh (TT 27)",
    "💬 4. AI Socratic Tutor 24/7",
    "🎮 5. Tạo Câu Hỏi Quizizz / Game"
])

# ==========================================
# TAB 1: SOẠN KẾ HOẠCH BÀI DẠY 5 CỘT (CV 2345)
# ==========================================
with tab1:
    st.subheader("📑 Soạn Kế Hoạch Bài Dạy 5 Cột Chuẩn Công Văn 2345/BGDĐT-GDTH")
    st.write(f"Đang sử dụng mô hình: **{model_labels.get(selected_model_id, selected_model_id)}**")
    
    # Bộ chọn bài học từ SGK (Hỗ trợ Toán & Tiếng Việt Lớp 1 - 5)
    curriculum_list_t1 = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, 0)
    default_topic_t1 = curriculum_list_t1[0]["title"] if curriculum_list_t1 else "Bài học mới"
    if selected_grade_num == 3 and "math" in selected_subject_id.lower():
        default_topic_t1 = "Bài 18: Góc, góc vuông, góc không vuông"
    elif selected_grade_num == 5 and "math" in selected_subject_id.lower():
        default_topic_t1 = "Bài 28: Hình tam giác. Diện tích hình tam giác"
        
    if curriculum_list_t1:
        sub_name_vi = "Toán" if any(k in selected_subject_id.lower() for k in ["math", "toán"]) else "Tiếng Việt"
        st.markdown(f"##### 📚 Chọn Bài Học Từ Danh Mục SGK {sub_name_vi} Lớp {selected_grade_num} (Chuẩn CTGDPT 2018):")
        col_v1, col_v2 = st.columns([1, 3])
        with col_v1:
            vol_choice = st.selectbox("Chọn Tập sách:", ["Tất cả (Tập 1 & 2)", "Tập 1 (HK I)", "Tập 2 (HK II)"], key="vol_t1")
            vol_idx = 1 if "Tập 1" in vol_choice else (2 if "Tập 2" in vol_choice else 0)
            available_lessons = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, vol_idx)
            lesson_labels = [f"{l['title']}  ({l['topic_group']})" for l in available_lessons]
        with col_v2:
            lesson_pick = st.selectbox(
                "Danh sách bài học chính thức:",
                ["✏️ [Tự nhập chủ đề tùy chỉnh...]"] + lesson_labels,
                key="sgk_pick_t1",
                on_change=sync_sgk_topic,
                args=("sgk_pick_t1", "input_topic_t1")
            )
            if lesson_pick != "✏️ [Tự nhập chủ đề tùy chỉnh...]":
                default_topic_t1 = lesson_pick.split("  (")[0]

    if "input_topic_t1" not in st.session_state or not st.session_state["input_topic_t1"].strip():
        st.session_state["input_topic_t1"] = default_topic_t1

    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        lesson_topic = st.text_input(
            "Tên bài học / Chủ đề (Có thể chỉnh sửa chi tiết):",
            key="input_topic_t1"
        )
    with col_t2:
        include_adv = st.checkbox("Thử thách HS khá giỏi", value=True, help="Tích hợp các câu hỏi mở và nhiệm vụ mở rộng tránh lặp lại SGK")

    # Đảm bảo topic không bao giờ rỗng
    final_topic_t1 = lesson_topic.strip() if lesson_topic.strip() else default_topic_t1

    # Hiển thị Trích dẫn Nội dung gốc từ Sách Giáo Khoa
    tb_detail_t1 = get_textbook_lesson_detail(selected_grade_num, final_topic_t1)
    if tb_detail_t1:
        with st.expander(f"📖 Trích Dẫn Nguyên Văn Từ SGK: {tb_detail_t1['title']} ({tb_detail_t1['page']})", expanded=True):
            st.markdown(f"**Vị trí:** `{tb_detail_t1['topic_group']}` • **Bộ sách:** *Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)*")
            st.markdown("##### 📌 Khái niệm & Quy tắc gốc trong SGK:")
            for c in tb_detail_t1.get("original_concepts", []):
                st.markdown(f"- {c}")
            st.markdown("##### 📝 Hoạt động khám phá & Bài tập mẫu gốc:")
            for e in tb_detail_t1.get("original_exercises", []):
                st.markdown(f"- {e}")

    if st.button("🚀 Tự Động Sinh Kế Hoạch Bài Dạy 2345", type="primary", key="btn_plan_2345"):
        with st.spinner(f"🔄 Đang phân tích Yêu cầu cần đạt SGK và xây dựng KHBD cho '{final_topic_t1}'..."):
            try:
                plan = generate_lesson_plan_2345(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=final_topic_t1,
                    advanced_focus=include_adv,
                    llm_client=llm_client
                )
                st.session_state["current_plan_2345"] = plan
                st.success("✅ Đã tạo Kế hoạch bài dạy thành công!")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

    if "current_plan_2345" in st.session_state:
        plan = st.session_state["current_plan_2345"]
        
        # Thanh công cụ Xuất File (Word & Google Docs Online)
        st.markdown("#### 📤 Xuất & Đồng Bộ Học Liệu:")
        col_d1, col_d2 = st.columns([1, 1])
        with col_d1:
            docx_data = create_lesson_plan_docx(plan)
            st.download_button(
                label="📥 Tải File Word (.docx)",
                data=docx_data,
                file_name=f"KHBD_{plan.subject}_Lop{selected_grade_num}_{final_topic_t1}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                help="Tải file Word có sẵn bảng biểu và màu sắc để mở trên Word hoặc kéo thả vào Google Drive"
            )
        with col_d2:
            st.link_button("🌐 Mở Google Docs Mới (docs.new)", url="https://docs.new", help="Mở một tài liệu Google Docs mới trên trình duyệt")
            
        with st.expander("📋 Sao Chép Bảng 5 Cột Cho Google Docs (Không Lỗi Format)", expanded=True):
            st.markdown("""
            <div style="background-color: #f0fdf4; border: 1px solid #86efac; border-left: 5px solid #16a34a; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px; color: #166534;">
                <strong>💡 Hướng dẫn dán vào Google Docs giữ 100% định dạng bảng:</strong><br>
                1. Bấm nút màu xanh <b>"📋 SAO CHÉP ĐỊNH DẠNG GOOGLE DOCS"</b> bên dưới.<br>
                2. Bấm nút <b>"🌐 Mở Google Docs Mới (docs.new)"</b> ở trên.<br>
                3. Nhấn <b>Ctrl + V</b> (hoặc Chuột phải &rarr; Dán) vào Google Docs &rarr; <i>Giáo án sẽ tự động chuyển thành bảng 5 cột có màu sắc, kẻ ô chuẩn đẹp!</i>
            </div>
            """, unsafe_allow_html=True)
            
            rich_html_content = export_lesson_plan_to_rich_html(plan)
            json_rich_html = json.dumps(rich_html_content)
            
            # Interactive Rich Clipboard Copy Component
            copy_widget_code = f"""
            <div style="font-family: Arial, sans-serif;">
                <button id="btn-copy-gdocs" onclick="copyRichText()" style="
                    background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);
                    color: #ffffff;
                    border: none;
                    padding: 12px 22px;
                    font-size: 14.5px;
                    font-weight: bold;
                    border-radius: 8px;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    box-shadow: 0 4px 10px rgba(22, 163, 74, 0.25);
                    transition: all 0.2s;
                ">
                    📋 BẤM VÀO ĐÂY ĐỂ SAO CHÉP ĐỊNH DẠNG GOOGLE DOCS
                </button>
                <div id="copy-status" style="display:none; margin-top: 10px; padding: 10px 14px; background-color: #dcfce7; border: 1.5px solid #4ade80; border-radius: 6px; color: #14532d; font-weight: bold; font-size: 14px;">
                    ✅ ĐÃ SAO CHÉP BẢNG 5 CỘT THÀNH CÔNG! Hãy mở Google Docs và bấm Ctrl + V.
                </div>
            </div>

            <script>
            function copyRichText() {{
                const htmlData = {json_rich_html};
                const plainText = htmlData.replace(/<style[^>]*>.*?<\\/style>/gs, '').replace(/<[^>]+>/g, ' ').replace(/\\s+/g, ' ').trim();
                
                if (navigator.clipboard && window.ClipboardItem) {{
                    const blobHtml = new Blob([htmlData], {{ type: 'text/html' }});
                    const blobText = new Blob([plainText], {{ type: 'text/plain' }});
                    const data = [new ClipboardItem({{ 'text/html': blobHtml, 'text/plain': blobText }})];
                    navigator.clipboard.write(data).then(() => {{
                        showSuccess();
                    }}).catch(err => {{
                        fallbackCopy(htmlData);
                    }});
                }} else {{
                    fallbackCopy(htmlData);
                }}
            }}

            function fallbackCopy(html) {{
                const div = document.createElement('div');
                div.innerHTML = html;
                div.style.position = 'fixed';
                div.style.left = '-9999px';
                document.body.appendChild(div);
                const range = document.createRange();
                range.selectNodeContents(div);
                const sel = window.getSelection();
                sel.removeAllRanges();
                sel.addRange(range);
                document.execCommand('copy');
                document.body.removeChild(div);
                showSuccess();
            }}

            function showSuccess() {{
                const status = document.getElementById('copy-status');
                status.style.display = 'block';
                const btn = document.getElementById('btn-copy-gdocs');
                btn.style.background = '#0f766e';
                btn.innerHTML = '✅ ĐÃ SAO CHÉP XONG!';
            }}
            </script>
            """
            components.html(copy_widget_code, height=95)
            
            st.markdown("##### 👁️ Xem trước bảng biểu định dạng Google Docs:")
            st.markdown(f"""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e1; max-height: 400px; overflow-y: auto; color: #000000;">
                {rich_html_content}
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"### 📋 Kế Hoạch Bài Dạy: {plan.lesson_title.upper()}")
        st.write(f"**Trường:** {plan.school_name} | **Khối lớp:** {plan.grade} | **Môn:** {plan.subject}")
        
        with st.expander("📌 I. YÊU CẦU CẦN ĐẠT (YCKĐN)", expanded=True):
            for req in plan.required_competencies:
                st.markdown(f"- {req}")
                
        with st.expander("🛠️ II. ĐỒ DÙNG DẠY HỌC & HỌC LIỆU SỐ", expanded=False):
            for eq in plan.teaching_equipment:
                st.markdown(f"- {eq}")

        st.markdown("### 📊 III. CÁC HOẠT ĐỘNG DẠY HỌC CHỦ YẾU (BẢNG 5 CỘT)")
        for i, act in enumerate(plan.activities, 1):
            st.markdown(f"#### 🔹 Hoạt động {i}: {act.activity_name}")
            col_a1, col_a2, col_a3 = st.columns(3)
            with col_a1:
                st.info(f"**Mục tiêu:**\n{act.objective}")
            with col_a2:
                st.warning(f"**Nội dung:**\n{act.content}")
            with col_a3:
                st.success(f"**Sản phẩm:**\n{act.product}")
                
            st.markdown("**Tổ chức thực hiện (4 bước chuẩn CV 2345):**")
            for step in act.implementation_steps:
                st.markdown(f"- **Bước {step.step_number} ({step.step_name}):**\n  - *Giáo viên:* {step.teacher_action}\n  - *Học sinh:* {step.student_action}")
                
            if act.advanced_extension:
                st.markdown(f"""
                <div class="advanced-challenge-box">
                    <span class="advanced-challenge-title">🌟 Thử thách mở rộng cho HS khá giỏi:</span>
                    <span class="advanced-challenge-content">{act.advanced_extension}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("---")

# ==========================================
# TAB 2: PHÂN HÓA NHIỆM VỤ 4 CẤP ĐỘ
# ==========================================
with tab2:
    st.subheader("🎯 Phân Hóa 4 Tầng Nhiệm Vụ Cho Học Sinh Khá Giỏi & Cần Hỗ Trợ")
    st.write("Từ 1 đơn vị kiến thức SGK, chia tách thành 4 tầng bài tập/nhiệm vụ với giàn giáo hỗ trợ (Scaffolding) phù hợp năng lực từng nhóm học sinh.")
    
    curriculum_list_t2 = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, 0)
    default_diff_t2 = curriculum_list_t2[0]["title"] if curriculum_list_t2 else "Bài học mới"
    if selected_grade_num == 3 and "math" in selected_subject_id.lower():
        default_diff_t2 = "Bài 18: Góc, góc vuông, góc không vuông"
    elif selected_grade_num == 5 and "math" in selected_subject_id.lower():
        default_diff_t2 = "Bài 28: Hình tam giác. Diện tích hình tam giác"
        
    if curriculum_list_t2:
        sub_name_vi = "Toán" if any(k in selected_subject_id.lower() for k in ["math", "toán"]) else "Tiếng Việt"
        st.markdown(f"##### 📚 Chọn Bài Học Từ SGK {sub_name_vi} Lớp {selected_grade_num}:")
        col_vd1, col_vd2 = st.columns([1, 3])
        with col_vd1:
            v_choice = st.selectbox("Chọn Tập:", ["Tất cả (Tập 1 & 2)", "Tập 1", "Tập 2"], key="vol_t2")
            v_idx = 1 if "Tập 1" in v_choice else (2 if "Tập 2" in v_choice else 0)
            avail_diff = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, v_idx)
            diff_labels = [f"{l['title']}  ({l['topic_group']})" for l in avail_diff]
        with col_vd2:
            p_pick = st.selectbox(
                "Danh sách bài học:",
                ["✏️ [Tự nhập chủ đề...]"] + diff_labels,
                key="sgk_pick_t2",
                on_change=sync_sgk_topic,
                args=("sgk_pick_t2", "input_diff_topic")
            )
            if p_pick != "✏️ [Tự nhập chủ đề...]":
                default_diff_t2 = p_pick.split("  (")[0]

    if "input_diff_topic" not in st.session_state or not st.session_state["input_diff_topic"].strip():
        st.session_state["input_diff_topic"] = default_diff_t2

    diff_topic = st.text_input(
        "Chủ đề / Đơn vị kiến thức cần phân hóa:",
        key="input_diff_topic"
    )
    
    final_topic_t2 = diff_topic.strip() if diff_topic.strip() else default_diff_t2

    tb_detail_t2 = get_textbook_lesson_detail(selected_grade_num, final_topic_t2)
    if tb_detail_t2:
        with st.expander(f"📖 Trích Dẫn Nguyên Văn Từ SGK: {tb_detail_t2['title']} ({tb_detail_t2['page']})", expanded=False):
            st.markdown(f"**Vị trí:** `{tb_detail_t2['topic_group']}` • **Bộ sách:** *Kết nối tri thức với cuộc sống*")
            st.markdown("##### 📌 Khái niệm & Quy tắc gốc:")
            for c in tb_detail_t2.get("original_concepts", []):
                st.markdown(f"- {c}")
            st.markdown("##### 📝 Hoạt động khám phá & Bài tập gốc:")
            for e in tb_detail_t2.get("original_exercises", []):
                st.markdown(f"- {e}")

    if st.button("✨ Thiết Kế 4 Tầng Nhiệm Vụ", type="primary", key="btn_differentiate"):
        with st.spinner(f"🔄 Đang thiết kế ma trận nhiệm vụ phân hóa 4 tầng cho '{final_topic_t2}'..."):
            try:
                taskset = generate_differentiated_taskset(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=final_topic_t2,
                    llm_client=llm_client
                )
                st.session_state["current_taskset"] = taskset
                st.success("✅ Đã thiết kế bộ nhiệm vụ phân hóa thành công!")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

    if "current_taskset" in st.session_state:
        ts = st.session_state["current_taskset"]
        st.markdown(f"### 📋 Bộ Nhiệm Vụ: {ts.topic.upper()} ({ts.grade} - Môn: {ts.subject})")
        st.caption(f"**Yêu cầu cần đạt cốt lõi:** {ts.core_competency}")
        
        for i, tier in enumerate(ts.tiers, 1):
            card_class = f"tier-card-{i}"
            st.markdown(f"""
            <div class="{card_class}">
                <h4 style="margin:0 0 8px 0;">📌 {tier.tier_name.upper()} (Đối tượng: {tier.target_student_group} • Mức Bloom: {tier.bloom_level})</h4>
                <p><strong>🛠️ Giàn giáo hỗ trợ:</strong> {tier.pedagogical_scaffolding}</p>
                <p><strong>📝 Nhiệm vụ giao cho HS:</strong> {tier.task_prompt}</p>
                <p><strong>✅ Sản phẩm kỳ vọng:</strong> {tier.expected_output}</p>
            </div>
            """, unsafe_allow_html=True)
            
        if ts.creative_challenge:
            st.markdown(f"""
            <div style="background-color: #fdf2f8; border: 1.5px solid #f472b6; border-left: 6px solid #db2777; border-radius: 8px; padding: 16px; margin-top: 14px; color: #0f172a;">
                <h4 style="color: #db2777; margin:0 0 6px 0; font-weight:700;">🚀 THỬ THÁCH SÁNG TẠO LIÊN MÔN / STEM</h4>
                <p style="color: #1e293b; font-size: 14.5px; font-weight: 500; margin:0;">{ts.creative_challenge}</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# TAB 3: TRỢ LÝ NHẬN XÉT HỌC SINH (THÔNG TƯ 27)
# ==========================================
with tab3:
    st.subheader("📊 Trợ Lý Đánh Giá & Nhận Xét Học Sinh Chuẩn Thông Tư 27/2020")
    st.write("Hỗ trợ viết nhận xét định tính có căn cứ, tích cực và cụ thể về Môn học, Năng lực cốt lõi và Phẩm chất chủ yếu.")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        student_alias = st.text_input("Mã học sinh (Ẩn danh):", value="HS08")
    with col_s2:
        eval_period = st.selectbox("Đợt đánh giá:", ["Giữa học kì I", "Cuối học kì I", "Giữa học kì II", "Cuối năm học"])
    with col_s3:
        pass
        
    student_notes = st.text_area(
        "Ghi chú thực tế của giáo viên về học sinh:",
        value="Học bài tích cực, tính nhẩm nhanh nhưng đôi lúc còn ẩu ở phép trừ có nhớ. Đọc to, diễn cảm, biết dùng từ gợi cảm trong tập làm văn. Rất hòa đồng và hay giúp đỡ bạn bè trong giờ học nhóm.",
        height=100
    )
    
    if st.button("✍️ Tạo Lời Nhận Xét Chuẩn Thông Tư 27", type="primary", key="btn_review_tt27"):
        with st.spinner("🔄 Đang phân tích dữ liệu và sinh lời nhận xét chuẩn mực..."):
            try:
                tt27_res = generate_tt27_assessment(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    student_alias=student_alias,
                    evaluation_notes=student_notes,
                    period=eval_period,
                    llm_client=llm_client
                )
                st.session_state["current_tt27"] = tt27_res
                st.success("✅ Đã sinh nhận xét Thông tư 27 thành công!")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

    if "current_tt27" in st.session_state:
        res = st.session_state["current_tt27"]
        st.markdown(f"### 📋 Bảng Đánh Giá Học Sinh: {res.student_alias} ({res.grade} • {res.evaluation_period})")
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.markdown("#### 1. Đánh giá Môn học & HĐGD")
            for sub in res.subject_evaluations:
                st.write(f"• **{sub.subject_name}** `[Mức: {sub.level}]`")
                st.write(f"  - *Điểm nổi bật:* {sub.strengths}")
                st.write(f"  - *Cần rèn luyện thêm:* {sub.improvements}")
                
            st.markdown("#### 2. Năng lực cốt lõi")
            for c in res.competency_evaluations:
                st.write(f"• **{c.competency_name}** `[{c.level}]`: {c.specific_evidence}")

        with col_r2:
            st.markdown("#### 3. Phẩm chất chủ yếu")
            for q in res.quality_evaluations:
                st.write(f"• **{q.quality_name}** `[{q.level}]`: {q.specific_evidence}")
                
            st.markdown("#### 💬 Lời nhận xét gửi Phụ huynh (Sao chép vào sổ liên lạc)")
            st.info(res.general_comment_for_parents)
            
            st.markdown("#### 🚀 Gợi ý nhiệm vụ tự học cá nhân hóa")
            for t in res.suggested_personalized_tasks:
                st.markdown(f"- {t}")

# ==========================================
# TAB 4: TRỢ GIẢNG AI SOCRATIC 24/7
# ==========================================
with tab4:
    st.subheader("💬 AI Socratic Tutor - Trợ Giảng Gợi Mở 24/7")
    st.write("Trò chuyện cùng các nhân vật ảo thân thiện. AI sử dụng phương pháp Socratic đặt câu hỏi dẫn dắt thay vì giải bài hộ.")
    
    col_c1, col_c2 = st.columns([1, 3])
    with col_c1:
        tutor_character = st.selectbox(
            "Chọn nhân vật Trợ giảng:",
            ["🦉 Bác Cú Thông Thái (Khoa học)", "🐰 Thỏ Trắng Dễ Thương (Lớp 1-2)", "👩‍🏫 Cô Giáo AI Dịu Dàng", "🔬 Nhà Bác Học Nhí (STEM)"]
        )
        if st.button("🗑️ Xóa Lịch Sử Chat", key="btn_clear_chat"):
            st.session_state["chat_messages"] = []
            st.rerun()
            
    with col_c2:
        if "chat_messages" not in st.session_state:
            st.session_state["chat_messages"] = [
                {"role": "assistant", "content": f"Xin chào bạn nhỏ! Mình là {tutor_character}. Hôm nay chúng mình cùng khám phá bài học gì nào? 🌟"}
            ]
            
        for msg in st.session_state["chat_messages"]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
        user_input = st.chat_input("Nhập câu hỏi của học sinh...")
        if user_input:
            st.session_state["chat_messages"].append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.write(user_input)
                
            with st.chat_message("assistant"):
                with st.spinner("Đang suy nghĩ câu hỏi gợi mở..."):
                    try:
                        reply = tutor_chat(
                            grade=selected_grade_num,
                            subject=selected_subject_id,
                            user_message=user_input,
                            conversation_history=st.session_state["chat_messages"][:-1],
                            llm_client=llm_client
                        )
                        st.write(reply)
                        st.session_state["chat_messages"].append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Lỗi: {str(e)}")

# ==========================================
# TAB 5: TẠO BỘ CÂU HỎI QUIZIZZ / WORDWALL
# ==========================================
with tab5:
    st.subheader("🎮 Tạo Bộ Câu Hỏi Trắc Nghiệm Đố Vui Cho Quizizz / Wordwall / Kahoot")
    st.write("Tự động sinh bộ câu hỏi trắc nghiệm đố vui và xuất ra file Excel chuẩn để nạp vào Quizizz chỉ trong 1 cú click.")
    
    curriculum_list_t5 = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, 0)
    default_quiz_t5 = curriculum_list_t5[0]["title"] if curriculum_list_t5 else "Bài học mới"
    if selected_grade_num == 3 and "math" in selected_subject_id.lower():
        default_quiz_t5 = "Bài 18: Góc, góc vuông, góc không vuông"
    elif selected_grade_num == 5 and "math" in selected_subject_id.lower():
        default_quiz_t5 = "Bài 28: Hình tam giác. Diện tích hình tam giác"
        
    if curriculum_list_t5:
        sub_name_vi = "Toán" if any(k in selected_subject_id.lower() for k in ["math", "toán"]) else "Tiếng Việt"
        st.markdown(f"##### 📚 Chọn Bài Học Từ SGK {sub_name_vi} Lớp {selected_grade_num}:")
        col_vq1, col_vq2 = st.columns([1, 3])
        with col_vq1:
            vq_choice = st.selectbox("Chọn Tập:", ["Tất cả (Tập 1 & 2)", "Tập 1", "Tập 2"], key="vol_t5")
            vq_idx = 1 if "Tập 1" in vq_choice else (2 if "Tập 2" in vq_choice else 0)
            avail_quiz = get_subject_curriculum_lessons(selected_subject_id, selected_grade_num, vq_idx)
            quiz_labels = [f"{l['title']}  ({l['topic_group']})" for l in avail_quiz]
        with col_vq2:
            q_pick = st.selectbox(
                "Danh sách bài học:",
                ["✏️ [Tự nhập chủ đề...]"] + quiz_labels,
                key="sgk_pick_t5",
                on_change=sync_sgk_topic,
                args=("sgk_pick_t5", "input_quiz_topic")
            )
            if q_pick != "✏️ [Tự nhập chủ đề...]":
                default_quiz_t5 = q_pick.split("  (")[0]

    if "input_quiz_topic" not in st.session_state or not st.session_state["input_quiz_topic"].strip():
        st.session_state["input_quiz_topic"] = default_quiz_t5

    col_q1, col_q2 = st.columns([3, 1])
    with col_q1:
        quiz_topic = st.text_input(
            "Chủ đề trò chơi trắc nghiệm:",
            key="input_quiz_topic"
        )
    with col_q2:
        num_q = st.slider("Số lượng câu hỏi:", min_value=3, max_value=10, value=5)
        
    final_topic_t5 = quiz_topic.strip() if quiz_topic.strip() else default_quiz_t5

    if st.button("🎲 Sinh Câu Hỏi Trắc Nghiệm Game", type="primary", key="btn_gen_quiz"):
        with st.spinner(f"🔄 Đang sinh bộ câu hỏi đố vui cho '{final_topic_t5}'..."):
            try:
                quiz_set = generate_quizizz_questions(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=final_topic_t5,
                    num_questions=num_q,
                    llm_client=llm_client
                )
                st.session_state["current_quiz_set"] = quiz_set
                st.success("✅ Đã tạo bộ câu hỏi thành công!")
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")
                
    if "current_quiz_set" in st.session_state:
        qs = st.session_state["current_quiz_set"]
        
        # Xuất Excel
        excel_data = export_quiz_to_excel(qs)
        st.download_button(
            label="📥 Tải File Excel Mẫu Chuẩn Quizizz (.xlsx)",
            data=excel_data,
            file_name=f"Quizizz_{qs.subject}_Lop{selected_grade_num}_{final_topic_t5}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        st.markdown(f"### 📋 Xem Trước Bộ Câu Hỏi: {qs.title}")
        for idx, q in enumerate(qs.questions, 1):
            with st.expander(f"Câu {idx}: {q.question} (Thời gian: {q.time_in_seconds}s)"):
                st.write(f"- A. {q.option1}")
                st.write(f"- B. {q.option2}")
                st.write(f"- C. {q.option3}")
                st.write(f"- D. {q.option4}")
                st.success(f"**Đáp án đúng:** Phương án {q.correct_option_number}")
                st.info(f"💡 **Giải thích:** {q.explanation}")
