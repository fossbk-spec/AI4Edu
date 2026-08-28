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
      { text: 'Ứng dụng Thực tế', link: '/applications/ai-tutor' },
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
          { text: 'Đạo đức & An toàn AI (Ethics & Safety)', link: '/overview/ethics-safety' }
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
        text: '💡 3. Prompt Engineering cho Giáo viên',
        collapsed: false,
        items: [
          { text: 'Kỹ thuật Prompt Cơ bản', link: '/prompt-engineering/basic-prompts' },
          { text: 'Bộ Thư viện Prompt Giáo dục', link: '/prompt-engineering/advanced-templates' }
        ]
      },
      {
        text: '💻 4. Thực hành Lập trình & SDK',
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
