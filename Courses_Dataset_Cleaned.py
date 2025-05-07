import pandas as pd
import random
import numpy as np


output_path = "/Users/sowmyakakularapu/Downloads/Courses_Dataset_for_All_Skills.csv"

# used skills required for job roles we used
skills = [
    'Python', 'Pandas', 'TensorFlow', 'Scikit-learn', 'SQL', 'Matplotlib', 'ETL', 'Apache Spark',
    'Hadoop', 'Airflow', 'HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'TypeScript', 'Java',
    'Spring Boot', 'REST APIs', 'Hibernate', 'PostgreSQL', 'Docker', 'Kubernetes', 'CI/CD',
    'Terraform', 'AWS', 'Linux', 'PyTorch', 'MLflow', 'Model Deployment', 'Azure',
    'CloudFormation', 'IAM', 'Node.js', 'MongoDB', 'Express.js', 'Kotlin', 'Swift', 'Flutter',
    'React Native', 'Xcode', 'Network Security', 'Firewalls', 'SIEM', 'Threat Analysis',
    'Encryption', 'Figma', 'Sketch', 'Adobe XD', 'User Research', 'Prototyping', 'Wireframing',
    'Selenium', 'Postman', 'TestNG', 'JUnit', 'Automation', 'Manual Testing', 'Deep Learning',
    'Neural Networks', 'NLP', 'Computer Vision', 'Unity', 'C#', 'Unreal Engine', 'Blender',
    'Game Physics', '3D Modeling', 'Oracle', 'Backup & Recovery', 'Performance Tuning', 'MySQL',
    'Excel', 'Power BI', 'Tableau', 'Business Strategy', 'Stakeholder Management', 'Agile',
    'Scrum', 'Jira', 'Team Facilitation', 'Sprint Planning', 'Retrospectives', 'Roadmapping',
    'User Stories', 'Stakeholder Communication', 'Analytics', 'MVP', 'Solidity', 'Ethereum',
    'Smart Contracts', 'Web3.js', 'Crypto Wallets', 'Truffle', 'Monitoring', 'Incident Management',
    'SLAs', 'Prometheus', 'Grafana'
]
#links of platforms
platforms = {
    "Coursera": "https://www.coursera.org/search?query={}",
    "Udemy": "https://www.udemy.com/courses/search/?q={}",
    "LinkedIn Learning": "https://www.linkedin.com/learning/search?keywords={}"
}

course_levels = ["Beginner", "Intermediate", "Advanced"]


rows = []
for skill in skills:
    for platform, url_template in platforms.items():
        rows.append({
            "Skill": skill,
            "CourseName": f"{skill} Mastery with {platform}",
            "Platform": platform,
            "Link": url_template.format(skill.lower().replace(" ", "%20")),
            "CourseLevel": random.choice(course_levels),
            "DurationHours": random.randint(8, 40),
            "Cost": random.choice(["Free", "$29", "$49", "$99"]),
            "CertificationAvailable": random.choice(["Yes", "No"]),
            "Rating": round(random.uniform(3.5, 5.0), 2),
            "ReviewCount": random.randint(500, 100000)
        })


df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)

print(f"✅ Exact dataset regenerated at:\n{output_path}")



