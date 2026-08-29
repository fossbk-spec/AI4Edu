from ai4edu.models.lesson_plan_2345 import LessonPlan2345

def export_lesson_plan_to_markdown_for_gdocs(plan: LessonPlan2345) -> str:
    """
    Chuyển đổi Kế hoạch bài dạy 5 cột sang Markdown / Text chuẩn đẹp
    để giáo viên sao chép trực tiếp vào Google Docs (docs.new).
    """
    md = []
    md.append(f"# KẾ HOẠCH BÀI DẠY: {plan.lesson_title.upper()}")
    md.append(f"**Trường:** {plan.school_name} | **Khối lớp:** {plan.grade} | **Môn học:** {plan.subject}\n")
    
    md.append("## I. YÊU CẦU CẦN ĐẠT (YCKĐN)")
    for req in plan.required_competencies:
        md.append(f"- {req}")
    md.append("")
    
    md.append("## II. ĐỒ DÙNG DẠY HỌC & HỌC LIỆU SỐ")
    for eq in plan.teaching_equipment:
        md.append(f"- {eq}")
    md.append("")
    
    md.append("## III. CÁC HOẠT ĐỘNG DẠY HỌC CHỦ YẾU (BẢNG 5 CỘT CHUẨN CÔNG VĂN 2345)")
    md.append("| Hoạt động học | Mục tiêu | Nội dung | Sản phẩm | Tổ chức thực hiện (4 bước) |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for act in plan.activities:
        steps_text = "<br>".join([
            f"<b>Bước {s.step_number} ({s.step_name}):</b><br>• GV: {s.teacher_action}<br>• HS: {s.student_action}"
            for s in act.implementation_steps
        ])
        if act.advanced_extension:
            steps_text += f"<br><br><b>🌟 Thử thách HS khá giỏi:</b> {act.advanced_extension}"
            
        # Clean newlines for markdown table
        obj_clean = act.objective.replace("\n", "<br>")
        content_clean = act.content.replace("\n", "<br>")
        prod_clean = act.product.replace("\n", "<br>")
        
        md.append(f"| **{act.activity_name}** | {obj_clean} | {content_clean} | {prod_clean} | {steps_text} |")
        
    md.append("")
    if plan.differentiation_notes:
        md.append("## IV. ĐIỀU CHỈNH SAU BÀI DẠY & GHI CHÚ PHÂN HÓA")
        md.append(plan.differentiation_notes)
        
    return "\n".join(md)
