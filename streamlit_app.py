import streamlit as st

# ----------------- Page config -----------------
st.set_page_config(page_title="Plant Chatbot", page_icon="🌱", layout="centered")

st.title("🌱 Plant Health Chatbot")
st.write("Ask any question about plant roots, nematodes, or diagnostics.")

# ----------------- File upload section -----------------
uploaded_file = st.file_uploader(
    "📤 Upload a plant root image (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Show a preview of the uploaded image
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
    st.success("Image uploaded successfully! (We can add automatic analysis here later.)")

st.markdown("---")  # nice separator between upload and chat

# ----------------- Chatbot logic -----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def bot_response(user_text: str) -> str:
    text = user_text.lower()

    if "nematode" in text or "root-knot" in text:
        return (
            "Root-knot nematodes (Meloidogyne spp.) cause galls on roots and reduce "
            "water and nutrient uptake. Do you want to talk about symptoms, "
            "management strategies, or detection methods?"
        )
    if "root" in text and "disease" in text:
        return (
            "Roots can show browning, lesions, galls, or rot depending on the pathogen. "
            "Which crop and what symptoms are you seeing (galls, rot, stunting, yellowing)?"
        )
    if "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help you today?"

    return (
        "I'm here to help with plant health questions, especially roots and nematodes. "
        "Tell me what crop you’re working with and what you’re observing."
    )

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box at the bottom
user_input = st.chat_input("Type your message…")

if user_input:
    # Store and show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot reply
    answer = bot_response(user_input)

    # Store and show bot reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
