import streamlit as st

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Your Name - Data Scientist",
    page_icon="📊",
    layout="wide",
)

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            font-size: 1.1rem;
            color: #555555;
            margin-bottom: 1.5rem;
        }
        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }
        .tag {
            display: inline-block;
            padding: 0.15rem 0.5rem;
            margin: 0.1rem;
            border-radius: 999px;
            border: 1px solid #dddddd;
            font-size: 0.8rem;
        }
        .small-text {
            font-size: 0.9rem;
            color: #777777;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "About",
        "Skills",
        "Experience",
        "Projects",
        "Publications",
        "Contact",
    ],
)

# Optional: sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("**Status:** Open to Data Scientist roles")
st.sidebar.markdown("📍 City, Country")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/)  |  [GitHub](https://github.com/)")

# ---------- HELPER FUNCTIONS ----------
def render_tags(tags):
    tag_html = " ".join([f"<span class='tag'>{t}</span>" for t in tags])
    st.markdown(tag_html, unsafe_allow_html=True)


def project_card(title, role, description, tech_stack, link=None):
    st.markdown(f"**{title}**  —  *{role}*")
    st.markdown(description)
    render_tags(tech_stack)
    if link:
        st.markdown(f"[View project]({link})")
    st.markdown("---")


def experience_item(role, company, period, location, bullets):
    st.markdown(f"**{role}** — *{company}*")
    st.markdown(f"<span class='small-text'>{period} | {location}</span>", unsafe_allow_html=True)
    for b in bullets:
        st.markdown(f"- {b}")
    st.markdown("")


def publication_item(title, venue, year, link=None, summary=None):
    st.markdown(f"**{title}**")
    st.markdown(f"*{venue}, {year}*")
    if summary:
        st.markdown(summary)
    if link:
        st.markdown(f"[Link]({link})")
    st.markdown("")


# ---------- PAGES ----------
if page == "About":
    col1, col2 = st.columns([1, 2])

    with col1:
        # Replace with your own image or remove if not needed
        # st.image("profile.jpg", width=180)
        st.markdown("### Your Name")
        st.markdown("Data Scientist | Machine Learning | Analytics")
        st.markdown("📍 City, Country")
        st.markdown("✉️ your.email@domain.com")

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

        st.markdown("#### Quick Summary")
        st.markdown(
            """
            - 🎓 Education: Your degree(s) and university
            - 💼 Experience: Brief summary of your most relevant roles
            - 🧠 Interests: e.g., time series, causal inference, recommendation systems
            - 🛠 Tech: Python, SQL, scikit-learn, PyTorch, Docker, etc.
            """
        )

        st.markdown("#### Highlights")
        st.markdown(
            """
            - Built [brief cool thing], impacting [metric or outcome].
            - Led [project / research] using [methods / tools].
            - Co-authored [X] academic works on [topic].
            """
        )

elif page == "Skills":
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

elif page == "Experience":
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

elif page == "Projects":
    st.markdown("<div class='section-title'>Selected Projects</div>", unsafe_allow_html=True)
    st.markdown(
        "Below are some projects showcasing my skills in data science, machine learning and analytics."
    )

    # ---- Project 1 ----
    project_card(
        title="Customer Churn Prediction",
        role="End-to-end ML project",
        description=(
            "Developed a churn prediction model using customer transaction and interaction data. "
            "Performed extensive feature engineering, model selection, and evaluation, then packaged the model for use in campaigns."
        ),
        tech_stack=["Python", "scikit-learn", "Pandas", "MLflow"],
        link="https://github.com/yourname/churn-project",
    )

    # ---- Project 2 ----
    project_card(
        title="NLP Topic Modeling on Research Papers",
        role="NLP / Text Mining",
        description=(
            "Collected and processed abstracts from scientific articles, built topic models (LDA, NMF), "
            "and created an interactive visualization to explore topics over time."
        ),
        tech_stack=["Python", "spaCy", "Gensim", "Scikit-learn"],
        link="https://github.com/yourname/nlp-topic-modeling",
    )

    # ---- Project 3 ----
    project_card(
        title="Interactive Analytics Dashboard",
        role="Analytics & Visualization",
        description=(
            "Created a Streamlit dashboard that allows business users to slice and analyze KPIs interactively, "
            "with built-in statistical tests and automated narratives."
        ),
        tech_stack=["Streamlit", "Plotly", "Pandas"],
        link="https://github.com/yourname/analytics-dashboard",
    )

elif page == "Publications":
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

elif page == "Contact":
    st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
    st.markdown(
        """
        I'm open to opportunities in data science, machine learning, and analytics.
        **Email:** your.email@domain.com  
        **Location:** City, Country  
        """
    )

    st.markdown("#### Profiles")
    st.markdown("- [LinkedIn](https://www.linkedin.com/)")
    st.markdown("- [GitHub](https://github.com/)")
    st.markdown("- [Kaggle](https://www.kaggle.com/)")

    st.markdown("#### Why work with me?")
    st.markdown(
        """
        - I write clear, reproducible code and care about maintainability.  
        - I communicate insights in a way that non-technical stakeholders understand.  
        - I like owning projects end-to-end: from raw data to deployed model and storytelling.
        """
    )

    st.markdown("#### Optional: Simple contact form (non-functional demo)")
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Message")

    if st.button("Send (demo)"):
        if name and email and message:
            st.success("Thanks! In a real deployment, this would send me an email.")
        else:
            st.warning("Please fill in all fields before sending.")
