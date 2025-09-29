import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# NanumGothic 폰트 경로 지정 및 설정
font_path = "fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False

st.title("예시 성적 데이터 시각화")

# 예시 성적 데이터
students = ["홍길동", "김철수", "이영희", "박민수", "최지우"]
scores = [85, 92, 78, 88, 95]

st.subheader("학생별 성적 데이터")
st.dataframe({"이름": students, "성적": scores})

st.subheader("막대 그래프")
fig, ax = plt.subplots()
ax.bar(students, scores, color="skyblue")
ax.set_ylabel("점수", fontproperties=fontprop)
ax.set_title("학생별 성적 막대 그래프", fontproperties=fontprop)
ax.set_xticklabels(students, fontproperties=fontprop)
st.pyplot(fig)

st.subheader("성적 분포 히스토그램")
fig2, ax2 = plt.subplots()
ax2.hist(scores, bins=5, color="lightgreen", edgecolor="black")
ax2.set_xlabel("점수", fontproperties=fontprop)
ax2.set_ylabel("학생 수", fontproperties=fontprop)
ax2.set_title("성적 분포 히스토그램", fontproperties=fontprop)
st.pyplot(fig2)
