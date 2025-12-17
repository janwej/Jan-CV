import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Animated background */
        .stApp {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Main container styling */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            margin: 1rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Animated main title */
        .main-title {
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s linear infinite;
        }
        
        @keyframes shimmer {
            to { background-position: 200% center; }
        }
        
        /* Subtitle with animation */
        .subtitle {
            font-size: 1.3rem;
            color: #4a5568;
            margin-bottom: 2rem;
            line-height: 1.8;
            animation: fadeInUp 1s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Section titles with gradient */
        .section-title {
            font-size: 2rem;
            font-weight: 800;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            padding-bottom: 0.5rem;
            position: relative;
            display: inline-block;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            border-radius: 2px;
            animation: expand 0.5s ease;
        }
        
        @keyframes expand {
            from { width: 0; }
            to { width: 100%; }
        }
        
        /* Enhanced tags with glow effect */
        .tag {
            display: inline-block;
            padding: 0.5rem 1rem;
            margin: 0.4rem 0.4rem 0.4rem 0;
            border-radius: 25px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            font-size: 0.9rem;
            font-weight: 600;
            color: #4a5568;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .tag::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(102, 126, 234, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .tag:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
            border-color: transparent;
        }
        
        .tag:hover::before {
            width: 300px;
            height: 300px;
        }
        
        /* Glassmorphism cards */
        .card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(102, 126, 234, 0.1), transparent);
            transform: rotate(45deg);
            transition: all 0.6s;
        }
        
        .card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 16px 40px rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
        }
        
        .card:hover::before {
            top: 100%;
            left: 100%;
        }
        
        /* Experience item with timeline effect */
        .experience-item {
            padding: 2rem;
            margin: 2rem 0;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border-left: 5px solid;
            border-image: linear-gradient(180deg, #667eea, #764ba2) 1;
            position: relative;
            transition: all 0.4s ease;
        }
        
        .experience-item::before {
            content: '●';
            position: absolute;
            left: -12px;
            top: 2rem;
            color: #667eea;
            font-size: 1.5rem;
            background: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
        }
        
        .experience-item:hover {
            transform: translateX(10px);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.2);
        }
        
        /* Enhanced project cards */
        .project-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(247, 250, 252, 0.9) 100%);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 2px solid rgba(102, 126, 234, 0.2);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .project-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transition: left 0.5s;
        }
        
        .project-card:hover {
            border-color: #667eea;
            box-shadow: 0 12px 32px rgba(102, 126, 234, 0.25);
            transform: translateY(-5px);
        }
        
        .project-card:hover::after {
            left: 100%;
        }
        
        /* Progress bar styling */
        .progress-container {
            background: rgba(102, 126, 234, 0.1);
            border-radius: 10px;
            height: 30px;
            margin: 1rem 0;
            overflow: hidden;
            position: relative;
        }
        
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 1rem;
            color: white;
            font-weight: 600;
            font-size: 0.85rem;
            animation: slideIn 1s ease;
            box-shadow: 0 2px 10px rgba(102, 126, 234, 0.4);
        }
        
        @keyframes slideIn {
            from { width: 0; }
        }
        
        /* Small text */
        .small-text {
            font-size: 0.9rem;
            color: #718096;
            font-style: italic;
        }
        
        /* Link styling with hover effect */
        a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            position: relative;
            transition: all 0.3s ease;
        }
        
        a::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s ease;
        }
        
        a:hover {
            color: #764ba2;
        }
        
        a:hover::after {
            width: 100%;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            padding-top: 2rem;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
        }
        
        /* Enhanced button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2.5rem;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }
        
        .stButton > button:hover::before {
            width: 300px;
            height: 300px;
        }
        
        .stButton > button:active {
            transform: translateY(-1px) scale(1.02);
        }
        
        /* Enhanced input styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: 12px;
            border: 2px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.9);
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        /* Floating animation for icons */
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        .floating {
            animation: float 3s ease-in-out infinite;
        }
        
        /* Stats card */
        .stat-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.4s ease;
            border: 2px solid rgba(102, 126, 234, 0.2);
        }
        
        .stat-card:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            border-color: #667eea;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
