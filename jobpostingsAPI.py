import requests
import csv
import time
import re
from datetime import datetime

# ----------------------------
# Adzuna API credentials
# ----------------------------
APP_ID = "f42441da"
APP_KEY = "53259a176b0b924677c79ea524ec278c"

# ----------------------------
# Countries & Roles
# ----------------------------
countries = [
    "au","at","be","br","ca","fr","de","in","it",
    "mx","nl","nz","pl","sg","za","ch","gb","us"
]

job_titles = [
    "AI Engineer","Machine Learning Engineer","Deep Learning Engineer",
    "NLP Engineer","Computer Vision Engineer","AI Researcher",
    "Prompt Engineer","AI Product Manager","Data Scientist","Data Analyst",
    "Data Engineer","BI Analyst","Business Intelligence Analyst",
    "Big Data Engineer","Data Architect","Database Administrator"
]

# ----------------------------
# Skills list for extraction
# ----------------------------
skills_list = [
    "python","tensorflow","pytorch","sql","nlp","computer vision","docker",
    "kubernetes","aws","azure","gcp","machine learning","deep learning",
    "transformers","llms","data analysis","big data","hadoop","spark",
    "statistics","prompt engineering","research"
]

# ----------------------------
# Functions for experience & skills
# ----------------------------
def extract_experience(text):
    """Extract years of experience from job description."""
    if not text:
        return None
    patterns = [
        r"(\d+)\+?\s*years?",
        r"minimum of (\d+)",
        r"at least (\d+)",
        r"(\d+)\s*yrs"
    ]
    for p in patterns:
        match = re.search(p, text.lower())
        if match:
            return int(match.group(1))
    return None

def extract_skills(text):
    """Return comma-separated list of skills found in job description."""
    if not text:
        return ""
    found = []
    t = text.lower()
    for skill in skills_list:
        if skill in t:
            found.append(skill)
    return ", ".join(found)

# ----------------------------
# Output CSV
# ----------------------------
output_file = f"enhanced_ai_jobs_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Country", "Role", "Job_Title", "Company", "Location",
        "Salary_Min", "Salary_Max", "Salary_Currency",
        "Created_Date", "Description",
        "Experience_Years", "Skills",
        "URL", "Timestamp"
    ])

    # ----------------------------
    # LOOP THROUGH COUNTRIES & ROLES
    # ----------------------------
    for country in countries:
        print(f"\n🌍 Collecting from {country.upper()} ...")
        for role in job_titles:
            print(f"  → Searching: {role}")

            jobs_collected = 0
            page = 1
            while jobs_collected < 300:  # up to 300 jobs per country
                url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
                params = {
                    "app_id": APP_ID,
                    "app_key": APP_KEY,
                    "what": role,
                    "results_per_page": 50,
                    "content-type": "application/json"
                }

                try:
                    response = requests.get(url, params=params)
                    data = response.json()
                    results = data.get("results", [])

                    if not results:
                        break  # no more jobs

                    for job in results:
                        desc = job.get("description", "")
                        writer.writerow([
                            country.upper(),
                            role,
                            job.get("title"),
                            job.get("company", {}).get("display_name"),
                            job.get("location", {}).get("display_name"),
                            job.get("salary_min"),
                            job.get("salary_max"),
                            job.get("salary_currency"),
                            job.get("created"),
                            desc,
                            extract_experience(desc),
                            extract_skills(desc),
                            job.get("redirect_url"),
                            datetime.now().strftime("%Y-%m-%d")
                        ])
                        jobs_collected += 1
                        if jobs_collected >= 300:
                            break

                    page += 1
                    time.sleep(0.4)  # polite delay

                except Exception as e:
                    print("Error:", e)
                    break

print("\n✅ DONE! Saved file:", output_file)
