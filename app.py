import streamlit as st
import base64

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Dimpal Ramesh Chaudhari | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #374151;
    }

    /* Main headings */
    h1 {
        color: #60a5fa;
        font-weight: 700;
    }

    h2 {
        color: #93c5fd;
    }

    h3 {
        color: #dbeafe;
    }

    /* Paragraph */
    p {
        color: #d1d5db;
        line-height: 1.7;
    }

    /* Cards */
    .card {
        background: #1f2937;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #374151;
        margin-bottom: 20px;
        transition: 0.3s;
    }

    .card:hover {
        border-color: #60a5fa;
        transform: translateY(-3px);
    }

    /* Skill badges */
    .skill {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        background-color: #1e3a8a;
        color: white;
        border-radius: 20px;
        font-size: 14px;
        border: 1px solid #3b82f6;
    }

    /* Project cards */
    .project-card {
        background: linear-gradient(
            135deg,
            #111827,
            #1f2937
        );
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #374151;
        height: 100%;
    }

    .project-number {
        font-size: 35px;
        font-weight: bold;
        color: #60a5fa;
    }

    /* Contact box */
    .contact-box {
        background-color: #111827;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #374151;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #3b82f6;
        background-color: #1d4ed8;
        color: white;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #2563eb;
        border-color: #60a5fa;
    }

    /* Divider */
    hr {
        border-color: #374151;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        padding: 30px;
        margin-top: 50px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 👩‍💻 Dimpal Chaudhari")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👩‍💻 About Me",
            "🛠️ Skills",
            "📊 Projects",
            "🎓 Education",
            "🏆 Certifications",
            "📬 Contact"
        ]
    )

    st.markdown("---")

    st.markdown("### Connect With Me")

    st.markdown(
        "[🔗 LinkedIn](https://www.linkedin.com/in/dimpal-chaudhari-645967274/)"
    )

    st.markdown(
        "[💻 GitHub](https://github.com/dimpalchaudhar)"
    )

    st.markdown(
        "[📧 Email](mailto:dimpalc586@gmail.com)"
    )


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

