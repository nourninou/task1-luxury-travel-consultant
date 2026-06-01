import streamlit as st

st.set_page_config(
    page_title="Luxury Travel Consultant",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Luxury Travel Consultant")
st.subheader("Task 1 - System Prompt Architect")

st.markdown("---")

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

st.header("System Prompt")

st.text_area(
    "Luxury Travel Consultant Prompt",
    prompt,
    height=350
)

st.markdown("---")

st.header("Example Customer Questions")

question = st.selectbox(
    "Choose a scenario",
    [
        "Luxury honeymoon in Maldives",
        "Discount request ($5,000)",
        "Discount request ($25,000)",
        "Competitor comparison",
        "Angry customer"
    ]
)

responses = {
    "Luxury honeymoon in Maldives":
    """
Thank you for considering Elite Horizons Travel.

For a luxury honeymoon, I recommend an overwater villa experience in the Maldives with private dining, spa treatments, and personalized excursions.

May I know your preferred travel dates?
    """,

    "Discount request ($5,000)":
    """
At this booking value, no promotional discounts are currently available.

However, I would be delighted to suggest premium enhancements to maximize your travel experience.
    """,

    "Discount request ($25,000)":
    """
You qualify for our 5% loyalty discount.

Additionally, we can discuss exclusive upgrades and concierge services to enhance your journey.
    """,

    "Competitor comparison":
    """
I can only speak about the services offered by Elite Horizons Travel.

Our focus is on delivering personalized luxury experiences tailored to each client.
    """,

    "Angry customer":
    """
I understand your concern and appreciate your feedback.

My goal is to help you find the best luxury experience that aligns with your expectations and budget.
    """
}

if st.button("Generate Response"):
    st.success(responses[question])

st.markdown("---")
st.caption("DecodeLabs Generative AI Internship - Task 1")