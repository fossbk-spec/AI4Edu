import argparse
import sys
import json
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.services.lesson_planner import generate_structured_lesson_plan, generate_markdown_lesson_plan
from ai4edu.services.ai_tutor import tutor_chat
from ai4edu.services.auto_grader import grade_student_submission
from ai4edu.services.hoang_mai_service import (
    generate_lesson_plan_2345,
    generate_differentiated_taskset,
    generate_tt27_assessment
)

# Đảm bảo UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def handle_list_grades(args):
    engine = PromptEngine()
    print("\n🎓 ================= DANH MỤC KHUNG CHƯƠNG TRÌNH K-12 (AI4Edu) =================")
    for level in engine.matrix.levels:
        print(f"\n📌 {level.name.upper()} ({level.age_range}) - {level.pedagogical_focus}")
        print("-" * 75)
        for g_num in level.grades:
            grade = engine.get_grade(g_num)
            if grade:
                subject_names = [f"{s.name} ({s.id})" for s in grade.subjects]
                print(f"  • {grade.name} (ID: {grade.id}):")
                print(f"    - Nhận thức: {grade.cognitive_stage}")
                print(f"    - Môn học: {', '.join(subject_names)}")
    print("\n" + "=" * 75 + "\n")

def handle_plan(args):
    print(f"\n🔄 Đang tạo Kế hoạch Bài dạy 5E cho {args.grade} | Môn: {args.subject} | Chủ đề: '{args.topic}'...")
    if args.json:
        plan = generate_structured_lesson_plan(
            grade=args.grade,
            subject=args.subject,
            topic=args.topic,
            duration_minutes=args.duration
        )
        print(json.dumps(plan.model_dump(), indent=2, ensure_ascii=False))
    else:
        markdown_plan = generate_markdown_lesson_plan(
            grade=args.grade,
            subject=args.subject,
            topic=args.topic,
            duration_minutes=args.duration
        )
        print("\n" + markdown_plan)

def handle_plan_2345(args):
    print(f"\n🏫 [TRƯỜNG TIỂU HỌC HOÀNG MAI] Đang soạn KHBD 5 cột (Công văn 2345) cho Lớp {args.grade} | Môn: {args.subject} | Bài: '{args.topic}'...")
    plan = generate_lesson_plan_2345(
        grade=args.grade,
        subject=args.subject,
        topic=args.topic,
        advanced_focus=args.advanced
    )
    if args.json:
        print(json.dumps(plan.model_dump(), indent=2, ensure_ascii=False))
    else:
        print(f"\n# KẾ HOẠCH BÀI DẠY: {plan.lesson_title.upper()}")
        print(f"**Trường:** {plan.school_name} | **Khối lớp:** {plan.grade} | **Môn học:** {plan.subject}")
        print("\n### I. YÊU CẦU CẦN ĐẠT:")
        for req in plan.required_competencies:
            print(f"- {req}")
        print("\n### II. ĐỒ DÙNG DẠY HỌC & HỌC LIỆU SỐ:")
        for eq in plan.teaching_equipment:
            print(f"- {eq}")
        print("\n### III. CÁC HOẠT ĐỘNG DẠY HỌC CHỦ YẾU (5 CỘT CV 2345):")
        for i, act in enumerate(plan.activities, 1):
            print(f"\n--- Hoạt động {i}: {act.activity_name} ---")
            print(f"• **Mục tiêu:** {act.objective}")
            print(f"• **Nội dung:** {act.content}")
            print(f"• **Sản phẩm:** {act.product}")
            print("• **Tổ chức thực hiện (4 bước):**")
            for step in act.implementation_steps:
                print(f"  + Bước {step.step_number} ({step.step_name}): GV: {step.teacher_action} | HS: {step.student_action}")
            if act.advanced_extension:
                print(f"• 🌟 **Thử thách nâng cao (HS khá giỏi):** {act.advanced_extension}")
        print(f"\n### IV. GHI CHÚ PHÂN HÓA:")
        print(plan.differentiation_notes)

