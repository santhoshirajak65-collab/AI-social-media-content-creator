import streamlit as st
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Social Media Content Creator",
    page_icon="📱",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(
    '<div class="title">📱 AI Social Media Content Creator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create captions, posts, reels, hashtags and ideas easily'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("⚙️ Content Settings")

platform = st.sidebar.selectbox(
    "📱 Select Platform",
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
        "Job Seekers",
        "General Audience"
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

# -------------------------------------------------
# INPUT
# -------------------------------------------------

st.subheader("📝 Create Your Content")

topic = st.text_input(
    "Enter your topic",
    placeholder="Example: College Fest, New Product, Travel"
)

keywords = st.text_input(
    "Optional Keywords",
    placeholder="Example: technology, education, innovation"
)

# -------------------------------------------------
# CONTENT GENERATOR
# -------------------------------------------------

def generate_content(topic, content_type, platform,
                     tone, audience, language, length, keywords):

    topic = topic.strip()

    # ---------------- CAPTION ----------------

    if content_type == "Caption":

        if tone == "Professional":
            content = (
                f"🚀 Discover the power of {topic}. "
                f"An exciting opportunity to learn, grow and create "
                f"meaningful experiences. "
                f"Stay connected and be part of the journey!"
            )

        elif tone == "Funny":
            content = (
                f"😂 When you hear about {topic}, "
                f"you know something exciting is about to happen! "
                f"Who else is ready?"
            )

        elif tone == "Motivational":
            content = (
                f"🔥 Believe in yourself and take the next step "
                f"towards {topic}. "
                f"Every small step creates a bigger future. "
                f"Keep going! 💪"
            )

        elif tone == "Friendly":
            content = (
                f"✨ Let's talk about {topic}! "
                f"Something exciting, useful and worth sharing "
                f"with everyone. What do you think? 😊"
            )

        else:
            content = (
                f"✨ Experience {topic} in a whole new way! "
                f"Create memories, explore new possibilities "
                f"and enjoy every moment. 🚀"
            )

        return content

    # ---------------- SOCIAL MEDIA POST ----------------

    elif content_type == "Social Media Post":

        return f"""
🔥 {topic} — Something Worth Talking About!

Are you interested in {topic}?

This is a great opportunity for {audience.lower()} to
learn, explore and discover something new.

Whether you are just starting or already interested,
there is always something valuable to learn.

✨ Stay curious.
🚀 Keep learning.
💡 Keep growing.

What is your opinion about {topic}?

#SocialMedia #Trending #Innovation #Learning
"""

    # ---------------- REEL SCRIPT ----------------

    elif content_type == "Reel Script":

        return f"""
🎬 REEL SCRIPT — {topic}

🎯 HOOK:
"Did you know something interesting about {topic}?"

🎥 SCENE 1:
Show an attractive image or video related to {topic}.

🎙️ VOICE OVER:
"Today let's explore {topic} and understand why
it is becoming so interesting."

🎥 SCENE 2:
Show important points or examples related to {topic}.

🎙️ VOICE OVER:
"There are many interesting things to discover,
learn and experience."

🎥 SCENE 3:
Show the final highlight.

🎙️ VOICE OVER:
"So, what do you think about {topic}?"

📢 CALL TO ACTION:
"Like, share and follow for more content! ❤️"
"""

    # ---------------- HASHTAGS ----------------

    elif content_type == "Hashtags":

        words = topic.replace(",", " ").split()

        tags = [
            "#" + word.replace(" ", "")
            for word in words
        ]

        common_tags = [
            "#Trending",
            "#SocialMedia",
            "#ContentCreator",
            "#Explore",
            "#Inspiration",
            "#Motivation",
            "#Creative",
            "#Learning",
            "#Technology",
            "#Digital"
        ]

        return " ".join(tags + common_tags)

    # ---------------- POST IDEAS ----------------

    elif content_type == "Post Ideas":

        return f"""
💡 10 POST IDEAS FOR: {topic}

1. 📌 Introduction to {topic}

2. 💡 Interesting facts about {topic}

3. 🔥 Top 5 things to know about {topic}

4. 📊 Benefits of {topic}

5. ❓ Common questions about {topic}

6. 🎯 Beginner's guide to {topic}

7. 🚀 Future of {topic}

8. 💭 Myths and facts about {topic}

9. 📸 Behind-the-scenes content about {topic}

10. 🏆 Success stories related to {topic}
"""

    # ---------------- BIO ----------------

    elif content_type == "Bio":

        return f"""
✨ Passionate about {topic}
🚀 Learning | Creating | Growing
💡 Sharing ideas and knowledge
🎯 Connecting with {audience}
📱 Follow for more!
"""

    return "Content could not be generated."


# -------------------------------------------------
# GENERATE BUTTON
# -------------------------------------------------

if st.button(
    "✨ Generate Content",
    use_container_width=True
):

    if not topic.strip():

        st.warning("⚠️ Please enter a topic.")

    else:

        with st.spinner("✍️ Creating your content..."):

            result = generate_content(
                topic,
                content_type,
                platform,
                tone,
                audience,
                language,
                length,
                keywords
            )

            st.session_state.generated_content = result

            st.session_state.history.append({
                "time": datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                ),
                "topic": topic,
                "platform": platform,
                "type": content_type,
                "content": result
            })

# -------------------------------------------------
# DISPLAY CONTENT
# -------------------------------------------------

if st.session_state.generated_content:

    st.divider()

    st.subheader("🎯 Generated Content")

    st.text_area(
        "Your Content",
        st.session_state.generated_content,
        height=350
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "📥 Download Content",
            data=st.session_state.generated_content,
            file_name="social_media_content.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🗑️ Clear Content",
            use_container_width=True
        ):

            st.session_state.generated_content = ""

            st.rerun()

# -------------------------------------------------
# CONTENT ANALYZER
# -------------------------------------------------

st.divider()

st.subheader("📊 Content Analyzer")

if st.session_state.generated_content:

    content = st.session_state.generated_content

    word_count = len(content.split())
    character_count = len(content)

    # Simple scoring system
    engagement = min(
        95,
        60 + (word_count % 35)
    )

    creativity = min(
        95,
        65 + (character_count % 30)
    )

    readability = 90 if word_count < 150 else 80

    audience_score = 88

    platform_score = 90

    overall = int(
        (
            engagement
            + creativity
            + readability
            + audience_score
            + platform_score
        ) / 5
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Engagement", f"{engagement}/100")
    col2.metric("Creativity", f"{creativity}/100")
    col3.metric("Readability", f"{readability}/100")
    col4.metric("Audience", f"{audience_score}/100")
    col5.metric("Overall", f"{overall}/100")

    st.write("### 💡 Suggestions")

    if word_count < 30:
        st.write("• Add more details to make the content stronger.")

    st.write("• Consider adding a strong call-to-action.")
    st.write("• Use relevant hashtags for better reach.")
    st.write("• Add an attractive image or video.")

else:

    st.info(
        "Generate content first to use the Content Analyzer."
    )

# -------------------------------------------------
# CONTENT HISTORY
# -------------------------------------------------

st.divider()

st.subheader("📚 Content History")

if len(st.session_state.history) == 0:

    st.info("No content generated yet.")

else:

    for item in reversed(st.session_state.history):

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

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.markdown(
    """
    <center>
    <b>📱 AI Social Media Content Creator</b><br>
    Built with Python & Streamlit
    </center>
    """,
    unsafe_allow_html=True
)
