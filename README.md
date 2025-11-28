import streamlit as st

# ---------------- Page config ----------------
st.set_page_config(page_title="Plant Chatbot", page_icon="🌱", layout="centered")

st.title("🌱 Plant Health Chatbot")
st.write("Ask any question about plant roots, nematodes, or diagnostics.")

# ---------------- FILE UPLOAD SECTION ----------------
uploaded_file = st.file_uploader(
    "📤 Upload a plant root image (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

has_image = uploaded_file is not None

if has_image:
    # Show a preview and confirmation
    st.image(uploaded_file, caption="Uploaded root image", use_column_width=True)
    st.success("Image uploaded successfully! I can now help you score galling or discuss symptoms.")
else:
    st.info("Upload a root image if you’d like help scoring galling or describing symptoms.")

st.markdown("---")

# ---------------- CHATBOT SECTION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def bot_response(user_text: str, has_image: bool) -> str:
    text = user_text.lower()

    # Galling / scoring questions
    if "gall" in text or "galling" in text or "score" in text:
        if has_image:
            return (
                "Here is the standard **1–5 root-knot galling scale** you can use on the uploaded root:\n\n"
                "1️⃣ **Score 1** – No visible galls; roots look normal.\n"
                "2️⃣ **Score 2** – Light galling: a few small galls on lateral roots.\n"
                "3️⃣ **Score 3** – Moderate galling: noticeable galls on many lateral roots; main root still visible.\n"
                "4️⃣ **Score 4** – Heavy galling: large, coalescing galls covering much of the root system.\n"
                "5️⃣ **Score 5** – Severe galling: root system almost completely replaced by galled tissue.\n\n"
                "Compare your uploaded root to this scale and tell me which score (1–5) you think it fits, "
                "and I can help interpret what that means for nematode pressure and management."
            )
        else:
            return (
                "To help you score galling, please **upload a root image above** first. "
                "Then ask again, and I’ll walk you through the 1–5 galling scale."
            )

    # Nematode questions
    if "nematode" in text or "root-knot" in text or "root knot" in text:
        return (
            "Root-knot nematodes (Meloidogyne spp.) cause galls on roots and reduce water and nutrient uptake. "
            "Management options include resistant varieties, crop rotation, organic amendments, solarization, and "
            "biorational or chemical nematicides. Are you interested in **symptoms**, **management**, or **detection**?"
        )

    # Generic hello
    if "hello" in text or "hi" in text:
        return "Hello! 👋 How can I assist you with plant roots or nematodes today?"

    # Default message
    return (
        "I'm here to help with plant health questions, especially roots and nematodes. "
        "Tell me what crop you’re working with and what you’re observing, or upload a root image "
        "and ask me to help score galling."
    )

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message…")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot reply (uses whether an image is uploaded)
    reply = bot_response(user_input, has_image)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
