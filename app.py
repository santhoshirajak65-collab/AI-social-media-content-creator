import streamlit as st
import ollama
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Social Media Content Creator",
    page_icon="📱",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">📱 AI Social Media Content Creator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create captions, posts, reels, hashtags and ideas using AI 🤖</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Content Settings")

platform = st.sidebar.selectbox(
    "📱 Platform",
    [
        "Instagram",
        "LinkedIn",
        "Facebook",
        "Twitter/X"
    ]
)

content_type = st.sidebar.selectbox(
    "✍️ Content Type",
    [
        "Caption",
        "Social Media Post",
        "Reel Script",
        "Hashtags",
        "Post Ideas",
        "Bio"
    ]
)

tone = st.sidebar.selectbox(
    "🎨 Tone",
    [
        "Professional",
        "Friendly",
        "Funny",
        "Creative",
        "Motivational",
        "Inspirational"
    ]
)

language = st.sidebar.selectbox(
    "🌐 Language",
    [
        "English",
        "Telugu",
        "Hindi"
    ]
)

audience = st.sidebar.selectbox(
    "🎯 Target Audience",
    [
        "Students",
        "Professionals",
        "Business Owners",
        "Content Creators",
        "General Audience",
        "Job Seekers"
    ]
)

length = st.sidebar.selectbox(
    "📏 Content Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "💡 Powered by Ollama + Llama 3.2"
)

# --------------------------------------------------
# MAIN INPUT
# --------------------------------------------------

st.subheader("📝 Create Your Content")

topic = st.text_input(
    "Enter your topic",
    placeholder="Example: College Fest, New Product, Travel, Education"
)

keywords = st.text_input(
    "Optional keywords",
    placeholder="Example: technology, students, innovation"
)

# --------------------------------------------------
# GENERATE FUNCTION
# --------------------------------------------------

def generate_content():

    prompt = f"""
You are an expert AI Social Media Content Creator.

Create content using the following information:

Topic: {topic}
Platform: {platform}
Content Type: {content_type}
Tone: {tone}
Language: {language}
Target Audience: {audience}
Content Length: {length}
Keywords: {keywords}

Follow these instructions:

1. Create high-quality and engaging content.
2. Make the content suitable for the selected platform.
3. Use the selected language.
4. Use emojis where appropriate.
5. Avoid unnecessary explanations.
6. Make the opening sentence attractive.
7. Include a call-to-action when appropriate.

Content type instructions:

If the content type is Caption:
Create an attractive social media caption.

If the content type is Social Media Post:
Create a complete social media post with:
- Hook
- Main content
- Call-to-action

If the content type is Reel Script:
Create a short video script containing:
- Hook
- Scene/Action
- Dialogue or Voice-over
- Ending
- Call-to-action

If the content type is Hashtags:
Generate 15 relevant hashtags.

If the content type is Post Ideas:
Generate 10 creative post ideas.

If the content type is Bio:
Create a short and attractive social media bio.
"""

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"ERROR: {str(e)}"


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

if st.button(
    "✨ Generate AI Content",
    use_container_width=True
):

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic.")

    else:

        with st.spinner("🤖 AI is creating your content..."):

            result = generate_content()

            st.session_state.generated_content = result

            # Save history
            st.session_state.history.append(
                {
                    "time": datetime.now().strftime(
                        "%d-%m-%Y %H:%M"
                    ),
                    "topic": topic,
                    "platform": platform,
                    "type": content_type,
                    "content": result
                }
            )

# --------------------------------------------------
# DISPLAY GENERATED CONTENT
# --------------------------------------------------

if st.session_state.generated_content:

    st.divider()

    st.subheader("🎯 AI Generated Content")

    st.text_area(
        "Generated Content",
        st.session_state.generated_content,
        height=350
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(
            "📥 Download",
            data=st.session_state.generated_content,
            file_name="social_media_content.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🔄 Generate Again",
            use_container_width=True
        ):

            with st.spinner("Generating new content..."):

                result = generate_content()

                st.session_state.generated_content = result

                st.rerun()

    with col3:

        if st.button(
            "🗑️ Clear",
            use_container_width=True
        ):

            st.session_state.generated_content = ""

            st.rerun()

# --------------------------------------------------
# CONTENT ANALYZER
# --------------------------------------------------

st.divider()

st.subheader("📊 AI Content Analyzer")

if st.session_state.generated_content:

    if st.button(
        "🔍 Analyze Content",
        use_container_width=True
    ):

        analysis_prompt = f"""
Analyze the following social media content.

Content:
{st.session_state.generated_content}

Give scores from 1 to 100 for:

1. Engagement
2. Creativity
3. Readability
4. Audience Appeal
5. Platform Suitability

Then calculate an Overall Score.

Finally provide 3 suggestions for improvement.

Use this format:

Engagement: XX/100
Creativity: XX/100
Readability: XX/100
Audience Appeal: XX/100
Platform Suitability: XX/100
Overall Score: XX/100

Suggestions:
1.
2.
3.
"""

        try:

            with st.spinner("🔍 Analyzing content..."):

                analysis = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": analysis_prompt
                        }
                    ]
                )

                analysis_result = analysis[
                    "message"
                ]["content"]

                st.text_area(
                    "📈 Analysis Result",
                    analysis_result,
                    height=300
                )

        except Exception as e:

            st.error(
                "Unable to analyze content."
            )

            st.write(e)

else:

    st.info(
        "Generate some content first to use the Content Analyzer."
    )

# --------------------------------------------------
# CONTENT HISTORY
# --------------------------------------------------

st.divider()

st.subheader("📚 Content History")

if len(st.session_state.history) == 0:

    st.info(
        "No content generated yet."
    )

else:

    for index, item in enumerate(
        reversed(st.session_state.history)
    ):

        with st.expander(
            f"📌 {item['topic']} | "
            f"{item['platform']} | "
            f"{item['time']}"
        ):

            st.write(
                "**Content Type:**",
                item["type"]
            )

            st.write(
                item["content"]
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <center>
    <b>📱 AI Social Media Content Creator</b><br>
    Built with Python, Streamlit and Ollama 🤖
    </center>
    """,
    unsafe_allow_html=True
)
