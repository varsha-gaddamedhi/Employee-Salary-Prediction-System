import pickle
import pandas as pd

# Load trained model
try:
    model = pickle.load(open("salary_model.pkl", "rb"))
except FileNotFoundError:
    print("Error: salary_model.pkl not found!")
    print("Run your notebook first to generate the model file.")
    exit()

print("\n===== Employee Salary Prediction System =====\n")

# Age
age = int(input("Enter Age: "))
if age < 18:
    print("Error: Employee age must be at least 18.")
    exit()

# Experience
experience = int(input("Enter Years of Experience: "))
if experience < 0:
    print("Error: Experience cannot be negative.")
    exit()

if experience > (age - 18):
    print("Error: Invalid input!")
    print("Experience cannot exceed working years after age 18.")
    exit()

# Skills
skills = int(input("Enter Skills Score (1-10): "))
if skills < 1 or skills > 10:
    print("Error: Skills Score must be between 1 and 10.")
    exit()

# Certifications
certifications = int(input("Enter Number of Certifications: "))
if certifications < 0:
    print("Error: Certifications cannot be negative.")
    exit()

# Education
print("\nEducation Level:")
print("0 - Bachelor's")
print("1 - Master's")
print("2 - PhD")

education = int(input("Enter choice: "))
if education not in [0, 1, 2]:
    print("Invalid Education Level.")
    exit()

# Job Role
print("\nJob Role:")
print("0 - Developer")
print("1 - Data Analyst")
print("2 - Manager")
print("3 - Designer")
print("4 - Data Scientist")

role = int(input("Enter choice: "))
if role not in [0, 1, 2, 3, 4]:
    print("Invalid Job Role.")
    exit()

# Company Type
print("\nCompany Type:")
print("0 - Startup")
print("1 - MNC")
print("2 - Medium Scale")

company = int(input("Enter choice: "))
if company not in [0, 1, 2]:
    print("Invalid Company Type.")
    exit()

# Gender
print("\nGender:")
print("0 - Male")
print("1 - Female")

gender = int(input("Enter choice: "))
if gender not in [0, 1]:
    print("Invalid Gender.")
    exit()

# Work Hours
hours = int(input("Enter Work Hours Per Week (20-80): "))
if hours < 20 or hours > 80:
    print("Invalid Work Hours.")
    exit()

# Create dataframe with feature names
sample = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "EducationLevel": [education],
    "YearsOfExperience": [experience],
    "JobRole": [role],
    "SkillsScore": [skills],
    "Certifications": [certifications],
    "CompanyType": [company],
    "WorkHoursPerWeek": [hours]
})

# Predict
prediction = model.predict(sample)

print("\n====================================")
print(f"Predicted Employee Salary: ₹{prediction[0]:,.2f}")
print("====================================")