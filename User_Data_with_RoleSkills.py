import pandas as pd
import random

# Load your Excel file
input_path = "/Users/sowmyakakularapu/Downloads/User_Data.xlsx"
output_path = "/Users/sowmyakakularapu/Downloads/User_Data_With_RoleSkills.csv"

user_data_df = pd.read_excel(input_path)

# Define 20 roles with their required skills
roles_skills = {
    "Data Scientist": ["Python", "Machine Learning", "Data Analysis", "SQL", "Statistics", "TensorFlow"],
    "Data Engineer": ["SQL", "Python", "AWS", "Spark", "Data Warehousing", "ETL"],
    "Software Developer": ["Java", "Spring Boot", "SQL", "React", "HTML", "CSS"],
    "Cloud Engineer": ["AWS", "Azure", "Linux", "Docker", "Kubernetes", "Terraform"],
    "Cybersecurity Analyst": ["Networking", "Python", "Ethical Hacking", "Cybersecurity", "Risk Assessment", "SIEM"],
    "AI Engineer": ["Python", "Deep Learning", "TensorFlow", "Keras", "PyTorch", "OpenCV"],
    "Business Analyst": ["Excel", "SQL", "Data Visualization", "Power BI", "Critical Thinking", "UML"],
    "DevOps Engineer": ["CI/CD", "Jenkins", "Docker", "Kubernetes", "Git", "Terraform"],
    "ML Engineer": ["Python", "Scikit-learn", "Machine Learning", "TensorFlow", "Pandas", "Model Deployment"],
    "UI/UX Designer": ["Figma", "Adobe XD", "User Research", "Prototyping", "Wireframing", "Sketch"],
    "Mobile App Developer": ["Kotlin", "Java", "Swift", "Flutter", "React Native", "APIs"],
    "Full Stack Developer": ["Node.js", "React", "MongoDB", "Express", "HTML", "CSS"],
    "System Administrator": ["Linux", "Shell Scripting", "Networking", "Monitoring Tools", "Windows Server", "Active Directory"],
    "Network Engineer": ["Routing", "Switching", "Firewall", "TCP/IP", "Cisco", "VPN"],
    "QA Tester": ["Selenium", "Test Cases", "Bug Tracking", "Automation", "JIRA", "Postman"],
    "Technical Writer": ["Documentation", "Markdown", "API Docs", "MS Word", "Confluence", "Version Control"],
    "Product Manager": ["Agile", "Scrum", "Wireframing", "User Stories", "Roadmapping", "Prioritization"],
    "Database Administrator": ["SQL", "Oracle", "Backup/Recovery", "Indexes", "Performance Tuning", "PL/SQL"],
    "Blockchain Developer": ["Solidity", "Ethereum", "Smart Contracts", "Cryptography", "Node.js", "Web3.js"],
    "Game Developer": ["Unity", "C#", "Game Physics", "Animation", "Level Design", "3D Modeling"]
}

# Define role descriptions
role_descriptions = {
    "Data Scientist": "Analyze and interpret complex data to help companies make decisions.",
    "Data Engineer": "Develop, construct, test and maintain architectures such as databases and large-scale processing systems.",
    "Software Developer": "Design, build, and maintain software applications.",
    "Cloud Engineer": "Design and manage cloud-based infrastructure and services.",
    "Cybersecurity Analyst": "Protect systems and networks from cyber threats and attacks.",
    "AI Engineer": "Build and deploy AI models and applications that simulate human behavior.",
    "Business Analyst": "Bridge the gap between business needs and tech solutions using data analysis.",
    "DevOps Engineer": "Automate and streamline development and deployment pipelines.",
    "ML Engineer": "Develop and deploy machine learning models in production.",
    "UI/UX Designer": "Design user-friendly interfaces based on research and usability principles.",
    "Mobile App Developer": "Build responsive mobile applications for iOS and Android.",
    "Full Stack Developer": "Develop front-end and back-end components of web applications.",
    "System Administrator": "Manage and maintain servers, networks, and IT infrastructure.",
    "Network Engineer": "Design and maintain computer networks including routers and firewalls.",
    "QA Tester": "Test applications to identify bugs and ensure quality and functionality.",
    "Technical Writer": "Create clear and concise user manuals and technical documentation.",
    "Product Manager": "Define product vision, manage roadmaps, and work with cross-functional teams.",
    "Database Administrator": "Maintain databases for performance, security, and availability.",
    "Blockchain Developer": "Develop and maintain decentralized blockchain applications.",
    "Game Developer": "Create interactive games using engines like Unity or Unreal."
}

# Generate updated user dataset
updated_users = []
for _, row in user_data_df.iterrows():
    role = random.choice(list(roles_skills.keys()))
    required_skills = roles_skills[role]
    known_skills = random.sample(required_skills, random.randint(3, 5))
    
    updated_row = row.copy()
    updated_row["Role"] = role
    updated_row["KnownSkills"] = ", ".join(known_skills)
    updated_row["RequiredSkills"] = ", ".join(required_skills)
    updated_row["RoleDescription"] = role_descriptions[role]
    
    updated_users.append(updated_row)

# Save the updated dataset
final_users_df = pd.DataFrame(updated_users)
final_users_df.to_csv(output_path, index=False)

print(f"✅ User data updated with 20 roles and saved to:\n{output_path}")

