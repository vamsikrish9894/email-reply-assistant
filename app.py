import streamlit as st
import openai

# 🔐 Your OpenAI API Key (replace this with your key)
openai.api_key = "sk-your-api-key"

st.set_page_config(page_title="📧 Email Auto-Reply Assistant", layout="centered")
st.title("📨 Auto Email Reply Assistant")
st.markdown("Generate context-aware replies using AI.")

# 1. Email content input
email_content = st.text_area("📥 Paste the incoming email:", height=200)

# 2. Tone selector
tone = st.selectbox("🎯 Choose reply tone:", ["Formal", "Friendly", "Neutral", "Urgent"])

# 3. Generate button
if st.button("🚀 Generate Reply"):
    if not email_content.strip():
        st.warning("❗ Please paste an email above.")
    else:
        prompt = f"""
        You are an AI assistant. Generate a professional and {tone.lower()} reply to the email below.

        Email:
        {email_content}

        Reply:
        """
        with st.spinner("Generating..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that writes email replies."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                reply = response['choices'][0]['message']['content']
                st.success("✅ Reply Generated:")
                st.text_area("✉️ AI-Generated Reply:", value=reply, height=200)
                st.download_button("📎 Download Reply", reply, file_name="email_reply.txt")
            except Exception as e:
                st.error(f"Error: {str(e)}")