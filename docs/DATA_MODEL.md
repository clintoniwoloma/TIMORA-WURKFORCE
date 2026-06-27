# TIMORA WURKFORCE — Data Model

## Entities

### Applicant
Stores all job applicant records from WhatsApp intake and manual entry.

| Field | Type | Description |
|-------|------|-------------|
| reference_id | string | TIM-APP-#### |
| full_name | string | Full name |
| phone_number | string | Contact number |
| whatsapp_number | string | WhatsApp number |
| current_location | string | City/area |
| state | string | Nigerian state |
| position_interested_in | string | Applied position |
| job_category | string | AI-assigned category |
| salary_expectation | string | Expected monthly salary |
| cv_url | string | CV file URL |
| cv_text | string | CV text content |
| cover_letter | string | Cover letter |
| suitability_score | number | AI score 0-100 |
| match_label | string | Excellent/Strong/Moderate/Weak |
| communication_quality | string | High/Medium/Low |
| recommended_status | string | Shortlist/Keep on File/Reject |
| interview_priority | string | High/Medium/Low |
| screening_summary | string | AI-generated summary |
| status | string | Pipeline status |
| sheet_sync_status | string | synced/pending_retry |
| flagged_for_human | boolean | Escalation flag |

### Client
| Field | Type | Description |
|-------|------|-------------|
| reference_id | string | TIM-CLI-#### |
| company_name | string | Company name |
| industry | string | Industry sector |
| contact_person | string | Contact name/title |
| phone_number | string | Phone |
| email | string | Email |
| location | string | Office location |
| status | string | Active/Inactive/Prospect |

### StaffRequest
| Field | Type | Description |
|-------|------|-------------|
| reference_id | string | TIM-REQ-#### |
| client_id | string | Linked client ID |
| client_name | string | Client company name |
| position_required | string | Position needed |
| number_of_staff | number | Headcount required |
| salary_budget | string | Monthly budget |
| location | string | Deployment location |
| start_date | string | Required start date |
| status | string | Pending/Approved/Recruiting/Filled |

### WhatsAppConversation
Tracks state of every WhatsApp conversation for flow continuity.

| Field | Type | Description |
|-------|------|-------------|
| phone_number | string | WhatsApp number (unique key) |
| contact_type | string | job_seeker/client/unknown |
| current_flow | string | Active flow name |
| current_step | string | Current step in flow |
| partial_data | string | JSON of answers so far |
| flow_completed | boolean | Whether intake is done |
| flagged_for_human | boolean | Escalation flag |

### ConversationFlag
Escalation records for human follow-up.

### GroupContentLog
Log of every WhatsApp group message sent.
