# AI Code Explainer using Generative AI

A web app that takes code snippets and explains what they do using Google Gemini AI.  
Great for beginners, educators, and developers who want to understand what code means.

---

## Features

- Explains code using Gemini 1.5 Flash (free tier)
- Supports multiple languages:  
  Python, JavaScript, Java, C, C++, SQL, Bash, HTML, CSS
- Dark themed, interactive UI built using Streamlit
- Easy to use — paste code and get an instant explanation
- Can be deployed to Streamlit Cloud

---

## 🛠️ Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/adarshkaran2002/ai-code-explainer.git
cd ai-code-explainer

2. Install dependencies:

pip install -r requirements.txt
3. Add your Gemini API key
Create a .env file:

GEMINI_API_KEY=your_gemini_key_here

4. Run the app locally:

streamlit run app.py
The app will open at: http://localhost:8501
