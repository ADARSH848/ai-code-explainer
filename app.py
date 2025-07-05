import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI config
st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🛠️ Settings")
    st.markdown("Built using [Gemini API](https://ai.google.dev/)")
    st.markdown("Developed by **Adarsh Anand Karan**")
    st.markdown("Email: adarshkaran2002@gmail.com")
    st.markdown("GitHub: [ai-code-explainer](https://github.com/ADARSH848/ai-code-explainer)")

# Title
st.markdown("<h1 style='text-align: center;'>🧠 AI Code Explainer tool by Adarsh Anand</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explain your code in plain English</p>", unsafe_allow_html=True)

# Language selector
languages = [
    "Python", "JavaScript", "C", "C++", "Java", "SQL", "Bash", "HTML", "CSS"
]
language = st.selectbox("Select Programming Language", languages)

# Code input box
code_input = st.text_area(
    f"Enter your {language} code here:",
    height=300,
    placeholder="Paste your code here..."
)

# Explain button
if st.button("✨ Explain Code"):
    if not code_input.strip():
        st.warning("Please enter a code snippet first.")
    else:
        with st.spinner("Analyzing your code..."):
            try:
                prompt = f"Explain the following {language} code in simple terms:\n\n{code_input}"
                response = model.generate_content(prompt)
                explanation = response.text

                with st.expander("🧾 Click to view explanation"):
                    st.markdown(explanation)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Made with ❤️ using Gemini API & Streamlit</p>",
    unsafe_allow_html=True
)
