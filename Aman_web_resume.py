import streamlit as st
from PIL import Image
import base64
import os
import datetime
from pathlib import Path
from io import BytesIO

# ✅ Set page configuration FIRST
st.set_page_config(page_title="Amandeep Singh Resume", 
                   page_icon="aman.jpeg", 
                   layout="wide")

# ✅ Function to encode image to base64 for background
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ✅ Function to set background image
def set_background(image_path):
    try:
        base64_str = get_base64(image_path)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{base64_str}");
                background-size: 95% 95%; ;
                background-position: center;
                background-attachment: fixed;    
            }}
            </style>
            """,unsafe_allow_html=True)
            
    except FileNotFoundError:
        st.error("Background image not found. Please check the file path.")

# ✅ Apply background image (Make sure the path is correct)
set_background("1.jpg")

# ---------- STYLING ----------
def set_custom_styles():
    st.markdown("""
    <style>
        .form-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 150px;
        }

        div[data-baseweb="input"] {
            width: 200px !important;
        }

        input {
            height: 40px !important;
            font-size: 16px !important;
            padding: 5px 10px !important;
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            background-color: #1e1e1e !important;
            color: white !important;
        }

        .stButton button {
            width: 200px;
            margin-top: 10px;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            background-color: #7b2cbf;
            color: white;
        }

        .stButton button:hover {
            background-color: #5a189a;
        }
    </style>
    """, unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    set_custom_styles()
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.markdown("### Welcome")

    username = st.text_input("", placeholder="e.g. Amantah", label_visibility="collapsed")

    if st.button("Explore Now"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("Please enter your name.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- WELCOME PAGE ----------
def welcome_page():
        # Encode local image to base64 string
        def get_base64_image(image_path):
            with Image.open(image_path) as img:
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                return base64.b64encode(buffered.getvalue()).decode()

        # Full absolute path to the image
        image_path = "Image Background Colorful Minimal Phone Wallpaper (1).jpg"

        # Check if image exists first
        if os.path.exists(image_path):
            img_base64 = get_base64_image(image_path)

            # Apply background to sidebar using a more reliable CSS selector
            st.markdown(
                f"""
                <style>
                [data-testid="stSidebar"] {{
                    background-image: url("data:image/png;base64,{img_base64}");
                    background-size: cover;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.sidebar.error("Image file not found!")

        # ✅ Function to encode image to base64 for background
        def get_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        def Home():
                    # ✅ Function to set background image
                    def set_background(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;    
                                }}
                                </style>
                                """,unsafe_allow_html=True)
                                
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")

                    # ✅ Apply background image (Make sure the path is correct)
                    set_background("photo-1454165804606-c3d57bc86b40.jpeg")
                    # ✅ Load the logo
                    logo = Image.open("aman.jpeg")
                    # ✅ Header Section
                    st.image(logo, width=150)
                    st.title("Welcome to My Portfolio")
                    # ✅ Display Current Date, Time, and Day
                    now = datetime.datetime.now()
                    date_today = now.strftime("%Y-%m-%d")
                    time_now = now.strftime("%H:%M:%S")
                    day_today = now.strftime("%A")
                    st.write(f"📅 **Date:** {date_today}",f"⏰ **Time:** {time_now}",f"🗓️ **Day:** {day_today}")
                    st.subheader("Exploring Aerospace, One Journey at a Time")
          
                    st.header("About My Journey of Education")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        font-size: 24px;
                        line-height: 1.8;
                        color: black;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        My name is Amandeep Singh, and my journey is not one paved with privileges or shortcuts, but one shaped by determination, resilience, and a deep desire to rewrite the narrative of my family.<br><br>
                        I come from a background where education was never a priority—not because it lacked value, but because it simply wasn’t accessible. My father was a hardworking transport businessman who spent long hours on the road to provide for our family. My mother, a dedicated housewife, managed everything at home with strength and silent sacrifice. Neither of them had the opportunity to pursue formal education, and in our household, academics were not something we talked much about. There were no degrees on the walls, no bedtime stories of college life—only the daily grind and the hope that their children might do better.<br><br>
                        Growing up in such an environment taught me one thing early on: if I wanted to create a different future, I had to fight for it. Education wasn’t just a personal goal—it became my mission. I had no mentors, no roadmap, and no family tradition of academics to follow. But I had something just as powerful: the will to learn and the hunger to grow.<br><br>
                        Despite the odds, I pursued my passion for aerospace engineering—a field that fascinated me with its complexity, precision, and connection to the vast skies I used to dream under as a child. I earned my B.Tech in Aerospace Engineering and went on to pursue an M.Tech, specializing in guided missiles. It wasn’t easy—there were moments of self-doubt, financial struggles, and academic pressure—but each challenge only strengthened my resolve.<br><br>
                        Through this journey, I’ve worked on multiple self-driven and collaborative projects—from UAV design tools and rocket motor analysis to wind tunnel development and app-based calculators for aerospace parameters. I also invested time in learning Python, data science, and software tools like ANSYS, knowing that being technically versatile is crucial in today’s world.<br><br>
                        But beyond the technical skills and degrees, what truly defines me is the story behind it all: a boy from a family with no academic legacy, who chose to chase the sky—literally and metaphorically. I want my story to serve as a reminder that where you come from doesn’t have to decide where you’re going. I am the first in my family to walk this path, but I know I won’t be the last.<br><br>
                        My vision now is bigger than just personal success. With Amantah Education and the Aerospace School, I aim to inspire and educate the next generation—especially those who, like me, come from places where dreams often seem out of reach.<br><br>
                        Because if my story proves anything, it’s this: when you have purpose, passion, and persistence, the sky is not the limit—it’s just the beginning.
                    </div>
                    """, unsafe_allow_html=True)
          
                    st.image("image.jpg", caption="About My Journey of Education", width=500)
          
                    # ✅ About Section
                    st.header("About My Focus")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        font-size: 24px;
                        line-height: 1.8;
                        color: black;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                            I have always focused on building and refining my personality each day, striving to grow not just professionally, but personally as well.
                            I believe that continuous self-improvement is the key to long-term success.
                            Every day, I seek out new experiences, explore unfamiliar ideas, and challenge myself to step beyond my comfort zone.
                            Whether it's learning a new concept, adopting a different perspective, or acquiring a fresh skill, I make it a point to evolve consistently.
                            This ongoing journey of self-discovery and learning helps me stay adaptable, motivated, and ready to take on new challenges with confidence.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.header("Mission")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3); 
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: black;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                                <li>To inspire and educate aspiring aerospace engineers through engaging, practical, and future-ready learning experiences.
                                <li>To contribute to the advancement of aerospace technology by combining academic insights with practical industrial knowledge.
                                <li>To mentor and guide students and professionals in cultivating both technical proficiency and innovative thinking.
                                <li>To promote a collaborative environment where knowledge, curiosity, and creativity fuel breakthroughs in aerospace engineering.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.header("My Vision")
                    st.markdown("""
                    <div style="
                        background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: black;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                            To bridge the gap between academic excellence and real-world aerospace innovation by fostering a culture of continuous learning, critical thinking,
                            and hands-on application. I envision a future where aerospace education is deeply integrated with industry needs,
                            empowering the next generation of engineers to lead with purpose, passion, and precision.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ✅ Features Section
                    st.header("Why Choose Me?")
                    col1, col2, col3,col4 = st.columns(4)
                    
                    col1, col2, col3, col4 = st.columns(4)  

                    with col1:
                        st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Dual Expertise</h5>
                                <p style="font-size:28px;">
                                    With a solid background in both academia and the aerospace industry,
                                    I offer a unique perspective that blends theoretical depth with hands-on experience.
                                </p>
                            </div>
                        """, unsafe_allow_html=True)  

                    with col2:
                        st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Educator at Heart</h5>
                                <p style="font-size:28px;">
                                    Passionate about teaching,
                                    I’ve developed learning programs and mentoring approaches that simplify complex aerospace concepts and make them accessible to all learners.
                                </p>
                            </div>
                        """, unsafe_allow_html=True) 

                    with col3:
                       st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Industry Insight</h5>
                                <p style="font-size:28px;">
                                     My time in the aerospace sector has equipped me with real-world problem-solving skills,
                                     project management experience, and a deep understanding of how innovation translates from idea to implementation.   
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

                    with col4:
                        st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Mentorship and Leadership</h5>
                                <p style="font-size:28px;">
                                    I believe in empowering others and have a track record of guiding students and professionals
                                    to unlock their potential and pursue meaningful careers in aerospace.   
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

        def Education():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("OSB34T.jpg")

            st.markdown("## 🎓 Education")
            st.markdown("""### 🛩 M.Tech in Aerospace Engineering""")
            st.markdown("""
            <div style="
                        background-color: rgba(240, 242, 246, 0.3); 
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                            <li> Specialization: Guided Missiles  
                            <li> 📍 Defence Institute of Advanced Technology (DIAT), Pune 
                            <li> 📅 Pursuing since May 2024
                        </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### ✈️ B.Tech in Aerospace Engineering""")
            st.markdown("""
            <div style="
                        background-color: rgba(240, 242, 246, 0.3); 
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;
                    ">
                        <div style="font-size: 28px;">
                                <li> 📍  Lovely Professional University, Punjab, India  
                                <li> 📅 Completed in 2022
                        </div>
            </div>
            """, unsafe_allow_html=True)

        def Work_Experience():
                # ✅ Function to set background image
                def set_background(image_path):
                        try:
                            base64_str = get_base64(image_path)
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("data:image/png;base64,{base64_str}");
                                    background-size: cover;
                                    background-position: center;
                                    background-attachment: fixed;    
                                }}
                                </style>
                                """,unsafe_allow_html=True)
                                
                        except FileNotFoundError:
                            st.error("Background image not found. Please check the file path.")

                # ✅ Apply background image (Make sure the path is correct)
                set_background("use-this-one.png")

                st.title("Work Experience")

                # Create vertical columns
                cols = st.columns(3)

                # Column 1
                with cols[0]:
                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                    padding: 30px;
                                    border-radius: 15px;
                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                    line-height: 1.8;
                                    color: white;
                                    backdrop-filter: blur(8px);
                                    -webkit-backdrop-filter: blur(8px);
                                    margin-bottom: 28px;">
                            <h5 style="color:#003366;">Orbitx India Aerospace</h5>
                            <p style="font-size:28px;">
                                  Role:Space Tutor Volunteer (Part-Time)<br>
                                  Location: Jaipur, Rajasthan, India<br>
                                  Duration: Mar 2024- Nov 2024<br>
                                <li>Promoted aerospace education through volunteering.
                                <li>Simplified complex concepts for students.
                                <li>Contributed to India’s space awareness journey.
                             </p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("---")

                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                            padding: 30px;
                            border-radius: 15px;
                            border: 1px solid rgba(255, 255, 255, 0.3);
                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                            line-height: 1.8;
                            color: white;
                            backdrop-filter: blur(8px);
                            -webkit-backdrop-filter: blur(8px);
                            margin-bottom: 28px;">
                        <h5 style="color:#003366;">Aharada Education, IIMT University</h5>
                        <p style="font-size:28px;">
                                 Role: Teaching Faculty<br>
                                 Location: Uttar Pradesh, India <br>
                                 Duration: Sept 2022 - Dec 2022 <br>
                                <li>Facilitated interactive sessions for students.
                                <li>Assisted in mastering difficult topics.
                                <li>Supported both students and educators.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                # Column 2
                with cols[1]:
                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                    padding: 30px;
                                    border-radius: 15px;
                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                    line-height: 1.8;
                                    color: white;
                                    backdrop-filter: blur(8px);
                                    -webkit-backdrop-filter: blur(8px);
                                    margin-bottom: 28px;">
                            <h5 style="color:#003366;">School of Aeronautics </h5>
                            <p style="font-size:28px;">
                                    Role:Instructor <br>
                                    Location:Neemrana, Rajasthan, India<br>
                                    Duration:Feb 2024- June 2024<br>
                                    <li>Taught subjects like flight dynamics, navigation.
                                    <li>Combined theory with hands-on learning.
                                    <li>Inspired curiosity in aerospace fields.
                             </p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("---")

                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                    padding: 30px;
                                    border-radius: 15px;
                                    border: 1px solid rgba(255, 255, 255, 0.3);
                                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                    line-height: 1.8;
                                    color: white;
                                    backdrop-filter: blur(8px);
                                    -webkit-backdrop-filter: blur(8px);
                                    margin-bottom: 28px;">
                            <h5 style="color:#003366;">Orbitx India Aerospace</h5>
                            <p style="font-size:28px;">
                                    Role: Researcher <br>
                                    Location: Rajasthan, India<br>
                                    Duration: May 2022- Aug2022<br>
                                    <li>Researched rocket nozzle design and optimization.
                                    <li>Focused on maximizing thrust and efficiency.
                                    <li>Considered thermal and material stress limits.
                             </p>
                    </div>
                    """, unsafe_allow_html=True)

                # Column 3
                with cols[2]:
                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                            padding: 30px;
                            border-radius: 15px;
                            border: 1px solid rgba(255, 255, 255, 0.3);
                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                            line-height: 1.8;
                            color: white;
                            backdrop-filter: blur(8px);
                            -webkit-backdrop-filter: blur(8px);
                            margin-bottom: 28px;">
                        <h5 style="color:#003366;">Indian Institute of Aeronautical Engineering</h5>
                        <p style="font-size:28px;">
                                Role: College Lecturer <br>
                                Location: Dehradun, Uttarakhand, India<br>
                                Duration: Aug 2023 - Oct2023<br>
                                <li>Taught aerodynamics, propulsion, avionics.
                                <li>Guided students academically and professionally.
                                <li>Enhanced curriculum and project quality.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("---")

                    st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                            padding: 30px;
                            border-radius: 15px;
                            border: 1px solid rgba(255, 255, 255, 0.3);
                            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                            line-height: 1.8;
                            color: white;
                            backdrop-filter: blur(8px);
                            -webkit-backdrop-filter: blur(8px);
                            margin-bottom: 28px;">
                        <h5 style="color:#003366;">Orbitx India Aerospace</h5>
                        <p style="font-size:28px;">
                                Role: Mentor <br>
                                Location: Rajasthan, India<br>
                                Duration: Jan 2021- Sept 2022<br>
                                <li>Mentored students in aerospace sciences.
                                <li>Supervised projects and workshops.
                                <li>Promoted practical understanding.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

        def Skill_Set():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("soft-hard-skills.png")
            st.header("Technical Skills")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Simulation & Design</h5>
                                <p style="font-size:35px;">
                                     <li> ANSYS (FEA & CFD)
                                     <li> PTC Creo 
                                     <li> Solidworks
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                        
            with col2:
                 st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Programming & AI</h5>
                                <p style="font-size:35px;">
                                     <li> Python
                                     <li> Web Dev 
                                     <li> HTML, CSS, JS – Beginner
                                     <li> Data Science
                                     <li> SQL
                                     <li> AI Tools & ChatGPT 
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

            with col3:
                st.markdown("""
                            <div style="background-color: rgba(240, 242, 246, 0.3);
                                        padding: 30px;
                                        border-radius: 15px;
                                        border: 1px solid rgba(255, 255, 255, 0.3);
                                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                        line-height: 1.8;
                                        color: black;
                                        backdrop-filter: blur(8px);
                                        -webkit-backdrop-filter: blur(8px);
                                        margin-bottom: 28px;">
                                <h5 style="color:#003366;">Productivity & Design</h5>
                                <p style="font-size:35px;">
                                     <li> MS Office Suite
                                     <li> Canva
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
           
            st.title("Skills Set")
            st.title("Simulation & Design")

            # List of image paths and captions
            images = [
                ("Ptc creo.jpg", "Ptc creo"),
                ("ANSYS.jpg", "ANSYS"),
                
            ]

            # Create 5 columns for horizontal layout
            cols = st.columns(len(images))

            # Display each image in a column
            for col, (img_path, caption) in zip(cols, images):
                image = Image.open(img_path)
                resized_image = image.resize((150, 150))
                col.image(resized_image, caption=caption)


            st.title("Programming & AI")

            # List of image paths and captions
            images = [
                ("Python.png", "Python"),
                ("Data Science Logo.jpg", "Data Science"),  
            ]

            # Create 5 columns for horizontal layout
            cols = st.columns(len(images))

            # Display each image in a column
            for col, (img_path, caption) in zip(cols, images):
                image = Image.open(img_path)
                resized_image = image.resize((150, 150))
                col.image(resized_image, caption=caption)

            st.title("Productivity & Design")

            # List of image paths and captions
            images = [
                ("Office.png", "Office"),
                ("Canva.png", "Canva"),
                
            ]

            # Create 5 columns for horizontal layout
            cols = st.columns(len(images))

            # Display each image in a column
            for col, (img_path, caption) in zip(cols, images):
                image = Image.open(img_path)
                resized_image = image.resize((150, 150))
                col.image(resized_image, caption=caption)    
                
        def  Internship_Certification():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("Abstract-of-web-developer-portfolio-images.jpg")

             # ✅ Features Section
            st.header("Internship")
            col1, col2, col3,col4,col5 = st.columns(5)
            col1, col2, col3, col4,col5 = st.columns(5)

            with col1:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Reusable Launch Vehcile "Atal Yaan" – Orbitx India Aerospace</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Orbitx India Aerospace-Rajasthan,India | 09 Aug 2022<br>
                            <li>worked on the Reusable Launch Vehicle (RLV) project named "Atal Yaan".
                            During this time, I contributed to the vehicle’s preliminary design and analysis,gaining hands-on experience in reusable
                            space systems and enhancing my understanding of launch vehicle technologies.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("Internship 2022.png", caption= "Reusable Launch Vehcile Atal Yaan – Orbitx India Aerospace", width=300) 

            with col2:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Spacecraft Design – Orbitx India Aerospace</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Orbitx India Aerospace-Rajasthan,India | 12 Dec 2021<br>
                            <li>Worked on a spacecraft design project under the mentorship of Orbitx India Aerospace. Contributed to structural layout, subsystem integration,
                            and conceptual modeling. Gained insights into real-world aerospace design challenges and team collaboration in a space-focused startup environment.  
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("Internship 2021_page-0001.jpg", caption="Spacecraft Design – Orbitx India Aerospace", width=300)

            with col3:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">ANSYS (SpaceClaim) Software Training</h5>
                        <p style="font-size:28px;">
                            <li>Issued by NSIC (A Goverment of India Enterprise)-New Delhi,India | 10 Jan 2020<br>
                            <li>Gained hands-on experience in 3D modeling and design using ANSYS SpaceClaim. Learned to create, modify,
                            and prepare geometries for simulation, focusing on aerospace components.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("Space claim.png", caption="ANSYS (SpaceClaim) Software Training", width=300)

            with col4:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">ANSYS (CAE + CFD) Analysis Training</h5>
                        <p style="font-size:28px;">
                             <li>Issued by NSIC (A Goverment of India Enterprise)-New Delhi,India  | 26 July 2019<br>
                             <li>Completed comprehensive training in Computer-Aided Engineering (CAE) and Computational Fluid Dynamics
                             (CFD) using ANSYS Workbench. Acquired skills in structural and fluid simulations, mesh generation,
                             and interpreting simulation results for aerospace applications.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("cfd cae.png", caption="ANSYS (CAE + CFD) Analysis Training", width=300)

            with col5:
               st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Geometric Dimensioning & Tolerancing (GD&T)</h5>
                        <p style="font-size:28px;">
                             <li>Issued by NSIC (A Goverment of India Enterprise)-New Delhi,India  | 28 June 2019<br>
                             <li>Trained in GD&T principles, understanding how to accurately define engineering tolerances
                             and ensure proper fit and function of components. Developed precision in technical drawings and interpretation of manufacturing requirements.    
                        </p>
                    </div>
                """, unsafe_allow_html=True)

               st.image("GD&T.png", caption="Geometric Dimensioning & Tolerancing (GD&T)", width=300)

            st.markdown("---")

            # ✅ Features Section
            st.header("Certification")
            col1, col2, col3,col4, col5  = st.columns(5)
            col1, col2, col3, col4, col5  = st.columns(5)  
          
            with col1:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">HTML, CSS, and JavaScript Certification Course for Beginners</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Udemy | 25 April 2025
                            <li>Developed skills in front-end web development, including building responsive web pages using HTML, CSS, and basic JavaScript.  
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("UC-092bc091-f698-447e-bf4f-ded9e81ad5a5.jpg", caption="HTML, CSS, and JavaScript Certification Course for Beginners", width=300)

            with col2:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Python App Development Master Class: App Development Bootcamp</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Udemy | 28 Mar 2025
                            <li>Completed an in-depth course focused on developing Python-based desktop applications. Gained experience with GUI development using Tkinter.  
                        </p>
                    </div>
                """, unsafe_allow_html=True)

                st.image("UC-f00aecbd-4347-41c3-85d7-286434923096.jpg", caption="Python App Development Master Class: App Development Bootcamp", width=300)

            with col3:
               st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Data Science</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Scaler | 17 Mar 2025
                            <li>Explored core concepts of data science including statistical analysis, machine learning basics, and Python libraries such as Pandas, NumPy, and Matplotlib.    
                        </p>
                    </div>
               """, unsafe_allow_html=True)
               
               st.image("Data Science.jpg", caption="Data Science", width=300)
    
            with col4:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Python and SQL for Data Science</h5>
                        <p style="font-size:28px;">
                                <li>Issued by Scaler | 08 Mar 2025
                                <li>Learned data manipulation and analysis using Python and SQL. Covered data cleaning, querying, and exploratory data analysis techniques.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.image("Python with Data Science.jpg", caption="Python and SQL for Data Science", width=300)

            with col5:
                st.markdown("""
                    <div style="background-color: rgba(240, 242, 246, 0.3);
                                padding: 30px;
                                border-radius: 15px;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                                line-height: 1.8;
                                color: white;
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                margin-bottom: 28px;">
                        <h5 style="color:#003366;">Python Course for Beginners</h5>
                        <p style="font-size:28px;">
                            <li>Issued by Scaler | 25 Feb 2025
                            <li>Gained foundational knowledge of Python programming, including syntax, data structures, and basic scripting.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.image("Python.jpg", caption="Python Course for Beginners", width=300)
         
        def Projects():

            # ✅ Function to set background image
            def set_background(image_path):
                try:
                    base64_str = get_base64(image_path)
                    st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url("data:image/png;base64,{base64_str}");
                            background-size: cover;
                            background-position: center;
                            background-attachment: fixed;    
                        }}
                        </style>
                        """,unsafe_allow_html=True)
                        
                except FileNotFoundError:
                    st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("photo-1572177812156-58036aae439c.jpeg")
            st.header("Projects")
            # Font size dropdown
            font_size = st.selectbox(
                "Select Text Size",
                options=["Small", "Medium", "Large"],
                index=1
            )

            # Font size mapping
            font_map = {
                "Small": "15px",
                "Medium": "20px",
                "Large": "25px"
            }
            selected_font_size = font_map[font_size]

            # Glass box styling function
            def glass_box(content):
                return f"""
                <div style="
                    background-color: rgba(240, 242, 246, 0.2); 
                    padding: 25px;
                    border-radius: 15px;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    line-height: 1.7;
                    color: white;
                    font-size: {selected_font_size};
                    backdrop-filter: blur(10px);
                    -webkit-backdrop-filter: blur(10px);
                    margin-bottom: 20px;
                ">
                    {content}
                </div>
                """
            
            st.markdown("## 🏅 Patent Published")
            # Appreciation Projects
            appreciation_projects = [
                {
                    "title": "A NOVEL DESIGN FOR SLANT BACK TAIL GENERATION AIRCRAFT",
                    "date": "Published in 2022",
                    "Application Number":"202211013218A"
                }
            ]

            # Display Appreciation Projects in Glass Boxes
            for proj in appreciation_projects:
                html_proj = f"""
                <b>🔸 {proj['title']}</b><br>
                📅 <i>{proj['date']}</i><br>
                📝 {proj['Application Number']}
                """
                st.markdown(glass_box(html_proj), unsafe_allow_html=True)
              
            st.image("Patent.png", caption="A NOVEL DESIGN FOR SLANT BACK TAIL GENERATION AIRCRAFT", width=300) 
          
            st.markdown("## 🏅 Appreciation Certificates")
            # Appreciation Projects
            appreciation_projects = [
                {
                    "title": "Appreciation Certificate - Orbitx India Aerospace",
                    "date": "Jan 2020",
                    "desc": "Recognized for contributions to the Reusable Launch Vehicle (RLV) Project."
                }
            ]

            # Display Appreciation Projects in Glass Boxes
            for proj in appreciation_projects:
                html_proj = f"""
                <b>🔸 {proj['title']}</b><br>
                📅 <i>{proj['date']}</i><br>
                📝 {proj['desc']}
                """
                st.markdown(glass_box(html_proj), unsafe_allow_html=True)
            
            st.image("RLV Rocket Design Project.png", caption="RLV Rocket Design Project", width=300)
          
            st.markdown("## 🏎️ Mechanical Projects")

            # Mechanical Engineering Projects
            mechanical_projects = [
                {
                    "title": "Mechanical Project – Go Kart",
                    "date": "Jan 2020",
                    "desc": "Hands-on experience in automotive engineering through team-based Go Kart build."
                }
            ]

            # Display Mechanical Projects in Glass Boxes
            for proj in mechanical_projects:
                html_proj = f"""
                <b>🔸 {proj['title']}</b><br>
                📅 <i>{proj['date']}</i><br>
                📝 {proj['desc']}
                """
                st.markdown(glass_box(html_proj), unsafe_allow_html=True)
            st.image("Go Kart.png", caption="Go Kart", width=300)
            st.markdown("## 💻 Programming Projects")

            # Programming Projects
            programming_projects = [
                {
                    "title": "Aerospace Web Page (Self)",
                    "date": "April 2025",
                    "desc": "Created an educational web platform for aerospace enthusiasts and learners."
                },
                {
                    "title": "Aerodynamic Parameter Calculator (Self)",
                    "date": "Feb 2025",
                    "desc": "Tool for computing key aerodynamic values like CL, CD, and Reynolds number."
                },
                {
                    "title": "Solid Rocket Motor Design & Analysis (Self)",
                    "date": "Feb 2025",
                    "desc": "Design and analytical modeling of SRMs including thrust-time profiling."
                },
                {
                    "title": "Low Subsonic Wind Tunnel Design (Self)",
                    "date": "Mar 2025",
                    "desc": "Designed a subsonic wind tunnel layout for small-scale aerodynamic testing."
                },
                {
                    "title": "Aerofoil Generator App (Self)",
                    "date": "Mar 2025",
                    "desc": "Python-based GUI app for generating NACA airfoils and exporting coordinates."
                },
                {
                    "title": "Fuel-Powered UAV Design Calculator (Self)",
                    "date": "Mar 2025",
                    "desc": "Tool to estimate performance parameters for gas-powered UAV systems."
                },
                {
                    "title": "Jet Engine Performance Estimator (Self)",
                    "date": "Mar 2025",
                    "desc": "Simulator to analyze key metrics like thrust, SFC, and efficiency across engine types."
                },
                {
                    "title": "Battery-Powered UAV Performance Evaluation (Self)",
                    "date": "May 2024",
                    "desc": "Python-based evaluator for mission planning and performance benchmarking of electric UAVs."
                }
            ]

            # Display Programming Projects in Glass Boxes
            for proj in programming_projects:
                html_proj = f"""
                <b>🔸 {proj['title']}</b><br>
                📅 <i>{proj['date']}</i><br>
                📝 {proj['desc']}
                """
                st.markdown(glass_box(html_proj), unsafe_allow_html=True)
              
            st.image("My Programming Project.png", caption="My Programming Project", width=800)
          
        def Conferance_Research_Publication():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("educational-light-bulb-qz50uzn6nrhc6pmv.jpg")
            
            st.header("📚 Conferences & Research Publications")
          
            # Font size dropdown
            font_size = st.selectbox(
                "Select Text Size",
                options=["Small", "Medium", "Large"],
                index=1
            )

            # Font size mapping
            font_map = {
                "Small": "15px",
                "Medium": "20px",
                "Large": "25px"
            }
            selected_font_size = font_map[font_size]

            # Glass box styling function
            def glass_box(content):
                return f"""
                <div style="
                    background-color: rgba(240, 242, 246, 0.2); 
                    padding: 25px;
                    border-radius: 15px;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    line-height: 1.7;
                    color: black;
                    font-size: {selected_font_size};
                    backdrop-filter: blur(10px);
                    -webkit-backdrop-filter: blur(10px);
                    margin-bottom: 20px;
                ">
                    {content}
                </div>
                """

            # 📌 Conference data
            conference_items = [
                {
                    "title": "Global Conference on Aeronautical, Aerospace and Mechanical Sciences",
                    "date": "May 2024",
                    "desc": "Python-Based Evaluation of Aircraft Performance Parameters for Battery-Powered UAV Design."
                            "Presented a Python tool for estimating endurance, range, and thrust needs in UAVs.",
                    "image": "Conference2.png",  # Add image path in data
                    "caption": "Global Conference on Aeronautical, Aerospace and Mechanical Sciences"
                },
                {
                    "title": "International Conference on Emerging Approaches in Mechanical & Automobile Engineering",
                    "date": "May 2024",
                    "desc": "A Comparative Study on Effect of Area Ratio and Nozzle Pressure Ratio (NPR) for CD Nozzle – Review. "
                            "Focused on propulsion analysis in supersonic nozzle configurations.",
                    "image": "Conference1.png",
                    "caption": "International Conference on Emerging Approaches in Mechanical & Automobile Engineering"
                }
            ]

            # 🎤 Conferences Section
            st.subheader("🎤 Conferences")
            for item in conference_items:
                html = f"""
                <b>🔹 {item['title']}</b><br>
                📅 <i>{item['date']}</i><br>
                📝 {item['desc']}
                """
                st.markdown(glass_box(html), unsafe_allow_html=True)

                # Only show image if available
                if item["image"]:
                    st.image(item["image"], caption=item["caption"], width=300)


                # 📝 Research paper data
            research_items = [
                {
                    "title": "Journal of Emerging Technologies and Innovative Research",
                    "date": "March 2024",
                    "desc": "Python Programming in the Aerospace Industry. "
                            "Explored automation, simulation, and design tools using Python in aerospace workflows.",
                    "link": "https://www.ijaresm.com/python-programming-in-the-aerospace-industry"
                },
                {
                    "title": "International Journal of All Research Education & Scientific Methods",
                    "date": "Feb 2024",
                    "desc": "Review Paper on CFD Analysis of Different NACA Airfoil Series. "
                            "Compared pressure and lift behavior of various NACA airfoils using CFD tools.",
                    "link": "https://www.jetir.org/papers/JETIR2403948.pdf"
                },
                {
                    "title": "International Journal of Creative Research Thoughts",
                    "date": "Sept 2023",
                    "desc": "Case Studies in Missile Design Failures by CFD Simulation. "
                            "Analyzed real-world failures and design improvements using CFD analysis.",
                    "link": "http://www.ijcrt.org/papers/IJCRT2308632.pdf"
                },
                {
                    "title": "International Journal of Research and Analytical Reviews",
                    "date": "Nov 2022",
                    "desc": "Wind Tunnel Design. "
                            "Outlined layout and principles behind a subsonic wind tunnel setup.",
                    "link": "http://www.ijrar.org/papers/IJRAR22D2210.pdf"
                },
                {
                    "title": "International Research Journal of Engineering and Technology",
                    "date": "Dec 2020",
                    "desc": "Effect of Pressure Coefficient on Missile Design. "
                            "Studied the aerodynamic impact of pressure coefficient variation on missile stability.",
                    "link": "https://www.irjet.net/archives/V7/i12/IRJET-V7I12410.pdf"
                },
                {
                    "title": "International Journal of Scientific Development and Research",
                    "date": "Oct 2020",
                    "desc": "Flow Variation Over Bi-Conic Nose Profile at Different Angle of Attack. "
                            "Examined drag on biconic shapes under varied angles.",
                    "link": "https://www.ijsdr.org/papers/IJSDR2009033.pdf"
                },
                {
                    "title": "International Journal of Scientific Development and Research",
                    "date": "Sept 2020 / Mar 2021",
                    "desc": "Aerodynamic Analysis on Missile Design. "
                            "Focused on fin configurations and nose designs through CFD modeling.",
                    "link": "https://www.ijsdr.org/papers/IJSDR2010034.pdf"
                }
            ]

            # 📖 Research Papers Section
            st.subheader("📖 Research Papers")
            for item in research_items:
                html = f"""
                <b>🔹 <a href="{item['link']}" target="_blank" style="text-decoration: none; color: #1f77b4;">{item['title']}</a></b><br>
                📅 <i>{item['date']}</i><br>
                📝 {item['desc']}
                """
                st.markdown(glass_box(html), unsafe_allow_html=True)
                
        def Educational_Activity():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("education-open-book-blackboard-24neqyjtkzc2rc21.jpg")

            st.markdown("## 📚 Educational Activities")
            
            # Activity 1: Akiic 
            st.markdown("""
            <div style="background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;">
                <h5 style="color:#003366;">Dr. A.P.J. Abdul Kalam Ideation and Innovation Challenge 2025</h5>
                <p style="font-size:28px;">
                        Topic: Guided Missile Design<br>
                        Role: Participant<br>
                        📅 21st Feb 2025<br>
                        Organizer: DIAT-IIC in collaboration with DIAT-SCEC<br> 
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Adjust image size (width: 600px, height: 400px)
            st.image("Screenshot (51).png", caption="Dr. A.P.J. Abdul Kalam Ideation and Innovation Challenge 2025", width=600)

            # Activity 1: Workshop
            st.markdown("""
            <div style="background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;">
                <h5 style="color:#003366;">Webinar Participation</h5>
                <p style="font-size:28px;">
                        Topic: Data Science using Gen AI & Python<br>
                        Role: Participant<br>
                        📅 April 2025<br>
                        Organizer: Scaler<br> 
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Adjust image size (width: 600px, height: 400px)
            st.image("9b69e3c1fa41dbf8a24931137d6dc0c037330b613191fcc227e86ef8e90a63a7.png", caption="Data Science using Gen AI & Python", width=600)

            st.markdown("---")
             
            # Activity 2: Workshop
            st.markdown("""
            <div style="background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;">
                <h5 style="color:#003366;">Webinar Participation</h5>
                <p style="font-size:28px;">
                        Topic: Data Science vs Machine Learning vs Artifical Intelligence<br>
                        Role: Participant<br>
                        📅 March 2025<br>
                        Organizer: Scaler<br> 
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Adjust image size (width: 600px, height: 400px)
            st.image("IMG_1741498105542.jpg", caption="Data Science vs Machine Learning vs Artifical Intelligence", width=600)

            st.markdown("---")
            
            # Activity 3: Workshop
            st.markdown("""
            <div style="background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;">
                <h5 style="color:#003366;">🧠 Idea Generation Workshop</h5>
                <p style="font-size:28px;">
                        Topic: Prototype / Process Design & Development of Drones<br>
                        Role: Speaker<br>
                        📅 May 2023<br>
                        Organizer:  Aharada Education<br> 
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Adjust image size (width: 600px, height: 400px)
            st.image("WhatsApp Image 2024-02-01 at 05.15.42.jpeg", caption="Speaking at the Drone Design Workshop – May 2023", width=600)

            st.markdown("---")

            # Activity 4: Educational Tour
            st.markdown("""
            <div style="background-color: rgba(240, 242, 246, 0.3);
                        padding: 30px;
                        border-radius: 15px;
                        border: 1px solid rgba(255, 255, 255, 0.3);
                        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                        line-height: 1.8;
                        color: white;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        margin-bottom: 28px;">
                <h5 style="color:#003366;">✈️ Educational Tour</h5>
                <p style="font-size:28px;">
                        Location: Indian Air Force Museum- New Delhi<br>
                        Role: Instructor<br>
                        📅 Feb 2023<br>
                        Organizer: Aharada Education<br> 
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Adjust image size (width: 600px, height: 400px)
            st.image("IMG_20230204141459.jpg", caption="Visit to the Indian Air Force Museum – Feb 2023", width=600)

        def Contact_Details():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("glowing-contact-us-logo-qx58564q7a51etk6.jpg")
            # ✅ Contact & Social Media
            st.header("Get in Touch")
            st.write("📍 Location: New Delhi")
            st.write("📧 Email: amandeepoct97@gmail.com")
            st.write("📞 Contact: +91-9211910555")
            st.write("🌐 Website: [https://amandeepsinghportfolio.streamlit.app/](#)")
            
            # ✅ Social Media Links
            st.header("Connect with Me")
            st.markdown("""
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/amandeep-singh-ae?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) 
            """)

        def  Resume_pdf_Download():
            # ✅ Function to set background image
            def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,unsafe_allow_html=True)
                            
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")

            # ✅ Apply background image (Make sure the path is correct)
            set_background("shutterstock_1046852695-Converted.jpg")
            
            st.title("📄 Resume PDF")

            PDF_SAVE_PATH = "Amandeep Singh Resume 2025.pdf"
          
            # --- Developer Options ---
            with st.expander("⚙️ Developer Login"):
                password = st.text_input("Enter developer password", type="password")
                is_developer = password == "your_secret_password"  # 🔑 Change this to your password
            
            if is_developer:
                st.success("Developer access granted.")
            
                # Upload option only for developer
                uploaded_file = st.file_uploader("Upload a PDF file (Developer only)", type="pdf")
            
                if uploaded_file is not None:
                    with open(PDF_SAVE_PATH, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    st.success("PDF uploaded and saved successfully.")
            
                # Delete option
                if st.button("🗑️ Delete PDF File"):
                    if os.path.exists(PDF_SAVE_PATH):
                        os.remove(PDF_SAVE_PATH)
                        st.success("PDF file deleted successfully.")
                    else:
                        st.warning("No PDF file to delete.")
            
            # --- Download Section ---
            st.subheader("⬇️ Download Resume PDF")
            if os.path.exists(PDF_SAVE_PATH):
                with open(PDF_SAVE_PATH, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                    href = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="Resume.pdf">📥 Click here to download the resume</a>'
                    st.markdown(href, unsafe_allow_html=True)
            else:
                st.info("No resume available for download. Please contact the developer.")
          
        # --- Setup Session State ---
        if 'page' not in st.session_state:
            st.session_state.page = 'Home'

        # --- CSS Hover Style ---
        st.markdown("""
            <style>
            .nav-link {
                display: block;
                padding: 12px;
                margin-bottom: 8px;
                background-color: #1f77b4;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                text-align: center;
                transition: 0.3s;
            }
            .nav-link:hover {
                background-color: #4fa3d1;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)

        # --- Sidebar Navigation ---
        st.sidebar.markdown("## 🚀 My Resume")

        nav_links = {
            "Home": "Home",
            "Education": "Education",
            "Work Experience":"Work Experience",
            "Skill Set":"Skill Set",
            "Internship & Certification":"Internship & Certification",
            "Projects":"Projects",
            "Conferance & Research Publication":"Conferance & Research Publication",
            "Educational Activity":"Educational Activity",
            "Contact Details":"Contact Details",
            "Resume pdf Download": "Resume pdf Download",
            "Logout":"Logout"
           
            
        }

        for key, label in nav_links.items():
            if st.sidebar.button(label):
                st.session_state.page = key

        if st.session_state.page == "Home":
                 st.balloons()
                 Home()
                    
        elif st.session_state.page == "Education":
               Education()

        elif st.session_state.page == "Work Experience":
              Work_Experience()

        elif st.session_state.page == "Skill Set":
              Skill_Set()
              
        elif st.session_state.page == "Internship & Certification":  
             Internship_Certification()
              
        elif st.session_state.page == "Projects":  
               Projects()

        elif st.session_state.page == "Conferance & Research Publication":  
               Conferance_Research_Publication()       
           
        elif st.session_state.page == "Educational Activity":
              Educational_Activity()
            
        elif st.session_state.page == "Contact Details":
                Contact_Details()
                
        elif st.session_state.page == "Resume pdf Download":
                Resume_pdf_Download()

        # 👇 Logout button logic
        elif st.session_state.page =="Logout":
                 def get_base64(image_path):
                                    with open(image_path, "rb") as img_file:
                                        return base64.b64encode(img_file.read()).decode()

                 def set_background(image_path):
                    try:
                        base64_str = get_base64(image_path)
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{base64_str}");
                                background-size: 95% 95%;
                                background-position: center;
                                background-attachment: fixed;    
                            }}
                            </style>
                            """,
                            unsafe_allow_html=True
                        )
                    except FileNotFoundError:
                        st.error("Background image not found. Please check the file path.")
                 set_background("10.jpg")

                 if st.button("Logout", key="logout_button"):
                            st.session_state.logged_in = False
                            st.session_state.username = ""

# ---------- LOGOUT FUNCTION ----------
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---------- MAIN ----------
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        welcome_page()
    else:
        login_page()

# Run the app
main()
