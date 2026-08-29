from ai4edu.models.lesson_plan_2345 import LessonPlan2345

def export_lesson_plan_to_rich_html(plan: LessonPlan2345) -> str:
    """
    Sinh mã HTML chuẩn phong cách văn bản sư phạm Google Docs / Microsoft Word.
    Bao gồm bảng biểu 5 cột chuẩn, định dạng heading, màu sắc viền và ô tiêu đề.
    """
    activities_html = []
    for act in plan.activities:
        steps_list = "".join([
            f"<p style='margin: 4px 0;'><b>Bước {s.step_number} ({s.step_name}):</b><br>"
            f"• <i>Giáo viên:</i> {s.teacher_action}<br>"
            f"• <i>Học sinh:</i> {s.student_action}</p>"
            for s in act.implementation_steps
        ])
        
        adv_html = ""
        if act.advanced_extension:
            adv_html = (
                f"<div style='background-color: #fffbeb; border-left: 4px solid #d97706; padding: 6px 10px; margin-top: 6px; font-size: 10.5pt; color: #92400e;'>"
                f"<b>🌟 Thử thách HS khá giỏi:</b> {act.advanced_extension}"
                f"</div>"
            )
            
        activities_html.append(f"""
        <tr>
            <td style="border: 1px solid #94a3b8; padding: 8px; vertical-align: top; font-weight: bold; width: 14%; color: #0f172a; background-color: #f8fafc;">
                {act.activity_name}
            </td>
            <td style="border: 1px solid #94a3b8; padding: 8px; vertical-align: top; width: 18%; color: #1e293b;">
                {act.objective.replace(chr(10), '<br>')}
            </td>
            <td style="border: 1px solid #94a3b8; padding: 8px; vertical-align: top; width: 20%; color: #1e293b;">
                {act.content.replace(chr(10), '<br>')}
            </td>
            <td style="border: 1px solid #94a3b8; padding: 8px; vertical-align: top; width: 18%; color: #1e293b;">
                {act.product.replace(chr(10), '<br>')}
            </td>
            <td style="border: 1px solid #94a3b8; padding: 8px; vertical-align: top; width: 30%; color: #1e293b;">
                {steps_list}
                {adv_html}
            </td>
        </tr>
        """)
        
    activities_rows = "".join(activities_html)
    
    req_list = "".join([f"<li style='margin-bottom: 4px;'>{r}</li>" for r in plan.required_competencies])
    eq_list = "".join([f"<li style='margin-bottom: 4px;'>{e}</li>" for e in plan.teaching_equipment])
    
    diff_html = ""
    if plan.differentiation_notes:
        diff_html = f"""
        <h3 style="color: #0b57d0; font-size: 13pt; margin-top: 18px; margin-bottom: 6px;">IV. ĐIỀU CHỈNH SAU BÀI DẠY & GHI CHÚ PHÂN HÓA</h3>
        <p style="color: #1e293b; line-height: 1.5;">{plan.differentiation_notes}</p>
        """

    html_document = f"""<div style="font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #000000; max-width: 900px; margin: auto;">
    <div style="text-align: center; margin-bottom: 16px;">
        <p style="margin: 0; font-size: 11pt; font-weight: bold; text-transform: uppercase; color: #1e40af;">{plan.school_name.upper()}</p>
        <h1 style="margin: 6px 0; font-size: 16pt; color: #0b57d0; text-transform: uppercase;">KẾ HOẠCH BÀI DẠY: {plan.lesson_title.upper()}</h1>
        <p style="margin: 0; font-size: 11pt; font-style: italic;">Khối lớp: {plan.grade} | Môn học: {plan.subject}</p>
    </div>

    <h3 style="color: #0b57d0; font-size: 13pt; margin-top: 14px; margin-bottom: 6px; border-bottom: 1.5px solid #0b57d0; padding-bottom: 4px;">I. YÊU CẦU CẦN ĐẠT (YCKĐN)</h3>
    <ul style="margin-top: 4px; padding-left: 24px; color: #1e293b;">
        {req_list}
    </ul>

    <h3 style="color: #0b57d0; font-size: 13pt; margin-top: 14px; margin-bottom: 6px; border-bottom: 1.5px solid #0b57d0; padding-bottom: 4px;">II. ĐỒ DÙNG DẠY HỌC & THIẾT BỊ SỐ</h3>
    <ul style="margin-top: 4px; padding-left: 24px; color: #1e293b;">
        {eq_list}
    </ul>

    <h3 style="color: #0b57d0; font-size: 13pt; margin-top: 14px; margin-bottom: 6px; border-bottom: 1.5px solid #0b57d0; padding-bottom: 4px;">III. CÁC HOẠT ĐỘNG DẠY HỌC CHỦ YẾU (BẢNG 5 CỘT CHUẨN CÔNG VĂN 2345)</h3>
    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; font-size: 10.5pt; border: 1px solid #94a3b8; margin-top: 8px;">
        <thead>
            <tr style="background-color: #0b57d0; color: #ffffff; text-align: center; font-weight: bold;">
                <th style="border: 1px solid #94a3b8; padding: 10px; width: 14%;">Hoạt động học</th>
                <th style="border: 1px solid #94a3b8; padding: 10px; width: 18%;">Mục tiêu</th>
                <th style="border: 1px solid #94a3b8; padding: 10px; width: 20%;">Nội dung</th>
                <th style="border: 1px solid #94a3b8; padding: 10px; width: 18%;">Sản phẩm</th>
                <th style="border: 1px solid #94a3b8; padding: 10px; width: 30%;">Tổ chức thực hiện (4 bước)</th>
            </tr>
        </thead>
        <tbody>
            {activities_rows}
        </tbody>
    </table>

    {diff_html}
</div>"""
    return html_document
