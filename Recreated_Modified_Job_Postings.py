import pandas as pd
import zipfile
from datetime import datetime
import numpy as np
import os

# Step 1: Define local paths
zip_path = "/Users/sowmyakakularapu/Downloads/job_skills.csv.zip"
extract_dir = "/Users/sowmyakakularapu/Downloads"
output_path = "/Users/sowmyakakularapu/Downloads/Recreated_Modified_Job_Postings.csv"

# Step 2: Extract ZIP and load CSV
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

csv_file = os.path.join(extract_dir, "job_skills.csv")
job_skills_df = pd.read_csv(csv_file)

# Step 3: Filter for USA jobs
usa_jobs_df = job_skills_df[job_skills_df['Location'].str.contains("United States", na=False)].copy()

# Step 4: Extract City and State
def extract_city_state(location):
    try:
        parts = location.split(',')
        if len(parts) >= 3:
            return pd.Series([parts[-3].strip(), parts[-2].strip()])
        elif len(parts) == 2:
            return pd.Series([parts[0].strip(), parts[1].strip()])
        else:
            return pd.Series(['Unknown', 'Unknown'])
    except:
        return pd.Series(['Unknown', 'Unknown'])

usa_jobs_df[['City', 'State']] = usa_jobs_df['Location'].apply(extract_city_state)

# Step 5: Combine skills
def combine_skills(min_q, pref_q):
    skills = []
    if pd.notna(min_q): skills.append(min_q.replace('\n', ', '))
    if pd.notna(pref_q): skills.append(pref_q.replace('\n', ', '))
    return ', '.join(skills)

usa_jobs_df['RequiredSkills'] = usa_jobs_df.apply(
    lambda row: combine_skills(row['Minimum Qualifications'], row['Preferred Qualifications']),
    axis=1
)

# Step 6: Simulate Realistic Fields
np.random.seed(42)

sample_roles = [
    'UI/UX Designer', 'Frontend Developer', 'Backend Developer',
    'Full Stack Developer', 'Product Manager', 'Data Scientist',
    'Machine Learning Engineer', 'DevOps Engineer', 'Cloud Architect',
    'Mobile App Developer', 'Software Engineer', 'Site Reliability Engineer',
    'AI Research Engineer', 'Cybersecurity Analyst', 'Data Engineer',
    'Business Intelligence Analyst', 'Systems Administrator',
    'Solutions Architect', 'QA Automation Engineer', 'Technical Program Manager'
]

sample_companies = [
    'Apple', 'Microsoft', 'Google', 'Amazon', 'Meta',
    'NVIDIA', 'Intel', 'IBM', 'Salesforce', 'Oracle',
    'Adobe', 'Netflix', 'Spotify', 'Zoom', 'Cisco'
]

sample_salaries = ['$80k-$100k', '$100k-$120k', '$120k-$140k', '$140k-$160k', 'Not Disclosed']
sample_experience = ['Entry', 'Mid', 'Senior']
sample_remote = ['Yes', 'No', 'Hybrid']
sample_jobtype = ['Full-time', 'Internship', 'Contract']
sample_link = 'https://company.com/job-description'

# Assign synthetic values
usa_jobs_df['Role'] = np.random.choice(sample_roles, size=len(usa_jobs_df))
usa_jobs_df['JobTitle'] = usa_jobs_df['Role']
usa_jobs_df['Company'] = np.random.choice(sample_companies, size=len(usa_jobs_df))
usa_jobs_df['SalaryRange'] = np.random.choice(sample_salaries, size=len(usa_jobs_df))
usa_jobs_df['ExperienceLevel'] = np.random.choice(sample_experience, size=len(usa_jobs_df))
usa_jobs_df['RemoteOption'] = np.random.choice(sample_remote, size=len(usa_jobs_df))
usa_jobs_df['JobType'] = np.random.choice(sample_jobtype, size=len(usa_jobs_df))
usa_jobs_df['Link'] = sample_link
usa_jobs_df['PostedDate'] = pd.to_datetime(np.random.choice(
    pd.date_range('2025-01-01', '2025-04-25'), size=len(usa_jobs_df)))
usa_jobs_df['Applications'] = np.random.randint(100, 500, size=len(usa_jobs_df))
usa_jobs_df['SavedCount'] = np.random.randint(100, 300, size=len(usa_jobs_df))
usa_jobs_df['ViewCount'] = np.random.randint(200, 1000, size=len(usa_jobs_df))

# Step 7: Assemble final structured DataFrame
final_df = pd.DataFrame()
final_df['Role'] = usa_jobs_df['Role']
final_df['JobTitle'] = usa_jobs_df['JobTitle']
final_df['Company'] = usa_jobs_df['Company']
final_df['SalaryRange'] = usa_jobs_df['SalaryRange']
final_df['Location'] = usa_jobs_df['Location']
final_df['ExperienceLevel'] = usa_jobs_df['ExperienceLevel']
final_df['RemoteOption'] = usa_jobs_df['RemoteOption']
final_df['JobType'] = usa_jobs_df['JobType']
final_df['Link'] = usa_jobs_df['Link']
final_df['City'] = usa_jobs_df['City']
final_df['State'] = usa_jobs_df['State']
final_df['RequiredSkills'] = usa_jobs_df['RequiredSkills']
final_df['PostedDate'] = usa_jobs_df['PostedDate']
final_df['Applications'] = usa_jobs_df['Applications']
final_df['SavedCount'] = usa_jobs_df['SavedCount']
final_df['ViewCount'] = usa_jobs_df['ViewCount']

# Step 8: Export to CSV
final_df.to_csv(output_path, index=False)
print(f"✅ Job dataset saved to: {output_path}")
