import os
import joblib
import pandas as pd

from student.models import Student


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    'ml',
    'models',
    'career_model.pkl'
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    'ml',
    'models',
    'feature_names.pkl'
)


model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)


SKILL_MAPPING = {
    'REST API': 'REST_API',
    'Scikit-learn': 'Scikit_learn',
    'Machine Learning': 'Machine_Learning',
    'Deep Learning': 'Deep_Learning',
    'Natural Language Processing': 'NLP',
    'Power BI': 'Power_BI',
    'Network Security': 'Network_Security',
    'Ethical Hacking': 'Ethical_Hacking',
    'Database Management': 'Database_Management',
    'CI/CD': 'CICD',
}


def predict_careers(student):

    student_skills = student.student_skills.select_related(
        'skill'
    ).all()

    skill_vector = {
        feature: 0
        for feature in feature_names
    }

    for student_skill in student_skills:

        skill_name = student_skill.skill.skill_name

        ml_skill_name = SKILL_MAPPING.get(
            skill_name,
            skill_name
        )

        if ml_skill_name in skill_vector:
            skill_vector[ml_skill_name] = 1

    input_data = pd.DataFrame(
        [skill_vector],
        columns=feature_names
    )

    probabilities = model.predict_proba(
        input_data
    )[0]

    classes = model.classes_

    results = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )

    top_results = []

    for career, probability in results[:3]:
        top_results.append({
            'career': career,
            'probability': round(
                probability * 100,
                2
            )
        })

    return top_results

from career.models import Career, CareerSkill


def get_skill_gap(student, career_name):

    # Get the selected career
    career = Career.objects.get(
        career_name=career_name
    )

    # Get student's current skills
    student_skill_names = set(
        student.student_skills.values_list(
            'skill__skill_name',
            flat=True
        )
    )

    # Get skills required for the career
    required_skills = CareerSkill.objects.filter(
        career=career
    ).select_related('skill')

    skills_have = []
    skills_missing = []

    for career_skill in required_skills:

        skill_name = career_skill.skill.skill_name

        if skill_name in student_skill_names:

            skills_have.append({
                'name': skill_name,
                'importance': career_skill.get_importance_display()
            })

        else:

            skills_missing.append({
                'name': skill_name,
                'importance': career_skill.get_importance_display()
            })

    return skills_have, skills_missing
SKILL_RECOMMENDATIONS = {

    'Python': {
        'description': 'Learn Python programming fundamentals and object-oriented programming.',
        'action': 'Practice Python programs and build small applications.'
    },

    'Django': {
        'description': 'Learn Django for building Python-based web applications.',
        'action': 'Build a CRUD web application using Django.'
    },

    'Flask': {
        'description': 'Learn Flask for developing lightweight Python web applications.',
        'action': 'Create a small Flask REST API project.'
    },

    'REST API': {
        'description': 'Learn how applications communicate using REST APIs.',
        'action': 'Build and consume a REST API using Django or Flask.'
    },

    'Git': {
        'description': 'Learn version control for managing source code.',
        'action': 'Practice Git commands and maintain your projects using Git.'
    },

    'GitHub': {
        'description': 'Learn GitHub for storing and collaborating on software projects.',
        'action': 'Create repositories and upload your projects to GitHub.'
    },

    'SQL': {
        'description': 'Learn SQL for storing, retrieving and manipulating database data.',
        'action': 'Practice SELECT, JOIN, GROUP BY, subqueries and database operations.'
    },

    'JavaScript': {
        'description': 'Learn JavaScript for adding interactive behavior to web applications.',
        'action': 'Build interactive pages using HTML, CSS and JavaScript.'
    },

    'HTML': {
        'description': 'Learn HTML for creating the structure of web pages.',
        'action': 'Create webpages using semantic HTML elements and forms.'
    },

    'CSS': {
        'description': 'Learn CSS for designing and styling web pages.',
        'action': 'Practice layouts, responsive design and modern CSS.'
    },

    'Bootstrap': {
        'description': 'Learn Bootstrap for creating responsive user interfaces quickly.',
        'action': 'Build responsive pages using Bootstrap components.'
    },

    'Pandas': {
        'description': 'Learn Pandas for data manipulation and analysis.',
        'action': 'Practice reading CSV files and performing data analysis with Pandas.'
    },

    'NumPy': {
        'description': 'Learn NumPy for numerical and array-based computing.',
        'action': 'Practice arrays, mathematical operations and data processing.'
    },

    'Statistics': {
        'description': 'Learn statistics to understand and interpret data.',
        'action': 'Practice mean, median, probability, distributions and correlation.'
    },

    'Excel': {
        'description': 'Learn Excel for organizing, analyzing and visualizing data.',
        'action': 'Practice formulas, functions, tables and charts.'
    },

    'Power BI': {
        'description': 'Learn Power BI for interactive data visualization and dashboards.',
        'action': 'Create dashboards using sample datasets.'
    },

    'Machine Learning': {
        'description': 'Learn machine learning concepts and algorithms.',
        'action': 'Practice classification, regression and model evaluation.'
    },

    'Scikit-learn': {
        'description': 'Learn Scikit-learn for implementing machine learning algorithms in Python.',
        'action': 'Build classification and regression models.'
    },

    'TensorFlow': {
        'description': 'Learn TensorFlow for building and training machine learning models.',
        'action': 'Build a basic neural network using TensorFlow.'
    },

    'Deep Learning': {
        'description': 'Learn neural networks and deep learning techniques.',
        'action': 'Practice basic neural networks and image classification.'
    },

    'Linux': {
        'description': 'Learn Linux commands and system administration basics.',
        'action': 'Practice Linux terminal commands and file management.'
    },

    'Docker': {
        'description': 'Learn containerization for packaging and deploying applications.',
        'action': 'Containerize a simple Python application using Docker.'
    },

    'AWS': {
        'description': 'Learn cloud computing concepts using Amazon Web Services.',
        'action': 'Explore basic AWS services and deploy a small application.'
    },

    'Cybersecurity': {
        'description': 'Learn the fundamentals of protecting systems and applications.',
        'action': 'Study common security threats and basic security practices.'
    },

    'Network Security': {
        'description': 'Learn how networks are protected from unauthorized access and attacks.',
        'action': 'Study firewalls, authentication and network security fundamentals.'
    },

    'Ethical Hacking': {
        'description': 'Learn authorized security testing techniques.',
        'action': 'Practice security concepts in legal lab environments.'
    },

    'Cryptography': {
        'description': 'Learn techniques used to protect information through encryption.',
        'action': 'Study encryption, hashing and digital signatures.'
    },
}
def get_skill_recommendations(skills_missing):

    recommendations = []

    for skill in skills_missing:

        skill_name = skill['name']

        recommendation = SKILL_RECOMMENDATIONS.get(
            skill_name,
            {
                'description': f'Learn the fundamentals of {skill_name}.',
                'action': f'Practice {skill_name} through tutorials and small projects.'
            }
        )

        recommendations.append({
            'name': skill_name,
            'importance': skill['importance'],
            'description': recommendation['description'],
            'action': recommendation['action']
        })

    return recommendations