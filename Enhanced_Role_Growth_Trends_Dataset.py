import pandas as pd
import random
import numpy as np

# File path for your Mac
output_path = "/Users/sowmyakakularapu/Downloads/Enhanced_Role_Growth_Trends_Dataset.csv"

# Define roles and associated attributes
roles_data = {
    "Data Scientist":     {"Category": "Data",    "Industry": "Healthcare"},
    "Data Engineer":      {"Category": "Data",    "Industry": "Finance"},
    "Software Developer": {"Category": "Software", "Industry": "Technology"},
    "Cloud Engineer":     {"Category": "Cloud",   "Industry": "Technology"},
    "Cybersecurity Analyst": {"Category": "Security", "Industry": "Defense"}
}

years = [2022, 2023, 2024]
seniority_levels = ["Entry", "Mid", "Senior"]
remote_options = ["Low", "Medium", "High"]
state_groups = {
    "Data Scientist": "CA, FL, WA",
    "Data Engineer": "TX, IL, WA",
    "Software Developer": "CA, NY, TX",
    "Cloud Engineer": "WA, TX, GA",
    "Cybersecurity Analyst": "VA, MD, DC"
}

# Simulate realistic growth percentages and salary by role and year
data = []
for role, attributes in roles_data.items():
    for year in years:
        openings = random.randint(1200, 2500)
        avg_salary = random.randint(85000, 160000)
        seniority = random.choice(seniority_levels)
        remote = random.choice(remote_options)
        growth = round(np.random.uniform(0, 60), 2)
        states = state_groups[role]
        
        data.append({
            "Role": role,
            "Year": year,
            "Openings": openings,
            "Category": attributes["Category"],
            "AvgSalary": avg_salary,
            "SeniorityLevel": seniority,
            "RemoteAvailability": remote,
            "TopHiringStates": states,
            "ProjectedGrowth(%)": growth,
            "Industry": attributes["Industry"]
        })

# Create and save DataFrame
df = pd.DataFrame(data)
df.to_csv(output_path, index=False)

print(f"✅ Dataset saved to:\n{output_path}")
