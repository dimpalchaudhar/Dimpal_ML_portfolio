import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Dimpal Ramesh Chaudhari | Data Analyst & ML Enthusiast",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #0b1120;
        --panel: #111c31;
        --panel-soft: #16243b;
        --text: #edf4ff;
        --muted: #a7b5ca;
        --accent: #62a8ff;
        --accent-2: #8b7cff;
        --line: rgba(148, 163, 184, .18);
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 85% 5%, rgba(98,168,255,.12), transparent 25%),
            radial-gradient(circle at 5% 35%, rgba(139,124,255,.10), transparent 25%),
            var(--bg);
        color: var(--text);
    }

    [data-testid="stHeader"] { background: rgba(11,17,32,.75); }
    /* No sidebar: use the horizontal navigation below */
    [data-testid="stSidebar"] { display: none; }
    .block-container { padding-top: 1.4rem; max-width: 1250px; }

    /* Horizontal top navigation */
    div[data-testid="stRadio"] > label { display: none; }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 5px;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background: transparent;
        border: 1px solid transparent;
        border-radius: 9px;
        padding: 7px 11px;
        color: #b9c8dc;
        transition: .2s ease;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background: rgba(98,168,255,.10);
        border-color: rgba(98,168,255,.25);
        color: #ffffff;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        background: rgba(98,168,255,.15);
        border-color: rgba(98,168,255,.45);
        color: #9dccff;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child { display: none; }


    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: -.5px;
    }
    h1 { color: var(--text); font-weight: 700; }
    h2 { color: #dceaff; }
    h3 { color: #b9d6ff; }
    p, li { color: var(--muted); line-height: 1.75; }

    .eyebrow {
        color: #8fc2ff;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        color: #f5f8ff;
        font-size: clamp(36px, 5vw, 58px);
        line-height: 1.08;
        font-weight: 700;
        margin: 0 0 12px 0;
    }
    .hero-title span {
        background: linear-gradient(90deg, #62a8ff, #a99cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 19px;
        color: #b8c9df;
        font-weight: 500;
        margin-bottom: 18px;
    }
    .hero-copy {
        color: #aebdd2;
        font-size: 16px;
        line-height: 1.85;
        max-width: 760px;
    }
    .panel {
        background: linear-gradient(145deg, rgba(22,36,59,.96), rgba(17,28,49,.96));
        border: 1px solid var(--line);
        border-radius: 18px;
                padding: 23px;
        height: 100%;
        box-shadow: 0 12px 35px rgba(0,0,0,.12);
    }
    .panel:hover {
        border-color: rgba(98,168,255,.55);
        transform: translateY(-2px);
        transition: .2s ease;
    }
    .project-tag {
        display: inline-block;
        padding: 5px 10px;
        border: 1px solid rgba(98,168,255,.35);
        background: rgba(98,168,255,.10);
        color: #a9d2ff;
        border-radius: 20px;
        font-size: 12px;
        margin: 3px 4px 3px 0;
    }
    .skill-chip {
        display: inline-block;
        padding: 8px 13px;
        margin: 5px 5px 5px 0;
        border-radius: 9px;
        background: #172945;
        border: 1px solid rgba(98,168,255,.22);
        color: #d7e8ff;
        font-size: 13px;
    }
    .section-kicker {
        color: #83baff;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .muted { color: var(--muted); }
    .metric-box {
        background: rgba(22,36,59,.8);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 17px;
        text-align: center;
    }
    .metric-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 27px;
        font-weight: 700;
        color: #8fc2ff;
    }
        .metric-label {
        color: #aebdd2;
        font-size: 12px;
        margin-top: 3px;
    }
    .skill-note {
        background: rgba(22,36,59,.8);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 18px 20px;
        color: var(--muted);
    }
    .timeline {
        border-left: 2px solid rgba(98,168,255,.5);
        padding: 2px 0 3px 18px;
        margin: 8px 0 18px 5px;
    }
    .footer {
        text-align: center;
        color: #8292aa;
        padding: 28px 8px 10px 8px;
        font-size: 13px;
    }
    div.stButton > button, div.stLinkButton > a {
        border-radius: 10px;
        border: 1px solid #579bfa;
        background: linear-gradient(90deg, #2563eb, #5750c9);
        color: white;
        font-weight: 600;
        padding: .55rem 1rem;
    }
    div.stButton > button:hover, div.stLinkButton > a:hover {
        border-color: #a9d2ff;
        color: white;
        background: #315fc5;
    }
    hr { border-color: var(--line); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# PERSONAL DETAILS
# Update these values before publishing if anything changes.
# ---------------------------------------------------------
NAME = "Dimpal Ramesh Chaudhari"
EMAIL = "dimpalc586@gmail.com"
PHONE = "+91 8010539750"
LINKEDIN = "https://www.linkedin.com/in/dimpal-chaudhari-645967274/"
GITHUB = "https://github.com/dimpalchaudhar"
PROFILE_IMAGE = "assets/Dimpal_IMG.jpeg"



# ---------------------------------------------------------
# REUSABLE HELPERS
# ---------------------------------------------------------
def section_heading(kicker, heading, description=None):
    st.markdown(f'<div class="section-kicker">{kicker}</div>', unsafe_allow_html=True)
    st.header(heading)
    if description:
        st.write(description)


def skill_chips(items):
    html = "".join(f'<span class="skill-chip">{item}</span>' for item in items)
    st.markdown(html, unsafe_allow_html=True)


def skill_card(icon, title, description, skills):
    pills = "".join(f'<span class="project-tag">{skill}</span>' for skill in skills)
    st.markdown(
        f"""
        <div class="panel">
            <div style="font-size:28px;">{icon}</div>
            <h3>{title}</h3>
            <p>{description}</p>
            <div>{pills}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_card(number, title, category, description, tools, highlights, github_url=None):
    tool_html = "".join(f'<span class="project-tag">{tool}</span>' for tool in tools)
    highlights_html = "".join(f"<li>{item}</li>" for item in highlights)
    github_html = ""
    if github_url:
        github_html = f"""
        <div style="margin-top:16px;">
            <a href="{github_url}" target="_blank" style="display:inline-block;padding:8px 14px;
            border-radius:8px;background:rgba(56,189,248,.12);border:1px solid rgba(56,189,248,.45);
            color:#7dd3fc;text-decoration:none;font-size:.88rem;font-weight:500;">
                🔗 View on GitHub
            </a>
        </div>
        """
    st.markdown(
        f"""
        <div class="panel">
            <div class="section-kicker">PROJECT {number:02d} · {category}</div>
            <h3>{title}</h3>
            <p>{description}</p>
            <div>{tool_html}</div>
            <br>
            <b style="color:#dceaff;">What I worked on</b>
            <ul>{highlights_html}</ul>
            {github_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

def education_card(kicker, title, institute, location, details, score=None, years=None):
    meta = ""
    if years:
        meta += f'<span class="project-tag">📅 {years}</span>'
    if score:
        meta += f'<span class="project-tag">🎯 {score}</span>'
    st.markdown(
        f"""
        <div class="panel">
            <div class="section-kicker">{kicker}</div>
            <h3>{title}</h3>
            <p><b>{institute}</b><br>{location}</p>
            <div>{meta}</div>
            <p style="margin-top:10px;">{details}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# TOP NAVIGATION BAR (NO SIDEBAR)
# ---------------------------------------------------------
nav_left, nav_right = st.columns([1.1, 3.9], vertical_alignment="center")

with nav_left:
    st.markdown(
        """
        <div style="font-family:'Space Grotesk',sans-serif;font-size:23px;
        font-weight:700;color:#f2f7ff;white-space:nowrap;">
            <span style="color:#62a8ff;">DC.</span> Dimpal Chaudhari
        </div>
        <div style="font-size:11px;color:#91a4bd;letter-spacing:1px;">
            DATA ANALYTICS · MACHINE LEARNING
        </div>
        """,
        unsafe_allow_html=True,
    )

with nav_right:
    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👋 About",
            "🧠 Skills",
            "📁 Projects",
            "🎓 Education",
            "🏅 Certifications",
            "✉️ Contact",
        ],
        horizontal=True,
        label_visibility="collapsed",
        key="portfolio_page",
    )

st.markdown("<hr style='margin-top:8px;margin-bottom:30px;'>", unsafe_allow_html=True)

def go_to_projects():
    st.session_state["portfolio_page"] = "📁 Projects"

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------
if page == "🏠 Home":
    left, right = st.columns([1.65, 1], gap="large")

    with left:
        st.markdown('<div class="eyebrow">WELCOME TO MY PORTFOLIO</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-title">Hi, I’m <span>Dimpal.</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-subtitle">Aspiring Data Analyst | Machine Learning Enthusiast</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="hero-copy">
                I am a Computer Science and Engineering graduate with an interest in
                turning raw data into useful insights. I work with Python, SQL, Excel
                and Power BI for data analysis and visualization, and I am building
                my machine learning skills through practical projects.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        a, b = st.columns([1, 1])
        with a:
            if st.button("Explore my projects  →", use_container_width=True, on_click=go_to_projects):
                st.session_state["portfolio_page"] = "📁 Projects"
                st.rerun()
        with b:
            st.link_button("Connect on LinkedIn ↗", LINKEDIN, use_container_width=True)

    with right:
        try:
            st.image(PROFILE_IMAGE, use_container_width=True)
        except Exception:
            st.markdown(
                """
                <div class="panel" style="height:320px;display:flex;align-items:center;
                justify-content:center;text-align:center;">
                    <div>
                        <div style="font-size:76px;">👩‍💻</div>
                        <div style="color:#aebdd2;">Add your photo at<br><b>assets/Dimpal_IMG.jpeg</b></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    m1, m2, m3, m4 = st.columns(4)
    metrics = [("05","Featured projects"), ("Python", "Core language"), ("Power BI", "Dashboarding"), ("ML", "Learning focus")]
    for col, (value, label) in zip([m1, m2, m3, m4], metrics):
        with col:
            st.markdown(
                f'<div class="metric-box"><div class="metric-number">{value}</div>'
                f'<div class="metric-label">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.write("")
    st.divider()
    section_heading("WHAT I DO", "Turning data into decisions")
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="panel"><h3>📊 Data Analysis</h3><p>Clean, explore and interpret datasets to identify patterns, trends and actionable insights.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="panel"><h3>📈 Business Intelligence</h3><p>Build clear reports and interactive dashboards with Power BI, Excel and data visualization.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="panel"><h3>🤖 Machine Learning</h3><p>Apply data preprocessing and foundational ML techniques to develop and evaluate predictive models.</p></div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------
elif page == "👋 About":
    section_heading("A LITTLE ABOUT ME", "Curious about data. Focused on learning.")
    st.markdown(
        """
        <div class="panel">
            <p>
                I have a B.Tech background in Computer Science and Engineering and
                a strong interest in Data Analytics, Business Intelligence and
                Machine Learning. I enjoy understanding a problem, exploring the
                available data and communicating findings in a simple, meaningful way.
            </p>
            <p>
                My hands-on learning includes data cleaning, exploratory data analysis,
                visualization, SQL querying and building Power BI dashboards. I am also
                developing my machine learning knowledge through model-building projects.
            </p>
            <p>
                I value continuous learning, practical problem-solving and the ability
                to explain technical work clearly.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    section_heading("CAREER OBJECTIVE", "Where I want to contribute")
    st.write(
        "To begin my career in Data Analytics, Business Intelligence or an entry-level "
        "Data Science role where I can apply my technical skills, learn from experienced "
        "professionals and contribute to data-driven decision-making."
    )
    st.write("")
    section_heading("AREAS OF INTEREST", "What I enjoy exploring")
    skill_chips(["Data Analytics", "Exploratory Data Analysis", "Business Intelligence",
                 "Data Visualization", "Machine Learning", "Predictive Modeling",
                 "Python", "SQL", "Power BI"])
# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
elif page == "🧠 Skills":
    section_heading(
        "MY TECHNICAL TOOLKIT",
        "Skills & Technologies",
        "A snapshot of the tools and concepts I use across data analysis, business intelligence and machine learning."
    )

    row1_col1, row1_col2 = st.columns(2, gap="large")
    with row1_col1:
        skill_card(
            "🐍",
            "Programming",
            "Writing clean Python code for data handling, analysis and automation.",
            ["Python", "OOP", "Functions", "Data Structures"],
        )
    with row1_col2:
        skill_card(
            "📊",
            "Data Analytics",
            "Preparing, exploring and interpreting datasets to find useful patterns.",
            ["Pandas", "NumPy", "Data Cleaning", "EDA", "Statistics"],
        )

    st.write("")
    row2_col1, row2_col2 = st.columns(2, gap="large")
    with row2_col1:
        skill_card(
            "📈",
            "Data Visualization & BI",
            "Presenting insights through clear reports, visuals and interactive dashboards.",
            ["Power BI", "DAX", "Power Query", "Excel", "Data Visualization"],
        )
    with row2_col2:
        skill_card(
            "🗄️",
            "Database & SQL",
            "Working with relational data and writing queries to retrieve and analyze information.",
            ["SQL", "MySQL", "Joins", "Aggregations", "Subqueries"],
        )

    st.write("")
    row3_col1, row3_col2 = st.columns(2, gap="large")
    with row3_col1:
        skill_card(
            "🤖",
            "Machine Learning",
            "Building foundational knowledge of predictive modeling through practical learning and projects.",
            ["Scikit-learn", "Regression", "Classification", "Preprocessing", "Model Evaluation"],
        )
    with row3_col2:
        skill_card(
            "🌐",
            "Tools & Other Skills",
            "Using supporting tools to collect data, build applications and present project work.",
            ["Jupyter Notebook", "Streamlit", "BeautifulSoup", "Web Scraping", "GitHub"],
        )

    st.write("")
    st.markdown(
        """
        <div class="skill-note">
            <b style="color:#dceaff;">Current learning focus</b><br>
            Strengthening machine learning fundamentals, improving SQL problem-solving
            and building end-to-end projects that combine analysis, modeling and clear
            communication of results.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------
elif page == "📁 Projects":
    section_heading("SELECTED WORK", "Projects", "A selection of practical projects demonstrating my work with data, dashboards and machine learning.")
    
    p1, p2 = st.columns(2, gap="large")
    with p1:
        project_card(
            1, "Employee Attrition Prediction", "MACHINE LEARNING",
            "A classification project focused on identifying employee-related factors associated with employee attrition.",
            ["Python", "Pandas", "Scikit-learn", "Classification"],
            ["Prepared and explored employee data.", "Performed preprocessing and feature preparation.",
             "Trained classification models and evaluated results using accuracy, precision, recall and F1-score."],
            github_url = "https://github.com/dimpalchaudhar/Employee_Attriation_Prediction_System",
        )
    with p2:
        project_card(
            2, "Blinkit Sales Dashboard", "POWER BI",
            "An interactive dashboard to explore sales performance across products, item categories and outlet segments.",
            ["Power BI", "DAX", "Power Query", "Data Modeling"],
            ["Created KPI cards and interactive report pages.", "Analyzed sales by outlet and item category.",
             "Used slicers and visuals to make business trends easier to explore."],
            github_url = "https://github.com/dimpalchaudhar/Blinkit-Business-Dashboard-Power-BI-",
        )
    st.write("")
    p3, p4 = st.columns(2, gap="large")
    with p3:
        project_card(
            3, "Flipkart Mobile Data Analysis", "WEB SCRAPING & EDA",
            "A product-data project exploring mobile prices, discounts, ratings and product attributes.",
            ["Python", "BeautifulSoup", "Pandas", "Visualization"],
            ["Collected product information through web scraping.", "Cleaned and prepared the collected data.",
             "Explored pricing, discounts and ratings to identify patterns."],
            github_url = "https://github.com/dimpalchaudhar/Filpkart_mobiles_EDA_project",
        )
    with p4:
        project_card(
            4, "House Rent Data Analysis", "EXPLORATORY DATA ANALYSIS",
            "An EDA project to understand rental-price patterns and the variables associated with house rent.",
            ["Python", "Pandas", "NumPy", "Statistics"],
            ["Handled missing values and explored outliers.", "Studied relationships between rental prices and property features.",
             "Created visualizations to communicate key observations."],
            github_url = "https://github.com/dimpalchaudhar/Hotel_Reservation_Analaysis",   
        )
    

    st.write("")
    p5, p6 = st.columns(2, gap="large")
    with p5:
        project_card(
            5, "Hotel Reservation Analysis", "SQL Analysis",
            "A SQL project to analyze sales data and answer business questions using queries on a relational database.",
            ["SQL", "MySQL", "Joins", "Aggregations"],
            ["Hotel Reservation Analysis is a SQL-based data analytics project that analyzes hotel bookings, guests, stays, rooms, staff, revenue, booking channels, cancellations, and no-shows.",
             "It uses SQL queries, joins, aggregations, and business analysis to identify booking trends, guest behavior, hotel performance, and operational issues."],
            github_url = "https://github.com/dimpalchaudhar/Hotel_Reservation_Analaysis",
        )
# ---------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------
elif page == "🎓 Education":
    section_heading("ACADEMIC BACKGROUND", "Education")

    education_card(
        "UNDERGRADUATE DEGREE",
        "B.Tech — Computer Science and Engineering",
        "Hindi Seva Mandal Shri Sant Gadge Baba College of Engineering and Technology",
        "Bhusawal, Maharashtra",
        "Studied core computer science concepts and developed an interest in programming",
        score="CGPA: 7.80",         
        years="2022 – 2026",         
    )
    st.write("")
    education_card(
        "HIGHER SECONDARY (12th / HSC)",
        "12 - Science Stream",
        "K. Narkhede Junior College, Bhusawal",                      
        "Bhusawal, Maharashtra",                               
        "Completed 12th with Physics, Chemistry, Mathematics.",  
        years="2021 – 2022",        
    )
 
# ---------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------
elif page == "🏅 Certifications":
    section_heading("CONTINUOUS LEARNING", "Certifications")

    # (icon, title, issuer, description, certificate link)
    certifications = [
        ("🐍", "Python Programming", "Innomatics Research Labs",
         "Python programming fundamentals and practical coding.",
         "https://online.innomatics.in/verify/M_303383"),
        ("📊", "Exploratory Data Analysis", "Innomatics Research Labs",
         "Data understanding, data cleaning, visualization and statistical analysis.",
         "https://online.innomatics.in/verify/M_204510"),
        ("📈", "Power BI", "Certification",
         "Dashboard development, reporting and business intelligence.",
         "https://online.innomatics.in/verify/M_205020"),
        ("🗄️", "MySQL", "Certification",
         "SQL fundamentals and working with relational databases.",
         "https://online.innomatics.in/verify/M_205439"),
    ]

    for start in range(0, len(certifications), 2):
        cols = st.columns(2, gap="large")
        for col, item in zip(cols, certifications[start:start + 2]):
            icon, title, issuer, description, link = item
            link_html = ""
            if link:
                link_html = (
                    f'<div style="margin-top:16px;">'
                    f'<a href="{link}" target="_blank" style="display:inline-block;padding:8px 14px;'
                    f'border-radius:8px;background:rgba(56,189,248,.12);border:1px solid rgba(56,189,248,.45);'
                    f'color:#7dd3fc;text-decoration:none;font-size:.88rem;font-weight:500;">'
                    f'🔗 View Certificate</a></div>'
                )
            with col:
                st.markdown(
                    f'<div class="panel">'
                    f'<div style="font-size:28px;">{icon}</div>'
                    f'<h3>{title}</h3>'
                    f'<p><b>{issuer}</b></p>'
                    f'<p>{description}</p>'
                    f'{link_html}'
                    f'</div>',
                    unsafe_allow_html=True,
                ) 
        st.write("")
# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------
elif page == "✉️ Contact":
    section_heading("GET IN TOUCH", "Let's connect", "I am open to entry-level opportunities, internships and discussions related to Data Analytics, Business Intelligence and Machine Learning.")
    left, right = st.columns([1.15, 1], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="panel">
                <h3>Contact details</h3>
                <p>✉️ <b>Email</b><br><a href="mailto:{EMAIL}" style="color:#8fc2ff;">{EMAIL}</a></p>
                <p>📱 <b>Phone</b><br>{PHONE}</p>
                <p>🔗 <b>LinkedIn</b><br><a href="{LINKEDIN}" style="color:#8fc2ff;">View LinkedIn profile ↗</a></p>
                <p>💻 <b>GitHub</b><br><a href="{GITHUB}" style="color:#8fc2ff;">View GitHub profile ↗</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <div class="panel">
                <h3>Open to opportunities</h3>
                <p>
                    If you are hiring for a junior Data Analyst, BI or entry-level
                    Data Science role, or would like to discuss a project, feel free
                    to reach out.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.link_button("Send me an email ↗", f"mailto:{EMAIL}?subject=Career%20Opportunity", use_container_width=True)
        st.link_button("Connect on LinkedIn ↗", LINKEDIN, use_container_width=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.divider()
st.markdown(
    f"""
    <div class="footer">
        © 2026 {NAME}<br>
        Data Analytics · Business Intelligence · Machine Learning<br>
        Designed with care using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)