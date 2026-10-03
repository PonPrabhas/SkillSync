import os
import random
import pandas as pd


# -----------------------------
# Skill list
# -----------------------------

skills = [
    'Python',
    'Java',
    'C',
    'C++',
    'JavaScript',
    'HTML',
    'CSS',
    'Bootstrap',
    'Django',
    'Flask',
    'REST_API',
    'SQL',
    'MySQL',
    'PostgreSQL',
    'MongoDB',
    'Database_Management',
    'Pandas',
    'NumPy',
    'Matplotlib',
    'Statistics',
    'Excel',
    'Power_BI',
    'Machine_Learning',
    'Scikit_learn',
    'TensorFlow',
    'Deep_Learning',
    'NLP',
    'Git',
    'GitHub',
    'Docker',
    'AWS',
    'Linux',
    'CICD',
    'Kubernetes',
    'Cybersecurity',
    'Network_Security',
    'Ethical_Hacking',
    'Cryptography'
]


# -----------------------------
# Career skill patterns
# -----------------------------

career_skills = {

    'Python Developer': [
        'Python',
        'Django',
        'Flask',
        'SQL',
        'REST_API',
        'Git',
        'GitHub'
    ],

    'Full Stack Developer': [
        'HTML',
        'CSS',
        'JavaScript',
        'Bootstrap',
        'Python',
        'Django',
        'SQL',
        'REST_API',
        'Git',
        'GitHub'
    ],

    'Data Analyst': [
        'Python',
        'SQL',
        'Pandas',
        'NumPy',
        'Statistics',
        'Excel',
        'Power_BI',
        'Matplotlib'
    ],

    'Data Scientist': [
        'Python',
        'SQL',
        'Pandas',
        'NumPy',
        'Statistics',
        'Matplotlib',
        'Machine_Learning',
        'Scikit_learn'
    ],

    'Machine Learning Engineer': [
        'Python',
        'NumPy',
        'Pandas',
        'Machine_Learning',
        'Scikit_learn',
        'TensorFlow',
        'Deep_Learning',
        'Git',
        'Docker'
    ],

    'Java Developer': [
        'Java',
        'SQL',
        'Database_Management',
        'REST_API',
        'Git',
        'GitHub'
    ],

    'Web Developer': [
        'HTML',
        'CSS',
        'JavaScript',
        'Bootstrap',
        'REST_API',
        'Git',
        'GitHub'
    ],

    'Database Administrator': [
        'SQL',
        'MySQL',
        'PostgreSQL',
        'Database_Management',
        'Linux',
        'Git'
    ],

    'DevOps Engineer': [
        'Linux',
        'Git',
        'GitHub',
        'Docker',
        'AWS',
        'CICD',
        'Kubernetes',
        'Python'
    ],

    'Cybersecurity Analyst': [
        'Cybersecurity',
        'Network_Security',
        'Linux',
        'Ethical_Hacking',
        'Cryptography',
        'Python'
    ]
}


# -----------------------------
# Generate dataset
# -----------------------------

rows = []

random.seed(42)

for career, required_skills in career_skills.items():

    for _ in range(150):

        row = {}

        for skill in skills:

            if skill in required_skills:

                # Required skills are usually present
                row[skill] = random.choice([0, 1, 1, 1])

            else:

                # Some unrelated skills may also be present
                row[skill] = random.choice([0, 0, 0, 1])

        row['Career'] = career

        rows.append(row)


# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame(rows)


# -----------------------------
# Save CSV
# -----------------------------

output_path = os.path.join(
    os.path.dirname(__file__),
    'dataset',
    'career_skills.csv'
)

df.to_csv(
    output_path,
    index=False
)

print("Dataset created successfully!")
print()
print("Rows:", len(df))
print("Columns:", len(df.columns))
print()
print("Career distribution:")
print(df['Career'].value_counts())
print()
print("Saved to:")
print(output_path)