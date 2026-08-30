import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'AI4Edu Hub',
  description: 'Bộ tài liệu & mã nguồn hướng dẫn ứng dụng Trí tuệ nhân tạo (AI) trong Giáo dục K-12 & Tiểu học Hoàng Mai',
  lang: 'vi-VN',
  cleanUrls: true,
  themeConfig: {
    logo: '🎓',
    siteTitle: 'AI4Edu Hub',
    nav: [
      { text: 'Trang chủ', link: '/' },
      { text: '📖 Hướng Dẫn Sử Dụng', link: '/user-guide/' },
      { text: '🏫 Tiểu học Hoàng Mai', link: '/hoang-mai-primary/' },
      { text: 'Khung K-12 (Lớp 1-12)', link: '/curriculum/' },
      { text: 'Ứng dụng Chung', link: '/applications/ai-tutor' },
      { text: 'Prompting', link: '/prompt-engineering/basic-prompts' },
      { text: 'Thực hành Code', link: '/hands-on/setup-gemini-api' }
    ],
    sidebar: [
      {
        text: '📖 1. Hướng Dẫn Sử Dụng AI4Edu Hub',
        collapsed: false,
        items: [
          { text: '🌟 Cẩm Nang Sử Dụng Tổng Quan', link: '/user-guide/' },
          { text: '🎒 Hướng Dẫn Từng Lớp & Môn Học (Lớp 1-5)', link: '/user-guide/grade-subject-guide' },
          { text: '📑 Hướng Dẫn Soạn KHBD 5 Cột & Xuất File', link: '/user-guide/lesson-planning-tutorial' }
        ]
      },
      {
        text: '📖 2. Tổng quan Hệ Thống AI4Edu',
        collapsed: true,
        items: [
          { text: 'Giới thiệu & Tầm nhìn', link: '/overview/' },
          { text: 'Lộ trình ứng dụng AI trong Giáo dục', link: '/overview/roadmap' },
          { text: 'Đạo đức & An toàn AI (Ethics & Safety)', link: '/overview/ethics-safety' },
          { text: '📔 Nhật ký Phát triển (Dev Journal)', link: '/dev-journal' }
        ]
      },
      {
        text: '🏫 2. Chuyên Trang Tiểu Học Hoàng Mai',
        collapsed: false,
        items: [
          { text: '🌟 Cẩm Nang Tổng Quan Hoàng Mai', link: '/hoang-mai-primary/' },
          { text: '📝 Soạn KHBD 5 Cột (Công văn 2345)', link: '/hoang-mai-primary/lesson-planning-2345' },
          { text: '🎯 Phân Hóa Nhiệm Vụ 4 Cấp Độ', link: '/hoang-mai-primary/differentiation-advanced' },
          { text: '📊 Đánh Giá & Nhận Xét (Thông tư 27)', link: '/hoang-mai-primary/assessment-tt27' },
          { text: '🛠️ Quy Trình Công Cụ Số (Toolchain)', link: '/hoang-mai-primary/digital-toolchain' },
          { text: '🚀 STEM/STEAM & Năng Lực Số Trẻ Em', link: '/hoang-mai-primary/stem-ai-literacy' },
          { text: '💡 Prompt Chaining & Trợ Lý Khối 1-5', link: '/hoang-mai-primary/prompt-engineering' },
          { text: '📐 Danh Mục Bài Học Toán 3 & 5 (Tập 1, 2)', link: '/hoang-mai-primary/math-grade3-grade5' },
          { text: '📚 Kho PDF Sách Giáo Khoa Lớp 1 - 5', link: '/hoang-mai-primary/textbook-pdf-library' }
        ]
      },
      {
        text: '📚 3. Khung K-12 theo Khối Lớp (CTGDPT 2018)',
        collapsed: true,
        items: [
          { text: '📊 Ma trận Phân cấp K-12 (Tổng quan)', link: '/curriculum/' },
          {
            text: '🎒 Cấp Tiểu học (Lớp 1 - 5)',
            collapsed: false,
            items: [
              { text: 'Tổng quan Cấp Tiểu học', link: '/curriculum/primary/' },
              { text: '🧸 Khối Lớp 1 (Trực quan & Chữ số)', link: '/curriculum/primary/grade-1' },
              { text: '🎒 Khối Lớp 2 (Kể chuyện & Tính toán 100)', link: '/curriculum/primary/grade-2' },
              { text: '📘 Khối Lớp 3 (Bảng cửu chương & Tin học)', link: '/curriculum/primary/grade-3' },
              { text: '🔬 Khối Lớp 4 (Khám phá Khoa học & Phân số)', link: '/curriculum/primary/grade-4' },
              { text: '🎓 Khối Lớp 5 (Số thập phân & Chuyển cấp)', link: '/curriculum/primary/grade-5' }
            ]
          },
          {
            text: '📘 Cấp THCS (Lớp 6 - 9)',
            collapsed: true,
            items: [
              { text: 'Tổng quan Cấp THCS', link: '/curriculum/lower-secondary/' },
              { text: '🌱 Khối Lớp 6 (KHTN Tích hợp & Số nguyên)', link: '/curriculum/lower-secondary/grade-6' },
              { text: '📐 Khối Lớp 7 (Đại số & Bảng tuần hoàn)', link: '/curriculum/lower-secondary/grade-7' },
              { text: '🔬 Khối Lớp 8 (Hóa đại cương & Nghị luận)', link: '/curriculum/lower-secondary/grade-8' },
              { text: '🎓 Khối Lớp 9 (Căn thức & Luyện thi vào 10)', link: '/curriculum/lower-secondary/grade-9' }
            ]
          },
          {
            text: '🎓 Cấp THPT (Lớp 10 - 12)',
            collapsed: true,
            items: [
              { text: 'Tổng quan Cấp THPT', link: '/curriculum/upper-secondary/' },
              { text: '🔭 Khối Lớp 10 (Phân ban & Định luật Newton)', link: '/curriculum/upper-secondary/grade-10' },
              { text: '🔬 Khối Lớp 11 (Lượng giác, Đạo hàm & Hóa hữu cơ)', link: '/curriculum/upper-secondary/grade-11' },
              { text: '🎯 Khối Lớp 12 (Tích phân, Oxyz & Thi TN THPT/ĐGNL)', link: '/curriculum/upper-secondary/grade-12' }
            ]
          }
        ]
      },
      {
        text: '🚀 4. Kịch bản & Ứng dụng Thực tế',
        collapsed: true,
        items: [
          { text: 'Trợ giảng AI Thông minh (AI Tutor)', link: '/applications/ai-tutor' },
          { text: 'Soạn Giáo án & Đề thi Tự động', link: '/applications/lesson-planning' },
          { text: 'Chấm điểm & Nhận xét Tự động', link: '/applications/automated-grading' },
          { text: 'Cá nhân hóa Lộ trình Học tập', link: '/applications/personalized-learning' }
        ]
      },
      {
        text: '🏛️ 5. Cụm Môn học & Khối Ngành',
        collapsed: true,
        items: [
          { text: 'Tổng quan Cụm Môn học K-12', link: '/subjects-k12/' },
          { text: '📐 Toán & Tin học', link: '/subjects-k12/math-computing' },
          { text: '🔬 Khoa học Tự nhiên', link: '/subjects-k12/natural-sciences' },
          { text: '📜 Xã hội & Nhân văn', link: '/subjects-k12/social-humanities' },
          { text: '🌍 Ngoại ngữ & Kỹ năng Giao tiếp', link: '/subjects-k12/languages' },
          { text: '🏛️ Khối Ngành Đại học (Tổng quan)', link: '/higher-ed-disciplines/' },
          { text: '⚙️ Kỹ thuật & Công nghệ', link: '/higher-ed-disciplines/engineering-tech' },
          { text: '📊 Kinh tế & Quản lý', link: '/higher-ed-disciplines/business-economics' },
          { text: '⚖️ Luật & Khoa học Xã hội', link: '/higher-ed-disciplines/law-social-sciences' },
          { text: '🩺 Y - Dược & Sức khỏe', link: '/higher-ed-disciplines/medical-health' }
        ]
      },
      {
        text: '💡 6. Prompt Engineering cho Giáo dục',
        collapsed: true,
        items: [
          { text: 'Kỹ thuật Prompt Cơ bản', link: '/prompt-engineering/basic-prompts' },
          { text: 'Bộ Thư viện Prompt Giáo dục', link: '/prompt-engineering/advanced-templates' }
        ]
      },
      {
        text: '💻 7. Thực hành Lập trình & SDK',
        collapsed: false,
        items: [
          { text: 'Cấu hình Môi trường với Gemini API', link: '/hands-on/setup-gemini-api' },
          { text: 'Lab 1: Chatbot Trợ giảng bằng Python', link: '/hands-on/python-lab-tutor' },
          { text: 'Lab 2: Hệ thống Chấm bài & Gợi ý Phản hồi', link: '/hands-on/python-lab-grading' }
        ]
      }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Xây dựng với ❤️ cho Cộng đồng Giáo dục Việt Nam & Trường Tiểu học Hoàng Mai',
      copyright: 'Copyright © 2026 AI4Edu Hub'
    }
  }
});