if page == "🏠 Home":

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.8, 1])

    with col1:

        st.markdown(
            "<h1>Hi, I'm Dimpal Ramesh Chaudhari 👋</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2>Data Analyst | Data Science Enthusiast</h2>",
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown("""
        ### Turning Data Into Meaningful Insights 📊

        I am a Computer Science and Engineering student with a strong
        interest in **Data Analytics, Data Visualization and Data Science**.

        I enjoy working with data to discover patterns, generate insights,
        create interactive dashboards and solve real-world problems using
        analytical techniques.
        """)

        st.write("")

        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.metric("Projects", "3+")

        with col_b:
            st.metric("Core Skills", "9+")

        with col_c:
            st.metric("Certifications", "2")

        st.write("")

        if st.button("📬 Contact Me"):

            st.info(
                "Email: dimpalc586@gmail.com"
            )

    with col2:

        try:

            st.image(
                "assets/Dimpal_IMG.jpeg",
                # caption="Dimpal Ramesh Chaudhari",
                use_container_width=True
            )

        except:

            st.markdown("""
            <div style="
                height:350px;
                background:#1f2937;
                border-radius:20px;
                display:flex;
                align-items:center;
                justify-content:center;
                border:1px solid #374151;
                font-size:80px;
            ">
            👩‍💻
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## What I Do")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

        ### 📊 Data Analysis

        Analyze datasets, identify trends, discover patterns
        and generate meaningful business insights.

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        ### 📈 Data Visualization

        Create interactive dashboards and visualizations
        using Power BI, Excel and Python.

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">

        ### 🐍 Python & SQL

        Use Python, Pandas, NumPy and SQL for data cleaning,
        analysis and extracting useful insights.

        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# ABOUT ME
# ---------------------------------------------------------

elif page == "👩‍💻 About Me":

    st.title("👩‍💻 About Me")

    st.markdown("""
    <div class="card">

    <h2>Hi, I'm Dimpal!</h2>

    <p>
    I am pursuing a <b>B.Tech in Computer Science and Engineering</b>
    and have a strong interest in Data Analytics and Data Science.
    </p>

    <p>
    My technical journey includes working with Python, SQL, Excel,
    Power BI and statistical techniques for analyzing and visualizing data.
    </p>

    <p>
    I enjoy transforming raw datasets into meaningful information
    and building dashboards that help communicate insights clearly.
    </p>

    <p>
    I am continuously improving my analytical and technical skills
    through projects, certifications and practical learning.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Career Objective")

    st.write("""
    To start my career in Data Analytics / Data Science where I can
    apply my analytical skills, continuously learn new technologies,
    and contribute to data-driven decision making.
    """)

    st.markdown("## 💡 My Interests")

    interests = [
        "Data Analytics",
        "Data Visualization",
        "Business Intelligence",
        "Exploratory Data Analysis",
        "Python",
        "SQL",
        "Power BI",
        "Machine Learning"
    ]

    for interest in interests:

        st.markdown(
            f'<span class="skill">{interest}</span>',
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------

elif page == "🛠️ Skills":

    st.title("🛠️ Technical Skills")

    skills = {
        "🐍 Programming": [
            "Python"
        ],

        "📊 Data Analytics": [
            "Data Analysis",
            "Exploratory Data Analysis",
            "Statistics"
        ],

        "📈 Visualization": [
            "Power BI",
            "Data Visualization",
            "Excel"
        ],

        "🗄️ Database": [
            "SQL"
        ],

        "🌐 Other Skills": [
            "Web Scraping"
        ]
    }

    for category, skill_list in skills.items():

        st.markdown(f"## {category}")

        for skill in skill_list:

            st.markdown(
                f'<span class="skill">{skill}</span>',
                unsafe_allow_html=True
            )

        st.write("")


# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------

elif page == "📊 Projects":

    st.title("📊 My Projects")

    st.write(
        "Here are some of my practical projects in Data Analytics, "
        "Web Scraping and Business Intelligence."
    )

    st.write("")

    # PROJECT 1

    st.markdown("""
    <div class="project-card">

    <div class="project-number">01</div>

    <h2>Flipkart Mobile Data Analysis</h2>

    <h3>🌐 Web Scraping Project</h3>

    <p>
    A data collection and analysis project where mobile product
    information was collected using web scraping techniques and
    analyzed to understand product pricing, ratings and other
    important attributes.
    </p>

    <b>Technologies:</b>

    <p>
    Python • Web Scraping • Pandas • Data Analysis • Visualization
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # PROJECT 2

    st.markdown("""
    <div class="project-card">

    <div class="project-number">02</div>

    <h2>House Rent Prediction Data Analysis</h2>

    <h3>📊 EDA Project</h3>

    <p>
    An Exploratory Data Analysis project focused on understanding
    house rental data, identifying patterns, analyzing important
    variables and extracting useful insights from the dataset.
    </p>

    <b>Technologies:</b>

    <p>
    Python • Pandas • NumPy • EDA • Statistics • Data Visualization
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # PROJECT 3

    st.markdown("""
    <div class="project-card">

    <div class="project-number">03</div>

    <h2>Blinkit Sales Dashboard</h2>

    <h3>📈 Power BI Project</h3>

    <p>
    An interactive Power BI dashboard designed to analyze Blinkit
    sales performance across products, categories, outlets, tiers
    and other business dimensions.
    </p>

    <b>Technologies:</b>

    <p>
    Power BI • DAX • Data Modeling • Power Query • Data Visualization
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("## 🔍 Project Highlights")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info("""
        **Data Collection**

        Web scraping and dataset preparation.
        """)

    with col2:

        st.info("""
        **Data Analysis**

        Cleaning, EDA, statistics and identifying patterns.
        """)

    with col3:

        st.info("""
        **Data Visualization**

        Interactive Power BI dashboards and visual reports.
        """)


# ---------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------

elif page == "🎓 Education":

    st.title("🎓 Education")

    st.markdown("""
    <div class="card">

    <h2>B.Tech in Computer Science and Engineering</h2>

    <h3>
    Hindi Seva Mandal Shri Sant Gadge Baba College
    Of Engineering and Technology, Bhusawal
    </h3>

    <p>
    <b>Field:</b> Computer Science and Engineering
    </p>

    <p>
    During my engineering journey, I developed an interest in
    programming, databases, data analytics, visualization and
    data-driven problem solving.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------

elif page == "🏆 Certifications":

    st.title("🏆 Certifications")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🐍 Python Programming</h2>

        <p>
        <b>Innomatics Research Labs</b>
        </p>

        <p>
        Certification focused on Python programming concepts
        and practical programming skills.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <h2>📊 Exploratory Data Analysis</h2>

        <p>
        <b>Innomatics Research Labs</b>
        </p>

        <p>
        Certification focused on Exploratory Data Analysis,
        data understanding, visualization and statistical analysis.
        </p>

        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------

elif page == "📬 Contact":

    st.title("📬 Contact Me")

    st.write("""
    I'm open to opportunities related to Data Analytics,
    Data Science and Business Intelligence.
    """)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="contact-box">

        ### 📧 Email

        dimpalc586@gmail.com

        ### 📱 Phone

        8010539750

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="contact-box">

        ### 🔗 LinkedIn

        [linkedin.com/in/dimpal-chaudhari-645967274](https://www.linkedin.com/in/dimpal-chaudhari-645967274/)

        ### 💻 GitHub

        [github.com/dimpalchaudhar](https://github.com/dimpalchaudhar)

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("## Let's Connect 🤝")

    st.write("""
    If you are interested in discussing Data Analytics,
    Business Intelligence, projects or career opportunities,
    feel free to connect with me.
    """)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">

© 2026 Dimpal Ramesh Chaudhari

<br>

Data Analyst | Data Science Enthusiast

<br><br>

Built with ❤️ using Python & Streamlit

</div>
""", unsafe_allow_html=True)