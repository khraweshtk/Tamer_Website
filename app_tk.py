# Update the Streamlit resume app with your real contact info, links, and headshot.
from pathlib import Path
import shutil

# Copy the uploaded headshot to a known filename
src = Path("/mnt/data/99fb4f34-758c-4cc8-a82b-ea94bc276cc1.jpeg")
dst = Path("/mnt/data/headshot.jpg")
if src.exists():
    shutil.copy(src, dst)

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Muneeb Khan — Resume", page_icon="💼", layout="wide")

# -------------------- THEME / CSS --------------------
CSS = """
<style>
:root{
  --bg1:#0b1220; --bg2:#101a2b; --text:#e6f0ff; --muted:#a8b3c7;
  --primary:#22d3ee; --primary-2:#60a5fa; --card:#0f172a;
  --shadow: 0 8px 30px rgba(34,211,238,.15), 0 0 40px rgba(96,165,250,.1);
}
html, body, .block-container { background: radial-gradient(1200px 600px at -10% -10%, #0e1a2f 0%, #0b1220 35%, #0b1220 100%); }
.block-container{padding-top:4rem; color:var(--text);}

.gradient-text{
  font-weight:800; letter-spacing:.3px;
  background: linear-gradient(90deg, var(--primary) 0%, var(--primary-2) 60%);
  -webkit-background-clip:text; background-clip:text; color: transparent;
}
.navbar{
  position:fixed; top:0; left:0; right:0; height:64px;
  background:linear-gradient(180deg, rgba(13,23,41,.75), rgba(13,23,41,.45));
  backdrop-filter: blur(10px);
  border-bottom:1px solid rgba(255,255,255,.06);
  display:flex; align-items:center; justify-content:space-between;
  padding:0 24px; z-index:999;
}
.nav-left{font-size:1.35rem; font-weight:800;}
.nav-links{display:flex; gap:24px; align-items:center;}
.nav-link a{color:var(--text); text-decoration:none; opacity:.85;}
.nav-link a:hover{opacity:1; text-shadow:0 0 12px rgba(34,211,238,.6);}
.nav-cta{ padding:8px 14px; border-radius:10px; font-weight:600;
  background:linear-gradient(135deg, var(--primary), var(--primary-2));
  color:#001018; text-decoration:none; box-shadow: var(--shadow); }
.card{
  background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01));
  border:1px solid rgba(255,255,255,.08);
  border-radius:18px; padding:22px; box-shadow: var(--shadow);
}
.card-outline{
  border:1px solid rgba(34,211,238,.35);
  box-shadow: 0 0 0 2px rgba(34,211,238,.18), inset 0 0 40px rgba(34,211,238,.05);
  border-radius:18px; padding:26px; background:rgba(2,8,23,.35);
}
.section-title{ font-size:2.2rem; font-weight:800; margin:0 0 .6rem 0; }
.rule{ height:4px; width:140px; border-radius:999px; background: linear-gradient(90deg, var(--primary), transparent); }
.chips{display:flex; flex-wrap:wrap; gap:12px; margin-top:14px;}
.chip{
  display:inline-flex; align-items:center; gap:8px;
  padding:10px 14px; border-radius:14px;
  background: radial-gradient(120px 60px at 30% 20%, rgba(34,211,238,.16), rgba(255,255,255,.04));
  border:1px solid rgba(255,255,255,.08); font-weight:600; color:var(--text);
  box-shadow: var(--shadow);
}
.badge{font-size:.85rem; color:#a8b3c7;}
.muted{color:#a8b3c7;}
.mt-2{margin-top:.5rem;} .mt-4{margin-top:1rem;} .mt-6{margin-top:1.5rem;}
.small{font-size:.9rem;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -------------------- NAVBAR --------------------
st.markdown("""
<div class="navbar">
  <div class="nav-left gradient-text">Muneeb Khan</div>
  <div class="nav-links">
    <div class="nav-link"><a href="#home">Home</a></div>
    <div class="nav-link"><a href="#education">Education</a></div>
    <div class="nav-link"><a href="#experience">Experience</a></div>
    <div class="nav-link"><a href="#projects">Projects</a></div>
    <div class="nav-link"><a href="#activities">Activities</a></div>
    <div class="nav-link"><a href="#skills">Skills</a></div>
    <a class="nav-cta" href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------- DATA --------------------
