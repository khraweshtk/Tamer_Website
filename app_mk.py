from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Muneeb Khan — Resume", page_icon="💼", layout="wide")

# -------------------- THEME / CSS --------------------
CSS = """
<style>
:root{
  --bg1:#0b1220; --bg2:#101a2b; --text:#e6f0ff; --muted:#a8b3c7;
  --primary:#22d3ee; --primary-2:#60a5fa; --card:#0f172a;
  --shadow: 0 8px 30px rgba(34,211,238,.15), 0 0 40px rgba(96,165,250,.1);
}
html, body, .block-container {
  background: radial-gradient(1200px 600px at -10% -10%, #0e1a2f 0%, #0b1220 35%, #0b1220 100%);
}
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

# --- Marquee styling for the coursework bar ---
CSS += """
<style>
.marquee{ position:relative; overflow:hidden; width:100%; }
.marquee__track{
  display:flex; gap:14px; align-items:center;
  padding:10px 0;
  animation: marquee-scroll 24s linear infinite;
  will-change: transform;
}
.marquee:hover .marquee__track{ animation-play-state: paused; }

.marquee .chip{
  white-space:nowrap;
  padding:10px 16px;
  border-radius:16px;
  background: radial-gradient(120px 60px at 30% 20%, rgba(34,211,238,.16), rgba(255,255,255,.05));
  border:1px solid rgba(255,255,255,.08);
  box-shadow: 0 6px 22px rgba(34,211,238,.12), 0 0 24px rgba(96,165,250,.08);
}

.marquee__fade{
  position:absolute; top:0; bottom:0; width:80px; pointer-events:none; z-index:2;
  background: linear-gradient(to right, rgba(11,18,32,1), rgba(11,18,32,0));
}
.marquee__fade.right{
  right:0; transform: scaleX(-1);
}

@keyframes marquee-scroll{
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
</style>
"""

CSS += """
<style>
.avatar {
  width: clamp(140px, 18vw, 220px);   /* min, fluid, max */
  border-radius: 16px;
  box-shadow: 0 8px 30px rgba(34,211,238,.15);
}
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
    "headshot": "headshot_mk.jpg"
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
      "role": "Student IT Assistant – Pathology",
      "org": "The Ohio State University College of Medicine",
      "place": "Columbus, Ohio",
      "period": "May 2025 – July 2025",
      "points": [
        "Configured and troubleshot pathology lab workstations and servers, ensuring uptime for digital pathology software used in research workflows.",
        "Organized and pre-processed 10,000+ whole slide images (WSIs) for AI model training, improving dataset accessibility and standardization.",
        "Assisted in building automated scripts for image annotation and feature extraction, reducing manual labeling time by 20%."
      ]
    },
    {
      "role": "Undergraduate Research Assistant",
      "org": "The Ohio State University College of Medicine",
      "place": "Columbus, Ohio",
      "period": "Dec 2023 – Feb 2024",
      "points": [
        "Conducted data analysis on cardiomyocyte activity, automating repetitive tasks and saving 8 hours/week.",
        "Developed visualization tools that improved data interpretation efficiency by 25%.",
        "Streamlined team workflows by enhancing data accessibility, reducing prep time by 10%."
      ]
    },
    {
      "role": "Software Developer Intern",
      "org": "Fee Dodger LLC",
      "place": "Columbus, Ohio",
      "period": "Mar 2024 – Present",
      "points": [
        "Collaborated with the team to design and integrate APIs, saving 10+ hours/month of manual inventory tracking.",
        "Spearheaded planning and development of iOS and Android apps for 100+ early adopters.",
        "Conducted beta testing with users, addressing 30 improvements for platform refinement."
      ]
    },
    {
      "role": "Student IT Assistant — Engineering Technology Services",
      "org": "The Ohio State University College of Engineering",
      "place": "Columbus, Ohio",
      "period": "Jul 2024 – Present",
      "points": [
        "Investigated and resolved cybersecurity incidents using CrowdStrike, securing 200+ devices.",
        "Performed networking tasks (router/switch configurations) to optimize departmental performance.",
        "Collaborated with the IT team to enhance security, reducing vulnerabilities by 20%."
      ]
    }
  ],
  "projects": [
    {
      "name": "Chatbot with Sentiment Analysis",
      "period": "Aug 2024 – Sep 2024",
      "points": [
        "Built chatbot using Rasa/Dialogflow; sentiment detection via VADER + BERT (92% accuracy).",
        "Customizable templates for adaptability; deployed with Flask for scalability."
      ]
    },
    {
      "name": "To-Do List Application with React",
      "period": "Oct 2024 – Nov 2024",
      "points": [
        "Responsive to-do app with add/update/delete.",
        "Used state management for smooth UX; local storage for up to 20 tasks/session."
      ]
    },
    {
      "name": "AI-Powered Predictive Maintenance for Automobiles",
      "period": "Nov 2024 – Dec 2024",
      "points": [
        "Python-based predictive maintenance system on sensor data (95% accuracy).",
        "Scikit-learn + TensorFlow to detect failures; dashboard with Plotly Dash."
      ]
    }
  ],
  "activities": [
    {
      "name": "NAIMA — Youth Coordinator",
      "place": "Columbus, Ohio",
      "period": "Aug 2021 – Current",
      "points": [
        "Led youth-oriented programs/initiatives for community development within a non-profit."
      ]
    },
    {
      "name": "Clubs — The Ohio State University",
      "place": "Columbus, Ohio",
      "period": "Aug 2023 – Current",
      "points": [
        "Member of AI Club, Collaborative Software Development Club, and Competitive Coding Club"
      ]
    }
  ],
  "skills": {
    "Programming": ["Java", "Python", "HTML/CSS", "JavaScript", "Node.js", "React.js", "MATLAB", "C++", "R"],
    "Tools": ["IntelliJ", "PyCharm", "Eclipse", "SolidWorks", "Webstorm", "MS Office"],
    "Non-Technical": ["Solution Oriented", "Skilled Collaborator", "Time Efficient", "Communication", "Critical Thinking"]
  }
}

