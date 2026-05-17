print("=== Resume Analyzer ===")
resume_text = input("Paste your resume text:\n").lower()
with open("skills.txt", "r") as file:
    skills = file.read().splitlines()
matched_skills = []
for skill in skills:
    if skill in resume_text:
        matched_skills.append(skill)
score = len(matched_skills)
print("\nResume Analysis Result")
print("------------------------")

if matched_skills:
    print("Skills Found:")

    for skill in matched_skills:
        print("-", skill)
else:
    print("No matching skills found.")

print("\nResume Score:", score)
if score >= 8:
    print("Strong Profile")
elif score >= 4:
    print("Moderate Profile")
else:
    print("Needs Improvement")
