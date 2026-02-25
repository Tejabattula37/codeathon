import streamlit as st
import pandas as pd

# ---------------------------------
# JOB ROLES & SKILLS
# ---------------------------------
job_roles = {
    "Software Developer": [
        "python", "java", "c", "data structures",
        "algorithms", "git", "sql", "problem solving"
    ],
    "Data Analyst": [
        "python", "excel", "sql",
        "statistics", "data analysis", "visualization"
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning",
        "numpy", "pandas", "model training"
    ],
    "Python Developer": [
        "python", "django", "flask",
        "sql", "git", "api development"
    ],
    "Java Developer": [
        "java", "spring", "sql",
        "oops", "git", "problem solving"
    ]
}

# ---------------------------------
# AI KEYWORD EXPANSION (SMART MATCH)
# ---------------------------------
ai_keywords = {
    "python": ["python", "py"],
    "java": ["java", "jdk"],
    "sql": ["sql", "mysql", "postgresql"],
    "git": ["git", "github"],
    "data structures": ["data structures", "dsa"],
    "algorithms": ["algorithms", "algo"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "visualization": ["visualization", "power bi", "tableau"],
    "api development": ["api", "rest api"],
    "oops": ["oops", "object oriented"]
}

# ---------------------------------
# RECOMMENDATIONS
# ---------------------------------
recommendations = {
    "python": "Practice Python on LeetCode / CodeChef",
    "java": "Build Java mini projects",
    "c": "Revise C fundamentals",
    "sql": "Practice SQL queries",
    "git": "Learn Git & GitHub",
    "data structures": "Practice DSA daily",
    "algorithms": "Solve algorithm problems",
    "machine learning": "Study ML algorithms",
    "deep learning": "Learn neural networks",
    "visualization": "Learn Power BI / Tableau",
    "api development": "Build REST APIs",
    "oops": "Revise OOP concepts"
}

# ---------------------------------
# HELPER FUNCTIONS
# ---------------------------------
def detect_experience(text):
    if "intern" in text or "fresher" in text:
        return "Fresher"
    elif "experience" in text or "worked" in text:
        return "Intermediate"
    else:
        return "Beginner"

def resume_strength(score):
    if score >= 80:
        return "Strong 💪"
    elif score >= 60:
        return "Moderate 🙂"
    else:
        return "Weak ⚠"

def ai_match(skill, text):
    words = ai_keywords.get(skill, [skill])
    return any(w in text for w in words)

# ---------------------------------
# UI
# ---------------------------------
st.set_page_config(page_title="Resume Screening Tool", layout="centered")

st.title("📄 Resume Screening & Scoring Tool")
st.subheader("AI-Powered | Hackathon Edition 🚀")

resume_text = st.text_area("📌 Paste Resume Text", height=220)
role = st.selectbox("🎯 Select Job Role", job_roles.keys())

if st.button("🔍 Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("⚠ Please paste resume text")
    else:
        text = resume_text.lower()
        skills = job_roles[role]

        matched = []
        missing = []

        for skill in skills:
            if ai_match(skill, text):
                matched.append(skill)
            else:
                missing.append(skill)

        score = round((len(matched) / len(skills)) * 100, 2)

        st.success("✅ Analysis Completed")

        # ---------------- METRICS ----------------
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Score", f"{score}%")
        col2.metric("🧑‍💼 Experience", detect_experience(text))
        col3.metric("⭐ Strength", resume_strength(score))

        st.progress(score / 100)

        # ---------------- GRAPH ----------------
        st.subheader("📊 Skill Match Overview")

        df = pd.DataFrame({
            "Skill Type": ["Matched", "Missing"],
            "Count": [len(matched), len(missing)]
        })

        st.bar_chart(df.set_index("Skill Type"))

        # ---------------- DETAILS ----------------
        st.markdown("### ✅ Matched Skills")
        for s in matched:
            st.write("✔", s)

        st.markdown("### ❌ Missing Skills")
        for s in missing:
            st.write("✖", s)

        st.markdown("### 📌 AI Recommendations")
        for s in missing:
            st.write("➜", recommendations.get(s, "Improve this skill"))

        st.markdown("---")
        st.caption("🚀 AI Resume Screening Tool | Codeathon Ready")