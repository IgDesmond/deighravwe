import streamlit as st
from io import BytesIO
from fpdf import FPDF

# Page Configuration
st.set_page_config(
    page_title="D.E. Ighravwe",
    page_icon="mypix.jpg",
    layout="centered",
    initial_sidebar_state="auto"
)

# Hide Streamlit toolbar and footer
st.markdown(
    """
    <style>
    header {
    background-color: transparent;
    }
    .stApp {
    background-color: #f0f0f0; /* Set your desired background color here */
    [data-testid="stToolbar"] {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to generate PDF of CV
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)  # Enable auto page break
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, txt="Desmond Eseoghene Ighravwe, PhD", ln=True, align="C")
    pdf.ln(10)

    # Personal Information
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=(
        "Desmond Eseoghene IGHRAVWE is an Associate Professor at the Department of Mechanical Engineering, "
        "Bells University of Technology, Ota, Nigeria. He holds a PhD in Mechanical Engineering from Ladoke Akintola "
        "University of Technology, Nigeria. He completed his B.Sc. and M.Sc. programs in Industrial Engineering at "
        "the University of Ibadan, Nigeria. His research areas include artificial intelligence, operations research, "
        "energy and waste management, and multi-criteria analysis. Currently, he is the Acting Director of Bells "
        "University of Technology ICT Resource Centre."
    ))
    pdf.ln(10)

    # Sections: Education, Work Experience, Publications, Skills, Contact
    sections = {
        "Education": (
            "- **B.Sc**, University of Ibadan, Nigeria (2002-2008): Industrial Engineering\n"
            "- **M.Sc**, University of Ibadan, Nigeria (2009-2011): Industrial Engineering\n"
            "- **PhD**, Ladoke Akintola University of Technology, Nigeria (2013-2018): Mechanical Engineering"
        ),
        "Work Experience": (
            "- Acting Director ICT Resource Center, Bells University of Technology (2023-2025):\n"
            "  - Managed ICT infrastructure\n"
            "  - Developed applications\n\n"
            "- Acting Head of Department, Bells University of Technology (2021-2023):\n"
            "  - Coordinated staff and managed students\n\n"
            "- Faculty @ Department of Mechanical Engineering, Bells University (2018-Present):\n"
            "  - Research, teaching, and community service"
        ),
        "Publication Links": (
            "- Google Scholar: https://scholar.google.com/citations?user=yYS_TYsAAAAJ&hl=en\n"
            "- ResearchGate: https://www.researchgate.net/profile/Desmond-Ighravwe\n"
            "- Scopus: https://www.scopus.com/authid/detail.uri?authorId=55990538400"
        ),
        "Skills": (
            "- Data Analytics\n"
            "- Machine Learning\n"
            "- Mathematical Modelling\n"
            "- Computational Intelligence"
        ),
        "Contact Information": (
            "- Email: ighravwedesmond@gmail.com\n"
            "- Phone: +2348033561227\n"
            "- LinkedIn: https://www.linkedin.com/in/ighravwe-desmond-eseoghene-05076724/\n"
            "- GitHub: https://github.com/IgDesmond"
        )
    }

    for title, content in sections.items():
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, title, ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.ln(10)

    return pdf.output(dest="S").encode("latin1")


# Streamlit Interface
st.title("Desmond Eseoghene Ighravwe, PhD")

# Display Image
try:
    st.image("mypix.jpg", width=300)  # Set width in pixels
except FileNotFoundError:
    st.warning("Profile picture not found. Please ensure 'mypix.jpg' is in the correct directory.")
    
# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Education", "Experience", "Publication Links", "Skills", "Contact"])

# Render Sections
content_map = { "Home":"Welcome to my CV! Explore my academic and professional journey.",
    "Education": """
    - **B.Sc**, University of Ibadan, Nigeria (2002-2008): Industrial Engineering
    - **M.Sc**, University of Ibadan, Nigeria (2009-2011): Industrial Engineering
    - **PhD**, Ladoke Akintola University of Technology, Nigeria (2013-2018): Mechanical Engineering
    """,
    "Experience": """
    - Acting Director ICT Resource Center, Bells University of Technology (2023-2025)
    - Acting Head of Department, Bells University of Technology (2021-2023)
    - Faculty @ Department of Mechanical Engineering, Bells University (2018-Present)
    """,
    "Publication Links": """
    - [Google Scholar](https://scholar.google.com/citations?user=yYS_TYsAAAAJ&hl=en)
    - [ResearchGate](https://www.researchgate.net/profile/Desmond-Ighravwe)
    - [Scopus](https://www.scopus.com/authid/detail.uri?authorId=55990538400)
    """,
    "Skills": "- Data Analytics\n- Machine Learning\n- Mathematical Modelling\n- Computational Intelligence",
    "Contact": """
    - Email: ighravwedesmond@gmail.com
    - Phone: +2348033561227
    - [LinkedIn](https://www.linkedin.com/in/ighravwe-desmond-eseoghene-05076724/)
    - [GitHub](https://github.com/IgDesmond)
    """
}

st.header(section)
st.write(content_map[section])

# Download Button for PDF
st.download_button(
    label="Download CV as PDF",
    data=generate_pdf(),
    file_name="Desmond_Ighravwe_CV.pdf",
    mime="application/pdf"
)
