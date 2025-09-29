import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Streamlit 요소 예시")

st.header("텍스트 요소")
st.write("이것은 일반 텍스트입니다.")
st.markdown("**마크다운**도 지원합니다!")

st.header("입력 요소")
name = st.text_input("이름을 입력하세요:")
age = st.slider("나이", 0, 100, 25)
st.write(f"안녕하세요, {name}님! 나이: {age}")

st.header("버튼과 체크박스")
if st.button("버튼 클릭"):
    st.success("버튼이 클릭되었습니다!")
if st.checkbox("체크박스 예시"):
    st.info("체크박스가 선택됨!")

st.header("파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file:
    st.write("업로드된 파일:", uploaded_file.name)

st.header("데이터프레임 예시")
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)

st.header("Matplotlib 차트 예시")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
st.pyplot(fig)
