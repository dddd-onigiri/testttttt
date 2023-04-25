import streamlit as st

st.set_page_config(page_title="Pythonで遊ぶやつ", layout="wide")

st.title("BMI 計算機（Streamlitデモ）")

height_cm = st.number_input("身長（cm）", min_value=100, max_value=250)

weight_kg = st.number_input("体重（kg）", min_value=20, max_value=250)

bmi = weight_kg / (height_cm / 100) ** 2

st.write("あなたのBMIは", bmi, "です。")

if bmi < 18.5:
    st.write("やせ型です")
elif bmi < 24.9:
    st.write("標準です")
elif bmi < 29.9:
    st.write("肥満気味です")
else:
    st.write("肥満です")


message = st.text_area("なんか入力")

if st.button("なんか投稿", key=0):
  st.write(message)