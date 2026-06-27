# 🏢 TIMORA WURKFORCE
### TIMORA Talent & Workforce Hub

> **Enterprise Workforce Outsourcing, Recruitment & Staff Deployment Platform**
> Built for Nigerian workforce management — powered by AI automation.

---

## 🌐 Live Platform
**WhatsApp Bot:** Active on WhatsApp (powered by Base44)
**Dashboard:** Coming soon — web platform in development

---

## 📋 Overview

TIMORA Talent & Workforce Hub is a full-stack workforce outsourcing and recruitment platform that automates:

- 🤝 **Recruitment** — WhatsApp-driven applicant intake, AI screening, pipeline management
- 👷 **Staff Deployment** — Client matching, deployment tracking, staff assignment
- 📊 **Attendance** — GPS clock-in/out, shift tracking, late detection
- 🏢 **Client Management** — Staffing requests, contracts, client portal
- 💬 **WhatsApp Automation** — Dual-group management (Job Seekers + Employees)
- 📈 **Analytics** — Hiring funnel, attendance rates, revenue trends

---

## 🤖 WhatsApp Groups

| Group | Purpose | Link |
|-------|---------|------|
| Job Seeker Community | Applicants — daily tips, vacancies, career content | [Join](https://chat.whatsapp.com/KFM3IY2ZOGo2QnmPQ0YUPB) |
| Employee Staff Group | Deployed workers — attendance, tips, ethics, sessions | [Join]() |

---

## 🗂️ Repository Structure

```
TIMORA-WURKFORCE/
├── README.md                    # This file
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md          # System architecture
│   ├── AUTOMATIONS.md           # All automation schedules
│   ├── DATA_MODEL.md            # Entity schemas
│   └── WHATSAPP_FLOWS.md        # WhatsApp conversation flows
├── agent/                       # AI Agent configuration
│   ├── rules/                   # Operating rules & policies
│   │   └── timora_workforce_policy.md
│   └── skills/                  # Agent skill scripts
│       ├── whatsapp_intake.py
│       ├── ai_screening.py
│       └── daily_group_content.py
├── platform/                    # Platform configuration
│   ├── entities/                # Database entity schemas
│   │   ├── Applicant.json
│   │   ├── Client.json
│   │   ├── StaffRequest.json
│   │   ├── WhatsAppConversation.json
│   │   ├── ConversationFlag.json
│   │   └── GroupContentLog.json
│   └── functions/               # Backend functions
└── scripts/                     # Utility scripts
    └── sheets_sync.py           # Google Sheets sync utility
```

---

## 🧩 Modules

### 1. WhatsApp Recruitment Assistant
- Detects job seekers vs clients automatically
- 6-step job seeker intake flow
- 9-step client staffing request flow
- AI screening: scores 0–100 across 5 criteria
- Auto-assigns job category and match label
- Syncs to Google Sheets automatically

### 2. Automated Group Content
**Job Seeker Group (daily 8:00am WAT):**
- Monday: CV Writing Tips
- Tuesday: Interview Tips
- Wednesday: Customer Service Tips
- Thursday: Career Development Tips
- Friday: Current Vacancies (live from database)
- Saturday: Professional Grooming Tips
- Sunday: Motivational Career Content

**Employee Group:**
- Mon/Wed/Fri 9:00am WAT: Hospitality Tips, Motivation & Ethics
- Thursday 12:00pm WAT: Weekly Team Interactive Session
- Mon–Fri 7:30am WAT: Attendance Reminders

### 3. Data Management
- **Google Sheets Sync:** Applicants, Clients, StaffRequests → TIMORA sheet
- **Entity Database:** 6 core entities with full CRUD
- **Audit Trail:** All records timestamped and tracked

---

## 📊 Google Sheets Integration

**Sheet:** [TIMORA Master Sheet](https://docs.google.com/spreadsheets/d/1seO1PcEoCijaaAndG924BjrgjTYViEC-q27bdJ6PmGM/edit)

| Tab | Purpose |
|-----|---------|
| Applicants | All job applicant records + AI screening results |
| Clients | Client company profiles |
| StaffRequests | Client staffing requests |
| Attendance | Employee attendance records |
| Reports | Daily/weekly/monthly reports |
| LeaveRequests | Staff leave applications |
| Complaints | Staff & client complaints |

---

## 🎯 AI Screening Engine

Scores applicants 0–100 across:
| Criteria | Weight |
|----------|--------|
| Experience (years + relevance) | 30pts |
| Skills match | 25pts |
| Communication quality | 20pts |
| Location fit | 10pts |
| Salary alignment | 15pts |

**Match Labels:** Excellent (80–100) · Strong (60–79) · Moderate (40–59) · Weak (0–39)

---

## 🔐 Security & Roles

| Role | Access Level |
|------|-------------|
| Super Admin | Full access — all data, analytics, config |
| Recruiter | Applicants, CVs, interviews, pipeline |
| Operations Manager | Deployments, attendance, reports, clients |
| HR Manager | Leave, complaints, performance |
| Client Manager | Client accounts, requests, contracts |
| Employee | Own profile, leave, complaints, assignments |
| Client Portal User | Staff requests, assigned staff, reports |

---

## 🚀 Deployment

This platform is built on **Base44** — a no-code AI agent and app builder platform.

**Tech Stack:**
- AI Agent: Base44 Superagent (TIMORA WURKFORCE)
- Database: Base44 entity store
- WhatsApp: Base44 WhatsApp connector
- Sheets: Google Sheets API
- Automations: Base44 scheduled + entity triggers

---

## 📞 Contact

**Owner:** Tamunosiki Iwoloma Clinton +2349025975247
**Platform:** TIMORA Talent & Workforce Hub
**WhatsApp Bot:** Message via the Job Seeker or Employee group links above

---

*Built with ❤️ by TIMORA WURKFORCE AI all rights Reserved— Nigeria's smartest workforce automation.*
