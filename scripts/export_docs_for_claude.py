"""
Script gom toàn bộ tài liệu Markdown trong docs/ thành 1 file ngữ cảnh duy nhất
để tải lên Claude.ai thẩm định tính khoa học và chính xác.
"""
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "AI4Edu_Full_Context_for_Claude.md")

def bundle_docs():
    docs_path = os.path.abspath(DOCS_DIR)
    output_path = os.path.abspath(OUTPUT_FILE)
    
    collected_files = []
    for root, _, files in os.walk(docs_path):
        for f in sorted(files):
            if f.endswith(".md"):
                collected_files.append(os.path.join(root, f))
                
    collected_files.sort()
    
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("# BỘ TÀI LIỆU DỰ ÁN AI4EDU - DÀNH CHO THẨM ĐỊNH KHOA HỌC VÀ CHÍNH XÁC\n\n")
        out.write(f"Tổng số tài liệu: {len(collected_files)} files\n\n")
        out.write("=" * 80 + "\n\n")
        
        for file_path in collected_files:
            rel_path = os.path.relpath(file_path, os.path.join(docs_path, ".."))
            out.write(f"## FILE: {rel_path}\n\n")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            out.write(content + "\n\n")
            out.write("-" * 80 + "\n\n")
            
    print(f"✅ Đã gom thành công {len(collected_files)} file tài liệu vào:")
    print(f"👉 {output_path}")
    print("Bạn có thể kéo thả file này trực tiếp vào Claude.ai để thẩm định!")

if __name__ == "__main__":
    bundle_docs()
