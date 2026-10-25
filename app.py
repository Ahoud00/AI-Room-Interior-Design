import streamlit as st
from PIL import Image
#اعداد واجهة تطبيق الذكاء الاصطناعي للديكور الداخلي 
st.set_page_config(page_title="AI Room-Interior Design",layout="wide")

st.title("AI Room- AI-Powered Interior Design")
st.write(".رفع صورة الغرفة و اختيار النمط المناسب لإعادة تصميمها باستخدام الذكاء الاصطناعي")

#رفع صورة الغرفة
uplodded_file = st.file_uploader("قم برفع صورة الغرفة (Room Image):",type=["jpg", "png", "jpeg"])

#اختيار نمط الغرفة
style = st.selectbox(
  ,":(Interior Style) اختر نمط التصميم"
["Modern Minimalist", "Bohemian", "Scandinavian","Classic Luxury", "Industrial"])

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="الصورة الاصلية", use_column_width=True)

if st.button("توليد التصميم الجديد "):
  st.success(f"جاري معالجة الصورة وتطبيق النمطة{style}...")
