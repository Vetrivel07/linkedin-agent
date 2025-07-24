import streamlit as st
import requests

st.set_page_config(page_title="LinkedIn Post Agent", layout="centered")
st.title("🤖 LinkedIn Post Agent")

# === Input: Only user's post idea ===
user_prompt = st.text_area("📝 What should your LinkedIn post say?", height=200)

if st.button("Generate & Post to LinkedIn"):
    if not user_prompt.strip():
        st.warning("Please enter a post idea.")
    else:
        with st.spinner("Generating and posting to LinkedIn..."):
            try:
                response = requests.post(
                    "http://localhost:8000/generate_and_post",
                    json={"user_prompt": user_prompt.strip()},
                    timeout=60
                )
                if response.status_code == 200:
                    data = response.json()
                    if data["status"] == "success":
                        st.success("✅ Post published successfully!")
                        st.markdown(f"[🔗 View it on LinkedIn]({data['url']})", unsafe_allow_html=True)
                    else:
                        st.error(f"❌ Failed: {data.get('message', 'Unknown error')}")
                else:
                    st.error(f"❌ Server error: {response.status_code}")
            except Exception as e:
                st.exception(f"🚨 Exception: {e}")