DATA = {
  "contact": {
    "name": "Muneeb Khan",
    "citizenship": "US Citizen",
    "email": "khan.529@buckeyemail.osu.edu",
    "phone": "614-812-7692",
    "linkedin": "https://www.linkedin.com/in/muneeb-khan-3090a6290/",
    "github": "https://github.com/mkhan2050",
    "city": "Columbus, Ohio",
    "headshot": "headshot.jpg"
  },
  "education": {
    "school": "The Ohio State University, Columbus, Ohio",
    "degree": "B.S. in Computer Science and Engineering",
    "deans_list": "Dean’s List (>3.5 GPA)",
    "grad": "Expected Graduation, May 2026",
    "coursework": [
      "Fundamentals of Engineering", "Calculus 1", "Engineering Calculus",
      "Linear Algebra", "Differential Equations", "Physics Kinematics & Motion",
      "Electrical Circuits Physics", "C++", "Python", "Java",
      "Software 2", "Engineering Statistics"
    ],
    "certs": ["JPMorgan Chase & Co — Software Engineering Job Simulation"]
  },
  "experience": [
    {
      "role": "Undergraduate Research Assistant",
      "org": "The Ohio State University College of Medicine",
      "place": "Columbus, Ohio",
      "period": "Dec 2023 – Feb 2024",
      "points": [
        "Conducted data analysis on cardiomyocyte activity, automating repetitive tasks and saving 8 hours/week for the research team.",
        "Developed visualization tools that improved data interpretation efficiency by 25%, enabling quicker decision‑making.",
        "Streamlined team workflows by enhancing data accessibility, reducing preparation time for experiments by 10%."
      ]
    },
    {
      "role": "Software Developer Intern",
      "org": "Fee Dodger LLC",
      "place": "Columbus, Ohio",
      "period": "Mar 2024 – Present",
      "points": [
        "Collaborated with the team to design and integrate APIs, creating a framework projected to save 10+ hours/month of manual inventory tracking.",
        "Spearheaded planning and development of iOS and Android apps to increase accessibility for 100+ early adopters.",
        "Conducted beta testing with users, gathering feedback and addressing 30 improvements to refine the platform ahead of launch."
      ]
    },
    {
      "role": "Student IT Assistant — Engineering Technology Services",
      "org": "The Ohio State University College of Engineering",
      "place": "Columbus, Ohio",
      "period": "Jul 2024 – Present",
      "points": [
        "Investigated and resolved cybersecurity incidents using CrowdStrike, improving response time and securing over 200 devices.",
        "Performed networking tasks (router/switch configurations) to optimize departmental performance.",
        "Collaborated with the IT team to enhance infrastructure security, reducing system vulnerabilities by 20%."
      ]
    }
  ],
  "projects": [
    {
      "name": "Chatbot with Sentiment Analysis",
      "period": "Aug 2024 – Sep 2024",
      "points": [
        "Designed and developed an AI‑powered chatbot using Rasa and Dialogflow for positive/negative/neutral classification.",
        "Implemented NLP with VADER and BERT, achieving 92% accuracy during testing.",
        "Built customizable response templates for adaptability across use cases.",
        "Deployed with Flask, enabling scalability and future integration."
      ]
    },
    {
      "name": "To‑Do List Application with React",
      "period": "Oct 2024 – Nov 2024",
      "points": [
        "Created a responsive to‑do app in React with add/update/delete tasks.",
        "Applied state management techniques for smooth cross‑screen interactions.",
        "Implemented local storage to save up to 20 tasks per session.",
        "Designed an intuitive interface and feedback collection for early testers."
      ]
    },
    {
      "name": "AI‑Powered Predictive Maintenance for Automobiles",
      "period": "Nov 2024 – Dec 2024",
      "points": [
        "Developed a Python‑based predictive system on vehicle sensor data with 95% accuracy.",
        "Used Scikit‑learn and TensorFlow to detect patterns leading to mechanical failures.",
        "Implemented anomaly detection for engine health, brake systems, tire pressure, etc.",
        "Built insights dashboard with Plotly Dash for proactive decision‑making."
      ]
    }
  ],
  "activities": [
    {
      "name": "NAIMA — Youth Coordinator",
      "place": "Columbus, Ohio",
      "period": "Aug 2021 – Current",
      "points": [
        "Spearheaded and managed youth‑oriented programs and initiatives aimed at community development within a non‑profit organization."
      ]
    },
    {
      "name": "Clubs — The Ohio State University",
      "place": "Columbus, Ohio",
      "period": "Aug 2023 – Current",
      "points": [
        "Member of AI Club, Member of Collaborative Software Development Club, Member of Competitive Coding Club"
      ]
    }
  ],
  "skills": {
    "Programming": ["Java", "Python", "HTML/CSS/JS", "Node.js", "React.js", "MATLAB", "C++", "R"],
    "Tools": ["IntelliJ", "PyCharm", "Eclipse", "SolidWorks", "Webstorm", "MS Excel", "MS Word", "MS PowerPoint", "Adobe Acrobat", "Adobe Premiere Pro"],
    "Non‑Technical": ["Solution Oriented", "Skilled Collaborator", "Time Efficient", "Communication", "Critical Thinking"]
  }
}

