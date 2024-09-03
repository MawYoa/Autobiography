import streamlit as st
from PIL import Image

# Title and Sidebar
st.set_page_config(page_title="Mark Edwin's Portfolio", layout="wide")
st.title("My Autobiography and Portfolio")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Autobiography", "Portfolio", "Contact"])

# Home Section
if options == "Home":
    st.header("Welcome to My Portfolio!")

    # Adjusting the profile image size
    image = Image.open("profilepic.jpg")
    st.image(image, width=200, caption="Mark Edwin E. Huyo-a")

    st.write(
        """
        Hello! I'm Mark Edwin Etcobanez Huyo-a, a 4th-year Information Technology student. 
        Welcome to my online portfolio where you can learn more about me, my work, and how to get in touch.
        """
    )

# Autobiography Section
elif options == "Autobiography":
    st.header("About Me")
    st.write(
        """
        **Name:** Mark Edwin E. Huyo-a  
        **Occupation:** 4th-year Information Technology Student  
        **Location:** Rizada Apartment, F.Pacanya Street, Tisa, Cebu City

        ### My Story
        I am a 4th-year student pursuing a Bachelor of Science in Information Technology. My journey started when I discovered my passion for technology and programming during high school. Since then, I've been honing my skills and working on various projects that have deepened my understanding of the field.
        """
    )

    # Adding expander sections for more details
    with st.expander("Early Life"):
        st.write(
            "I was born in Bagong Silang, Caloocan City and raised in Barangay Pili, Municipality of Placer, Masbate. My interest in technology began when I was in high school, where I started exploring programming and computer science."
        )

    with st.expander("Education"):
        st.write(
            "I am currently in my 4th year of pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology - University. Throughout my academic journey, I have been actively involved in projects and coursework that have equipped me with the necessary skills for a career in IT."
        )

    with st.expander("Career Goals"):
        st.write(
            "Upon graduation, I aspire to work in either software development, cybersecurity, or data science. I am particularly interested in cybersecurity, and I hope to contribute to the field by working on innovative projects."
        )

# Portfolio Section
elif options == "Portfolio":
    st.header("My Portfolio")
    st.write("Here are some of the projects I have worked on:")

    # Projects Grid with more descriptive project titles and links
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Project 1: [Your Project Name]")
        st.image("https://via.placeholder.com/400x200.png")
        st.write("Description: This project is about [Project 1 Description].")
        st.write("[Link to Project 1](#)")

    with col2:
        st.subheader("Project 2: [Your Project Name]")
        st.image("https://via.placeholder.com/400x200.png")
        st.write("Description: This project is about [Project 2 Description].")
        st.write("[Link to Project 2](#)")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Project 3: [Your Project Name]")
        st.image("https://via.placeholder.com/400x200.png")
        st.write("Description: This project is about [Project 3 Description].")
        st.write("[Link to Project 3](#)")

    with col4:
        st.subheader("Project 4: [Your Project Name]")
        st.image("https://via.placeholder.com/400x200.png")
        st.write("Description: This project is about [Project 4 Description].")
        st.write("[Link to Project 4](#)")

# Contact Section
elif options == "Contact":
    st.header("Get in Touch")

    # Contact Form with placeholders
    st.write("Feel free to reach out to me through the form below!")

    with st.form(key="contact_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Enter your message")
        submit_button = st.form_submit_button(label="Send Message")

        if submit_button:
            st.success(f"Thank you {name}! Your message has been sent successfully.")
