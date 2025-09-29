import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Streamlit 요소 예시 및 일차함수 그래프 활동지")

st.header("기본 Streamlit 요소들")
st.write("텍스트, 버튼, 슬라이더, 체크박스, 셀렉트박스 등 다양한 UI 요소를 활용할 수 있습니다.")

st.subheader("텍스트 입력")
name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"안녕하세요, {name}님!")

st.subheader("버튼")
if st.button("버튼을 눌러보세요"):
    st.info("버튼이 눌렸습니다!")

st.subheader("슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"선택한 값: {value}")

st.subheader("체크박스")
checked = st.checkbox("체크박스 예시")
if checked:
    st.write("체크박스가 선택되었습니다.")

st.subheader("셀렉트박스")
option = st.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write(f"선택한 옵션: {option}")

st.header("Matplotlib 차트 예시")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("사인 함수 그래프")
st.pyplot(fig)

st.header("일차함수 그래프 활동지")
st.write("아래에 일차함수식을 입력하면 그래프로 그려줍니다. 예시: y=2x+1")

eq_input = st.text_input("일차함수식을 입력하세요 (예: y=2x+1)")
def parse_linear_equation(equation):
    import re
    match = re.match(r"y\s*=\s*([+-]?\d*\.?\d*)x\s*([+-]\s*\d+)?", equation.replace(" ", ""))
    if match:
        a = match.group(1)
        b = match.group(2) if match.group(2) else "0"
        a = float(a) if a not in ["", "+", "-"] else float(f"{a}1")
        b = float(b.replace(" ", ""))
        return a, b
    return None, None

if eq_input:
    a, b = parse_linear_equation(eq_input)
    if a is not None:
        x = np.linspace(-10, 10, 100)
        y = a * x + b
        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, label=eq_input)
        ax2.set_title(f"그래프: {eq_input}")
        ax2.legend()
        st.pyplot(fig2)
    else:
        st.error("올바른 일차함수식을 입력해주세요. 예: y=2x+1")
