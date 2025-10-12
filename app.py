import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Set page configuration
st.set_page_config(
    page_title="My Gaming AI assistant",
    page_icon="🎮",
    layout="centered"
)

# Add custom CSS for gaming theme
st.markdown("""
    <style>
    .main {
        background-color: #0a0e27;
    }
    .stTextInput > div > div > input {
        background-color: #1a1f3a;
        color: #00ff88;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title("🎮 My Gaming AI assistant")

# Welcome message
st.markdown("""
### 👋 Welcome to Your Gaming AI assistant!

I'm your personal gaming companion, here to help you with:
- 🎯 **Game Recommendations** - Find your next favorite game
- 🛠️ **Hardware Advice** - Choose the best gaming gear
- 📊 **Strategy Tips** - Level up your gameplay
- 🏆 **Esports Insights** - Stay updated on competitive gaming
- 💬 **General Gaming Chat** - Discuss anything gaming-related!

Choose your preferred personality from the sidebar and let's chat! 🚀
---
""")

# Define personality system prompts
personality_prompts = {
    "😊 Friendly": """You are a warm and friendly gaming AI assistant. You are knowledgeable about video games, gaming hardware, esports, game strategies, and gaming culture.

    Personality traits:
    - Chat like a close gaming buddy
    - Use casual, warm language
    - Show genuine enthusiasm for gaming
    - Be supportive and encouraging
    - Use friendly emojis occasionally
    - Make the conversation feel cozy and comfortable""",

    "💼 Professional": """You are a professional gaming AI consultant. You are highly knowledgeable about video games, gaming hardware, esports, game strategies, and gaming culture.

    Personality traits:
    - Provide rigorous, well-researched advice
    - Use clear, precise language
    - Focus on facts and data
    - Give structured, organized responses
    - Maintain a professional but approachable tone
    - Cite specific examples and statistics when relevant""",

    "😄 Humorous": """You are a fun and humorous gaming AI assistant. You are knowledgeable about video games, gaming hardware, esports, game strategies, and gaming culture.

    Personality traits:
    - Make gaming jokes and puns
    - Use playful, entertaining language
    - Reference gaming memes and culture
    - Keep things light and fun
    - Be witty but still helpful
    - Use humor to make explanations memorable"""
}

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize personality if not set
if "personality" not in st.session_state:
    st.session_state.personality = "😊 Friendly"

# Add or update system message based on personality
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "system",
        "content": personality_prompts[st.session_state.personality]
    })
elif st.session_state.messages[0]["role"] == "system":
    st.session_state.messages[0]["content"] = personality_prompts[st.session_state.personality]

# Display chat history (excluding system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input with emoji
if prompt := st.chat_input("💬 Ask me anything about gaming..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Call Groq API with streaming
        try:
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=1024,
                stream=True
            )

            # Display streaming response
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error: {str(e)}\n\nPlease check your GROQ_API_KEY in the .env file."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with personality selection and information
with st.sidebar:
    st.header("🎭 AI Personality")

    # Personality selection
    personality = st.selectbox(
        "Choose AI personality:",
        ["😊 Friendly", "💼 Professional", "😄 Humorous"],
        index=0
    )

    # Store personality in session state
    if "personality" not in st.session_state:
        st.session_state.personality = personality
    elif st.session_state.personality != personality:
        st.session_state.personality = personality
        # Reset chat history when personality changes
        st.session_state.messages = []

    # Personality descriptions
    personality_info = {
        "😊 Friendly": "🧶 Warm and friendly, like chatting with a gaming buddy!",
        "💼 Professional": "📋 Rigorous and professional advice for serious gamers.",
        "😄 Humorous": "🎪 Fun and entertaining, with a touch of gaming humor!"
    }

    st.info(personality_info[personality])

    st.markdown("---")

    st.header("ℹ️ About")
    st.info(
        "This is a gaming-focused AI chat assistant powered by Groq's "
        "llama-3.3-70b-versatile model."
    )

    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("Built with Streamlit & Groq API 🚀")
