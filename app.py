import streamlit as st
from huggingface_hub import InferenceClient

def local_css():
    css = """
        <style>
            /* Import Google Font */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

            /* General Body and Font */
            body, .stApp {
                font-family: 'Poppins', sans-serif;
            }

            /* Main container styling - warmer, homelike background */
            [data-testid="stAppViewContainer"] {
                background-color: #FFF8E7; /* A soft, warm, creamy off-white */
            }

            /* Title and Caption */
            [data-testid="stHeading"] h1 {
                font-weight: 600;
                color: #31333F !important; /* A strong, dark grey for visibility */
                padding-bottom: 0;
            }
            [data-testid="stCaptionContainer"] {
                color: #65676b;
            }

            /* --- Chat Styling --- */

            /* Chat Input Box */
            [data-testid="stChatInput"] {
                background-color: #ffffff;
                border-top: 1px solid #dddfe2;
                padding-top: 1rem;
                box-shadow: 0 -2px 5px rgba(0,0,0,0.05);
            }

            /* Chat Bubbles */
            [data-testid="stChatMessage"] {
                padding: 1rem 1.25rem;
                margin-bottom: 1rem;
                border-radius: 25px;
                max-width: 80%;
                box-shadow: 0 4px 6px rgba(0,0,0,0.07);
                border: none;
            }

            /* Avatar styling */
            [data-testid="stChatMessage"] [data-testid="stAvatar"] {
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }

            /* AI's message bubble (left side) */
            div[data-testid="stChatMessage"]:not(:has(div[data-testid="stMarkdownContainer"] > div[data-testid="stHorizontalBlock"][style*="flex-direction: row-reverse;"])) {
                background-color: #FFFFFF;
            }
            
            /* User's message bubble (right side) */
            div[data-testid="stChatMessage"]:has(div[data-testid="stMarkdownContainer"] > div[data-testid="stHorizontalBlock"][style*="flex-direction: row-reverse;"]) {
                background-color: #FFE0B2;
            }

            /* Target the text directly inside the chat bubbles */
            [data-testid="stMarkdownContainer"] p {
                color: #1a1a1a !important;
            }
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)


try:
    client = InferenceClient(token=st.secrets["HUGGINGFACE_API_TOKEN"])
except Exception as e:
    st.error("Hugging Face API token not found. Please add it to your Streamlit secrets.", icon="🔒")
    st.stop()


HUGGINGFACE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

SYSTEM_PROMPT = """You are a warm, empathetic, and supportive AI wellness companion for youth in India.
Your role is to be a non-judgmental, active listener.
- DO NOT provide medical advice, diagnoses, or therapy. You are NOT a doctor.
- Keep your responses gentle, supportive, and relatively brief.
- Validate the user's feelings and offer encouragement.
- If the user talks about everyday stress, anxiety, or sadness, help them explore their feelings with open-ended questions.
- Gently guide the conversation towards self-care and positive coping mechanisms if appropriate, without being prescriptive.
- NEVER give advice or information on methods of self-harm.
- Maintain a safe, supportive, and confidential tone at all times."""

AI_AVATAR = "🧠"
USER_AVATAR = "👤"

def check_for_crisis(message):
    lower_case_message = message.lower()
    crisis_keywords = [
        'kill myself', 'suicide', 'suicidal', 'want to die', 'end my life',
        'no reason to live', 'hang myself', 'self-harm', 'overdose'
    ]
    return any(keyword in lower_case_message for keyword in crisis_keywords)

st.set_page_config(
    page_title="MindMate",
    page_icon=AI_AVATAR,
    layout="centered"
)

local_css()

st.title(f"{AI_AVATAR} MindMate")
st.caption("Your safe, anonymous, and confidential space to talk.")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm here to listen. Feel free to share what's on your mind. Remember, this is a safe and anonymous space."}
    ]

for message in st.session_state.messages:
    avatar = AI_AVATAR if message["role"] == "assistant" else USER_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("What's on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    if check_for_crisis(prompt):
        alert_html = """
        <div style="background-color: #F8D7DA; border: 2px solid #DC3545; border-radius: 12px; padding: 1.5rem; color: black !important;">
            <p style="color: black !important; margin-bottom: 1rem;">🚨 It sounds like you are going through a very difficult time. Please reach out for immediate support. You are not alone.</p>
            <strong style="color: #d32f2f; font-size: 1.1em;">AASRA (India):</strong>
            <ul style="margin-top: 0.5rem; margin-bottom: 1rem; list-style-position: inside;">
                <li style="color: black !important;">Helpline: +91-9820466726 (24x7)</li>
            </ul>
            <strong style="color: #d32f2f; font-size: 1.1em;">Vandrevala Foundation:</strong>
            <ul style="margin-top: 0.5rem; margin-bottom: 1rem; list-style-position: inside;">
                <li style="color: black !important;">Helplines: 9999 666 555 / 1860 2662 345 (24x7)</li>
            </ul>
            <p style="color: black !important; margin-top: 1rem;">This chat will now pause. Please contact one of these helplines.</p>
        </div>
        """
        st.markdown(alert_html, unsafe_allow_html=True)
        st.stop()

    try:
        with st.spinner("Thinking..."):
            hf_messages = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + st.session_state.messages

            response_stream = client.chat_completion(
                messages=hf_messages,
                model=HUGGINGFACE_MODEL,
                max_tokens=1024,
                stream=False
            )
            
            ai_response = response_stream.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant", avatar=AI_AVATAR):
            st.markdown(ai_response)

    except Exception as e:
        st.error(f"Sorry, I'm having trouble connecting. Please try again. Error: {e}")

