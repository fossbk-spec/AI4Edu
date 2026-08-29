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
from ai4edu.data.math_curriculum import get_math_lessons
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

# Nạp danh mục chương trình từ PromptEngine
engine = PromptEngine()

# Header Banner
st.markdown("""
<div class="main-header">
    <div class="badge-hm">🏫 TRƯỜNG TIỂU HỌC HOÀNG MAI • CHẤT LƯỢNG CAO & ĐỔI MỚI SÁNG TẠO</div>
    <h1>🎓 AI4Edu Hub - Trợ Lý AI Giáo Dục Đa Mô Hình (Gemini / Claude / GPT)</h1>
    <p>Tích hợp trọn bộ danh mục bài học SGK Toán Lớp 3 & Lớp 5 (Tập 1, 2) • Soạn KHBD 5 cột • Phân hóa 4 tầng • Xuất Google Docs / Word.</p>
</div>
""", unsafe_allow_html=True)

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
        index=2 if 3 in grade_options else 0, # Mặc định chọn Lớp 3 hoặc 5
        format_func=lambda x: f"Khối Lớp {x}"
    )
    
    grade_info = engine.get_grade(selected_grade_num)
    
    subject_map = {s.id: s.name for s in grade_info.subjects} if grade_info else {}
    selected_subject_id = st.selectbox(
        "Chọn Môn Học:",
        list(subject_map.keys()),
        format_func=lambda x: subject_map.get(x, x)
    )
    
    st.markdown("---")
    st.markdown("### 🤖 Chọn AI Model")
    
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
    
    # Quản lý API Key cho từng Provider
    active_api_key = None
    if "Gemini" in selected_provider:
        env_key = os.getenv("GEMINI_API_KEY")
        if env_key:
            st.success("✅ Gemini API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có GEMINI_API_KEY")
            active_api_key = st.text_input("Nhập Gemini API Key:", type="password")
            if active_api_key:
                os.environ["GEMINI_API_KEY"] = active_api_key
    elif "Claude" in selected_provider or "Anthropic" in selected_provider:
        env_key = os.getenv("ANTHROPIC_API_KEY")
        if env_key:
            st.success("✅ Anthropic Claude API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có ANTHROPIC_API_KEY")
            active_api_key = st.text_input("Nhập Claude API Key:", type="password")
            if active_api_key:
                os.environ["ANTHROPIC_API_KEY"] = active_api_key
    elif "OpenAI" in selected_provider:
        env_key = os.getenv("OPENAI_API_KEY")
        if env_key:
            st.success("✅ OpenAI API Key: Đã sẵn sàng")
            active_api_key = env_key
        else:
            st.warning("⚠️ Chưa có OPENAI_API_KEY")
            active_api_key = st.text_input("Nhập OpenAI API Key:", type="password")
            if active_api_key:
                os.environ["OPENAI_API_KEY"] = active_api_key

    st.markdown("---")
    st.markdown("### 📌 Chuẩn Sư Phạm")
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
    
    # Bộ chọn bài học từ SGK nếu là Toán Lớp 3 hoặc Lớp 5
    selected_topic_default = "Hình vuông - Hình tròn"
    if selected_subject_id == "math" and selected_grade_num in [3, 5]:
        st.markdown(f"##### 📚 Chọn Bài Học Từ Danh Mục SGK Toán Lớp {selected_grade_num} (Chuẩn CTGDPT 2018):")
        col_v1, col_v2 = st.columns([1, 3])
        with col_v1:
            vol_choice = st.selectbox("Chọn Tập sách:", ["Tất cả (Tập 1 & 2)", "Tập 1 (HK I)", "Tập 2 (HK II)"], key="vol_t1")
            vol_idx = 1 if "Tập 1" in vol_choice else (2 if "Tập 2" in vol_choice else 0)
            available_lessons = get_math_lessons(selected_grade_num, vol_idx)
            lesson_labels = [f"{l['title']}  ({l['topic_group']})" for l in available_lessons]
        with col_v2:
            lesson_pick = st.selectbox(
                "Danh sách bài học chính thức:",
                ["✏️ [Tự nhập chủ đề tùy chỉnh...]"] + lesson_labels,
                key="sgk_pick_t1"
            )
        if lesson_pick != "✏️ [Tự nhập chủ đề tùy chỉnh...]":
            # Trích xuất tên bài
            selected_topic_default = lesson_pick.split("  (")[0]
        else:
            selected_topic_default = "Diện tích hình thang" if selected_grade_num == 5 else "Bảng nhân 7, bảng chia 7"

    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        lesson_topic = st.text_input(
            "Tên bài học / Chủ đề (Có thể chỉnh sửa chi tiết):",
            value=selected_topic_default,
            key="input_topic_t1"
        )
    with col_t2:
        include_adv = st.checkbox("Thử thách HS khá giỏi", value=True, help="Tích hợp các câu hỏi mở và nhiệm vụ mở rộng tránh lặp lại SGK")

    if st.button("🚀 Tự Động Sinh Kế Hoạch Bài Dạy 2345", type="primary", key="btn_plan_2345"):
        with st.spinner("🔄 Đang phân tích Yêu cầu cần đạt và xây dựng Kế hoạch bài dạy 5 cột..."):
            try:
                plan = generate_lesson_plan_2345(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=lesson_topic,
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
                file_name=f"KHBD_{plan.subject}_Lop{selected_grade_num}_{lesson_topic}.docx",
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
    st.write("Từ 1 đơn vị kiến thức, chia tách thành 4 tầng bài tập/nhiệm vụ với giàn giáo hỗ trợ (Scaffolding) phù hợp năng lực từng nhóm học sinh.")
    
    diff_topic_default = "Diện tích hình thang" if selected_grade_num == 5 else "Cộng trừ có nhớ trong phạm vi 100"
    if selected_subject_id == "math" and selected_grade_num in [3, 5]:
        st.markdown(f"##### 📚 Chọn Bài Học Từ SGK Toán Lớp {selected_grade_num}:")
        col_vd1, col_vd2 = st.columns([1, 3])
        with col_vd1:
            v_choice = st.selectbox("Chọn Tập:", ["Tất cả (Tập 1 & 2)", "Tập 1", "Tập 2"], key="vol_t2")
            v_idx = 1 if "Tập 1" in v_choice else (2 if "Tập 2" in v_choice else 0)
            avail_diff = get_math_lessons(selected_grade_num, v_idx)
            diff_labels = [f"{l['title']}  ({l['topic_group']})" for l in avail_diff]
        with col_vd2:
            p_pick = st.selectbox("Danh sách bài học:", ["✏️ [Tự nhập chủ đề...]"] + diff_labels, key="sgk_pick_t2")
        if p_pick != "✏️ [Tự nhập chủ đề...]":
            diff_topic_default = p_pick.split("  (")[0]

    diff_topic = st.text_input(
        "Chủ đề / Đơn vị kiến thức cần phân hóa:",
        value=diff_topic_default,
        key="input_diff_topic"
    )
    
    if st.button("✨ Thiết Kế 4 Tầng Nhiệm Vụ", type="primary", key="btn_differentiate"):
        with st.spinner("🔄 Đang thiết kế ma trận nhiệm vụ phân hóa 4 tầng..."):
            try:
                taskset = generate_differentiated_taskset(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=diff_topic,
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
    
    quiz_topic_default = "Bài 23: Hình thang. Diện tích hình thang" if selected_grade_num == 5 else "Bài 10: Bảng nhân 7, bảng chia 7"
    if selected_subject_id == "math" and selected_grade_num in [3, 5]:
        st.markdown(f"##### 📚 Chọn Bài Học Từ SGK Toán Lớp {selected_grade_num}:")
        col_vq1, col_vq2 = st.columns([1, 3])
        with col_vq1:
            vq_choice = st.selectbox("Chọn Tập:", ["Tất cả (Tập 1 & 2)", "Tập 1", "Tập 2"], key="vol_t5")
            vq_idx = 1 if "Tập 1" in vq_choice else (2 if "Tập 2" in vq_choice else 0)
            avail_quiz = get_math_lessons(selected_grade_num, vq_idx)
            quiz_labels = [f"{l['title']}  ({l['topic_group']})" for l in avail_quiz]
        with col_vq2:
            q_pick = st.selectbox("Danh sách bài học:", ["✏️ [Tự nhập chủ đề...]"] + quiz_labels, key="sgk_pick_t5")
        if q_pick != "✏️ [Tự nhập chủ đề...]":
            quiz_topic_default = q_pick.split("  (")[0]

    col_q1, col_q2 = st.columns([3, 1])
    with col_q1:
        quiz_topic = st.text_input(
            "Chủ đề trò chơi trắc nghiệm:",
            value=quiz_topic_default,
            key="input_quiz_topic"
        )
    with col_q2:
        num_q = st.slider("Số lượng câu hỏi:", min_value=3, max_value=10, value=5)
        
    if st.button("🎲 Sinh Câu Hỏi Trắc Nghiệm Game", type="primary", key="btn_gen_quiz"):
        with st.spinner("🔄 Đang sinh bộ câu hỏi đố vui hấp dẫn..."):
            try:
                quiz_set = generate_quizizz_questions(
                    grade=selected_grade_num,
                    subject=selected_subject_id,
                    topic=quiz_topic,
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
            file_name=f"Quizizz_{qs.subject}_Lop{selected_grade_num}_{quiz_topic}.xlsx",
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
