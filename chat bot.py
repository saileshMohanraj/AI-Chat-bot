import streamlit as st
from google import genai

st.title("My Gemini Chatbot")
st.write("Ask a question and Gemini will answer.")


API_KEY =st.secrets["GEMINI_API_KEY"]


@st.cache_resource
def get_genai_client():
    return genai.Client(api_key=API_KEY)

client = get_genai_client()

query = st.text_input("Enter your question")

if st.button("Ask Gemini"):
    if query.strip():
        with st.spinner("Gemini is thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",  # Using the current standard Flash model
                    contents=query
                )
                st.subheader("Gemini's Answer")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")