def handle_differentiate(args):
    print(f"\n🎯 [TIỂU HỌC HOÀNG MAI] Đang tạo 4 tầng nhiệm vụ phân hóa cho Lớp {args.grade} | Môn: {args.subject} | Chủ đề: '{args.topic}'...")
    taskset = generate_differentiated_taskset(
        grade=args.grade,
        subject=args.subject,
        topic=args.topic
    )
    if args.json:
        print(json.dumps(taskset.model_dump(), indent=2, ensure_ascii=False))
    else:
        print(f"\n# BỘ NHIỆM VỤ HỌC TẬP PHÂN HÓA: {taskset.topic.upper()}")
        print(f"**Môn:** {taskset.subject} ({taskset.grade}) | **YCKĐN:** {taskset.core_competency}\n")
        for tier in taskset.tiers:
            print(f"📌 **[{tier.tier_name.upper()}]** (Đối tượng: {tier.target_student_group} - Cấp độ: {tier.bloom_level})")
            print(f"  • **Giàn giáo hỗ trợ:** {tier.pedagogical_scaffolding}")
            print(f"  • **Nhiệm vụ:** {tier.task_prompt}")
            print(f"  • **Sản phẩm kỳ vọng:** {tier.expected_output}\n")
        if taskset.creative_challenge:
            print(f"🚀 **THỬ THÁCH SÁNG TẠO LIÊN MÔN / STEM:**\n{taskset.creative_challenge}\n")

def handle_review_tt27(args):
    print(f"\n📝 [TIỂU HỌC HOÀNG MAI] Đang sinh nhận xét Thông tư 27 cho học sinh {args.alias} (Lớp {args.grade} - Môn: {args.subject})...")
    result = generate_tt27_assessment(
        grade=args.grade,
        subject=args.subject,
        student_alias=args.alias,
        evaluation_notes=args.notes,
        period=args.period
    )
    if args.json:
        print(json.dumps(result.model_dump(), indent=2, ensure_ascii=False))
    else:
        print(f"\n📊 BẢNG ĐÁNH GIÁ HỌC SINH TIỂU HỌC (THÔNG TƯ 27/2020)")
        print(f"**Học sinh:** {result.student_alias} | **Khối lớp:** {result.grade} | **Đợt:** {result.evaluation_period}")
        print("\n1. ĐÁNH GIÁ MÔN HỌC:")
        for s in result.subject_evaluations:
            print(f"  • {s.subject_name} [Mức: {s.level}]: Điểm nổi bật: {s.strengths} | Cần hỗ trợ: {s.improvements}")
        print("\n2. NĂNG LỰC CỐT LÕI:")
        for c in result.competency_evaluations:
            print(f"  • {c.competency_name} [{c.level}]: {c.specific_evidence}")
        print("\n3. PHẨM CHẤT CHỦ YẾU:")
        for q in result.quality_evaluations:
            print(f"  • {q.quality_name} [{q.level}]: {q.specific_evidence}")
        print(f"\n💬 LỜI NHẬN XÉT GỬI PHỤ HUYNH:\n\"{result.general_comment_for_parents}\"")
        print("\n🚀 NHIỆM VỤ TỰ HỌC GỢI Ý:")
        for t in result.suggested_personalized_tasks:
            print(f"  -> {t}")

def handle_tutor(args):
    print(f"\n💬 [AI Tutor - Lớp {args.grade}{f' - {args.subject}' if args.subject else ''}]")
    print(f"👤 Học sinh: {args.message}\n")
    reply = tutor_chat(
        grade=args.grade,
        subject=args.subject,
        user_message=args.message
    )
    print(f"🤖 Trợ giảng AI:\n{reply}\n")

def handle_grade(args):
    print(f"\n📝 Đang chấm bài cho Lớp {args.grade} | Môn: {args.subject}...")
    result = grade_student_submission(
        grade=args.grade,
        subject=args.subject,
        assignment_prompt=args.prompt,
        student_work=args.work,
        rubric_guidelines=args.rubric
    )
    print(f"\n📊 KẾT QUẢ ĐÁNH GIÁ (Tổng điểm: {result.overall_score}/10)")
    print(f"💬 Nhận xét chung: {result.general_comment}")
    print("\n🌟 Điểm mạnh:")
    for s in result.strengths:
        print(f"  + {s}")
    print("\n⚠️ Cần cải thiện:")
    for a in result.areas_for_improvement:
        print(f"  - {a}")
    if result.criteria_breakdown:
        print("\n📋 Chi tiết theo Rubric:")
        for c in result.criteria_breakdown:
            print(f"  • {c.criterion_name} ({c.score_achieved}/{c.max_score}đ - {c.weight_percentage}%): {c.feedback}")
    print("\n🚀 Đề xuất bước tiếp theo:")
    for step in result.suggested_next_steps:
        print(f"  -> {step}")