def chips(items):
    st.markdown("<div class='chips'>" + "".join(f"<div class='chip'>{i}</div>" for i in items) + "</div>", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
left, right = st.columns([3,1.2], vertical_alignment="center")
with left:
    st.title(DATA["contact"]["name"])
    st.caption(f"{DATA['contact']['citizenship']}  •  {DATA['contact']['city']}")
    st.markdown(f"📞 **{DATA['contact']['phone']}**  |  ✉️ [{DATA['contact']['email']}](mailto:{DATA['contact']['email']})  |  🔗 [LinkedIn]({DATA['contact']['linkedin']})  |  🔧 [GitHub]({DATA['contact']['github']})")
with right:
    headshot_path = Path(DATA['contact']['headshot'])
    if headshot_path.exists():
        st.image(str(headshot_path), caption="", use_container_width=True)
    else:
        st.markdown("<div class='muted'>Upload headshot.jpg next to app.py</div>", unsafe_allow_html=True)

# -------------------- EDUCATION --------------------
st.markdown('<a id="education"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Education</div>", unsafe_allow_html=True)
st.markdown(f"<div class='card'><strong>{DATA['education']['school']}</strong><br/>{DATA['education']['degree']}<br/><span class='muted'>{DATA['education']['grad']} · {DATA['education']['deans_list']}</span></div>", unsafe_allow_html=True)
st.markdown("**Related Coursework**")
chips(DATA["education"]["coursework"])
st.markdown("**Certifications**")
for c in DATA["education"]["certs"]:
    st.markdown(f"- {c}")

# -------------------- EXPERIENCE --------------------
st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Experience</div>", unsafe_allow_html=True)
for e in DATA["experience"]:
    st.markdown(f"<div class='card'><div style='display:flex;justify-content:space-between;align-items:center;'>"
                f"<div><strong>{e['role']}</strong> · {e['org']} — <span class='muted'>{e['place']}</span></div>"
                f"<div class='muted'>{e['period']}</div></div></div>", unsafe_allow_html=True)
    for p in e["points"]:
        st.markdown(f"- {p}")

# -------------------- PROJECTS --------------------
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Projects</div>", unsafe_allow_html=True)
for p in DATA["projects"]:
    st.markdown(f"<div class='card-outline'><div style='display:flex;justify-content:space-between;align-items:center;'>"
                f"<div style='font-weight:700;font-size:1.05rem'>{p['name']}</div>"
                f"<div class='muted'>{p['period']}</div></div></div>", unsafe_allow_html=True)
    for b in p["points"]:
        st.markdown(f"- {b}")

# -------------------- ACTIVITIES --------------------
st.markdown('<a id="activities"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Activities & Leadership</div>", unsafe_allow_html=True)
for a in DATA["activities"]:
    st.markdown(f"<div class='card'><div style='display:flex;justify-content:space-between;align-items:center;'>"
                f"<div><strong>{a['name']}</strong> — <span class='muted'>{a['place']}</span></div>"
                f"<div class='muted'>{a['period']}</div></div></div>", unsafe_allow_html=True)
    for b in a["points"]:
        st.markdown(f"- {b}")

# -------------------- SKILLS --------------------
st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Skills</div>", unsafe_allow_html=True)
tabs = st.tabs(list(DATA["skills"].keys()))
for tab, key in zip(tabs, DATA["skills"].keys()):
    with tab:
        chips(DATA["skills"][key])

# -------------------- CONTACT --------------------
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Contact</div>", unsafe_allow_html=True)
st.markdown(f"**Email:** [{DATA['contact']['email']}](mailto:{DATA['contact']['email']})  ")
st.markdown(f"**Phone:** {DATA['contact']['phone']}  ")
st.markdown(f"**Location:** {DATA['contact']['city']}  ")
st.markdown(f"**LinkedIn:** {DATA['contact']['linkedin']}  ")
st.markdown(f"**GitHub:** {DATA['contact']['github']}  ")

st.markdown("<div class='muted mt-6 small'>Built with Streamlit in Python</div>", unsafe_allow_html=True)

