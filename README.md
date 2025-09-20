# 🧠 MindMate: Your AI Wellness Ally

MindMate is a safe, anonymous, and confidential web application designed to provide empathetic mental wellness support for youth in India. Built with **Streamlit** and powered by **generative AI**, it offers a non-judgmental space to talk, manage stress, and access help 24/7.

[Try Chat With MindMate](https://yourmindmate.streamlit.app/)

---

## ❤️ Project Motivation

Mental health remains a significant societal taboo in India. Young adults and students, facing intense academic and social pressures, often feel isolated with their concerns. The fear of judgment from family and peers, combined with the high cost and scarcity of professional help, creates a formidable barrier to seeking support.  

MindMate was born from the belief that **everyone deserves a safe space to be heard**. It aims to be the crucial first step in a user's wellness journey—a **confidential friend** that listens without judgment, available anytime, anywhere. By leveraging AI, we can offer a scalable, accessible, and private resource to help **destigmatize mental health conversations** and guide users toward the support they need.

---

## ✨ Key Features

- **Empathetic AI Companion**: Engage in supportive, context-aware conversations powered by a generative AI model.  
- **Complete Anonymity**: No sign-ups, no personal data collection, and no stored conversations. Your space is 100% private.  
- **Critical Safety Protocol**: Automatically detects crisis-level keywords and immediately provides users with verified national helpline numbers for immediate support.  
- **Warm & Friendly UI**: A calming and intuitive interface designed to feel like a safe and welcoming space to talk.  

---

## ⚙️ How It Works

The application follows a simple but secure workflow to manage conversations:

1. **User Input**: The user sends a message through the Streamlit chat interface.  
2. **Crisis Detection**: Before any AI processing, the message is scanned locally for high-risk keywords related to self-harm or suicide.  
3. **Safety First**: If a crisis is detected, the AI conversation is immediately halted, and a non-dismissible alert with Indian helpline numbers is displayed.  
4. **AI Interaction**: If the message is safe, it is sent along with the system prompt to the Hugging Face Inference API.  
5. **Empathetic Response**: The AI model generates a supportive, non-advisory response, which is then displayed back to the user in the chat interface.  

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit  
- **AI Model**: Hugging Face Inference API (`mistralai/Mistral-7B-Instruct-v0.2`)  
- **Core Library**: huggingface_hub for API communication  

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.8+  
- A code editor like Visual Studio Code  

---

### 2. Installation & Setup

Clone the repository and install the required dependencies:

```bash
# Clone this repository to your local machine
git clone https://github.com/your-username/your-repo-name.git

# Navigate into the project directory
cd your-repo-name

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required Python packages
pip install -r requirements.txt

