import streamlit as st

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Your Name - Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
        /* Main container styling */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main title */
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Subtitle */
        .subtitle {
            font-size: 1.2rem;
            color: #4a5568;
            margin-bottom: 2rem;
            line-height: 1.6;
        }
        
        /* Section titles */
        .section-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #2d3748;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        /* Tags/Skills */
        .tag {
            display: inline-block;
            padding: 0.4rem 0.9rem;
            margin: 0.3rem 0.3rem 0.3rem 0;
            border-radius: 20px;
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            border: 1.5px solid #667eea40;
            font-size: 0.85rem;
            font-weight: 500;
            color: #4a5568;
            transition: all 0.3s ease;
        }
        
        .tag:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
        }
        
        /* Small text */
        .small-text {
            font-size: 0.9rem;
            color: #718096;
            font-style: italic;
        }
        
        /* Card styling */
        .card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.2);
            transform: translateY(-2px);
        }
        
        /* Experience item */
        .experience-item {
            padding: 1.5rem;
            margin: 1.5rem 0;
            background: #f7fafc;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        
        /* Project card */
        .project-card {
            background: linear-gradient(135deg, #ffffff 0%, #f7fafc 100%);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .project-card:hover {
            border-color: #667eea;
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
        }
        
        /* Link styling */
        a {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }
        
        a:hover {
            color: #764ba2;
            text-decoration: underline;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            padding-top: 2rem;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        
        /* Input styling */
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 2px solid #e2e8f0;
        }
        
        .stTextArea > div > div > textarea {
            border-radius: 8px;
            border: 2px solid #e2e8f0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
st.sidebar.markdown(
    """
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='font-size: 1.8rem; margin-bottom: 0.5rem;'>📊 Portfolio</h1>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 About",
        "💻 Skills",
        "💼 Experience",
        "🚀 Projects",
        "📚 Publications",
        "📧 Contact",
    ],
    label_visibility="collapsed"
)

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Info")
st.sidebar.markdown("**Status:** Open to opportunities")
st.sidebar.markdown("📍 City, Country")
st.sidebar.markdown("---")
st.sidebar.markdown("### Connect")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/)")
st.sidebar.markdown("💻 [GitHub](https://github.com/)")
st.sidebar.markdown("📊 [Kaggle](https://www.kaggle.com/)")

# ---------- HELPER FUNCTIONS ----------
def render_tags(tags):
    """Render tags with modern styling"""
    tag_html = " ".join([f"<span class='tag'>{t}</span>" for t in tags])
    st.markdown(tag_html, unsafe_allow_html=True)


def project_card(title, role, description, tech_stack, link=None, github_link=None):
    """Render a project card with enhanced styling"""
    st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)
    st.markdown(f"### {title}")
    st.markdown(f"*{role}*")
    st.markdown("")
    st.markdown(description)
    st.markdown("")
    st.markdown("**Technologies:**")
    render_tags(tech_stack)
    st.markdown("")
    if link or github_link:
        links_html = ""
        if link:
            links_html += f"🔗 [View Project]({link})  "
        if github_link:
            links_html += f"💻 [GitHub]({github_link})"
        st.markdown(links_html)
    st.markdown("</div>", unsafe_allow_html=True)


def experience_item(role, company, period, location, bullets):
    """Render an experience item with enhanced styling"""
    st.markdown(f"<div class='experience-item'>", unsafe_allow_html=True)
    st.markdown(f"#### {role}")
    st.markdown(f"**{company}**")
    st.markdown(f"<span class='small-text'>{period} | 📍 {location}</span>", unsafe_allow_html=True)
    st.markdown("")
    for b in bullets:
        st.markdown(f"• {b}")
    st.markdown("</div>", unsafe_allow_html=True)


def publication_item(title, venue, year, link=None, summary=None, authors=None):
    """Render a publication item with enhanced styling"""
    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"**{title}**")
    if authors:
        st.markdown(f"*{authors}*")
    st.markdown(f"*{venue}, {year}*")
    if summary:
        st.markdown("")
        st.markdown(summary)
    if link:
        st.markdown("")
        st.markdown(f"🔗 [Read Paper]({link})")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------- PAGES ----------
if page == "🏠 About":
    # Hero Section
    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile image placeholder - uncomment and add your image
        # st.image("profile.jpg", width=200, use_column_width=False)
        st.markdown(
            """
            <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); 
                        border-radius: 15px; margin-bottom: 1rem;'>
                <h2 style='margin-bottom: 0.5rem;'>Your Name</h2>
                <p style='color: #4a5568; margin-bottom: 0.5rem;'>Data Scientist</p>
                <p style='color: #4a5568; margin-bottom: 0.5rem;'>Machine Learning | Analytics</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("📍 **City, Country**")
        st.markdown("✉️ your.email@domain.com")
        st.markdown("")
        st.markdown("**Quick Links:**")
        st.markdown("- [LinkedIn](https://www.linkedin.com/)")
        st.markdown("- [GitHub](https://github.com/)")
        st.markdown("- [Resume/CV](link-to-resume.pdf)")

    with col2:
        st.markdown("<div class='main-title'>Hi, I'm Your Name 👋</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='subtitle'>
            I am a data scientist with a background in [your background: e.g., statistics, economics, computer science].
            I enjoy turning messy real-world data into clear, actionable insights and deployable models.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    
    # Quick Summary Section
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("#### 🎓 Education")
        st.markdown(
            """
            - **Degree:** Your degree(s) and university
            - **Focus:** Machine Learning, Statistics, Data Science
            - **Year:** Graduation year
            """
        )
        
        st.markdown("#### 💼 Experience")
        st.markdown(
            """
            - **Current Role:** Brief summary
            - **Previous:** Key roles and achievements
            - **Years:** X+ years in data science
            """
        )
    
    with col4:
        st.markdown("#### 🧠 Interests")
        st.markdown(
            """
            - Time series analysis
            - Causal inference
            - Recommendation systems
            - Deep learning applications
            """
        )
        
        st.markdown("#### 🛠 Tech Stack")
        st.markdown(
            """
            - **Languages:** Python, SQL, R
            - **ML/DL:** scikit-learn, PyTorch, TensorFlow
            - **Tools:** Docker, Git, AWS/GCP
            - **Visualization:** Streamlit, Plotly, Dash
            """
        )

    st.markdown("---")
    
    # Highlights Section
    st.markdown("#### ✨ Key Highlights")
    highlight_cols = st.columns(3)
    
    with highlight_cols[0]:
        st.markdown(
            """
            <div class='card' style='text-align: center;'>
                <h3>🚀 Projects</h3>
                <p>Built impactful ML models and data products</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with highlight_cols[1]:
        st.markdown(
            """
            <div class='card' style='text-align: center;'>
                <h3>📊 Impact</h3>
                <p>Delivered measurable business value</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with highlight_cols[2]:
        st.markdown(
            """
            <div class='card' style='text-align: center;'>
                <h3>📚 Research</h3>
                <p>Published academic work and contributions</p>
            </div>
            """,
            unsafe_allow_html=True
        )

elif page == "💻 Skills":
    st.markdown("<div class='section-title'>Technical Skills</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Programming & Tools**")
        render_tags(["Python", "R", "SQL", "Git", "Linux", "Docker", "Bash"])

        st.markdown("**Machine Learning**")
        render_tags([
            "Supervised Learning",
            "Unsupervised Learning",
            "Time Series",
            "Model Evaluation",
            "Feature Engineering",
        ])

        st.markdown("**Deep Learning (if applicable)**")
        render_tags(["PyTorch", "TensorFlow", "CNNs", "RNNs", "Transformers"])

    with col2:
        st.markdown("**Data & Analytics**")
        render_tags([
            "Pandas",
            "NumPy",
            "EDA",
            "Experiment Design",
            "A/B Testing",
            "Dashboards",
        ])

        st.markdown("**Databases & Cloud (customize)**")
        render_tags([
            "PostgreSQL",
            "BigQuery",
            "Snowflake",
            "AWS",
            "GCP",
        ])

        st.markdown("**Soft Skills**")
        render_tags([
            "Communication",
            "Storytelling with Data",
            "Collaboration",
            "Mentoring",
        ])

elif page == "💼 Experience":
    st.markdown("<div class='section-title'>Experience</div>", unsafe_allow_html=True)

    # ---- Example job 1 ----
    experience_item(
        role="Data Scientist",
        company="Company Name",
        period="2023 – Present",
        location="City, Country",
        bullets=[
            "Built and deployed a churn prediction model using XGBoost, improving retention campaign precision by 15%.",
            "Designed and maintained ETL pipelines for customer behavior data from multiple sources.",
            "Collaborated with product and marketing teams to translate findings into business decisions.",
        ],
    )

    # ---- Example job 2 ----
    experience_item(
        role="Junior Data Scientist",
        company="Other Company",
        period="2021 – 2023",
        location="City, Country",
        bullets=[
            "Developed forecasting models for sales data using ARIMA and Prophet.",
            "Created interactive dashboards for stakeholders using Streamlit / Power BI.",
        ],
    )

    st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
    st.markdown("**MSc in Something Data-Related**, University Name (Year – Year)")
    st.markdown("- Thesis: *Title of your thesis*")
    st.markdown("- Main topics: Machine Learning, Statistics, [Others]")
    st.markdown("")

    st.markdown("**BSc in Something**, University Name (Year – Year)")
    st.markdown("- Relevant coursework: [Course 1], [Course 2], [Course 3]")

elif page == "🚀 Projects":
    st.markdown("<div class='section-title'>Selected Projects</div>", unsafe_allow_html=True)
    st.markdown(
        """
        Below are some projects showcasing my skills in data science, machine learning, and analytics. 
        Each project demonstrates different aspects of the data science workflow, from data collection 
        and preprocessing to model deployment and visualization.
        """
    )
    st.markdown("")

    # ---- Project 1 ----
    project_card(
        title="Customer Churn Prediction",
        role="End-to-end ML project",
        description=(
            "Developed a churn prediction model using customer transaction and interaction data. "
            "Performed extensive feature engineering, model selection, and evaluation, then packaged the model for use in campaigns. "
            "The model achieved 85% accuracy and helped reduce churn by 15% through targeted retention campaigns."
        ),
        tech_stack=["Python", "scikit-learn", "Pandas", "MLflow", "XGBoost", "Docker"],
        github_link="https://github.com/yourname/churn-project",
        link="https://yourname-churn-demo.streamlit.app",
    )

    # ---- Project 2 ----
    project_card(
        title="NLP Topic Modeling on Research Papers",
        role="NLP / Text Mining",
        description=(
            "Collected and processed abstracts from scientific articles, built topic models (LDA, NMF), "
            "and created an interactive visualization to explore topics over time. "
            "Analyzed over 10,000 research papers to identify emerging trends in machine learning research."
        ),
        tech_stack=["Python", "spaCy", "Gensim", "Scikit-learn", "Plotly", "Streamlit"],
        github_link="https://github.com/yourname/nlp-topic-modeling",
    )

    # ---- Project 3 ----
    project_card(
        title="Interactive Analytics Dashboard",
        role="Analytics & Visualization",
        description=(
            "Created a Streamlit dashboard that allows business users to slice and analyze KPIs interactively, "
            "with built-in statistical tests and automated narratives. "
            "The dashboard processes real-time data and provides actionable insights for decision-making."
        ),
        tech_stack=["Streamlit", "Plotly", "Pandas", "SQL", "PostgreSQL"],
        github_link="https://github.com/yourname/analytics-dashboard",
        link="https://yourname-dashboard.streamlit.app",
    )
    
    st.markdown("")
    st.markdown("---")
    st.markdown("#### 💡 More Projects")
    st.markdown("Check out my [GitHub](https://github.com/yourname) for additional projects and code samples.")

elif page == "📚 Publications":
    st.markdown("<div class='section-title'>Publications & Academic Work</div>", unsafe_allow_html=True)

    st.markdown(
        "You can list peer-reviewed papers, theses, technical reports, or notable academic projects here."
    )

    # ---- Example publication 1 ----
    publication_item(
        title="Your Paper Title",
        venue="Journal / Conference Name",
        year="2024",
        link="https://doi.org/...",
        summary="Short 1–2 sentence summary of what the paper is about and your main contribution.",
    )

    # ---- Example publication 2 ----
    publication_item(
        title="Your Thesis Title",
        venue="Master's Thesis, University Name",
        year="2023",
        link="https://...",
        summary="Investigated [topic] using [methods], with key findings including [brief results].",
    )

    st.markdown("<div class='section-title'>Other Academic Links</div>", unsafe_allow_html=True)
    st.markdown(
        """
        - [Google Scholar](https://scholar.google.com/)
        - [ORCID](https://orcid.org/)
        - [ResearchGate](https://www.researchgate.net/)
        """
    )

elif page == "📧 Contact":
    st.markdown("<div class='section-title'>Get In Touch</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h3>📬 Contact Information</h3>
                <p><strong>Email:</strong> your.email@domain.com</p>
                <p><strong>Location:</strong> City, Country</p>
                <p><strong>Status:</strong> Open to opportunities</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("")
        st.markdown("#### 🌐 Online Profiles")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/)")
        st.markdown("💻 [GitHub](https://github.com/)")
        st.markdown("📊 [Kaggle](https://www.kaggle.com/)")
        st.markdown("📚 [Google Scholar](https://scholar.google.com/)")
    
    with col2:
        st.markdown(
            """
            <div class='card'>
                <h3>💼 What I'm Looking For</h3>
                <p>I'm open to opportunities in:</p>
                <ul>
                    <li>Data Science</li>
                    <li>Machine Learning Engineering</li>
                    <li>Analytics & Business Intelligence</li>
                    <li>Research & Development</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("")
        st.markdown("#### ✨ Why Work With Me?")
        st.markdown(
            """
            - ✅ **Clean Code:** I write clear, reproducible code and care about maintainability
            - 📊 **Communication:** I translate technical insights for non-technical stakeholders
            - 🚀 **End-to-End:** I own projects from raw data to deployed models and storytelling
            - 🎯 **Results-Driven:** I focus on delivering measurable business value
            """
        )
    
    st.markdown("---")
    
    # Contact Form
    st.markdown("#### 📝 Send a Message")
    st.markdown("Feel free to reach out! Fill out the form below or send me an email directly.")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name *")
        email = st.text_input("Your Email *")
        subject = st.text_input("Subject")
        message = st.text_area("Message *", height=150)
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you for your message! I'll get back to you soon.")
                st.info("💡 Note: This is a demo form. In a production deployment, this would send an email notification.")
            else:
                st.warning("⚠️ Please fill in all required fields (marked with *)")
