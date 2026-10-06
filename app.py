import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# ---------------------------------------------------------
# LOAD API KEY
# ---------------------------------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Social Media Content Creator",
    page_icon="✨",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff, #eef2ff);
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #4f46e5;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555555;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        color: #3730a3;
        font-size: 22px;
        font-weight: 700;
        margin-top: 15px;
    }

    /* Info card */
    .info-card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    /* Output card */
    .output-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #4f46e5;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-size: 17px;
        font-weight: 700;
        background-color: #4f46e5;
        color: white;
        border: none;
    }

    .stButton > button:hover {
        background-color: #3730a3;
        color: white;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">✨ AI Social Media Content Creator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create engaging social media content quickly using Artificial Intelligence</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# CHECK API KEY
# ---------------------------------------------------------
if not API_KEY:
    st.error("⚠️ Gemini API key not found.")

    st.info(
        "Please add your API key in the .env file as:\n\n"
        "GEMINI_API_KEY=your_api_key_here"
    )

    st.stop()

# ---------------------------------------------------------
# GEMINI CLIENT
# ---------------------------------------------------------
client = genai.Client(api_key=API_KEY)

# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------
st.markdown(
    '<div class="section-title">📝 Create Your Content</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="info-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    platform = st.selectbox(
        "📱 Select Platform",
        [
            "Instagram",
            "Facebook",
            "LinkedIn",
            "Twitter / X",
            "YouTube"
        ]
    )

    content_type = st.selectbox(
        "📌 Content Type",
        [
            "Post Caption",
            "Short Post",
            "Advertisement",
            "Product Promotion",
            "Educational Content",
            "Motivational Content",
            "Reel / Video Caption"
        ]
    )

with col2:

    tone = st.selectbox(
        "🎨 Select Tone",
        [
            "Professional",
            "Friendly",
            "Creative",
            "Funny",
            "Inspirational",
            "Educational",
            "Trendy"
        ]
    )

    language = st.selectbox(
        "🌐 Language",
        [
            "English",
            "Telugu",
            "Hindi"
        ]
    )

topic = st.text_area(
    "💡 Enter your topic or idea",
    placeholder="Example: Create an Instagram post about the importance of learning Python...",
    height=120
)

additional_details = st.text_input(
    "✨ Additional details (optional)",
    placeholder="Example: Include emojis, call-to-action, and hashtags"
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------------
generate = st.button("🚀 Generate Content")

# ---------------------------------------------------------
# AI GENERATION
# ---------------------------------------------------------
if generate:

    if not topic.strip():
        st.warning("⚠️ Please enter a topic or idea first.")

    else:

        prompt = f"""
You are a professional social media content creator.

Create high-quality social media content using the following details:

Platform: {platform}
Content Type: {content_type}
Tone: {tone}
Language: {language}
Topic: {topic}

Additional Requirements:
{additional_details}

Instructions:

1. Create an attractive and engaging title if appropriate.
2. Write clear and easy-to-understand content.
3. Match the selected social media platform.
4. Match the requested tone.
5. Use suitable emojis where appropriate.
6. Include a strong Call-To-Action when suitable.
7. Add 5-10 relevant hashtags.
8. Avoid unnecessary repetition.
9. Make the content ready to copy and publish.
10. Keep the content professional and engaging.

Return only the final social media content.
"""

        try:

            with st.spinner("✨ Creating your content..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            generated_content = response.text

            # -------------------------------------------------
            # OUTPUT
            # -------------------------------------------------
            st.markdown(
                '<div class="section-title">✨ Generated Content</div>',
                unsafe_allow_html=True
            )

            st.markdown('<div class="output-card">', unsafe_allow_html=True)

            st.markdown(generated_content)

            st.markdown('</div>', unsafe_allow_html=True)

            # -------------------------------------------------
            # COPYABLE OUTPUT
            # -------------------------------------------------
            st.markdown("### 📋 Copy Your Content")

            st.code(
                generated_content,
                language="text"
            )

            # -------------------------------------------------
            # SUCCESS MESSAGE
            # -------------------------------------------------
            try:

    with st.spinner("✨ Creating your content..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    generated_content = response.text

    st.markdown("### ✨ Generated Content")
    st.write(generated_content)

except Exception as e:
    st.exception(e)
# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#666;">
        ✨ AI Social Media Content Creator |
        Powered by Gemini AI
    </div>
    """,
    unsafe_allow_html=True
)
