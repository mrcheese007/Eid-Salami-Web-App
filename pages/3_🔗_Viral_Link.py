import streamlit as st
import urllib.parse

st.set_page_config(page_title="Viral Link বানাও", page_icon="🔗", layout="centered")

st.title("🔗 Viral Link বানাও")
st.subheader("সবাইকে ফাঁদে ফেলার সময় এসেছে 😈")

st.divider()

st.write(
    "নিচে তোমার নাম আর বিকাশ নাম্বার দাও। "
    "তোমার একটা পার্সোনাল সালামি লিঙ্ক তৈরি হবে। "
    "সেটা বন্ধুদের পাঠাও এবং অপেক্ষা করো। 😎"
)

st.divider()

# Form
with st.form("link_generator"):
    name = st.text_input("তোমার নাম", placeholder="যেমন: রাফি, তানভীর, মিম...")
    number = st.text_input("তোমার বিকাশ নাম্বার", placeholder="017XXXXXXXX")
    submitted = st.form_submit_button("✨ আমার Viral Link বানাও!")

if submitted:
    if not name:
        st.error("⚠️ নাম দাও আগে!")
    elif not number or len(number.strip()) < 11:
        st.error("⚠️ সঠিক বিকাশ নাম্বার দাও (১১ ডিজিট)!")
    else:
        name_encoded   = urllib.parse.quote(name.strip())
        number_encoded = urllib.parse.quote(number.strip())

        # Change this to your real deployed URL later
        base_url = "https://eidsalami2026.streamlit.app/"
        link = f"{base_url}/Salami_Dao?user={name_encoded}&acc={number_encoded}"

        st.success("🎉 তোমার ভাইরাল লিঙ্ক তৈরি হয়েছে!")
        st.code(link)

        st.divider()

        st.write("**এই লিঙ্কটি কোথায় শেয়ার করবে?**")
        st.write("📱 WhatsApp গ্রুপে পাঠাও")
        st.write("📘 Facebook-এ পোস্ট করো")
        st.write("💌 সরাসরি বন্ধুদের মেসেজ করো")
        st.write("📧 ক্লাসের গ্রুপ চ্যাটে দাও")

        st.divider()

        # WhatsApp and Facebook share links
        wa_text = urllib.parse.quote(
            f"🧧 ঈদ সালামি দাও, নইলে সম্পর্ক শেষ! 😂\n{link}"
        )
        fb_url = urllib.parse.quote(link)

        st.link_button(
            "💬 WhatsApp-এ শেয়ার করো",
            f"https://wa.me/?text={wa_text}"
        )
        st.link_button(
            "📘 Facebook-এ শেয়ার করো",
            f"https://www.facebook.com/sharer/sharer.php?u={fb_url}"
        )

st.divider()

st.caption(
    "💡 Tip: অ্যাপটি Streamlit Cloud-এ deploy করলে "
    "localhost-এর জায়গায় আসল URL বসাও।"
)

st.link_button(
    "🎵 ঈদ মোবারক!",
    "https://www.youtube.com/watch?v=R6ePrTGODHs"
)
