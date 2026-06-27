"""
TIMORA WURKFORCE — AI Applicant Screening Skill
Analyzes applicant data and returns screening results.
Uses built-in AI reasoning — no external LLM API needed.
"""

SCREENING_PROMPT_TEMPLATE = """
You are an expert HR screener for TIMORA Talent & Workforce Hub, a Nigerian workforce outsourcing company.

Analyze the following applicant and provide a structured screening report.

## APPLICANT DATA
- Full Name: {full_name}
- Position Interested In: {position}
- Current Location: {location}
- Salary Expectation: {salary}
- CV / Work Experience: {cv_text}
- Cover Letter: {cover_letter}

## YOUR TASK
Score this applicant out of 100 using these criteria:
1. Experience (30 pts): Years of experience + relevance to the position applied for
2. Skills Match (25 pts): Skills mentioned vs typical requirements for the position
3. Communication Quality (20 pts): Clarity, grammar, coherence of their cover letter and CV
4. Location Fit (10 pts): Proximity and suitability of their location for deployment in Nigeria
5. Salary Alignment (15 pts): Does their expectation align with typical Nigerian market rates for the role?

## NIGERIAN SALARY REFERENCE (monthly, NGN)
- Waiter/Bartender: ₦40,000–₦80,000
- Chef/Cook: ₦60,000–₦150,000
- Security Officer: ₦40,000–₦80,000
- Driver: ₦50,000–₦100,000
- Cleaner/Housekeeper: ₦35,000–₦70,000
- Receptionist/Cashier: ₦50,000–₦100,000
- Nurse/Caregiver: ₦80,000–₦200,000
- Electrician/Plumber: ₦70,000–₦150,000
- Supervisor/Manager: ₦100,000–₦300,000
- Admin Officer: ₦60,000–₦120,000
- Sales Rep/Customer Service: ₦50,000–₦120,000

## JOB CATEGORIES (assign the most accurate one)
Waiter, Bartender, Supervisor, Manager, Chef, Cook, Kitchen Assistant, Cleaner,
Housekeeper, Receptionist, Cashier, Security Officer, Driver, Electrician, Plumber,
HVAC Technician, IT Support, Nurse, Caregiver, Sales Representative, Customer Service Agent,
Administrative Officer, Storekeeper, Technical Staff

## OUTPUT FORMAT (respond ONLY with valid JSON — no extra text)
{{
  "job_category": "<assigned category from the list above>",
  "suitability_score": <number 0-100>,
  "match_label": "<Excellent Match|Strong Match|Moderate Match|Weak Match>",
  "communication_quality": "<High|Medium|Low>",
  "recommended_status": "<Shortlist for Interview|Keep on File|Reject>",
  "interview_priority": "<High|Medium|Low>",
  "experience_score": <number 0-30>,
  "skills_score": <number 0-25>,
  "communication_score": <number 0-20>,
  "location_score": <number 0-10>,
  "salary_score": <number 0-15>,
  "screening_summary": "<2-3 sentence summary of the applicant's suitability, strengths, and any concerns>",
  "applicant_message": "<A warm, encouraging 2-sentence message to send to the applicant about their application category and next steps — do NOT mention the score>"
}}

## MATCH LABEL GUIDE
- 80-100 → Excellent Match
- 60-79 → Strong Match
- 40-59 → Moderate Match
- 0-39 → Weak Match
"""

def build_screening_prompt(applicant_data: dict) -> str:
    return SCREENING_PROMPT_TEMPLATE.format(
        full_name=applicant_data.get("full_name", "Not provided"),
        position=applicant_data.get("position_interested_in", "Not specified"),
        location=applicant_data.get("current_location", "Not provided"),
        salary=applicant_data.get("salary_expectation", "Not stated"),
        cv_text=applicant_data.get("cv_text", "No CV provided"),
        cover_letter=applicant_data.get("cover_letter", "No cover letter provided")
    )

print("AI Screening skill loaded.")
print("Screening criteria: Experience(30) + Skills(25) + Communication(20) + Location(10) + Salary(15) = 100")
