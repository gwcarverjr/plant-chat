import streamlit as st

st.set_page_config(page_title="Plant Chatbot", page_icon="🌱", layout="centered")

st.title("🌱 Plant Health Chatbot")
st.write("Ask any question about plant roots, nematodes, or diagnostics.")

# ----------------- FILE UPLOAD SECTION -----------------
uploaded_file = st.file_uploader(
    "📤 Upload a plant root image (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

# Remember in session that an image is available
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
    st.success("Image uploaded successfully!")
    st.session_state["has_image"] = True
else:
    st.session_state["has_image"] = False

st.markdown("---")  # separator between upload and chat

# ----------------- CHATBOT SECTION -----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def bot_response(user_text: str, has_image: bool) -> str:
    """Simple rule-based bot, now aware of whether an image was uploaded."""
    text = user_text.lower()

    # If user mentions upload / figure / image
    if any(w in text for w in ["upload", "figure", "image", "photo"]):
        if has_image:
            return (
                "I see that you’ve uploaded an image. I don’t automatically analyze it yet, "
                "but you can describe what you see (e.g., number of galls, root color), and "
                "I’ll help you interpret or score the infection (0–5)."
            )
        else:
            return (
                "You can upload a figure using the **file uploader at the top of the page**. "
                "Once it’s uploaded, ask me how to interpret it."
            )

    if "gall" in text and any(x in text for x in ["score", "rating", "1-5", "1–5", "scale"]):
        if has_image:
            return (
                "You’ve uploaded a root image. I can’t read the image directly yet, but here’s a "
                "typical 0–5 galling scale you can apply:\n\n"
                "- **0** – No galls\n"
                "- **1** – 1–10% of roots with small galls\n"
                "- **2** – 11–25% of roots galled\n"
                "- **3** – 26–50% of roots galled\n"
                "- **4** – 51–80% of roots galled\n"
                "- **5** – >80% of roots severely galled, root system deformed\n\n"
                "Compare your uploaded root to this scale and tell me which score seems closest."
            )
        else:
            return (
                "To score galling 0–5, you can use this general scale:\n\n"
                "- **0** – No galls\n"
                "- **1** – 1–10% of roots with small galls\n"
                "- **2** – 11–25% of roots galled\n"
                "- **3** – 26–50% of roots galled\n"
                "- **4** – 51–80% of roots galled\n"
                "- **5** – >80% of roots severely galled, root system deformed\n\n"
                "If you upload a root image above, I can help you interpret which score fits best."
            )

    if "nematode" in text or "root knot" in text or "root-knot" in text:
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

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message…")

if user_input:
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot reply, now aware of whether an image is uploaded
    answer = bot_response(user_input, st.session_state.get("has_image", False))
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
