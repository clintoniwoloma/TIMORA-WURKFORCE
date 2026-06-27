"""
TIMORA WURKFORCE — WhatsApp Intake Skill
Handles: Job Seeker intake, Client intake, Status check, General QA
Called by: WhatsApp inbound message automation

This skill manages conversation state via WhatsAppConversation entity.
"""

import os
import json
import sys
from datetime import datetime

# ── Constants ──────────────────────────────────────────────────────────────────
JOB_CATEGORIES = [
    "Waiter", "Bartender", "Supervisor", "Manager", "Chef", "Cook",
    "Kitchen Assistant", "Cleaner", "Housekeeper", "Receptionist",
    "Cashier", "Security Officer", "Driver", "Electrician", "Plumber",
    "HVAC Technician", "IT Support", "Nurse", "Caregiver",
    "Sales Representative", "Customer Service Agent",
    "Administrative Officer", "Storekeeper", "Technical Staff"
]

JOB_SEEKER_STEPS = [
    "full_name",
    "current_location",
    "position_interested_in",
    "salary_expectation",
    "cv",
    "cover_letter",
    "complete"
]

CLIENT_STEPS = [
    "company_name",
    "contact_person",
    "industry",
    "position_required",
    "number_of_staff",
    "salary_budget",
    "location",
    "start_date",
    "special_requirements",
    "complete"
]

CATEGORY_LIST = "\n".join([f"{i+1}. {cat}" for i, cat in enumerate(JOB_CATEGORIES)])

# ── Prompts ────────────────────────────────────────────────────────────────────
JOB_SEEKER_PROMPTS = {
    "full_name": "Great! Let's get your application started. 😊\n\nFirst, what is your *full name*?",
    "current_location": "Thank you! 👍\n\nWhat is your *current location*? (City and State e.g. Lagos, Ikeja)",
    "position_interested_in": f"What *position* are you interested in?\n\nHere are our available categories:\n\n{CATEGORY_LIST}\n\nYou can type the name or number.",
    "salary_expectation": "What is your *expected monthly salary*? (in Nigerian Naira e.g. ₦80,000)",
    "cv": "Please *upload your CV* as a document or image. 📄\n\nIf you don't have a digital CV, you can type a brief summary of your experience and qualifications instead.",
    "cover_letter": "Almost done! ✅\n\nPlease write a *short cover letter* right here in WhatsApp. Tell us:\n- Why you're interested in this role\n- What makes you a great candidate\n- Any relevant experience\n\n(A few sentences is fine — just be yourself!)",
}

CLIENT_PROMPTS = {
    "company_name": "Welcome to TIMORA Talent & Workforce Hub! 🏢\n\nWe're pleased to assist you with your staffing needs. Let's get your request set up.\n\nWhat is your *company name*?",
    "contact_person": "Who is the *contact person* for this request? (Full name and job title)",
    "industry": "What *industry* is your organisation in? (e.g. Hospitality, Healthcare, Facility Management, Manufacturing, Retail)",
    "position_required": f"What *position(s)* do you need to fill?\n\nAvailable categories:\n\n{CATEGORY_LIST}",
    "number_of_staff": "How many staff members do you need?",
    "salary_budget": "What is your *monthly salary budget per staff member*? (in Naira)",
    "location": "Where will the staff be *deployed/working*? (City and State)",
    "start_date": "What is your *preferred start date*? (e.g. 1st July 2026)",
    "special_requirements": "Do you have any *special requirements* or additional details for this request?\n\n(If none, just reply *No*)",
}

# ── Helper ─────────────────────────────────────────────────────────────────────
def get_step_prompt(flow: str, step: str) -> str:
    if flow == "job_seeker_intake":
        return JOB_SEEKER_PROMPTS.get(step, "Please continue.")
    elif flow == "client_intake":
        return CLIENT_PROMPTS.get(step, "Please continue.")
    return "Please continue."

def generate_ref_id(prefix: str, record_id: str) -> str:
    suffix = record_id[-4:].upper() if len(record_id) >= 4 else record_id.upper()
    return f"{prefix}{suffix}"

def detect_intent(message: str) -> str:
    """Detect if a message is from a job seeker or client."""
    msg = message.lower()
    job_seeker_keywords = ["job", "work", "apply", "application", "hire me", "looking for work",
                           "looking for a job", "vacancy", "vacancies", "employment", "position",
                           "i want to work", "need a job", "find work", "seeking"]
    client_keywords = ["staff", "hire", "recruit", "worker", "employee", "need workers",
                       "looking for staff", "staffing", "outsourc", "company", "organisation",
                       "organization", "we need", "our company", "we are looking"]
    status_keywords = ["status", "application status", "my application", "what happened",
                       "follow up", "interview", "shortlisted", "update", "ref", "tim-app"]

    js_score = sum(1 for kw in job_seeker_keywords if kw in msg)
    cl_score = sum(1 for kw in client_keywords if kw in msg)
    st_score = sum(1 for kw in status_keywords if kw in msg)

    if st_score > 0 and js_score == 0 and cl_score == 0:
        return "status_check"
    if js_score > cl_score:
        return "job_seeker"
    if cl_score > js_score:
        return "client"
    return "unknown"

print("TIMORA WURKFORCE intake skill loaded successfully.")
print(f"Job categories: {len(JOB_CATEGORIES)}")
print(f"Job seeker steps: {JOB_SEEKER_STEPS}")
print(f"Client steps: {CLIENT_STEPS}")
