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

# Track whether an image exists
has_image = uploaded_file is not None

if has_image:
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
    st.success("Image uploaded successfully!")
else:
    st.info("Upload a root image if you want help scoring galling.")

st.markdown("---")

# ---------------- CHATBOT SECTION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []


def bot_response(user_text: str, has_image: bool) -> str:
    text = user_text.lower()

    # Galling scoring
    if "gall" in text or "galling" in text or "score" in text:
        if has_image:
            return (
                "Here is the **1–5 galling severity scale**:\n\n"
                "**1 – No galls**: Roots appear normal.\n"
                "**2 – Light galling**: A few small galls on lateral roots.\n"
                "**3 – Moderate galling**: Many galls across lateral roots; main root visible.\n"
                "**4 – Heavy galling**: Large, coalescing galls covering much of the system.\n"
                "**5 – Severe galling**: Root system almost completely replaced by galled tissue.\n\n"
                "Look at your uploaded root image above and tell me which score (1–5) it most closely matches."
            )
        else:
            return "Please **upload a root image above** so I can help you score the galling."

    # Nematode questions
    if "nematode" in text or "root-knot" in text or "root knot" in text:
        return (
            "Root-knot nematodes (Meloidogyne spp.) cause galls and reduce water and nutrient uptake. "
            "Would you like help with **symptoms**, **management**, or **diagnostics**?"
        )

    # Greeting
    if "hello" in text or "hi" in text:
        return "Hello
