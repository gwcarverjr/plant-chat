import streamlit as st

st.set_page_config(page_title="Plant Chatbot", page_icon="🌱", layout="centered")

st.title("🌱 Plant Health Chatbot")
st.write("Ask any question about plant roots, nematodes, or diagnostics.")

if "messages" not in st.session_state:
    st.session_state.messages = []

def bot_response(user_text):
    text = user_text.lower()

    if "nematode" in text or "root-knot" in text:
        return ("Root-knot nematodes (Meloidogyne spp.) cause galls on roots and reduce water and nutrient uptake. "
                "Would you like info on symptoms, management, or detection?")
    if "root" in text and "disease" in text:
        return "Roots can show browning, lesions, galls, or rot depending on the pathogen. What crop are you examining?"
    if "hello" in text or "hi" in text:
        return "Hello! How can I assist you today?"
    return "I'm here to help with plant health questions. What would you like to know?"

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    answer = bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
