import streamlit as st

st.set_page_config(
    page_title="EID Salami Portal ",
    page_icon="🌙",
    layout="centered"
)

#st.title("🌙 EID Salami Portal")
st.subheader("ঈদ মোবারক! স্বাগতম!")

st.divider()

st.write(
    "আপনি এসে পড়েছেন এই বছরের সবচেয়ে গুরুত্বপূর্ণ ওয়েব পেজে। "
    "তাকাব্বাল্লাহু মিন্না ওয়া মিনকুম।"
)

st.info("👈 বাম দিকের মেনু থেকে যেকোনো পেজে যান!")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(label="😇 সালামি দাতা", value="**")
with col2:
    st.metric(label="💸 মোট আদায়", value="৳****")


st.divider()

st.success("✅ এই পোর্টাল ১০০% হালাল এবং ঈদ-সার্টিফাইড।")
st.balloons()