# ---------- Helpers ----------
def chips(items):
    st.markdown("<div class='chips'>" + "".join(f"<div class='chip'>{i}</div>" for i in items) + "</div>", unsafe_allow_html=True)

def marquee_chips(items, seconds: float = 26):
    """Neon pill marquee that scrolls horizontally; pauses on hover."""
    doubled = items + items  # duplicate for seamless loop
    chips_html = "".join(f"<div class='chip'>{i}</div>" for i in doubled)
    html = f"""
    <div class="marquee">
      <div class="marquee__fade"></div>
      <div class="marquee__fade right"></div>
      <div class="marquee__track" style="animation-duration:{float(seconds)}s">
        {chips_html}
      </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
left, right = st.columns([3,1.2])
with left:
    st.title(DATA["contact"]["name"])
    st.caption(f"{DATA['contact']['citizenship']}  •  {DATA['contact']['city']}")
    st.markdown(
        f"📞 **{DATA['contact']['phone']}**  |  ✉️ "
        f"[{DATA['contact']['email']}](mailto:{DATA['contact']['email']})  |  "
        f"🔗 [LinkedIn]({DATA['contact']['linkedin']})  |  "
        f"🔧 [GitHub]({DATA['contact']['github']})"
    )
with right:
    headshot_path = Path(DATA['contact']['headshot'])
    if headshot_path.exists():
        st.image(str(headshot_path), use_container_width=True)
    else:
        st.markdown("<div class='muted'>Upload headshot_mk.jpg next to app.py</div>", unsafe_allow_html=True)
        

# -------------------- EDUCATION --------------------
st.markdown('<a id="education"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Education</div>", unsafe_allow_html=True)
st.markdown(
    f"<div class='card'><strong>{DATA['education']['school']}</strong><br/>{DATA['education']['degree']}<br/><span class='muted'>{DATA['education']['grad']} · {DATA['education']['deans_list']}</span></div>",
    unsafe_allow_html=True
)
st.markdown("**Related Coursework**")
# marquee version (replaces chips(...))
marquee_chips(DATA["education"]["coursework"], seconds=26)

st.markdown("**Certifications**")
for c in DATA["education"]["certs"]:
    st.markdown(f"- {c}")

# -------------------- EXPERIENCE --------------------
st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Experience</div>", unsafe_allow_html=True)
for e in DATA["experience"]:
    st.markdown(
        f"<div class='card'><div style='display:flex;justify-content:space-between;align-items:center;'>"
        f"<div><strong>{e['role']}</strong> · {e['org']} — <span class='muted'>{e['place']}</span></div>"
        f"<div class='muted'>{e['period']}</div></div></div>",
        unsafe_allow_html=True
    )
    for p in e["points"]:
        st.markdown(f"- {p}")

# -------------------- PROJECTS --------------------
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Projects</div>", unsafe_allow_html=True)
for p in DATA["projects"]:
    st.markdown(
        f"<div class='card-outline'><div style='display:flex;justify-content:space-between;align-items:center;'>"
        f"<div style='font-weight:700;font-size:1.05rem'>{p['name']}</div>"
        f"<div class='muted'>{p['period']}</div></div></div>",
        unsafe_allow_html=True
    )
    for b in p["points"]:
        st.markdown(f"- {b}")

# -------------------- ACTIVITIES --------------------
st.markdown('<a id="activities"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title mt-6'>Activities & Leadership</div>", unsafe_allow_html=True)
for a in DATA["activities"]:
    st.markdown(
        f"<div class='card'><div style='display:flex;justify-content:space-between;align-items:center;'>"
        f"<div><strong>{a['name']}</strong> — <span class='muted'>{a['place']}</span></div>"
        f"<div class='muted'>{a['period']}</div></div></div>",
        unsafe_allow_html=True
    )
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
st.markdown(f"**Email:** [{DATA['contact']['email']}](mailto:{DATA['contact']['email']})")
st.markdown(f"**Phone:** {DATA['contact']['phone']}")
st.markdown(f"**Location:** {DATA['contact']['city']}")
st.markdown(f"**LinkedIn:** {DATA['contact']['linkedin']}")
st.markdown(f"**GitHub:** {DATA['contact']['github']}")

st.markdown("<div class='muted mt-6 small'>Built with Streamlit & Python</div>", unsafe_allow_html=True)
