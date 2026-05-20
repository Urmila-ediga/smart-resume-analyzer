#last modified with css
import streamlit as st
import os
import fitz
from docx import Document
from dotenv import load_dotenv
from groq import Groq

# -------------------------------
# UI Styling
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load API Key
# -------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ Groq API key not found! Add it in .env file")

# -------------------------------
# Extract Text
# -------------------------------
def extract_text(uploaded_file):
    text = ""
    try:
        if uploaded_file.type == "application/pdf":
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
                for page in pdf:
                    text += page.get_text()
        elif uploaded_file.type in [
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/msword",
        ]:
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        else:
            st.warning("⚠️ Upload PDF or DOCX only")
    except Exception as e:
        st.error(f"Error reading file: {e}")
    return text.strip()

# -------------------------------
# AI Analysis
# -------------------------------
def analyze_resume(resume_text, job_description=None):
    try:
        client = Groq(api_key=GROQ_API_KEY)

        prompt = f"""
        You are an AI resume analyzer.

        1. Extract candidate name
        2. Summarize education and experience
        3. List key skills
        4. Give strengths and weaknesses
        5. Suggest suitable job roles
        """

        if job_description:
            prompt += f"\nCompare with this job description:\n{job_description}"

        prompt += f"\n\nResume:\n{resume_text[:8000]}"

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"

# -------------------------------
# Skill Gap (Fixed)
# -------------------------------
def skill_gap_analysis(resume_text):
    text = resume_text.lower()

    domain_skills = {
        "IT": ["python", "java", "sql", "react", "machine learning"],
        "Mechanical": ["solidworks", "thermodynamics", "manufacturing"],
        "Civil": ["construction", "surveying", "staad", "etabs", "revit"],
        "ECE": ["embedded", "vlsi", "microcontroller"],
        "Management": ["marketing", "finance", "excel", "communication"]
    }

    best_domain = "General"
    max_matches = 0
    present = []
    suggestions = []

    for domain, skills in domain_skills.items():
        matches = [s for s in skills if s in text]

        if len(matches) > max_matches:
            max_matches = len(matches)
            best_domain = domain
            present = matches
            suggestions = [s for s in skills if s not in text]

    return best_domain, present, suggestions

# -------------------------------
# Job Match Score
# -------------------------------
def job_match_score(resume_text, job_description):
    if not job_description:
        return None

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    if len(jd_words) == 0:
        return 0

    match = resume_words.intersection(jd_words)
    score = int((len(match) / len(jd_words)) * 100)

    return min(score, 100)

# -------------------------------
# Job Recommendation
# -------------------------------
def recommend_jobs(domain):
    if domain == "Civil":
        return ["Civil Engineer", "Site Engineer", "Structural Engineer"]
    elif domain == "Mechanical":
        return ["Mechanical Engineer", "Design Engineer"]
    elif domain == "IT":
        return ["Software Developer", "Data Analyst"]
    elif domain == "ECE":
        return ["Embedded Engineer", "VLSI Engineer"]
    elif domain == "Management":
        return ["Business Analyst", "Marketing Executive"]
    else:
        return ["General Graduate Roles"]

# -------------------------------
# UI HEADER
# -------------------------------
st.markdown('<div class="title">📄 Smart Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Career Guidance System</div>', unsafe_allow_html=True)

# -------------------------------
# INPUT SECTION
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Upload Resume", type=["pdf", "docx"])

with col2:
    job_description = st.text_area("📋 Job Description (optional)", height=150)

# -------------------------------
# BUTTON
# -------------------------------
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
analyze_btn = st.button("🚀 Analyze Resume")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# OUTPUT
# -------------------------------
if analyze_btn:
    if not uploaded_file:
        st.warning("Please upload a resume")
    else:
        text = extract_text(uploaded_file)

        if text:
            result = analyze_resume(text, job_description)

            score = job_match_score(text, job_description)
            if score is None:
                score = 75

            domain, present, suggestions = skill_gap_analysis(text)

            final_report = f"{result}\n\n🎯 Job Match Score: {score}%\n🎯 Field: {domain}"

            # AI RESULT
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("## 📊 AI Analysis")
            st.write(final_report)
            st.markdown('</div>', unsafe_allow_html=True)

            # SCORE
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("## 🎯 Job Match Score")
            st.progress(score)
            st.write(f"{score}% match")
            st.markdown('</div>', unsafe_allow_html=True)

            # SKILL ANALYSIS
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("## 📉 Skill Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.success(f"✅ Skills: {present}")

            with col2:
                st.info(f"📈 Suggestions: {suggestions}")

            st.markdown('</div>', unsafe_allow_html=True)

            # JOBS
            jobs = recommend_jobs(domain)

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("## 💼 Recommended Jobs")

            for job in jobs:
                st.write(f"🔹 {job}")

            st.markdown('</div>', unsafe_allow_html=True)

            # DOWNLOAD
            st.download_button("📥 Download Report", final_report)

        else:
            st.error("❌ Could not read file")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>🚀 Final Year Project | AI Resume Parser</p>", unsafe_allow_html=True)