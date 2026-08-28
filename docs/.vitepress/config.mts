import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'AI4Edu Hub',
  description: 'Bộ tài liệu & mã nguồn hướng dẫn ứng dụng Trí tuệ nhân tạo (AI) trong Giáo dục',
  lang: 'vi-VN',
  cleanUrls: true,
  themeConfig: {
    logo: '🎓',
    siteTitle: 'AI4Edu Hub',
    nav: [
      { text: 'Trang chủ', link: '/' },
      { text: 'Tổng quan', link: '/overview/' },
      { text: 'Ứng dụng Chung', link: '/applications/ai-tutor' },
      { text: 'Theo Cấp học', link: '/education-levels/' },
      { text: 'Theo Môn & Ngành', link: '/subjects-k12/' },
      { text: 'Prompting', link: '/prompt-engineering/basic-prompts' },
      { text: 'Thực hành Code', link: '/hands-on/setup-gemini-api' }
    ],
    sidebar: [
      {
        text: '📖 1. Tổng quan AI4Edu',
        collapsed: false,
        items: [
          { text: 'Giới thiệu & Tầm nhìn', link: '/overview/' },
          { text: 'Lộ trình ứng dụng AI trong Giáo dục', link: '/overview/roadmap' },
          { text: 'Đạo đức & An toàn AI (Ethics & Safety)', link: '/overview/ethics-safety' },
          { text: '📔 Nhật ký Phát triển (Dev Journal)', link: '/dev-journal' }
        ]
      },
      {
        text: '🚀 2. Kịch bản & Ứng dụng Thực tế',
        collapsed: false,
        items: [
          { text: 'Trợ giảng AI Thông minh (AI Tutor)', link: '/applications/ai-tutor' },
          { text: 'Soạn Giáo án & Đề thi Tự động', link: '/applications/lesson-planning' },
          { text: 'Chấm điểm & Nhận xét Tự động', link: '/applications/automated-grading' },
          { text: 'Cá nhân hóa Lộ trình Học tập', link: '/applications/personalized-learning' }
        ]
      },
      {
        text: '🏫 3. Phân loại theo Cấp học (K-16)',
        collapsed: false,
        items: [
          { text: 'Ma trận Phân cấp AI (Tổng quan)', link: '/education-levels/' },
          { text: '🧸 Giáo dục Mầm non', link: '/education-levels/preschool' },
          { text: '🎒 Cấp Tiểu học', link: '/education-levels/primary' },
          { text: '📘 Cấp Trung học Cơ sở (THCS)', link: '/education-levels/secondary' },
          { text: '🎓 Cấp Trung học Phổ thông (THPT)', link: '/education-levels/high-school' },
          { text: '🏛️ Đại học & Sau Đại học', link: '/education-levels/higher-education' }
        ]
      },
      {
        text: '📚 4. Cụm Môn học Phổ thông (K-12)',
        collapsed: false,
        items: [
          { text: 'Tổng quan Cụm Môn học', link: '/subjects-k12/' },
          { text: '📐 Toán & Tin học', link: '/subjects-k12/math-computing' },
          { text: '🔬 Khoa học Tự nhiên (Lý - Hóa - Sinh)', link: '/subjects-k12/natural-sciences' },
          { text: '📜 Xã hội & Nhân văn (Văn - Sử - Địa - GDCD)', link: '/subjects-k12/social-humanities' },
          { text: '🌍 Ngoại ngữ & Kỹ năng Giao tiếp', link: '/subjects-k12/languages' }
        ]
      },
      {
        text: '🎓 5. Khối Ngành Đại học & NCKH',
        collapsed: false,
        items: [
          { text: 'Tổng quan Khối Ngành Đại học', link: '/higher-ed-disciplines/' },
          { text: '⚙️ Kỹ thuật & Công nghệ', link: '/higher-ed-disciplines/engineering-tech' },
          { text: '📊 Kinh tế, Kinh doanh & Quản lý', link: '/higher-ed-disciplines/business-economics' },
          { text: '⚖️ Luật & Khoa học Xã hội', link: '/higher-ed-disciplines/law-social-sciences' },
          { text: '🩺 Y - Dược & Khoa học Sức khỏe', link: '/higher-ed-disciplines/medical-health' }
        ]
      },
      {
        text: '💡 6. Prompt Engineering cho Giáo viên',
        collapsed: false,
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
      message: 'Xây dựng với ❤️ cho Cộng đồng Giáo dục Việt Nam',
      copyright: 'Copyright © 2026 AI4Edu Hub'
    }
  }
});
