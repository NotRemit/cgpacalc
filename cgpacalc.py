import streamlit as st

st.set_page_config(
    page_title="GradeGauge",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="auto"
)


credits = [3, 2, 1.5, 1]
grades = ['O', 'A+', 'A', 'B', 'C', 'D', 'E', 'F']
st.title("CGPA Calculator")

st.text("Calculate Your CGPA with ease!!")

st.markdown("___")

st.subheader("Enter your details.")
previous_cgpa = st.number_input("Last CGPA")
nos_subject = st.select_slider("Number of Subjects", options=[5, 6, 7, 8, 9, 10, 11])

st.markdown("___")

grade_points = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B': 7,
    'C': 6,
    'D': 5,
    'E': 4,
    'F': 0
}

selected_values = []
total_credits = 0
for i in range(nos_subject):
    selected = st.selectbox(f"Subject {i + 1} Credits:", credits, key=f"selectbox_{i}")
    grade = st.selectbox(f"Grade secured in Subject {i + 1}:", grades, key=f"selectbox_{i}_grade")
    points = grade_points.get(grade, 0)
    selected_values.append(selected * points)
    total_credits += selected

result = st.button("Calculate CGPA")

if result:
    st.balloons()
    sgpa = sum(selected_values) / total_credits
    cgpa = (previous_cgpa + sgpa)/2
    st.success(f"Your SGPA is {sgpa:.2f}")
    st.success(f"Your CGPA is {cgpa:.2f}")

st.markdown("___")
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgb(14, 17, 23);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        With ❤️ by Remit
    </div>
    """, unsafe_allow_html=True)
