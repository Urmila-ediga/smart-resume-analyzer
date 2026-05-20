# smart-resume-analyzer
AI-powered resume parser and career guidance system using NLP and LLaMA
🚀 Overview

Smart Resume Analyzer is an AI-powered web application developed to automate resume analysis and provide intelligent career guidance. The system extracts information from resumes, analyzes candidate profiles using Large Language Models (LLaMA 3.1 via Groq API), identifies skills, determines domain, calculates job match scores, and recommends suitable job roles.

The project is developed using Python and Streamlit with integration of Natural Language Processing (NLP), Artificial Intelligence (AI), and Machine Learning concepts.

✨ Features
📤 Upload Resume (PDF/DOCX)
📄 Resume Text Extraction
🤖 AI-Based Resume Analysis
🧠 Skill Extraction
🎯 Domain Detection
📊 Job Match Score Calculation
💼 Job Recommendations
📉 Skill Gap Analysis
📧 Automatic Email Sending of Reports
📥 Downloadable Resume Analysis Report
🌐 Interactive Streamlit UI
🛠️ Technologies Used
Technology	Purpose
Python	Core Programming
Streamlit	Frontend UI
Groq API	LLaMA AI Integration
NLP	Resume Text Processing
PyMuPDF	PDF Text Extraction
python-docx	DOCX Text Extraction
Pandas	Data Handling
Scikit-learn	Job Match Logic
SMTP	Email Sending
📂 Project Structure
Smart-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── sample_resumes/
⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/smart-resume-analyzer.git
2️⃣ Open Project Folder
cd smart-resume-analyzer
3️⃣ Install Required Libraries
pip install -r requirements.txt
🔑 API Setup
Groq API
Create account at:
👉 https://console.groq.com/
Generate API Key
Create .env file:
GROQ_API_KEY=your_api_key_here
📧 Email Setup

To enable automatic email sending:

Step 1:

Create Gmail account

Step 2:

Enable 2-Step Verification

Step 3:

Generate App Password

👉 https://myaccount.google.com/apppasswords

Step 4:

Update in app.py

sender_email = "your_email@gmail.com"
app_password = "your_generated_app_password"
▶️ Run the Project
streamlit run app.py
📌 Working Flow
User uploads resume
System extracts text
AI analyzes resume
Skills are identified
Domain is detected
Job match score is calculated
Suitable job roles are recommended
Final report is generated
Report is downloaded and sent to email
📊 Output Includes
Candidate Summary
Skills
Strengths & Weaknesses
Job Match Score
Domain Identification
Skill Suggestions
Recommended Jobs
Downloadable Report
Email Report Delivery
🎯 Future Enhancements
Multilingual Resume Support
LinkedIn Integration
Cloud Database Support
Deep Learning Models
Real-Time Job Portal Integration
Mobile Application Support
👨‍💻 Developed By

Urmila Ediga
Final Year Project
AI-Powered Career Guidance System Through Resume Parsing

📜 License

This project is developed for educational and academic purposes.
