# Esse código gera mais linhas do dataset, com dropout_risk = Yes

import pandas as pd
import numpy as np

# Definir colunas
columns = [
    "student_id", "age", "gender", "major", "study_hours_per_day", "social_media_hours", "netflix_hours",
    "part_time_job", "attendance_percentage", "sleep_hours", "diet_quality", "exercise_frequency",
    "parental_education_level", "internet_quality", "mental_health_rating", "extracurricular_participation",
    "previous_gpa", "semester", "stress_level", "dropout_risk", "social_activity", "screen_time",
    "study_environment", "access_to_tutoring", "family_income_range", "parental_support_level",
    "motivation_level", "exam_anxiety_score", "learning_style", "time_management_score", "exam_score"
]

# Valores possíveis
genders = ["Male", "Female", "Other"]
majors = ["Computer Science", "Engineering", "Business", "Psychology", "Biology", "Mathematics", "Physics", "Economics"]
part_time_job = ["Yes", "No"]
diet_qualities = ["Poor", "Average", "Good", "Excellent"]
exercise_frequencies = list(range(8))
parental_education_levels = ["None", "High School", "Some College", "Bachelor", "Master", "PhD"]
internet_qualities = ["Low", "Medium", "High"]
extracurricular_participation = ["Yes", "No"]
study_environments = ["Home", "Library", "Co-Learning Group", "Cafe", "Quiet Room"]
access_to_tutoring = ["Yes", "No"]
family_income_ranges = ["Low", "Medium", "High"]
parental_support_levels = list(range(1, 11))
motivation_levels = list(range(1, 10))
learning_styles = ["Reading", "Visual", "Auditory", "Kinesthetic"]
semesters = list(range(1, 11))
social_activities = list(range(8))

# Gerador de uma linha
def generate_row(student_id):
    smh = np.random.uniform(1, 5)
    nh = np.random.uniform(0, 4)
    screen_time = smh + nh + np.random.uniform(0, 5)
    return [
        student_id,
        np.random.randint(18, 30),
        np.random.choice(genders),
        np.random.choice(majors),
        np.random.uniform(0.5, 8),
        smh,
        nh,
        np.random.choice(part_time_job),
        np.random.uniform(50, 90),
        np.random.uniform(4, 8),
        np.random.choice(diet_qualities),
        np.random.choice(exercise_frequencies),
        np.random.choice(parental_education_levels),
        np.random.choice(internet_qualities),
        np.random.uniform(1, 10),
        np.random.choice(extracurricular_participation),
        np.random.uniform(0, 4),
        np.random.choice(semesters),
        np.random.uniform(4, 10),
        "Yes",
        np.random.choice(social_activities),
        screen_time,
        np.random.choice(study_environments),
        np.random.choice(access_to_tutoring),
        np.random.choice(family_income_ranges),
        np.random.choice(parental_support_levels),
        np.random.choice(motivation_levels),
        np.random.uniform(1, 10),
        np.random.choice(learning_styles),
        np.random.uniform(1, 10),
        np.random.uniform(40, 100)
    ]

# Gerar 10.000 linhas
data = [generate_row(i) for i in range(196964, 196964 + 10000)]
df = pd.DataFrame(data, columns=columns)

# Salvar em CSV se desejar
df.to_csv("dropout_students_yes.csv", index=False)