st.sidebar.markdown(
    """
    <div style='text-align: center; padding: 1.5rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; margin-bottom: 1rem; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);'>
        <h1 style='font-size: 2rem; margin-bottom: 0.5rem; color: white; font-weight: 800;'>📊 Portfolio</h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 0.9rem;'>Data Scientist</p>
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


def render_skill_bar(skill, level, color="#667eea"):
    """Render a skill with progress bar"""
    st.markdown(f"**{skill}**")
    progress_html = f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {level}%; background: linear-gradient(90deg, {color}, #764ba2);">
            {level}%
        </div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)


def create_skill_chart(skills_data):
    """Create a radar chart for skills"""
    categories = list(skills_data.keys())
    values = list(skills_data.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skills',
        line_color='#667eea',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#4a5568')
    )
    
    return fig


def stat_card(number, label, icon="📊"):
    """Render a stat card"""
    html = f"""
    <div class="stat-card">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;" class="floating">{icon}</div>
        <div class="stat-number">{number}</div>
        <div style="color: #718096; font-weight: 600; margin-top: 0.5rem;">{label}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def send_email(name, sender_email, subject, message):
    """
    Send an email using SMTP.
    Configure your email settings in Streamlit secrets or environment variables.
    """
    try:
        # Get email configuration from Streamlit secrets
        # If secrets are not configured, try environment variables
        try:
            smtp_server = st.secrets["email"]["smtp_server"]
            smtp_port = st.secrets["email"]["smtp_port"]
            smtp_username = st.secrets["email"]["smtp_username"]
            smtp_password = st.secrets["email"]["smtp_password"]
            recipient_email = st.secrets["email"]["recipient_email"]
        except (KeyError, FileNotFoundError):
            # Fallback to environment variables or default Gmail settings
            import os
            smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("SMTP_PORT", "587"))
            smtp_username = os.getenv("SMTP_USERNAME", "")
            smtp_password = os.getenv("SMTP_PASSWORD", "")
            recipient_email = os.getenv("RECIPIENT_EMAIL", "")
            
            if not smtp_username or not smtp_password or not recipient_email:
                return False, "Email configuration not found. Please set up Streamlit secrets or environment variables."
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = f"Portfolio Contact Form: {subject if subject else 'No Subject'}"
        msg['Reply-To'] = sender_email
        
        # Create email body
        body = f"""
        New message from your portfolio contact form:
        
        Name: {name}
        Email: {sender_email}
        Subject: {subject if subject else 'No Subject'}
        Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Message:
        {message}
        
        ---
        This email was sent from your portfolio website contact form.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable encryption
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        
        return True, "Email sent successfully!"
        
    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed. Please check your email credentials."
    except smtplib.SMTPException as e:
        return False, f"SMTP error occurred: {str(e)}"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"


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
    
    # Stats Section
    st.markdown("#### 📈 By The Numbers")
    stats_cols = st.columns(4)
    
    with stats_cols[0]:
        stat_card("50+", "Projects", "🚀")
    
    with stats_cols[1]:
        stat_card("5+", "Years Experience", "💼")
    
    with stats_cols[2]:
        stat_card("10+", "Publications", "📚")
    
    with stats_cols[3]:
        stat_card("100%", "Satisfaction", "⭐")
    
    st.markdown("---")
    
    # Highlights Section with enhanced visuals
    st.markdown("#### ✨ Key Highlights")
    highlight_cols = st.columns(3)
    
    with highlight_cols[0]:
        st.markdown(
            """
            <div class='card' style='text-align: center; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);'>
                <div style='font-size: 4rem; margin-bottom: 1rem;' class="floating">🚀</div>
                <h3 style='color: #667eea; margin-bottom: 0.5rem;'>Projects</h3>
                <p style='color: #4a5568;'>Built impactful ML models and data products that drive business decisions</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with highlight_cols[1]:
        st.markdown(
            """
            <div class='card' style='text-align: center; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);'>
                <div style='font-size: 4rem; margin-bottom: 1rem;' class="floating">📊</div>
                <h3 style='color: #667eea; margin-bottom: 0.5rem;'>Impact</h3>
                <p style='color: #4a5568;'>Delivered measurable business value through data-driven insights</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with highlight_cols[2]:
        st.markdown(
            """
            <div class='card' style='text-align: center; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);'>
                <div style='font-size: 4rem; margin-bottom: 1rem;' class="floating">📚</div>
                <h3 style='color: #667eea; margin-bottom: 0.5rem;'>Research</h3>
                <p style='color: #4a5568;'>Published academic work and contributions to the data science community</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Visual Timeline or Chart
    st.markdown("---")
    st.markdown("#### 📅 Experience Timeline")
    
    # Create a simple timeline visualization
    timeline_data = pd.DataFrame({
        'Year': [2020, 2021, 2022, 2023, 2024],
        'Projects': [5, 8, 12, 15, 20],
        'Impact Score': [60, 70, 80, 85, 90]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=timeline_data['Year'],
        y=timeline_data['Projects'],
        mode='lines+markers',
        name='Projects',
        line=dict(color='#667eea', width=3),
        marker=dict(size=10, color='#667eea')
    ))
    
    fig.add_trace(go.Scatter(
        x=timeline_data['Year'],
        y=timeline_data['Impact Score'],
        mode='lines+markers',
        name='Impact Score',
        line=dict(color='#764ba2', width=3),
        marker=dict(size=10, color='#764ba2'),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="Growth Over Time",
        xaxis_title="Year",
        yaxis_title="Number of Projects",
        yaxis2=dict(title="Impact Score", overlaying='y', side='right'),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#4a5568'),
        hovermode='x unified',
        legend=dict(x=0.7, y=0.1)
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "💻 Skills":
    st.markdown("<div class='section-title'>Technical Skills</div>", unsafe_allow_html=True)
    
    # Skills Overview Chart
    st.markdown("#### 📊 Skills Overview")
    skills_data = {
        "Python": 95,
        "Machine Learning": 90,
        "Data Analysis": 88,
        "Deep Learning": 85,
        "Cloud Platforms": 80,
        "SQL": 92
    }
    
    col_chart, col_stats = st.columns([2, 1])
    
    with col_chart:
        fig = create_skill_chart(skills_data)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_stats:
        st.markdown("#### 🎯 Proficiency Levels")
        for skill, level in list(skills_data.items())[:3]:
            render_skill_bar(skill, level)
    
    st.markdown("---")
    
    # Detailed Skills Sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 💻 Programming & Tools")
        render_skill_bar("Python", 95)
        render_skill_bar("SQL", 92)
        render_skill_bar("R", 85)
        render_skill_bar("Git", 90)
        render_skill_bar("Docker", 85)
        render_skill_bar("Linux/Bash", 88)
        
        st.markdown("")
        st.markdown("#### 🤖 Machine Learning")
        render_skill_bar("Supervised Learning", 92)
        render_skill_bar("Unsupervised Learning", 88)
        render_skill_bar("Time Series", 85)
        render_skill_bar("Model Evaluation", 90)
        render_skill_bar("Feature Engineering", 93)

        st.markdown("")
        st.markdown("#### 🧠 Deep Learning")
        render_skill_bar("PyTorch", 88)
        render_skill_bar("TensorFlow", 85)
        render_skill_bar("CNNs", 82)
        render_skill_bar("RNNs", 80)
        render_skill_bar("Transformers", 85)

    with col2:
        st.markdown("#### 📊 Data & Analytics")
        render_skill_bar("Pandas", 95)
        render_skill_bar("NumPy", 93)
        render_skill_bar("EDA", 90)
        render_skill_bar("Experiment Design", 88)
        render_skill_bar("A/B Testing", 85)
        render_skill_bar("Dashboards", 90)
        
        st.markdown("")
        st.markdown("#### ☁️ Databases & Cloud")
        render_skill_bar("PostgreSQL", 88)
        render_skill_bar("BigQuery", 85)
        render_skill_bar("Snowflake", 82)
        render_skill_bar("AWS", 80)
        render_skill_bar("GCP", 78)

        st.markdown("")
        st.markdown("#### 🤝 Soft Skills")
        render_skill_bar("Communication", 95)
        render_skill_bar("Storytelling", 92)
        render_skill_bar("Collaboration", 90)
        render_skill_bar("Mentoring", 88)
    
    st.markdown("---")
    
    # Skill Tags Section
    st.markdown("#### 🏷️ All Technologies")
    st.markdown("**Programming Languages:**")
    render_tags(["Python", "R", "SQL", "JavaScript", "Bash"])
    
    st.markdown("**ML/DL Frameworks:**")
    render_tags(["scikit-learn", "PyTorch", "TensorFlow", "XGBoost", "LightGBM", "Keras"])
    
    st.markdown("**Data Tools:**")
    render_tags(["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Streamlit"])
    
    st.markdown("**Cloud & DevOps:**")
    render_tags(["AWS", "GCP", "Docker", "Kubernetes", "Git", "CI/CD"])

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
    
    # Project Stats
    proj_cols = st.columns(4)
    with proj_cols[0]:
        stat_card("15+", "ML Models", "🤖")
    with proj_cols[1]:
        stat_card("10+", "Dashboards", "📊")
    with proj_cols[2]:
        stat_card("5+", "Deployments", "🚀")
    with proj_cols[3]:
        stat_card("85%", "Avg Accuracy", "🎯")
    
    st.markdown("---")
    
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
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name *")
        sender_email = st.text_input("Your Email *")
        subject = st.text_input("Subject")
        message = st.text_area("Message *", height=150)
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and sender_email and message:
                # Validate email format
                import re
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_pattern, sender_email):
                    st.error("❌ Please enter a valid email address.")
                else:
                    # Show loading state
                    with st.spinner("📧 Sending your message..."):
                        success, result_message = send_email(name, sender_email, subject, message)
                    
                    if success:
                        st.success("✅ Thank you for your message! I'll get back to you soon.")
                        st.balloons()  # Celebration animation
                    else:
                        st.error(f"❌ Failed to send email: {result_message}")
                        st.info("💡 You can also reach me directly at the email address shown above.")
            else:
                st.warning("⚠️ Please fill in all required fields (marked with *)")
