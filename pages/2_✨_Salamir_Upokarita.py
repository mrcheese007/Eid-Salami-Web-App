import streamlit as st
import random

st.set_page_config(page_title="সালামির উপকারিতা", page_icon="✨", layout="centered")

st.title("✨ সালামির উপকারিতা")
st.subheader("বৈজ্ঞানিকভাবে প্রমাণিত (প্রায়)")

st.divider()

st.write(
    "সালামি দেওয়া শুধু একটি আর্থিক লেনদেন না — "
    "এটি একটি আধ্যাত্মিক, সামাজিক এবং রাজনৈতিক বিনিয়োগ।"
)

st.divider()

# Spiritual benefits
st.header("🤲 আত্মিক উপকার")
st.write("মন থেকে দোয়া পাবেন — গ্যারান্টিড।")
st.write("ঘুমের মধ্যে ভালো স্বপ্ন দেখবেন।")
st.write("পরকালে সওয়াব পাবেন (উৎস: বিশ্বস্ত সূত্র)।")

st.divider()

# Social benefits
st.header("🍛 সামাজিক উপকার")
st.write("পরের বার বিরিয়ানি খাওয়ার ইনভাইট পাবেন।")
st.write("এলাকায় আপনার সম্মান বাড়বে।")
st.write("চা-সিঙ্গারার দাওয়াত আসবে অপ্রত্যাশিতভাবে।")

st.divider()

# Political benefits
st.header("🗳️ রাজনৈতিক উপকার")
st.write("সামনে ভোটে দাঁড়ালে বেশি ভোট পাবেন।")
st.write("ওয়ার্ড কমিশনারের সাথে পরিচয় হওয়ার সুযোগ।")
st.write("মহল্লায় আপনার নাম উচ্চারিত হবে শ্রদ্ধার সাথে।")

st.divider()

# Fun risk meter
st.header("⚠️ না দিলে কী হবে?")

risk = st.slider(
    "তুমি কতদিন ধরে সালামি আটকে রেখেছ?",
    min_value=0, max_value=30, value=0,
    help="দিন সংখ্যায়"
)

danger_level = int((risk / 30) * 100)

if danger_level == 0:
    st.success("😇 তুমি এখনো নিরাপদ। তাড়াতাড়ি দিয়ে দাও।")
elif danger_level < 40:
    st.warning(f"😟 বিপদ মাত্রা: {danger_level}% — সম্পর্ক নাজুক হয়ে পড়ছে।")
elif danger_level < 80:
    st.error(f"😠 বিপদ মাত্রা: {danger_level}% — ব্লক হওয়ার সম্ভাবনা আছে!")
else:
    st.error(f"💀 বিপদ মাত্রা: {danger_level}% — তুমি ইতোমধ্যে ব্লক হয়ে গেছ কিনা চেক করো।")

st.divider()

# Fake testimonials
st.header("💬 সালামি দাতাদের অভিজ্ঞতা")

testimonials = [
    ("রাহেলা, ঢাকা", "সালামি দেওয়ার পরদিনই পরীক্ষায় A+ পেয়েছি। কাকতালীয় নয়।"),
    ("তানভীর, চট্টগ্রাম", "৫০ টাকা দিয়েছিলাম। পরের সপ্তাহে চাকরি হয়েছে।"),
    ("মিম, সিলেট", "না দিয়েছিলাম। ফোন হারিয়েছে। এখন দিই।"),
    ("রাফি, কুষ্টিয়া", "দোয়া পেয়েছি, বিরিয়ানি পেয়েছি। জীবন সুন্দর।"),
]

random.shuffle(testimonials)
for name, quote in testimonials[:3]:
    with st.expander(f"⭐⭐⭐⭐⭐ — {name}"):
        st.write(f'"{quote}"')
