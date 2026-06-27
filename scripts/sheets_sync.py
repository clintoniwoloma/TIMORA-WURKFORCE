"""
TIMORA WURKFORCE — Google Sheets Sync Utility
Syncs Applicant and StaffRequest records to the TIMORA Google Sheet.

Sheet ID: 1seO1PcEoCijaaAndG924BjrgjTYViEC-q27bdJ6PmGM
Tabs: Applicants, Clients, StaffRequests
"""

SHEET_ID = "1seO1PcEoCijaaAndG924BjrgjTYViEC-q27bdJ6PmGM"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"

APPLICANT_COLUMNS = [
    "ReferenceID", "FullName", "Gender", "DateOfBirth", "PhoneNumber",
    "WhatsAppNumber", "Email", "CurrentAddress", "CurrentLocation", "State",
    "Country", "PositionInterestedIn", "JobCategory", "SalaryExpectation",
    "ExperienceYears", "CurrentEmploymentStatus", "Education", "Skills",
    "CoverLetter", "CVUrl", "SuitabilityScore", "MatchLabel",
    "CommunicationQuality", "RecommendedStatus", "InterviewPriority",
    "ScreeningSummary", "Status", "RecruiterAssigned", "Source",
    "SheetSyncStatus", "FlaggedForHuman", "DateApplied"
]

CLIENT_COLUMNS = [
    "ReferenceID", "CompanyName", "Industry", "ContactPerson", "PhoneNumber",
    "WhatsAppNumber", "Email", "Address", "Location", "Status",
    "ContractStartDate", "ContractEndDate", "Notes", "SheetSyncStatus",
    "FlaggedForHuman", "DateAdded"
]

STAFF_REQUEST_COLUMNS = [
    "ReferenceID", "ClientName", "PositionRequired", "JobCategory",
    "NumberOfStaff", "SalaryBudget", "Location", "StartDate", "EndDate",
    "SpecialRequirements", "Status", "SheetSyncStatus", "DateSubmitted"
]

def map_applicant_to_row(record: dict) -> list:
    """Map an Applicant entity record to a Sheets row."""
    return [
        record.get("reference_id", ""),
        record.get("full_name", ""),
        record.get("gender", ""),
        record.get("date_of_birth", ""),
        record.get("phone_number", ""),
        record.get("whatsapp_number", ""),
        record.get("email", ""),
        record.get("current_address", ""),
        record.get("current_location", ""),
        record.get("state", ""),
        record.get("country", "Nigeria"),
        record.get("position_interested_in", ""),
        record.get("job_category", ""),
        record.get("salary_expectation", ""),
        record.get("experience_years", ""),
        record.get("current_employment_status", ""),
        record.get("education", ""),
        record.get("skills", ""),
        record.get("cover_letter", ""),
        record.get("cv_url", ""),
        record.get("suitability_score", ""),
        record.get("match_label", ""),
        record.get("communication_quality", ""),
        record.get("recommended_status", ""),
        record.get("interview_priority", ""),
        record.get("screening_summary", ""),
        record.get("status", ""),
        record.get("recruiter_assigned", ""),
        record.get("source", "WhatsApp"),
        record.get("sheet_sync_status", "pending"),
        str(record.get("flagged_for_human", False)),
        record.get("created_date", ""),
    ]

def map_client_to_row(record: dict) -> list:
    return [
        record.get("reference_id", ""),
        record.get("company_name", ""),
        record.get("industry", ""),
        record.get("contact_person", ""),
        record.get("phone_number", ""),
        record.get("whatsapp_number", ""),
        record.get("email", ""),
        record.get("address", ""),
        record.get("location", ""),
        record.get("status", ""),
        record.get("contract_start_date", ""),
        record.get("contract_end_date", ""),
        record.get("notes", ""),
        record.get("sheet_sync_status", "pending"),
        str(record.get("flagged_for_human", False)),
        record.get("created_date", ""),
    ]

def map_staff_request_to_row(record: dict) -> list:
    return [
        record.get("reference_id", ""),
        record.get("client_name", ""),
        record.get("position_required", ""),
        record.get("job_category", ""),
        record.get("number_of_staff", ""),
        record.get("salary_budget", ""),
        record.get("location", ""),
        record.get("start_date", ""),
        record.get("end_date", ""),
        record.get("special_requirements", ""),
        record.get("status", ""),
        record.get("sheet_sync_status", "pending"),
        record.get("created_date", ""),
    ]

print("Sheets sync utility loaded.")
print(f"Target sheet: {SHEET_URL}")
