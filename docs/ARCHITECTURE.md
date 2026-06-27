# TIMORA WURKFORCE — System Architecture

## Overview

TIMORA is a multi-channel, AI-powered workforce management platform built on Base44.

## Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    TIMORA WURKFORCE                          │
│                  (Base44 Superagent)                         │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│  WhatsApp   │  Database   │  Google     │   Automations     │
│  Connector  │  (Entities) │  Sheets     │   (15 active)     │
├─────────────┼─────────────┼─────────────┼───────────────────┤
│ Job Seeker  │ Applicant   │ Applicants  │ 7x Daily Content  │
│ Group       │ Client      │ Clients     │ 4x Employee Tips  │
│             │ StaffReq    │ StaffReqs   │ 1x Team Session   │
│ Employee    │ WAConvo     │ Attendance  │ 3x Entity Alerts  │
│ Group       │ ConvoFlag   │ Reports     │                   │
│             │ GroupLog    │ Leave/Comp  │                   │
└─────────────┴─────────────┴─────────────┴───────────────────┘
```

## Data Flow

### Job Seeker Intake
```
WhatsApp Message → Intent Detection → 6-Step Intake Flow
→ Applicant Record Created → AI Screening (0-100 score)
→ Google Sheets Sync → WhatsApp Confirmation + Group Invite
→ [If Excellent Match] → Priority Alert to TIMORA Team
```

### Client Intake
```
WhatsApp Message → Intent Detection → 9-Step Intake Flow
→ Client Record + StaffRequest Created → Google Sheets Sync
→ WhatsApp Confirmation → Alert to TIMORA Team
→ Candidate Matching Engine (upcoming)
```

### Scheduled Automations
```
Cron Trigger → Agent Awakens → Generate AI Content
→ Send to WhatsApp Group → Log in GroupContentLog
```

## Technology Stack
- **Agent:** Base44 Superagent (Claude-based LLM)
- **Database:** Base44 entity store (JSON schema)
- **WhatsApp:** Base44 WhatsApp Business connector
- **Sheets:** Google Sheets API v4
- **Hosting:** Base44 cloud (auto-scaled)
- **Git:** GitHub (clintoniwoloma/TIMORA-WURKFORCE)
