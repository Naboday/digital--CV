from pathlib import Path
import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/ "main.css"
resume_file = current_dir/"assests"/"digital-cv.pdf"
profile_pic = current_dir /"assests"/ "pic.jpg"

PAGE_TITLE = "Digital CV | Naboday Saha"
PAGE_ICON = ":wave:"
NAME = "Naboday saha"
DESCRIPTION = """
Student At Sapthagiri College of Engineering
"""
EMAIL = "sahanaboday90@gmail.com"
SOCIAL_MEDIA = {
    "GeeksforGeeks": "https://auth.geeksforgeeks.org/user/sahanab8efh",
    "LinkedIn": "https://www.linkedin.com/in/naboday-saha-20a725269/",
    "GitHub": "https://github.com/Naboday",
    "Microsoft Profile": "https://learn.microsoft.com/en-us/users/nabodaysaha-9383/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col2:
    st.image(profile_pic, width=200)

with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("---")

st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ current experience close to none but open to work on projects
- ✔️ knowledge in Python and database management systems
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

st.write("---")

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, C.
- 📊 Data Visulization: MS Excel.
- 🗄️ Databases: MySQL, RDBMS.
"""
)

st.write("---")

st.write('\n')
st.subheader("Work History")

# --- JOB 1
st.write("🚧", "**Web Developer Associate | GDSC**")
st.write("2023-2024")
st.write(
    """
-working on projects.\n
-management and organization of events.\n
-development of new skills.\n
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Desgination in 2nd job | Name of the company**")
st.write("work period")
st.write(
    """
-experience and skills learnt during the occupation
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Desgination in 3rd job | Name of the company**")
st.write("work period")
st.write(
    """
-experience and skills learnt during the occupation
"""
)

st.write("---")