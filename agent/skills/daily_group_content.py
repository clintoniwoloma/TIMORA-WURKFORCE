"""
TIMORA WURKFORCE — Daily WhatsApp Group Content Generator
Generates day-appropriate content for the Job Seeker WhatsApp group.
Triggered by scheduled automations Mon–Sun at 08:00 WAT.
"""

CONTENT_SCHEDULE = {
    "Monday": "cv_tips",
    "Tuesday": "interview_tips",
    "Wednesday": "customer_service_tips",
    "Thursday": "career_development",
    "Friday": "current_vacancies",
    "Saturday": "grooming_tips",
    "Sunday": "motivational"
}

CONTENT_PROMPTS = {
    "cv_tips": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Monday CV Writing Tips* message for our Job Seeker Community Group.

Requirements:
- Start with a warm Monday greeting
- Share 3-5 practical, actionable CV writing tips relevant to Nigerian job seekers (hospitality, facility management, healthcare, security sectors)
- Keep it brief, easy to read, formatted with emojis and line breaks
- End with an encouraging call to action (e.g. "Need help with your CV? Start your TIMORA application today!")
- Tone: warm, encouraging, professional
- Length: max 300 words
""",

    "interview_tips": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Tuesday Interview Tips* message for our Job Seeker Community Group.

Requirements:
- Start with a cheerful Tuesday greeting
- Share 3-5 practical interview tips relevant to Nigerian workplace culture (punctuality, dress code, body language, common questions)
- Include at least one tip specific to hospitality, security, healthcare, or facility management roles
- Keep it brief, easy to read, formatted with emojis and line breaks
- End with encouragement
- Tone: warm, motivating, practical
- Length: max 300 words
""",

    "customer_service_tips": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Wednesday Customer Service Tips* message for our Job Seeker Community Group.

Requirements:
- Start with a midweek Wednesday greeting
- Share 3-5 practical customer service excellence tips relevant to Nigerian hospitality and service sectors
- Make it applicable to roles like Waiter, Receptionist, Cashier, Customer Service Agent
- Keep it brief, easy to read, formatted with emojis and line breaks
- End with a professional growth encouragement
- Tone: professional, energetic, motivating
- Length: max 300 words
""",

    "career_development": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Thursday Career Development Tips* message for our Job Seeker Community Group.

Requirements:
- Start with a Thursday greeting
- Share 3-5 tips on growing professionally in the Nigerian workforce market
- Cover topics like: upskilling, professional certifications, networking, performance at work, building work ethic
- Relevant to blue-collar and skilled/semi-skilled Nigerian workers
- Keep it brief, easy to read, formatted with emojis and line breaks
- Tone: inspiring, practical, grounded
- Length: max 300 words
""",

    "grooming_tips": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Saturday Professional Grooming Tips* message for our Job Seeker Community Group.

Requirements:
- Start with a Saturday greeting
- Share 4-5 professional grooming and appearance tips for Nigerian job seekers
- Cover: personal hygiene, uniform/dress code standards, hair, nails, scent — appropriate for hospitality, healthcare, facility management roles
- Culturally appropriate for Nigerian workplace context
- Keep it brief, easy to read, formatted with emojis and line breaks
- Tone: friendly, non-judgmental, encouraging
- Length: max 300 words
""",

    "motivational": """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Sunday Motivational Career Message* for our Job Seeker Community Group.

Requirements:
- Start with a warm Sunday/weekend greeting
- Share an inspiring career message for Nigerian job seekers — encourage persistence, hard work, and belief in their journey
- Include one powerful quote or affirmation
- Speak to the struggles of job seekers in Nigeria — show empathy and real encouragement
- End with a positive call to the week ahead
- Keep it brief, easy to read, formatted with emojis and line breaks
- Tone: warm, deeply encouraging, soulful
- Length: max 300 words
"""
}

VACANCIES_PROMPT_TEMPLATE = """
You are TIMORA WURKFORCE, the recruitment assistant for TIMORA Talent & Workforce Hub in Nigeria.

Generate a WhatsApp-friendly *Friday Current Vacancies* message for our Job Seeker Community Group.

## ACTIVE VACANCIES
{vacancies_list}

Requirements:
- Start with an exciting Friday greeting
- Present the active vacancies clearly and attractively
- For each vacancy, show: Position, Location, Number Needed, Salary Budget (if available)
- Add a clear call to action: how to apply via WhatsApp
- Keep it well-formatted with emojis and line breaks
- If no vacancies: say TIMORA is always accepting applications and encourage them to apply
- Tone: exciting, opportunity-focused, professional
- Length: max 400 words
"""

def get_content_type_for_day(day_name: str) -> str:
    return CONTENT_SCHEDULE.get(day_name, "motivational")

def get_content_prompt(content_type: str) -> str:
    return CONTENT_PROMPTS.get(content_type, CONTENT_PROMPTS["motivational"])

def build_vacancies_prompt(vacancies: list) -> str:
    if not vacancies:
        vacancies_list = "No specific vacancies currently listed — accepting general applications."
    else:
        lines = []
        for v in vacancies:
            line = f"• {v.get('position_required', 'Position')} — {v.get('location', 'Location TBD')}"
            if v.get('number_of_staff'):
                line += f" ({v['number_of_staff']} needed)"
            if v.get('salary_budget'):
                line += f" | Budget: {v['salary_budget']}"
            lines.append(line)
        vacancies_list = "\n".join(lines)
    return VACANCIES_PROMPT_TEMPLATE.format(vacancies_list=vacancies_list)

print("Daily Group Content skill loaded.")
print(f"Schedule: {CONTENT_SCHEDULE}")