def main():
    parser = argparse.ArgumentParser(
        description="AI4Edu CLI - Công cụ điều hành AI cho Giáo dục K-12 & Trường Tiểu học Hoàng Mai",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Lệnh chức năng")

    # Lệnh: list-grades
    subparsers.add_parser("list-grades", help="Hiển thị danh mục 12 khối lớp và môn học")

    # Lệnh: plan (5E chung)
    plan_parser = subparsers.add_parser("plan", help="Sinh giáo án 5E chung theo lớp và môn học")
    plan_parser.add_argument("--grade", type=int, required=True, help="Khối lớp (1-12)")
    plan_parser.add_argument("--subject", type=str, required=True, help="Mã môn học")
    plan_parser.add_argument("--topic", type=str, required=True, help="Chủ đề bài dạy")
    plan_parser.add_argument("--duration", type=int, default=45, help="Thời lượng bài học (phút)")
    plan_parser.add_argument("--json", action="store_true", help="Xuất định dạng Pydantic JSON")

    # Lệnh: plan-2345 (Chuyên biệt Tiểu học Hoàng Mai chuẩn CV 2345)
    p2345_parser = subparsers.add_parser("plan-2345", help="[Hoàng Mai] Sinh KHBD 5 cột chuẩn Công văn 2345")
    p2345_parser.add_argument("--grade", type=int, required=True, help="Khối lớp tiểu học (1-5)")
    p2345_parser.add_argument("--subject", type=str, required=True, help="Môn học (math, vietnamese, science, nature_society...)")
    p2345_parser.add_argument("--topic", type=str, required=True, help="Tên bài học")
    p2345_parser.add_argument("--advanced", action="store_true", default=True, help="Bao gồm nhiệm vụ mở rộng cho HS khá giỏi")
    p2345_parser.add_argument("--json", action="store_true", help="Xuất định dạng JSON")

    # Lệnh: differentiate (Phân hóa 4 tầng nhiệm vụ)
    diff_parser = subparsers.add_parser("differentiate", help="[Hoàng Mai] Sinh 4 tầng nhiệm vụ phân hóa năng lực")
    diff_parser.add_argument("--grade", type=int, required=True, help="Khối lớp (1-5)")
    diff_parser.add_argument("--subject", type=str, required=True, help="Môn học")
    diff_parser.add_argument("--topic", type=str, required=True, help="Chủ đề kiến thức")
    diff_parser.add_argument("--json", action="store_true", help="Xuất định dạng JSON")

    # Lệnh: review-tt27 (Nhận xét Thông tư 27)
    tt27_parser = subparsers.add_parser("review-tt27", help="[Hoàng Mai] Sinh nhận xét học sinh chuẩn Thông tư 27/2020")
    tt27_parser.add_argument("--grade", type=int, required=True, help="Khối lớp (1-5)")
    tt27_parser.add_argument("--subject", type=str, required=True, help="Môn học")
    tt27_parser.add_argument("--alias", type=str, default="HS01", help="Mã ẩn danh học sinh")
    tt27_parser.add_argument("--notes", type=str, required=True, help="Ghi chú thực tế của giáo viên về học sinh")
    tt27_parser.add_argument("--period", type=str, default="Cuối học kì I", help="Đợt đánh giá")
    tt27_parser.add_argument("--json", action="store_true", help="Xuất định dạng JSON")

    # Lệnh: tutor
    tutor_parser = subparsers.add_parser("tutor", help="Trò chuyện với AI Socratic Tutor")
    tutor_parser.add_argument("--grade", type=int, required=True, help="Khối lớp (1-12)")
    tutor_parser.add_argument("--subject", type=str, default=None, help="Môn học (tùy chọn)")
    tutor_parser.add_argument("--message", type=str, required=True, help="Câu hỏi của học sinh")

    # Lệnh: grade
    grade_parser = subparsers.add_parser("grade", help="Chấm bài và sinh phản hồi định hình")
    grade_parser.add_argument("--grade", type=int, required=True, help="Khối lớp (1-12)")
    grade_parser.add_argument("--subject", type=str, required=True, help="Môn học")
    grade_parser.add_argument("--prompt", type=str, required=True, help="Đề bài đã giao")
    grade_parser.add_argument("--work", type=str, required=True, help="Nội dung bài làm của học sinh")
    grade_parser.add_argument("--rubric", type=str, default=None, help="Hướng dẫn chấm điểm rubric")

    args = parser.parse_args()

    if args.command == "list-grades":
        handle_list_grades(args)
    elif args.command == "plan":
        handle_plan(args)
    elif args.command == "plan-2345":
        handle_plan_2345(args)
    elif args.command == "differentiate":
        handle_differentiate(args)
    elif args.command == "review-tt27":
        handle_review_tt27(args)
    elif args.command == "tutor":
        handle_tutor(args)
    elif args.command == "grade":
        handle_grade(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
