# Portfolio Website

A modern, interactive portfolio website built with Streamlit showcasing your data science projects, experience, and skills.

## Features

- 🏠 **About Page**: Personal introduction and highlights
- 💻 **Skills Page**: Technical and soft skills with visual tags
- 💼 **Experience Page**: Work history and education
- 🚀 **Projects Page**: Showcase your data science projects
- 📚 **Publications Page**: Academic work and research
- 📧 **Contact Page**: Functional contact form that sends emails directly to you

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository or navigate to the project directory:
   ```bash
   cd Jan-CV
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. The app will automatically open in your default web browser at `http://localhost:8501`

## Customization

### Personal Information

Edit `app.py` to customize:

1. **Page Title & Icon**: Update `st.set_page_config()` at the top
2. **Personal Details**: Replace placeholder text in the "About" section
3. **Experience**: Update the `experience_item()` calls with your work history
4. **Projects**: Modify the `project_card()` calls with your actual projects
5. **Skills**: Update the skill tags in the "Skills" page
6. **Contact Info**: Update email, location, and social media links

### Profile Image

1. Add your profile image to the project directory (e.g., `profile.jpg`)
2. Uncomment the `st.image()` line in the About page section

### Email Configuration (Contact Form)

The contact form can send emails directly to you! Here's how to set it up:

#### Option 1: Using Streamlit Secrets (Recommended)

1. Create a `.streamlit` folder in your project directory (if it doesn't exist)
2. Copy the example secrets file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```
3. Edit `.streamlit/secrets.toml` and add your email credentials:
   ```toml
   [email]
   smtp_server = "smtp.gmail.com"
   smtp_port = 587
   smtp_username = "your-email@gmail.com"
   smtp_password = "your-app-password"
   recipient_email = "your-email@gmail.com"
   ```

#### Option 2: Using Environment Variables

Set these environment variables:
```bash
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USERNAME="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
export RECIPIENT_EMAIL="your-email@gmail.com"
```

#### Gmail Setup (Most Common)

1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and "Other (Custom name)"
   - Enter "Streamlit Portfolio" as the name
   - Copy the generated 16-character password
   - Use this password in your `secrets.toml` file (not your regular Gmail password)

#### Other Email Providers

- **Outlook/Hotmail**: `smtp-mail.outlook.com`, port `587`
- **Yahoo**: `smtp.mail.yahoo.com`, port `587`
- **Custom SMTP**: Use your provider's SMTP settings

**Important**: Never commit your `secrets.toml` file to Git! It's already in `.gitignore`.

### Styling

The CSS styles are defined in the `CUSTOM CSS` section. You can customize:
- Colors (currently using a purple gradient theme)
- Font sizes
- Spacing and layout
- Card styles

## Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Set the main file path to `app.py`
6. Deploy!

### Other Platforms

You can also deploy to:
- Heroku
- AWS EC2
- Google Cloud Run
- Any platform that supports Python web apps

## Project Structure

```
Jan-CV/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .streamlit/
│   └── secrets.toml.example       # Example email configuration
└── .streamlit/
    └── secrets.toml                # Your email config (not in Git)
```

## Technologies Used

- **Streamlit**: Web framework for building the portfolio
- **Python**: Programming language
- **HTML/CSS**: Custom styling

## License

This project is open source and available for personal use.

## Contributing

Feel free to fork this project and customize it for your own portfolio!

---

Built with ❤️ using Streamlit