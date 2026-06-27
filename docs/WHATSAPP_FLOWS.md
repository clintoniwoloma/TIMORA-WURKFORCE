# TIMORA WURKFORCE — WhatsApp Conversation Flows

## Job Seeker Intake (6 Steps)

```
User contacts WhatsApp
        ↓
[Intent Detection]
"Are you looking for a job or to hire staff?"
        ↓
Step 1: Full Name
Step 2: Current Location (City, State)
Step 3: Position Interested In (show category list)
Step 4: Salary Expectation (₦ monthly)
Step 5: CV Upload (file or text description)
Step 6: Cover Letter (typed in WhatsApp)
        ↓
[Record Created — TIM-APP-####]
        ↓
[AI Screening — Score 0-100]
        ↓
[Google Sheets Sync]
        ↓
[Confirmation Message + Reference ID]
        ↓
[Job Seeker Group Invite]
https://chat.whatsapp.com/KFM3IY2ZOGo2QnmPQ0YUPB
```

## Client Intake (9 Steps)

```
User contacts WhatsApp
        ↓
[Intent Detection — client keywords]
        ↓
Step 1: Company Name
Step 2: Contact Person (name + title)
Step 3: Industry
Step 4: Position Required (show category list)
Step 5: Number of Staff Needed
Step 6: Salary Budget (₦ per staff monthly)
Step 7: Deployment Location
Step 8: Preferred Start Date
Step 9: Special Requirements
        ↓
[Client Record — TIM-CLI-####]
[StaffRequest Record — TIM-REQ-####]
        ↓
[Google Sheets Sync]
        ↓
[Confirmation + Reference IDs]
        ↓
[Alert sent to TIMORA Team]
```

## Status Check Flow

```
User asks: "What is my application status?"
        ↓
[Lookup by phone number in Applicant entity]
        ↓
[Found] → Return: Reference ID, Category, Status, Next Steps
[Not Found] → Invite to apply
```

## Escalation Flow

```
Trigger detected (payment, threat, >50 staff, etc.)
        ↓
[ConversationFlag record created]
[flagged_for_human = true]
        ↓
[User told: "Team will follow up shortly"]
        ↓
[WhatsApp alert to Tamunosiki]
        ↓
[Intake paused until flag resolved]
```

## AI Screening Criteria

| Criteria | Points |
|----------|--------|
| Experience (years + relevance) | /30 |
| Skills match to position | /25 |
| Communication quality (cover letter) | /20 |
| Location fit | /10 |
| Salary alignment (vs Nigerian market) | /15 |
| **Total** | **/100** |

| Score | Label |
|-------|-------|
| 80–100 | ✅ Excellent Match |
| 60–79 | 🟢 Strong Match |
| 40–59 | 🟡 Moderate Match |
| 0–39 | 🔴 Weak Match |
