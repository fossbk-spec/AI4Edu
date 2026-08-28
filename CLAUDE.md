# AI4Edu Hub - Project Overview & Rules

## 1. Tech Stack
- Documentation Engine: VitePress (Vue 3, Markdown, TypeScript)
- AI & Automation Labs: Python 3.13+, `google-genai` SDK, Pydantic v2
- Environment Management: `python-dotenv`

## 2. Execution Commands (Do not guess commands)
- Run Docs Dev Server: `npm run docs:dev`
- Build Docs Site: `npm run docs:build`
- Preview Built Docs: `npm run docs:preview`
- Run AI Tutor (Lab 1): `python3 scripts/gemini_client.py`
- Run Lesson Planner (Lab 2): `python3 scripts/demo_lesson_plan.py`
- Run Auto Grader (Lab 3): `python3 scripts/demo_auto_grader.py`

## 3. Strict Coding Conventions
- All Python scripts must use `google-genai` official SDK (`from google import genai`).
- Use Pydantic models for Structured Outputs in AI assessment scripts.
- Markdown documents in `docs/` must follow VitePress frontmatter & markdown standards.

## 4. Agent Operational Constraints
- DO NOT commit `.env` containing real API Keys to git repository.
- DO NOT edit `node_modules/` or `.vitepress/dist/`.
- Always run `npm run docs:build` to verify documentation syntax before completing tasks.
