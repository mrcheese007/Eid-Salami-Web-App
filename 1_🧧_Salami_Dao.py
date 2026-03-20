import streamlit as st

st.set_page_config(page_title="সালামি ", page_icon="🧧", layout="centered")

st.title("আসসালামুলাইকুম বড় ভাই/আপু")
st.subheader("ঈদের চাঁদ আকাশে, সালামি দিন বিকাশে!")

st.divider()

# Read URL params for personalization
params = st.query_params
user_name = params.get("user", "রুবায়েত")
bkash_num = params.get("acc", "01568059172")

st.write(f"**{user_name}** ভাই এর চরিত্র, ফুলের মত পবিত্র!")

st.divider()

# The pitch
st.header("কেন সালামি দেওয়া উচিত?")
st.write("পৃথিবীতে ভালো মানুষের সংখ্যা কম।")
st.write("সালামি আমাদের অনুল্লেখিত মৌলিক চাহিদা।")
st.write("দোয়াই হলো জীবনের পথ।")
st.write("এই জাতির ভবিষ্যৎ প্রেসিডেন্ট।")
st.divider()

# bKash section
st.header("💸 সালামির গেটওয়ে")
st.success(f"📱 বিকাশ করো (Personal):")

if st.button("📋 নাম্বার দেখাও"):
    st.code(bkash_num)
    st.info("উপরের নাম্বার কপি করে বিকাশ অ্যাপ থেকে পাঠিয়ে দাও!")

st.warning("⚠️ সালামি না পাঠালে পরের ঈদে ডাবল চওয়া হবে।")

st.divider()

st.write("**সালামি পাঠানোর পর কী করবেন?**")
st.write("পরবর্তী পেজে গিয়ে সালামির উপকারিতা পড়ুন।")
